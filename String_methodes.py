
def clr_scrn():
    '''clears screen by making new lines'''    
    print("\n"*7)






def add_line_breaks(string, every=20):
    """
    This function takes a string and puts "/n" every 20 letters.

    Args:
      string: The string to add line breaks to.
      every: break line every number of letters

    Returns:
      A new string with line breaks added every 20 letters.
    """
    string = string.strip()

    new_string = ""
    for i in range(len(string)):
        if i % every == 0: # if index is divisable by 20
            new_string += "\n" if string[i] in [" ", ".", ","] else "-\n"
        new_string += string[i]
    result = "\n".join(new_string.strip().split("\n")).strip()
    result2 = [i.strip() for i in result.split("\n")]
    return "\n".join(result2)[1:]


def warn(message, auto_break_lines = True, auto_break_lines_every= 20, title = None, clear_screen = True):
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

def ask(question, ans = None, auto_break_lines = True, auto_break_lines_every = 20, prompt = True):
    '''just like warn but instead asks the user for an input of number like choosing an option

    Args:
        question (str): the question to ask
        ans (list, optional): an list of all answers (recommended max: 3-4 answers). Defaults to ["yes","no"].
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.

    Returns:
        str: the answer choosen not the index
    '''    
    if ans is None:
        ans = ["yes","no"]
    while True:
        
        if prompt:warn("{question}\n\npress exe".format(question=question), auto_break_lines, auto_break_lines_every)
        else:print(add_line_breaks(question))

        print("-", end="")
        try: user_input = int(input("{}\n".format("\n-".join(ans))))
        except (ValueError,TypeError): continue

        try: user_input -= 1
        except TypeError: continue

        if user_input < 0:
            continue
        clr_scrn()
        try: return ans[user_input]
        except IndexError: continue

def view_list(list_items, page_size=3, pick_confirm=True, pick_confirm_question="you picked {}\n you sure?", readonly=False, title="--------"):
    current_page = 0 # used for navigation and generating pages
    controls = "+:nxt -:prv|pg:{}"
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
                print("{number}) {item}".format(number=i+1, item=pages[current_page][i]))
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
            continue

        if current_page < 0: 
            current_page = 0
            continue
        
        # return picked item
        if readonly is True: 
            break

            
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