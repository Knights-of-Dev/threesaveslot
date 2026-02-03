"""
moduleName.py

This is where all the functions, classes, variables, etc lie in your custom module.
"""

savelist = []


def createsaveslot(name = "savefile"):
  open(name, "x")


def basicsave(listtosave = savelist, filename = "savefile"):
  filename = str(filename)
