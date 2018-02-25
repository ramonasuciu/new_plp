"""
JSON (JavaScript Object Notation) is an increasingly popular format for data exchange.
It is compatible with a large number of programming languages, it's lightweight, and it's easy to validate.
Python's json module lets us read JSON easily with the json.load function.

In this exercise, you are analyzing test data in a high school.
Test scores are in a set of files in the `scores` directory; each file represents the scores for one class,
and contains JSON. Thus, if we are trying to analyze the scores from class 9a, the scores would be in a file called
'9a.json`:

[{"math" : 90, "literature" : 98, "science" : 97},
{"math" : 65, "literature" : 79, "science" : 85},
{"math" : 78, "literature" : 83, "science" : 75},
{"math" : 92, "literature" : 78, "science" : 85},
{"math" : 100, "literature" : 80, "science" : 90}
]

The directory may also contain files for 10th grade (10a.json, 10b.json, and 10c.json), and other grades and classes in
the high school.

Note that valid JSON uses double quotes ("), not single quotes ('). This can be surprising and frustrating for Python
developers to discover!  Also notice that the file contains the JSON equivalent of a list of dicts.

For this exercise, you must summarize, for each class, the highest, lowest, and average test scores for each subject.
Given two files (9a.json and 9b.json) in the scores directory, we would see the following output:

scores/9a.json
   science: min 75, max 97, average 86.4
   literature: min 78, max 98, average 83.6
   math: min 65, max 100, average 85.0
scores/9b.json
   science: min 35, max 95, average 82.0
   literature: min 38, max 98, average 72.0
   math: min 38, max 100, average 77.0

"""
import os
import sys
import json
from collections import defaultdict


path_to_json_dir = sys.argv[1]
folder_name = path_to_json_dir.split("/")[-1]

json_files = [pos_json for pos_json in os.listdir(path_to_json_dir) if pos_json.split('.')[-1] == 'json']


def merge_dicts(*dict_args):
    result = defaultdict(list)

    for dictionary in dict_args:
        for x, y in dictionary.items():
            result[x].append(y)
    return result


def grade_info(dictionary, grade_compare):
    for key in dictionary.keys():
        if grade_compare.lower() == 'max':
            return key, max(dictionary[key])
        elif grade_compare.lower() == 'min':
            return key, min(dictionary[key])
        elif grade_compare.lower() == 'average':
            return key, sum(dictionary[key])/len(dictionary[key])


def print_data(info):
    for json_file in json_files:
        data = json.load(open("{}/{}".format(path_to_json_dir, json_file)))
        print("{}/{}".format(folder_name, json_file))
        class_info = merge_dicts(*data)
        return grade_info(class_info, info)

maximum = print()





