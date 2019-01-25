import re

pattern = r'((#[0-9A-Fa-f]{6})|(#[0-9A-Fa-f]{3}))'
open = False

for i in range(int(input())):
    s = input()

    if re.search(r'.*{$', s):
        open = True
        continue

    if not open:
        continue
    else:
        hexes = re.findall(pattern, s)
        for hex in hexes:
            print(hex[0])

    if re.search(r'.*}$', s):
        open = False

'''
35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}
'''

'''



14
.stitched {
   padding: 20px;
   margin: 10px;
   background: #ff0030;
   color: #fff;
   font-size: 21px;
   font-weight: bold;
   line-height: 1.3em;
   border: 2px dashed #fff;
   border-radius: 10px;
   box-shadow: 0 0 0 4px #ff0030, 2px 1px 6px 4px rgba(10, 10, 0, 0.5);
   text-shadow: -1px -1px #aa3030;
   font-weight: normal;
}

Expected Output
#ff0030
#fff
#fff
#ff0030
#aa3030
'''

'''    
Sample Input
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   

Sample Output
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
'''
