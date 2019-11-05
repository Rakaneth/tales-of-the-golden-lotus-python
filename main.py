import tcod
import tcod.event

class EventBus(tcod.event.EventDispatch):
    def on_enter(self):
        pass

    def on_draw(self):
        pass

    def ev_keydown(self, event: tcod.event.KeyDown):
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()

    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

def main():
    SW = 100
    SH = 40

    tcod.console_set_custom_font('arial12x12.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    root = tcod.console_init_root(SW, SH, "Tales of the Golden Lotus", renderer=tcod.RENDERER_OPENGL2, vsync=False)
    eb = EventBus()

    while True:
        tcod.console_put_char(root, 1, 1, '@', tcod.BKGND_NONE)
        tcod.console_flush()

        for ev in tcod.event.get():
            eb.dispatch(ev)


if __name__ == "__main__":
    main()
