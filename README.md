# SevenSegmentDisplay

This is a 7 segment display library for Raspberry Pi.

## How to use

Initialize SevenSegment with pins number array like 
```d = SevenSegment([11,12,13,15,16,18,22,23])```

The index in the pins array corresponds to the number in the diagram below.

```
  #(0)#
 #      # 
(6)    (1)
 #      #
  #(2)#
 #      # 
(5)    (3)
 #      #
  #(4)#     #(7)
```

Assign the number of the pin connected to the display to the corresponding index.


