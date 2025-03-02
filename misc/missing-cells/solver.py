# Binary Sudoku Solver 1.0
# Rafa Rios
# Dec 2016
# Python 3 conversion

class MyException(Exception):
    pass

import sys
import time

nr = 0  # number of rows
nc = 0  # number of columns

def sum_row(s, p, c):
    s1 = s[(p//nc)*nc:(p//nc)*nc+nc]
    if (c == '1') and (nc % 2 == 1):
        return s1.count(c) > nc//2
    else:
        return s1.count(c) >= nc//2

def sum_col(s, p, c):
    s1 = ""
    for i in range(nr):
        s1 += s[i*nc + p%nc]
    if (c == '1') and (nr % 2 == 1):
        return s1.count(c) > nr//2
    else:
        return s1.count(c) >= nr//2

def seq_row(s, p, c):
    if (p%nc > 1) and (s[p-2] == s[p-1] and s[p-1] == c):
        return True
    if (p%nc > 0 and p%nc < nc-1) and (s[p-1] == c and s[p+1] == c):
        return True
    if (p%nc < nc-3) and (s[p+2] == s[p+1] and s[p+1] == c):
        return True
    return False

def seq_col(s, p, c):
    if (p//nc > 1) and (s[p-nc*2] == s[p-nc] and s[p-nc] == c):
        return True
    if (p//nc > 0 and p//nc < nr-1) and (s[p-nc] == c and s[p+nc] == c):
        return True
    if (p//nc < nr-3) and (s[p+nc*2] == s[p+nc] and s[p+nc] == c):
        return True
    return False

def same_row(s, p, c):
    current_row = s[(p//nc)*nc:(p//nc)*nc+nc]
    new_row = current_row[:p%nc] + c + current_row[p%nc+1:]
    for i in range(nr):
        if i != p//nc:
            other_row = s[i*nc:(i+1)*nc]
            if '*' not in other_row and other_row == new_row:
                return True
    return False

def same_col(s, p, c):
    col_idx = p % nc
    new_col = []
    for i in range(nr):
        if i == p//nc:
            new_col.append(c)
        else:
            new_col.append(s[i*nc + col_idx])
    
    for other_col_idx in range(nc):
        if other_col_idx == col_idx:
            continue
        other_col = [s[i*nc + other_col_idx] for i in range(nr)]
        if '*' not in other_col and other_col == new_col:
            return True
    return False

def r(s):
    p = s.find('*')
    if p == -1:
        raise MyException(s)

    excluded = set()
    for c in '01':
        if (sum_row(s, p, c) or sum_col(s, p, c) or
            seq_row(s, p, c) or seq_col(s, p, c) or
            same_row(s, p, c) or same_col(s, p, c)):
            excluded.add(c)

    for m in '01':
        if m not in excluded:
            r(s[:p] + m + s[p+1:])

def display(s):
    c = 1
    for i in s:
        print(i, end=' ')
        if c % nc == 0:
            print()
        c += 1

if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = ""
        try:
            with open(sys.argv[1], "r") as f:
                for line in f:
                    clean_line = line.strip("\n").strip()
                    s += clean_line
                    nr += 1
                    if len(clean_line) != len(s)//nr:
                        sys.exit("ERROR: Inconsistent line lengths")
            nc = len(s) // nr
        except (OSError, IOError) as e:
            sys.exit(f"ERROR: Can't read file {sys.argv[1]}")

        print("\nInput")
        display(s)

        try:
            r(s)
        except MyException as e:
            print("\nSolution")
            display(str(e.args[0]))
    else:
        print('Usage: python binary-sudoku-solver.py puzzle')
        print('Puzzle format: matrix with 0s and 1s (* for blanks)')
