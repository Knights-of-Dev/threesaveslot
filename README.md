# Threesaveslot


## Install

```
pip install threesaveslot
```

or

```
python -m pip install --user threesaveslot
```


## Documentation


### To make a save file
```Python
createsavefile(name)
```
name: the string that the file will be named, if left blank it will be named savefile

This function makes a file to save stuff in.

### To save
```Python
basicsave(listtosave, filename)
```
filename: the string that the program will look for when finding a file, do not include .json, leave it blank for looking for a file named savefile

listtosave: set this equal to the list you want to save, leave blank for the basic save list.

This function saves a list of varibles to a save file.

### To load
```Python
basicload(listtoload, filename)
```
filename: the string that the program will look for when finding a file, do not include .json, leave it blank for looking for a file named savefile

listtoload: set this equal to the list you want to load, leave blank for the basic save list.

This function loads the varibles from the save file. If your using the built in save list then leave listtoload blank, the code will set the savelist to the loaded list. If your using a custom list then set listtoload to the list. **Instead of setting the list it will return it!** 

