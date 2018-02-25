"""
The challenge for this exercise is to write a version of wc (word count) in Python.
However, your version of wc will return four different types of information about the files:

Number of characters (including whitespace)
Number of words (separated by whitespace)
Number of lines
Number of unique words

The program should ask the user for the name of an input file, and then produce output for that file.
"""
import sys

if len(sys.argv) < 2:
    print("You must provide the path to the text file to read data from!")


def word_count(path_to_file):
    data_dict = {}
    with open(path_to_file, "r") as f:
        data_dict['number_of_chars'] = len(f.read())
        f.seek(0)
        data_dict['number_of_words'] = len(f.read().split())
        f.seek(0)
        data_dict['number_of_lines'] = len(f.readlines())
        f.seek(0)
        data_dict['number_of_unique_words'] = len(set(f.read().split()))
    return data_dict

print(word_count(input("Please provide path to file to read data from: ")))
