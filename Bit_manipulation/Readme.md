# Bit_manipulation

## Concept
- Bitwise operators are a type of operation that can be performed on binary values. They perform operations on each bit of the binary representation of the numbers and are mainly used for manipulation of individual bits in a value stored in memory
- Bit Manipulation has a lot of real world applications too. It’s heavily used for Encryptions like Exclusive-Or Encryption and Data compressions. In both of these we have to extract the data at a bit level.
- We all know that 1 byte comprises of 8 bits and `any integer or character` can be represented using bits in computers, which we call its binary form(contains only 1 or 0) or in its base 2 form.

- For characters, we use ASCII representation, which are in the form of integers which again can be represented using bits 

### **Bitwise Operators**:
- **NOT ( ~ )** Bitwise NOT is an unary operator that flips the bits of the number

- **AND ( & )** If both bits in the compared position of the bit patterns are 1, the bit in the resulting bit pattern is 1, otherwise 0.

- **OR ( | )**  If both bits in the compared position of the bit patterns are 0, the bit in the resulting bit pattern is 0, otherwise 1.

- **XOR ( ^ )** If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.
A = 5 = (101)2 , B = 3 = (011)2
A ^ B = (101)2 ^ (011)2 = (110)2 = 6
- **Left Shift ( << )** Left shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the left and append 0 at the end. Left shift is equivalent to multiplying the bit pattern with 2 to the power k (no.of shift)
for Example consider the binary number 1101 (decimal 13). If we perform a left shift of two positions on this number, the bits are shifted two positions to the left:
```
1101 (13) << 2
----------
110100 (52)
```
```
13 * (2^2) = 13 * 4 = 52

```
- **Right Shift ( >> )**Right shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the right and append 1 at the end. `Right shift is equivalent to dividing the bit pattern with 2k `( if we are shifting k bits ).
```
1101 (13) >> 2
----------
0011 (3)
```
```
13 / (2^2) = 13 / 4 = 3
```

![all bitwise operator](https://he-s3.s3.amazonaws.com/media/uploads/cb985c2.png)

> Difference between  && and &

The "&&" symbol is the logical AND operator, which is used to perform a logical AND operation on two boolean values (i.e. values that are either true or false). The logical AND operation returns true if both of the operands are true, and false otherwise.

The "&" symbol is the bitwise AND operator, which is used to perform a bitwise AND operation on two integer values. In a bitwise AND operation, each bit in the first operand is ANDed with the corresponding bit in the second operand. The result is a new integer value in which each bit is set to 1 only if both corresponding bits in the operands were 1.