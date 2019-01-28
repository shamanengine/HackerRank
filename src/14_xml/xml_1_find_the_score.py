'''
Input Format
The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format
Output a single line, the integer score of the given XML document.
'''

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    print(node.tag, node.attrib)
    for child in node:
        print(child.tag, child.attrib)

    return len(node.attrib) + sum([len(child.attrib) for child in node])

'''
Input
11
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>

Expected Output
8
'''

if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    xml1 = '''
    <feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
    </feed>
    '''
    xml2 = '''
    <feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
        <entry>
  	        <author gender='male'>Harsh</author>
            <question type='hard'>XML 1</question>
            <description type='text'>This is related to XML parsing</description>
        </entry>
    </feed>
    '''
    tree = etree.ElementTree(etree.fromstring(xml1))
    root1 = tree.getroot()
    print(get_attr_number(root1))
    print(get_attr_number(etree.ElementTree(etree.fromstring(xml2)).getroot()))

'''
Sample Input
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output
5
'''