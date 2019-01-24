'''
Print the single-line comments, multi-line comments and the data
in order of their occurrence from top to bottom in the snippet.
'''
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment\n", data, sep="")
        else:
            print(">>> Single-line Comment\n", data, sep="")

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data\n", data, sep="")


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

'''
Sample Input
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->

Sample Output
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
'''
