import curses


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_GREEN)
    GREEN_WHITE = curses.color_pair(1)

    stdscr.clear()
    stdscr.addstr(5, 5, "Hello world", curses.A_UNDERLINE)
    stdscr.addstr(3, 30, "Hello again", GREEN_WHITE | curses.A_BOLD)
    stdscr.addstr(10, 15, "SUS Text", curses.color_pair(2) | curses.A_ITALIC)
    stdscr.refresh()
    stdscr.getch()

    for c in range(0, 500): 
        stdscr.clear()    
        color = curses.color_pair(1) if c % 2 == 0 else curses.color_pair(2)
        stdscr.addstr('The super tuper ultra hyper god damn motherfuckr', color)
        stdscr.refresh()
        curses.napms(100)

curses.wrapper(main)
