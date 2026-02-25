"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of N followed by N lines of commands
where each command will be of the types listed above. Iterate through each command
in order and perform the corresponding operation on your list.

Input Format:
    The first line contains an integer N, denoting the number of commands.
    Each line of the N subsequent lines contains one of the commands described above.

Constraints:
    The elements added to the list must be integers.

Output Format:
    For each command of type print, print the list on a new line.

Sample Input:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

Sample Output:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()
