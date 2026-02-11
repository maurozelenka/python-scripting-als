"""
PROBLEM: Mutations

Strings are immutable in Python (they cannot be changed). 
You are given an immutable string, and you want to make changes to it.

Task:
Read a given string, change the character at a given index and then print the modified string.

Function Description:
Complete the mutate_string function.

mutate_string has the following parameters:
- string string: the string to change
- int position: the index to insert the character at
- string character: the character to insert

Returns:
- string: the altered string

Input Format:
The first line contains a string, s.
The next line contains an integer i (position) and a string c (character), separated by a space.

Sample Input:
abracadabra
5 k

Sample Output:
abrackdabra

Explanation:
We need to replace the character at index 5 with 'k'.
Original: a b r a c a d a b r a
Index:    0 1 2 3 4 5 6 7 8 9 10
After:    a b r a c k d a b r a

SOLUTION:
We can use string slicing to create a new string:
- Take everything before the position: string[:position]
- Add the new character: character
- Add everything after the position: string[position+1:]
"""

def mutate_string(string, position, character):
    # Use string slicing to replace character at given position
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
