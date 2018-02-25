"""
This exercise assumes that you have access to a copy of /etc/passwd, the file in which basic user information is stored
on Unix computers. If you don't, then you can likely find such a file by searching for "/etc/passwd example" on the Web.

The format is:

nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false

In other words, each line is a set of fields, separated by colon (:) characters. The first field is the username, and
the third field is the ID of the user. The nobody user has ID -2, the root user has ID 0, and the daemon user has ID 1.
You can ignore all but the first and third fields in the file.

There is one exception to this format: A line that begins with a # character is a comment,
and should be ignored by the parser.

For this exercise, you must create a dictionary based on /etc/passwd,
in which the dict's keys are usernames and the values are the numeric IDs of those users.
You should then iterate through this dict, displaying one username and user ID on each line in alphabetical order.

"""

import sys
import operator

if len(sys.argv) < 2:
    print("You must specify the path of the passwd example file to read from!")

passwd_dict = {}


def read_passwd_file(path_to_file):
    with open(path_to_file, "r") as f:
        for line in f.readlines():
            if not line.startswith("#"):
                line_list = line.split(":")
                passwd_dict.update({line_list[0]: line_list[2]})
    return sorted(passwd_dict.items(), key=operator.itemgetter(0))

for item in read_passwd_file(sys.argv[1]):
    print(item)
