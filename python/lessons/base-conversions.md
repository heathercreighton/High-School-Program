---
title: "base-conversions"
type: "lesson"
---
# Base Introduction

Our everyday number system is a Base-10 system. The Base-10 number system is known as the decimal system and has 10 digits to show all numbers `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`.

We do not have a single-digit numeral for "ten". (The Romans did, in their character "X".) Yes, we write "10", but this stands for "1 ten and 0 ones". This is two digits; we have no single solitary digit that stands for "ten".

Instead, when we need to count to one more than nine, we zero out the ones column and add one to the tens column. When we get too big in the tens column — when we need one more than nine tens and nine ones ("99"), we zero out the tens and ones columns, and add one to the ten-times-ten, or hundreds, column.

The only reason base-ten math seems "natural" and the other bases don't is that you've been doing base-ten since you were a child. And (nearly) every civilization has used base-ten math probably for the simple reason that we have ten fingers. If instead we lived in a cartoon world, where we would have only four fingers on each hand (count them next time you're watching TV or reading the comics), then the "natural" base system would likely have been base-eight, or "octal".

##Binary

Let's look at base-two, or binary, numbers. How would you write, for instance, 1210 ("twelve, base ten") as a binary number? You would have to convert to base-two columns, the analogue of base-ten columns. In base ten, you have columns or "places" for 100 = 1, 101 = 10, 102 = 100, 103 = 1000, and so forth. Similarly in base two, you have columns or "places" for 20 = 1, 21 = 2, 22 = 4, 23 = 8, 24 = 16, and so forth.

| Binary | Decimal | Expansion |
| --- | --- | --- |
| 

0

 | 

0

 | 

0 ones

 |
| 

1

 | 

1

 | 

1 one

 |
| 

10

 | 

2

 | 

1 two and 0 ones

 |
| 

11

 | 

3

 | 

1 two and 1 one

 |
| 

100

 | 

4

 | 

1 four, 0 twos, and 0 ones

 |
| 

101

 | 

5

 | 

1 fours, 0 twos, and 1 one

 |
| 

110

 | 

6

 | 

1 four, 0 twos, and 1 one

 |
| 

111

 | 

7

 | 

1 eight, 0 fours, 0 twos, and 0 ones

 |
| 

1000

 | 

8

 | 

1 eight, 0 fours, 0 twos, and 1 ones

 |
| 

1001

 | 

9

 | 

1 eight, 0 fours, 1 twos, and 0 ones

 |
| 

1010

 | 

10

 | 

1 eight, 0 fours, 1 twos, and 1 ones

 |
| 

1011

 | 

11

 | 

1 eight, 1 fours, 0 twos, and 0 ones

 |
| 

1100

 | 

12

 | 

1 eight, 1 fours, 0 twos, and 1 ones

 |
| 

1101

 | 

13

 | 

1 eight, 1 fours, 1 twos, and 0 ones

 |
| 

1110

 | 

14

 | 

1 eight, 1 fours, 1 twos, and 0 ones

 |
| 

1111

 | 

15

 | 

1 eight, 1 fours, 1 twos, and 1 ones

 |
| 

10000

 | 

16

 | 

1 sixteen, 1 eight, 0 fours, 0 twos, and 0 ones

 |

The following table can help with the conversion from binary to decimal.

| 

Binary Number

 |  |  |  |  |  |  |  |  |
|  | 

27

 | 

26

 | 

25

 | 

24

 | 

23

 | 

22

 | 

21

 | 

20

 |
|  | 

128

 | 

64

 | 

32

 | 

16

 | 

8

 | 

4

 | 

2

 | 

1

 |
| 

Decimal Number

 |  |  |  |  |  |  |  |  |

To convert 101110102 to decimal, you first need to place each binary digit in a separate column.

| Binary Number | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 

27

 | 

26

 | 

25

 | 

24

 | 

23

 | 

22

 | 

21

 | 

20

 |
|  | 

128

 | 

64

 | 

32

 | 

16

 | 

8

 | 

4

 | 

2

 | 

1

 |
| 

Decimal Number

 |  |  |  |  |  |  |  |  |

Then multiply each binary digit with the corresponding 2n.

| Binary Number | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 

27

 | 

26

 | 

25

 | 

24

 | 

23

 | 

22

 | 

21

 | 

20

 |
|  | 

128

 | 

64

 | 

32

 | 

16

 | 

8

 | 

4

 | 

2

 | 

1

 |
| 

Decimal Number

 | 

128

 | 

0

 | 

32

 | 

16

 | 

8

 | 

0

 | 

2

 | 

0

 |

Then add all of the numbers of the last row.

`128+0+32+16+8+0+2+0` which equals `186`.

This means 101110102 equals 18610.

##Hexadecimal

In this activity, you will learn convert from one base to another using Python. We are going to create a program to convert hex (base-16) to binary (base-2). In your project called Cryptography, create a base _conversion file. Hexadecimal in relation to decimal (base-10) counting from zero upward

| 

Hexadecimal

 | 

Decimal

 |
| 

0

 | 

0

 |
| 

1

 | 

1

 |
| 

2

 | 

2

 |
| 

3

 | 

3

 |
| 

4

 | 

4

 |
| 

5

 | 

5

 |
| 

6

 | 

6

 |
| 

7

 | 

7

 |
| 

8

 | 

8

 |
| 

9

 | 

9

 |
| 

A

 | 

10

 |
| 

B

 | 

11

 |
| 

C

 | 

12

 |
| 

D

 | 

13

 |
| 

E

 | 

14

 |
| 

F

 | 

15

 |

##Hexadecimal to Binary

| 

Hexadecimal

 | 

Binary

 |
| 

0

 | 

0000

 |
| 

1

 | 

0001

 |
| 

2

 | 

0010

 |
| 

3

 | 

0011

 |
| 

4

 | 

0100

 |
| 

5

 | 

0101

 |
| 

6

 | 

0110

 |
| 

7

 | 

0111

 |
| 

8

 | 

1000

 |
| 

9

 | 

1001

 |
| 

A

 | 

1010

 |
| 

B

 | 

1011

 |
| 

C

 | 

1100

 |
| 

D

 | 

1101

 |
| 

E

 | 

1110

 |
| 

F

 | 

1111

 |

Example of `A1F5` to Binary

| `A` | `1` | `F` | `5` |
| --- | --- | --- | --- |
| 

`1010`

 | 

`0001`

 | 

`1111`

 | 

`0101`

 |

So, `A1F5` equates to `1010000111110101`.

Create a function, `hex _to _bin(hexstring)`, that will take in a string of hexadecimal, and return the binary equivalent!

print(hex_to_bin('A1F5'))
Output: `1010000111110101`