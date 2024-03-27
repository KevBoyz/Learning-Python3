import curses


def main(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_GREEN)
    GREEN_WHITE = curses.color_pair(1)

    x, y = 0, 0
    while True:
        key = stdscr.getkey()
        if key == 'KEY_LEFT':
            x -= 1
        elif key == 'KEY_RIGHT':
            x += 1
        elif key == 'KEY_DOWN':
            y -= 1
        elif key == 'KEY_UP':
            y += 1
        
        stdscr.clear()
        stdscr.addstr(y, x, '0')
        stdscr.refresh()
 
    
curses.wrapper(main)
