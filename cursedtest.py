import curses
import time

def menu(root, current_row):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    height, width = root.getmaxyx()

    menu = [ "Option 1", "Option 2", "Option 3", "Option 4" ]

    for idx, element in enumerate(menu):
        y = height // 2 + idx
        x = width // 2 - len(element) // 2 

        if idx == current_row:
            root.attron(curses.color_pair(1))
            root.addstr(y, x, element)
            root.attroff(curses.color_pair(1))

        else:
            root.addstr(y, x, element)

    root.refresh()
#   time.sleep(5)

def main(root):
    curses.curs_set(0)

    current_row = 0

    menu(root, current_row)

    while True:
        key = root.getch()

        if key == curses.KEY_UP:
           current_row -= 1 
        
        elif key == curses.KEY_DOWN:
            current_row += 1

        elif key == ord("e"):
            break

        elif key == ord("q"):
            break

        menu(root, current_row)

    root.refresh()


curses.wrapper(main)
