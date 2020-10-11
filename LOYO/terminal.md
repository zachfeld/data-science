# File Explorers and Shell Commands (Terminal and Finder)

## Quick note about 'Unix'

This guide might reference 'Unix' based systems. What that refers to is both mac and linux machines, as their terminals descend from the same base.

## What is a GUI?

GUI stands for `Graphical User Interface`, and if you've navigated to this page on your computer you've used one before. GUI encompasses every graphic you can click on during your computer session to activate a task. Behind the scenes the operating system is executing commands with the help the graphics you press on.

## Why Command Line? I like my GUI!

The command line provides benefits that the normal GUI of a file system can not provide. The main attraction here is the additional speed a user can achieve when becoming comfortable with the commands at their disposal. Being comfortable in a command line environment will exponentially increase your work productivity!

## What is a folder tree / hierarchy

The folder hierarchy is the structure of how folders and files are stored & displayed in an operating system. Starting from a root directory, folders encapsulate files and other folders, and a tree-like structure is made

### Example Tree

```bash
    Desktop/
    ├── CS230
    ├── MA347
    │   └── homework1.py
    └── favorite_songs.txt

    2 directories, 2 files
```

## What is a file path & how to express it

A file path can either be absolute (meaning that it begins at the root directory), or it can be a relative portion of a reference starting from a specific directory.

It specifies either a directory or a specific file, and it serves as a way to identify where information exists on a machine

On unix based systems, file paths are displayed as such:
`/{dir}/{dir}/{dir/file}`

Example:
`/Users/zach/Desktop/MA347/homework1.py`

All drives are mounted into a single unified path, which is called **root** and it is represented by the forward slash: `/`

## Navigating in the Terminal

### How to open the terminal app (on a mac)

To open the terminal, you can move your cursor to the top right hand corner of the screen and do a spotlight search for **Terminal**  

Alternatively, you can activate the spotlight search by shortcut: `[⌘ + space]`

### How to Navigate to your home folder

#### Termimal

On unix based systems, the home directory is represented as: `~`  

To get to the home folder using the terminal, you can execute one of two commands: `cd` or `cd ~`

#### Finder
Open a the finder context from the dock of your computer, then type the shortcut `⇧⌘H` to bring up the home folder

### How to move up & down the folder hierarchy

#### Terminal

`cd ..` moved back one folder in the working directory  

`cd {directory name}` moves forward one directory  
ex. from the home folder: `cd Desktop`  

`cd {full path}` moves the terminal to the specified location, regardless of where you currently are located  
ex. full path to desktop: `/Users/zach/Desktop`

#### Finder

You can double click directories in the finder window to move up, and use the arrows in the top left corner to move backwards in the hierarchy

### How to copy or move a file

#### Terminal

`cp {source file path} {destination directory path}` copies a file to the destination directory

ex. copy homework to another file for editing: 
`cp /Users/zach/Desktop/MA347/homework1.py /Users/zach/Desktop/MA347/homework1_copy.py`

The syntax is the same for moving a file, instead of `cp` you can specify `mv`

#### Finder

From the finder window you can right click any directory or file you would like to copy and select `copy`, then right click on any open space in the finder pane and `paste` the file or directory

You can then drag the file anywhere you would like it to go. Your desktop, for example

### How to remove files

`rm {filename}` removes a specified file (you can use absolute path or relative if you are in the same directory as the file

ex. from the MA347 directory: `rm homework1_copy.py`

**DANGER!** you can remove directories in the command line by recursively deleting their contents, but this is dangerous! One small typo and your entire operating system can be wiped out!

### How to list all files in current folder

`ls` lists all files in the current terminal directory  
`ls -l` lists the files in the current terminal directory in alphabetical list format (with access level & ownership)  
`ls -la` lists all files as above, but also includes hidden files like dotfiles  

### How to view contents of a text file

`cat {filename/path}` prints the contents of a text file to the terminal  
`head {filename/path}` prints the first lines of a text file to the terminal  
`tail {filename/path}` prints the last lines of a text file to the terminal  

## What happens when you double-click a file in finder

The operating system looks at the file extention of the file, and it matches the type of program it deems as best suitable to run or open the file.

## What do file extensions do & when can you change them

File extensions are used by the operating system to figure out how to open a given file. If you understand how your data is stored, you can change file extensions. But, buyer beware that changing the file extension of a file can cause issues if you don’t fully understand what kind of data exists in your file. When you change a file extension, it doesn’t actually change the ‘data’ of the file so to speak. That is to say, if you change the extention and change it back your data should be safe in most cases.

However, there is an example specific to this class that may be useful. If you wrote a python script `.py file` that you want to convert into a notebook `.ipynb file`, you can not change the extention and expect it to run in a program like jupyter. the data that an `.ipynb` file contains is different than a traditional python file, and the conversion would cause problems.
