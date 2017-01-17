#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir, chdir, rename

valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789._'
path = input("Enter Folder path: ")
dirlist = listdir(path)
total_files = len(dirlist)
renamed = 0

chdir(path)
for filename in dirlist:
    name = ''
    for char in filename:
        if char.lower() in valid_chars:
            name += char
        else:
            if char == ' ':
                name += '_'

    if name != filename:
        rename(filename, name)
        renamed += 1

# Final Verification
print('Number of files present initially: ', total_files)
print('Number of file renamed: ', renamed)
print('Difference: ', (total_files - renamed))
