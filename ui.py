import tcod
import tcod.event
import esper

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

    def ev_quit(self):
        pass

class MainScreen(Screen):
    def __init__(self, world: esper.World):
        super.__init__(self, 'test', world)
        self.map_con = tcod.console.Console(50, 30, "F")
        self.stat_con = tcod.console.Console(50, 30, "F")
        self.msg_con = tcod.console.Console(30, 10, "F")
        self.skil_con = tcod.console.Console(30, 10, "F")
        self.info_con = tcod.console.Console(40, 10, "F")
    
    def on_draw(self):
        self.draw_map()
        self.draw_stats()
        self.draw_msgs()
        self.draw_skills()
        self.draw_info()
    
    def draw_map(self):
        pass

    def draw_stats(self):
        self.map_con.blit(self.root, 0, 0, 0, 0, self.map_con.)

    def draw_msgs(self):
        pass

    def draw_skills(self):
        pass

    def draw_info(self):
        pass

    def ev_keydown(self):
        pass

    def ev_quit(self):
        #TODO: autosave, etc
        raise SystemExit()