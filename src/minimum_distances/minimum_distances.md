# Minimum Distances
We define the distance between two array values as the number of indices between the two values. Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, print -1.

For example, if a = [3, 2, 1, 2, 3], there are two matching pairs of values: 3 and 2. The indices of the 3's are i = 0 and j = 4, so their distance is d[i, j] = |j - i| = 4. The indices of the 2's are i = 1 and j = 3, so their distance is d[i, j] = |j - i| = 2.

## Function Description

Complete the minimumDistances function in the editor below. It should return the minimum distance between any two matching elements.

minimumDistances has the following parameter(s):
- a: an array of integers
## Input Format

The first line contains an integer n, the size of array a. 
The second line contains n space-separated integers a[i].

## Constraints
- 1 <= n <= 10^3
- 1 <= a[i] <= 10^5

## Output Format

Print a single integer denoting the minimum  in . If no such value exists, print .

## Sample Input

6
7 1 3 4 1 7

## Sample Output

3

## Explanation
 
Here, we have two options:
- a[1] and a[4] are both 1, so a[1, 4] = |1 - 4| = 3.
- a[0] and a[5] are both 7, so d[0, 5] = |0 - 5| = 5.
The answer is min(3, 5) = 3.

## Test Cases

### Case 1

**Input:**
500
20 760 143 550 365 559 539 299 160 955 706 462 329 786 989 867 47 648 171 369 625 975 538 532 973 25 515 395 724 487 618 745 247 113 647 612 24 186 263 537 493 321 999 174 108 988 394 507 988 917 228 613 892 118 497 218 144 13 613 220 500 583 965 748 49 613 712 73 151 976 610 997 297 961 171 757 949 565 616 937 483 844 903 727 963 400 945 459 765 910 31 266 494 997 366 895 962 78 968 465 406 931 814 56 892 338 813 194 255 782 483 90 626 386 818 941 139 115 752 904 26 784 522 872 133 888 767 447 967 87 264 725 370 79 781 263 417 947 809 672 729 292 763 355 31 933 649 522 48 401 426 426 537 301 650 670 189 769 469 508 857 734 234 227 813 15 842 582 314 651 606 43 296 721 751 679 654 400 201 55 153 979 481 691 280 484 713 470 253 183 978 462 269 564 690 434 580 884 16 894 536 622 290 184 696 41 863 350 441 64 757 946 395 239 989 676 75 703 498 328 238 828 791 507 393 833 941 325 717 309 571 605 283 861 141 979 902 4 682 695 420 439 642 816 30 631 844 105 686 342 786 276 170 577 135 915 762 428 240 831 737 812 437 373 673 930 352 928 935 34 623 707 826 617 523 856 601 719 314 287 413 100 916 584 677 51 499 791 480 92 622 569 904 411 942 577 342 647 857 629 33 481 336 859 450 212 716 51 931 30 691 345 130 607 281 159 10 132 302 490 224 924 60 480 336 354 410 30 1 267 659 35 100 347 894 551 911 962 602 195 344 293 892 474 252 173 985 263 657 639 105 234 564 165 714 252 872 124 634 873 744 293 908 844 992 803 395 904 765 998 99 462 643 991 936 248 516 274 863 525 913 968 759 829 486 826 81 358 302 67 231 46 360 140 891 705 295 286 609 412 636 60 874 632 403 163 232 919 789 95 796 54 63 556 884 901 734 317 259 36 385 491 83 97 983 326 154 630 964 763 42 953 175 269 585 578 432 817 849 573 264 998 627 327 906 511 229 640 181 840 676 918 683 111 15 666 789 170 648 754 285 43 707 813 312 644 743 96 813 945 669 77 943 296 404 849 160 985 489 693 826 517 611 509 981 978 528 770 148 528 524 786 571 583 951 883 227 694 979 40

**Output:**
1