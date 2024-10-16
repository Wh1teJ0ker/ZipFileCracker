"""Some utility functions for the zipCracker package to use."""

def _(str: str):
    return str

VER = "0.0.1 20230414"

CREDIT = '''
\033[1m=*= Translator Tools =*=\033[0m
Made by \033[1;36m@Sunnyboy971\033[0m(https://github.com/Sunnyboy971)
'''

WEB = "https://github.com/Sunnyboy971/translator-tools"

CLI = {
    "na": _("Not Available")
}

COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "bold": "\033[1;0m"
}

SHARED = {
    "yesno": [_("No"), _("Yes")],
    "target": _("Target file:"),
    "cnf": _("Command not found."),
    "invalid": _("Invalid input."),
    "argn": _("{} needs an argument."),
    "unknownerror": _("An unknown error just occurred. Please report the problem at your convience on Github."),
    "choice": _("Selection:"),
    "fopened": _("File opened: {}"),
    "fclosed": _("File closed: {}"),
    "faclosed": _("No opened file found."),
    "aoverwrite":_("Do you really want to save directly over {} ?\nThis is considered unsafe, and we suggest using saveas."),
    "overwrite": _("Overwriting existing {} !"),
    "sfinished": _("Successfully write to {}."),
    "finished": _("Operation done."),
    "permission": _("Permission denied. Check if you can access the specified file."),
    "ns": _("{} feature not supported yet. Please keep up with our Github project page for details!"),
    "nm": _("We are still writing help messages for {}. Check it out later!"),
    "total": _("Total:{}")
}

REPLACE = {
    "title": _("Replace"),
    "modelist": [_("Simple"), _("Advanced"), _("Template")],
    "source": _("String to be replaced:"),
    "target": _("Replace to:"),
    "ntodo": _("We have nothing to do currently."),
    "doing": _("Using {0} to replace {1} to {2} ..."),
    "rerror": _("Cannot parse {}. Make sure everything is right."),
    "replaceall": _("Replace all occurences in the file?"),
    "nsf1": _("Multiple {*}s")
}

HELP = {
    "main": _("""
    Available commands:
    help: Display this help message.
    exit: Exit the program.
    about: Show author of the program.
    replace: Enter replace mode.
    [Tip: In the command line, you can go back using ^C.]
    """),
    "replace": _("""
    Available commands in replace mode:
    help: Display this help message.
    exit: Go back to the main menu.
    wizard: Go through the wizard to do what you want to do.
    open: Open the specific file.
    close: Close opened files.
    mode: Choose the replace mode. Available: simple, advanced, template.
    source: Specify the string to be replaced.
    target: Specift the string to be replaced with the source string.
    exec: Execute staged operations to the buffer.
    preview: Preview the changes.
    reveal: Cancel all the changes.
    save: Write changes to the opened file.
    saveas: Write changes to another file specified.
    """)
}

def gethelp(index: str):
    try:
        return HELP[index]
    except KeyError:
        return SHARED["nm"].format(index)

