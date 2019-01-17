"""

Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""

N, M = int(input()), int(input())

for i in range(int((N - 1) / 2)):
    print((".|." * (2 * i + 1)).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in reversed(range(int((N - 1) / 2))):
    print((".|." * (2 * i + 1)).center(M, "-"))
