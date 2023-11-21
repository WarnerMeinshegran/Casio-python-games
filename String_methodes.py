"""1.2
improved add_line_breaks()
more navigation controls for view_list()
modifiable configs
"""

# SETTINGS
SCREEN_MAX_LINES = 7
SCREEN_MAX_LETTERS_PER_LINE = 21


def clr_scrn():
    '''clears screen by making new lines'''    
    print("\n"*SCREEN_MAX_LINES)

# def add_line_breaks(string, every=20):
#     """
#     This function takes a string and puts "/n" every 20 letters.

#     Args:
#       string: The string to add line breaks to.
#       every: break line every number of letters

#     Returns:
#       A new string with line breaks added every 20 letters.
#     """
#     string = string.strip()

#     new_string = ""
#     for i in range(len(string)):
#         if i % every == 0: # if index is divisable by 20
#             new_string += "\n" if string[i] in [" ", ".", ","] else "-\n"
#         new_string += string[i]
#     result = "\n".join(new_string.strip().split("\n")).strip()
#     result2 = [i.strip() for i in result.split("\n")]
#     return "\n".join(result2)[1:]

def add_line_breaks(string, length=SCREEN_MAX_LETTERS_PER_LINE-1):
    """
    This function takes a string and puts "/n" every x letters.

    Args:
      string: The string to add line breaks to.
      length: break line every number of letters

    Returns:
      A new string with line breaks added every x letters.
    """
    words = string.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= length:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line != "":
        lines.append(current_line.strip())
    return "\n".join(lines)


def warn(message, auto_break_lines = True, auto_break_lines_every=SCREEN_MAX_LETTERS_PER_LINE-1, title = None, clear_screen = True):
    '''Prints the given message ans waits for the user to press enter

    Args:
        message (str): the message to display
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.
    '''    
    if clear_screen:clr_scrn()
    if title is not None: print(title, end="")
    if auto_break_lines: s = input(add_line_breaks(message, auto_break_lines_every))
    else:s = input(message)
    if clear_screen:clr_scrn()
    return s

def ask(question, ans = None, auto_break_lines = True, auto_break_lines_every = SCREEN_MAX_LETTERS_PER_LINE-1, prompt = True):
    '''just like warn but instead asks the user for an input of number like choosing an option

    Args:
        question (str): the question to ask
        ans (list, optional): an list of all answers (recommended max: 3-4 answers). Defaults to ["yes","no"].
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.

    Returns:
        str: the answer choosen not the index
    '''    
    if ans is None:ans = ["yes","no"]

    while True:
        clr_scrn()
        if prompt:warn("{}".format(question), auto_break_lines, auto_break_lines_every)
        else:
            if auto_break_lines:print(add_line_breaks(question, auto_break_lines_every))
            else:print(question)


        for i in range(len(ans)):
            print("{number}) {item}".format(number=i+1, item=ans[i]))

        try:user_input = int(input())
        except (TypeError, ValueError): continue

        try: user_input -= 1
        except TypeError: continue

        if user_input < 0:
            continue
        clr_scrn()
        try: return ans[user_input]
        except IndexError: continue

def find_matches(items, search_term):
    matches = []
    for item in items:
        if search_term in str(item):
            matches.append(item)
    return matches


def view_list(list_items, page_size=SCREEN_MAX_LINES-4, pick_confirm=True, pick_confirm_question="you picked {}\n you sure?", readonly=False, title="--------", indexed = True):
    '''View list items in a 'scrollable' page

    Args:
        list_items (list): items to show
        page_size (int, optional): number of items to show in screen. Defaults to 3.
        pick_confirm (bool, optional): confirm about the option the user picked. Defaults to True.
        pick_confirm_question (str, optional): confirm question to ask. Defaults to "you picked {}\nyou sure?".
        readonly (bool, optional): Doesnt let the user pick an item. Defaults to False.
        title (str, optional): title to show on the first line. Defaults to "--------".

    Returns:
        str: item picked not index
    '''    

    current_page = 0 # used for navigation and generating pages
    controls = "type c for controls"
    HOWTO="""CONTROLS
+   |  page down
-   |  page up
*   |  go to page
/   |  search
1-{} |  pick item
""".format(page_size)
    # generate pages
    pages = []
    while True:
        page = []
        try:
            for i in range(page_size):
                page.append(list_items[i+current_page])
            current_page += page_size   
        except IndexError:
            break
        finally:
            pages.append(page)
    # view pages
    current_page = 0 # reset value to use for navigation
    while True:
        clr_scrn()

        print(title)
        
        try:
            for i in range(len(pages[current_page])):
                if indexed: print("{number}) {item}".format(number=i+1, item=pages[current_page][i]))
                else: print(pages[current_page][i])
        except IndexError: 
            current_page = 0
            continue

        
        print("_"*len(list(controls))) # seperator between controls and items
        if not readonly: 
            print(controls.format(current_page+1))
            user_navigation = input("pick item(1-{})".format(len(pages[current_page])))
        elif readonly:
            user_navigation = input(controls.format(current_page+1))

        if user_navigation == "+":
            current_page += 1
            continue
        elif user_navigation == "-":
            current_page -= 1
            if current_page <= -1:current_page = 0
            continue
        elif user_navigation == "*":
            clr_scrn()
            try:
                cp = int(input("Navigate to page:\n"))
                if cp > len(pages):raise ValueError
            except Exception:
                continue
            else: current_page = cp-1
        elif user_navigation == "/":
            clr_scrn()
            try:
                search = input("Search:\n")
                clr_scrn()
                print("Searching")
                results = find_matches(list_items, search)
                while len(results) < 3:
                    results.append("----")
                    
                clr_scrn()
                results = results[0:3]
                print("Results")
                for i in range(page_size):
                    print("{0}.{1}".format(i+1,results[i]))
                
                
                goto = int(input("Enter result number:\n"))
                if goto > 3:
                    warn("You should choose a number between 1 and 3")
                    continue
                elif results[goto-1] == "----":
                    warn("You choose a blank result")
                    continue
                
                clr_scrn()
                print("Please wait...")
                pi = -1
                ii = -1
                for p in pages:
                    pi += 1
                    for i in p:
                        ii += 1
                        if i == results[goto-1]:
                            current_page = pi
                            break
                continue


            except ValueError:
                clr_scrn()
                print("Value error\nthis happened probably\nbecause you didnt\ntype a number\nPRESS EXE\nTO IGNORE")
                continue
            # except Exception as e:
            #     if str(input("error occured!\n1=check output(quits program)\n2=ignore")) == "1":
            #         warn(e)
            #         raise SystemError
            #     continue
        elif user_navigation == "c":
            clr_scrn()
            input(HOWTO)

        if current_page < 0: 
            current_page = 0
            continue
        
        
        if readonly is True: 
            break

        # return picked item    
        try: 
            user_navigation = int(user_navigation)
            picked_item = pages[current_page][int(user_navigation)-1]

            if user_navigation >= 1 or user_navigation <= page_size:
                if picked_item == None or picked_item.strip() == "":
                    warn("Invalid")
                    continue
                else: 
                    if not pick_confirm: return picked_item
                    if ask(pick_confirm_question.format(picked_item), ["yes","no"], prompt=False) == "yes":return picked_item
                    else:continue
            else: 
                continue

        except (ValueError, TypeError, IndexError): 
            continue


if __name__ == "__main__":
    clr_scrn()
    input(add_line_breaks("add line break function makes a line every 20 letters"))
    warn("warning!")
    ask("ask function is a good one")
    view_list(["item 1", "item 2", "item 3", "item 4"])
