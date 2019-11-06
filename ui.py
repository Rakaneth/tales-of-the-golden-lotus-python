import tcod
import tcod.event
import esper
from constants import *

class Screen(tcod.event.EventDispatch):
    def __init__(self, name: str, world: esper.World, root: tcod.console.Console):
        self.name = name
        self.world = world
        self.root = root
    
    def on_enter(self):
        print(f'Entering {self.name} screen.')
    
    def on_draw(self):
        pass

    def ev_keydown(self, ev: tcod.event.KeyDown):
        pass

    def on_exit(self):
        pass

    def ev_quit(self, ev: tcod.event.Quit):
        #TODO: autosave, etc
        raise SystemExit()

class ScreenManager:
    def __init__(self):
        self.screens = []
    
    def push_screen(self, screen: Screen):
        self.screens.append(screen)
        screen.on_enter()
    
    def pop_screen(self):
        popped = self.screens.pop()
        popped.on_exit()
    
    def clear(self):
        while len(self.screens) > 0:
            self.pop_screen()
    
    @property
    def cur_screen(self):
        return self.screens[-1]

MANAGER = ScreenManager()

class MainScreen(Screen):
    def __init__(self, world: esper.World, root: tcod.console.Console):
        super().__init__('main', world, root)
        self.map_con = tcod.console.Console(MAP_W, MAP_H, "F")
        self.stat_con = tcod.console.Console(STAT_W, STAT_H, "F")
        self.msg_con = tcod.console.Console(MSG_W, MSG_H, "F")
        self.skil_con = tcod.console.Console(SKIL_W, SKIL_H, "F")
        self.info_con = tcod.console.Console(INFO_W, INFO_H, "F")
    
    def on_draw(self):
        self.draw_map()
        self.draw_stats()
        self.draw_msgs()
        self.draw_skills()
        self.draw_info()
    
    def draw_map(self):
        pass

    def draw_stats(self):
        self.stat_con.draw_frame(0, 0, STAT_W, STAT_H, 'Stats')
        self.stat_con.blit(self.root, STAT_X, STAT_Y, 0, 0)

    def draw_msgs(self):
        self.msg_con.draw_frame(0, 0, MSG_W, MSG_H, 'Messages')
        self.msg_con.blit(self.root, MSG_X, MSG_Y, 0, 0)

    def draw_skills(self):
        self.skil_con.draw_frame(0, 0, SKIL_W, SKIL_H, 'Skills')
        self.skil_con.blit(self.root, SKIL_X, SKIL_Y, 0, 0)

    def draw_info(self):
        self.info_con.draw_frame(0, 0, INFO_W, INFO_H, 'Info')
        self.info_con.blit(self.root, INFO_X, INFO_Y, 0, 0)

    def ev_keydown(self, ev: tcod.event.KeyDown):
        if ev.sym == tcod.event.K_ESCAPE:
            self.dispatch(tcod.event.Quit())
        elif ev.sym == tcod.event.K_t:
            MANAGER.push_screen(Menu('test', self.world, self.root, None, 'New Game', 'Continue'))


class Menu(Screen):
    def __init__(self, name: str, world: esper.World, root: tcod.console.Console, caption: str=None, *items: str):
        super().__init__(name, world, root)
        if len(items) == 0:
            raise ValueError('Menu must contain items')

        self.items = items
        self.selected = 0
        s_items = sorted(self.items, key=len)
        longest = s_items[0]
        self.w = len(longest) + 2
        self.h = len(self.items) + 2
        self.menu_con = tcod.console.Console(self.w, self.h)
        self.caption = caption if caption else ""
    
    def on_draw(self):
        x = (SW - self.w) // 2
        y = (SH - self.h) // 2
        self.menu_con.draw_frame(0, 0, self.w, self.h, self.caption)
        for idx, item in enumerate(self.items):
            color = tcod.white
            if idx == self.selected:
                color = tcod.cyan
            self.menu_con.print(1, 1+idx, item, color)

        self.menu_con.blit(self.root, x, y, 0, 0)
    
    def on_select(self, sel_str):
        print(f'{sel_str} selected on {self.name} menu.')
        MANAGER.pop_screen()
    
    def ev_keydown(self, ev: tcod.event.KeyDown):
        if ev.sym == tcod.event.K_RETURN:
            self.on_select(self.items[self.selected])
        elif ev.sym == tcod.event.K_KP_8 or ev.sym == tcod.event.K_UP:
            self.selected = (self.selected - 1) % len(self.items)
        elif ev.sym == tcod.event.K_KP_2 or ev.sym == tcod.event.K_DOWN:
            self.selected = (self.selected + 1) % len(self.items)



