#!/usr/bin/python3

print("{}".format(''.join(chr(i) for i in range(ord('a'), ord('z')+1)
                          if chr(i) not in ('e', 'q'))), end='')
