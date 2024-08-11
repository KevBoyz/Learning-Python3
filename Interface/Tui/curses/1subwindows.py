import curses

screen = curses.initscr()

screen.addstr(0,0, "Hello world!")
screen.refresh()

curses.napms(800)

my_window = curses.newwin(20,40,4,3)
my_window.addstr("I'm a window inside a screen!")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long string on this window.")
my_window.addstr("And this is a test of a long str")

my_window.refresh()

sec_win = curses.newwin(15,5,4,45)
sec_win.addstr(0, 1,"Other window, or something like it.")
sec_win.addstr(1, 3, "Here you can see a realy beatiful interface on terminal.")
sec_win.refresh()

curses.napms(6000)

curses.endwin()
