'''
 ' Brainfuck Interpreter
 ' @author: Sanjan Geet Singh <sanjangeet2109s@gmail.com>
 '
 ' Description:
 ' Brainfuck is an esoteric programming language with only eight instructions.
 ' As it is turning complete, it can be used to implement litterally any type of program.
 '
 ' Instructions:
 ' +  Increment the value of current cell by 1
 ' -  Decrement the value of current cell by 1
 ' >  Move to next cell
 ' <  Return to previous cell
 ' .  Print the value of current cell
 ' ,  Read a single char from keyboard and put it into current cell
 ' [  If value of current cell is 0, Jump to matching ] Instruction.
 ' ]  If value of current cell is not 0, Jump to matching [ Instruction.
'''

import sys
from msvcrt import getch      # Getch: Function to read a single char from keyboard without displaying it.

def build_bracemap(code):     # Generates map of [ and ] Instructions.
      temp = []
      bmap = {}

      for i in range(len(code)):
            c = code[i]

            if c == '[':
                  temp.append(i)
            elif c == ']':
                  j = temp.pop()
                  bmap[i] = j
                  bmap[j] = i

      if len(temp) != 0:
            print("[ERROR] Incorrect number of braces")

      return bmap

def execute(code):
      code = ''.join(filter(lambda x: x in ['+', '-', '.', ',', '<', '>', '[', ']'], list(code)))
      bmap = build_bracemap(code)
      codel = len(code) # code length
      codep = 0         # code position
      cellp = 0         # cell position
      cells = [0]

      while codep < codel:
            cmd = code[codep]

            if cmd == '+':
                  if cells[cellp] == 255:       # cell size if 8-bit, or ranged from 0 to 255
                        cells[cellp] = 0
                  else:
                        cells[cellp] += 1
            elif cmd == '-':
                  if cells[cellp] == 0:
                        cells[cellp] = 255
                  else:
                        cells[cellp] -= 1
            elif cmd == '.':
                  print(chr(cells[cellp]), end='')    # print the matching character from ASCII Table with value of current cell
            elif cmd == ',':
                  cells[cellp] = ord(getch())
            elif cmd == '<':
                  if cellp > 0:
                        cellp -= 1
            elif cmd == '>':
                  cellp += 1
                  if len(cells) == cellp:
                        cells.append(0)
            elif cmd == '[':
                  if cells[cellp] == 0:
                        codep = bmap[codep]
            elif cmd == ']':
                  if cells[cellp] != 0:
                        codep = bmap[codep]

            codep += 1

def main(args):
      if len(args) != 2:
            print("Usage: python \"Brainfuck Interpreter.py\" [brainfuck source]")
            exit()

      try:
            file = open(args[1], 'r')
            code = file.read()
            file.close()
      except FileNotFoundError:
            print("[ERROR] File Not Found")
            exit()

      execute(code)

if __name__ == '__main__':
      main(sys.argv)
