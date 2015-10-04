# mkpkg
mkpkg is just like mkdir, but includes an \_\_init\_\_.py file that includes the date of creation in a comment,
and optionally a docstring.

This tool adds mkpkg script to your command line. 

## Installation 

````
pip install https://github.com/Technigami/pymkpkg/archive/master.zip
````


## Usage

```
mkpkg [directory] -m (optional argument adds to the packages' docstring)
```

- Makes a directory with an \_\_init\_\_.py file that includes the current date in a comment.  
- Optionally includes a -m argument which adds a docstring with that comment in it. 
