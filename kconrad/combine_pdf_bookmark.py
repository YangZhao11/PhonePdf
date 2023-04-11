#!/usr/bin/python3

import sys
import subprocess
import re

def NumPages(lines):
    regex = re.compile(r'^NumberOfPages: (.*)')
    for line in lines:
        x= regex.match(line)
        if x:
            return int(x.group(1))

def Bookmarks(lines, offset):
    title_re = re.compile(r'^BookmarkTitle: (.*)')
    page_re = re.compile(r'^BookmarkPageNumber: (.*)')
    result = []
    for line in lines:
        title = title_re.match(line)
        if title:
            matched = title.group(1)
            continue
        page = page_re.match(line)
        if page:
            page_int=int(page.group(1))+offset
            result.append(f'[/Title ({matched}) /Page {page_int} /OUT pdfmark')
    return(result)

filetitle = {}
with open('index_cleaned.txt') as index_file:
    for line in index_file:
        x=line.rstrip().split(" ", 1)
        if len(x) > 1:
            filetitle[x[0]] = x[1]

counter=1
for f in sys.argv[1:]:
    info = subprocess.run(['pdftk', f, 'dump_data_utf8'], stdout=subprocess.PIPE)
    lines = info.stdout.decode('utf-8').split("\n")
    pages = NumPages(lines)
    bookmarks = Bookmarks(lines, counter-1)
    title = filetitle[f] or f
    print(f"[/Count -{len(bookmarks)} /Title ({title}) /Page {counter} /OUT pdfmark")
    for b in bookmarks:
        print(b)
    counter += pages
