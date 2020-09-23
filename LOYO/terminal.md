# File Explorers and Shell Commands (Terminal and Finder)

## What is a folder tree / hierarchy

The folder hierarchy is the structure of how folders and files are stored & displayed in an operating system. Starting from a root directory, folders encapsulate files and other folders, and a tree-like structure is made

### Example Tree

```bash
    ExampleTree/
    ├── ThisIsAFolder
    ├── ThisIsAnotherFolder
    │   └── example_file
    └── example_text

    2 directories, 2 files
```

## What is a file path & how to expresss it

A file path can either be absolute (meaning that it begins at the root directory), or it can be a relative portion of a reference starting from a specific directory.

It specifies either a directory or a specific file, and it serves as a way to identify where information exists on a machine

On unix based systems, file paths are displayed as such:
`/{dir}/{dir}/{dir/file}`

All drives are mounted into a single unified path, which is called **root** and it is represented by the forward slash: `\`

## Navigating in the Terminal

### How to Navigate to your home folder

On unix based systems, the home directory is represented as: `~`  

to get to the home folder using the terminal, you can execute one of two commands: `cd` or `cd ~`

### How to move up & down the folder hierarchy

`cd ..` moved back one folder in the working directory  
`cd {directory name}` moves forward one directory  
`cd {full path}` moves the terminal to the specified location, regardless of where you currently are located  

### How to copy or move a file

`mv {source file path} {destination directory path}` moves a file to the destination directory  
`cp {source file path} {destination directory path}` copies a file to the destination directory  

### How to list all flies in current folder

`ls` lists all files in the current terminal directory  
`ls -l` lists the files in the current terminal directory in alphabetical list format (with access level & ownership)  
`ls -la` lists all files as above, but also includes hidden files like dotfiles  

### How to view contents of a text file

`cat {filename/path}` prints the contents of a text file to the terminal  
`head {filename/path}` prints the first lines of a text file to the terminal  
`tail {filename/path}` prints the last lines of a text file to the terminal  

## What happens when you double-click a file in finder

The operating system looks at the file type from the headers of the metadata on the file, and it matches the type of program it deems as best suitable to run or open the file

## What do file extensions do & when can you change them

File extensions are used by the operating system to figure out how to open a given file. If you understand how your data is stored, you can change file extensions. But, buyer beware that changing the file extension of a file can cause issues if you don’t fully understand what kind of data exists in your file. When you change a file extension, it doesn’t actually change the ‘format’ of the file so to speak.

On a mac, file extensions aren’t actually particularly necessary, because when the OS goes to open the file, it looks at the metadata of the file, particularly the header of the file to see what the type of file is. So, if you're working with rich data and you change the extension, you likely aren’t doing much to change the file.
