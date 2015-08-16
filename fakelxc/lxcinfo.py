#!/usr/bin/env python
import sys

def main():
  if sys.argv[2] == 'test1':
    print('Name:           test1')
    print('State:          RUNNING')
    print('PID:            12345')
    print('IP:             10.0.0.2')
    print('CPU use:        10.10 seconds')
    print('Memory use:     10.20 MiB')
    print('Link:           vethtest1')
    print(' TX bytes:      1.65 MiB')
    print(' RX bytes:      24.65 MiB')
    print(' Total bytes:   26.30 MiB')

  if sys.argv[2] == 'test2':
    print('Name:           test2')
    print('State:          STOPPED')

  if sys.argv[2] == 'test3':
    print('Name:           test3')
    print('State:          FROZEN')
    print('PID:            12346')
    print('IP:             10.0.0.3')
    print('CPU use:        10.10 seconds')
    print('Memory use:     10.20 MiB')
    print('Link:           vethtest1')
    print(' TX bytes:      1.65 MiB')
    print(' RX bytes:      24.65 MiB')
    print(' Total bytes:   26.30 MiB')

if __name__ == '__main__':
  main()
