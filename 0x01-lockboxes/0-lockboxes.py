#!/usr/bin/python3
"""
0-lockboxes.py
"""

def canUnlockAll(boxes):
    n = len(boxes)
    
    opened = set()
    opened.add(0)
    
    keys = boxes[0].copy()
    
    while keys:
        key = keys.pop()
        if key not in opened and key < n:
            opened.add(key)
            keys.extend(boxes[key])
    
    return len(opened) == n
