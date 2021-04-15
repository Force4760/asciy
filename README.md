# ASCIY
A python Command Line Tool to turn images into ASCII Art.

## ASCII

Ascii is a standard for encoding characters in eletronic comunication.

## Install

**I'm still trying to make this into a pypi package**

### Prerequisites
* Python 3
* Pip
* Python Pillow package

To install this tool, clone this git repo and install it using:

``` 
pip3 install -e .
```

## Usage
Open the terminal and run the *asciy* command.

```
asciy path -w=new_width -chars=abcdefghij
```


* **path:** path to the image
                
    * if path is a folder all images inside will be transformed

* **Flags:**            
    * **-w:** if specified the image will be resized to that width

    * **-chars:** if specified the characters provided will be used to draw the image                                                                                                                  

