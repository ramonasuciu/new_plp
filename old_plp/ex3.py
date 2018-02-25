"""
In a CSV ("comma-separated values") file, each record is stored on one line, and fields are separated by commas.
Sometimes, the comma is replaced by another character, so as to avoid potential ambiguity; use a TAB character
('\t' in Python strings).

Python comes with a csv module that handles many of the tasks associated with writing to and reading from CSV files.
For example, you can write to a file with the following:

import csv

with open('/tmp/stuff.csv', 'w') as f:
   o = csv.writer(f)
   o.writerow(range(5))
   o.writerow(['a', 'b', 'c', 'd', 'e'])

For this exercise, create a program that reads from one CSV file (/etc/passwd), and writes to another one.
You are to read from /etc/passwd, and produce a file whose contents are the username (index 0) and the user ID (index 2)
Note that a record may contain a comment, in which it will not have anything at index 2; you should take that into
consideration when writing the file.  The output file should use TAB characters to separate the elements.

Thus, the input will look like:

root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
_ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
"""
import csv
import sys
from ex1 import read_passwd_file

passwd_data = read_passwd_file(path_to_file=sys.argv[1])
csv.register_dialect('tab_dialect', delimiter='\t', quoting=csv.QUOTE_NONE)


with open('/Users/ramona/Desktop/stuff.csv', 'w') as f:
    writer = csv.writer(f, dialect='tab_dialect')
    for item in passwd_data:
        writer.writerow(item)
