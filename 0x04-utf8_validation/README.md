<!-- repo image -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/Abubacer/README-Template/blob/master/images/banner.png" alt="IMG" 
  </a>

<h1 align="center"></h1>
<div align="left">
<br />

# 0x04. UTF-8 Validation 

## Learning Objectives

At the end of this project, we are expected to be able to learn:

- UTF-8 encoding
- UTF-8 Validation

## Requirements


  -  Allowed editors: vi, vim, emacs
  -  All files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
  -  All files should end with a new line
  -  The first line of all files should be exactly #!/usr/bin/python3
  -  A ```README.md``` file, at the root of the folder of the project, is mandatory
  -  The code should use the PEP 8 style (version 1.7.x)
  -  All files must be executable

### subhead 2
Write a method that determines if a given data set represents a valid UTF-8 encoding.

  - Prototype: ```def validUTF8(data)```
  - Return: ```True``` if data is a valid UTF-8 encoding, else return ```False```
  - A character in UTF-8 can be 1 to 4 bytes long
  - The data set can contain multiple characters
  - The data will be represented by a list of integers
  - Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

```
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
```

```
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

</div>
