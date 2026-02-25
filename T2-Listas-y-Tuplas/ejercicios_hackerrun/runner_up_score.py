"""
Find the Runner-Up Score!
-------------------------
Given n scores, find the runner-up (second highest) score.

Input Format:
    - First line: integer n
    - Second line: n integers separated by spaces

Output Format:
    Print the runner-up score.

Sample Input:       Sample Output:
    5                   5
    2 3 6 6 5
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    runner_up = sorted(set(arr))[-2]
    print(runner_up)
