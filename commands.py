import String_methodes as sm

CHARACTERS = {'*/33': '!',
'*/34': '"',
'*/35': '#',
'*/36': '$',
'*/37': '%',
'*/38': '&',
'*/39': "'",
'*/40': '(',
'*/41': ')',
'*/42': '*',
'*/43': '+',
'*/44': ',',
'*/45': '-',
'*/46': '.',
'*/47': '/',
'*/58': ':',
'*/59': ';',
'*/60': '<', 
'*/61': '=', 
'*/62': '>', 
'*/63': '?', 
'*/64': '@', 
'*/91': '[', 
'*/92': '\\', 
'*/93': ']', 
'*/94': '^', 
'*/95': '_', 
'*/96': '`', 
'*/123': '{',
'*/124': '|',
'*/125': '}',
'*/126': '~'}

HELP_EDIT = {
    "!e" : "edit a specific line",
    "!h" : "show help menu",
    "!v" : "view text",
    "!r" : "run text as python commands",
    "!q" : "exit editor without saving",
    "!hc" : "show character help",
    "!-" : "remove the last line",
}

print("Command Line!")

def find_key_from_value(dictionary, value_as_a_key):
    for key in list(dictionary.keys()):
        if dictionary[key] == value_as_a_key:
            return key

def replace_with_char(stre):
    code = []
    for line in stre.splitlines():
        for key in list(CHARACTERS.keys()):
            line = line.replace(key, CHARACTERS[key])
        code.append(line)
    return "\n".join(code)

while True:
 cmd = str(input(">"))
 if cmd.startswith("!") is False:
  try:exec(cmd, {})
  except Exception as e:print(e)
 else:
  if cmd == "!edit":
   text = []
   while True:
    sm.clr_scrn()
    for i in range(len(text)):
     print("{0}|{1}".format(i+1, text[i]))
    print("__!h for help__")
    line = str(input("{}|".format(len(text)+1)))
    if not line.startswith("!"): 
     text.append(replace_with_char(line))
     continue
    
    if line == "!h":
     x = sm.view_list(list(HELP_EDIT.keys()), pick_confirm=False)
     sm.warn(HELP_EDIT[x])
    elif line == "!hc":
     x = sm.view_list(list(CHARACTERS.values()), pick_confirm=False)
     sm.warn(find_key_from_value(CHARACTERS,x)) 
    elif line == "!e":
     x = sm.view_list(text, title="PICK LINE TO EDIT", pick_confirm=False) 
     y = str(input("{}|".format(text.index(x)+1)))
     text.insert(text.index(x), y)
     text.remove(x)
    elif line == "!-":
      text.remove(sm.view_list(text, title="PICK LINE TO REMOVE", pick_confirm=False))
    elif line == "!v":
      sm.view_list(text, title="PREVIEW", readonly=True)
    elif line == "!q":
      break
    elif line == "!r":
      try:exec("\n".join(text))
      except Exception as e:sm.warn(e)
      continue




