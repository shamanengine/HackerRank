'''
Input Format
The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format
Output a single line, the integer value of the maximum level of nesting in the XML document.
'''

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    # your code goes here
    '''
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
    '''
    maxdepth = level
    # print(etree.tostring(elem))
    parser = etree.XMLPullParser(['start', 'end', 'start-ns', 'end-ns'])
    parser.feed(etree.tostring(elem))
    # print(parser)
    for (event, elem) in parser.read_events():
        # print(elem)
        if event == 'start':
            level += 1
            if level > maxdepth: maxdepth = level
        elif event == 'end':
            level -= 1
    return



if __name__ == '__main__':
    '''
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    '''
    xml = '''
    <feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
    </feed>
    '''
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

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
1

'''
