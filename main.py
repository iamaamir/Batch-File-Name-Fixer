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


# this is the way of doing the same thing with regex
# but beware of "\" while using this

# import re
# invalid_chars = re.compile("[^a-zA-z\d\s\._]")
# path = input("Enter the Folder path: ")
# dir_list = listdir(path)
# total_files = len(dir_list)
# total_renamed = 0

# chdir(path)
# for name in dir_list:
#     new_name = re.sub(invalid_chars, "", name).replace(' ', '_')
#     if name != new_name:
#         rename(name, new_name)
#         total_renamed += 1


# # Final Verification
# print('Number of files present initially: ', total_files)
# print('Number of file Renamed: ', total_renamed)
# print('Difference: ', (total_files - total_renamed))
