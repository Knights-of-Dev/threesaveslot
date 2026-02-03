"""
moduleName.py

This is where all the functions, classes, variables, etc lie in your custom module.
"""
import json


savelist = []


def createsavefile(name = "savefile"):
  open(name, "x")


def basicsave(listtosave = savelist, filename = "savefile"):
  filename = str(filename)
  with open(str(filename + ".json"), "w") as f:
    json.dump(listtosave, f)


def basicload(listtoload = "savelist", filename = "savefile"):
  filename = str(filename)
  global savelist
  if listtoload == "savelist":
    open(filename + ".json") as f:
      savelist = json.load(f)
  else:
    open(filename + ".json") as f:
      return json.load(f)
  
