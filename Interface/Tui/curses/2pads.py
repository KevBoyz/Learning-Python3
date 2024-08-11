
import curses


def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_GREEN)
    GREEN_WHITE = curses.color_pair(1)

    pad = curses.newpad(100, 100)
    pad.keypad(1)
    for c in range(100):
        for j in range(26):
            pad.addstr(chr(65+j), GREEN_WHITE)

    for c in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, c, 5, c, 20, 25+c)
        curses.napms(60)    

    
curses.wrapper(main)
