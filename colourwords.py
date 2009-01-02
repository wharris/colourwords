#!/usr/bin/env python

# colourwords.py - find HTML colours that look like words.
# Copyright (C) 2008  Will Harris
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

def colorwords(dictionary, letters):
    for line in dictionary:
        word = line[:-1].lower()
    
        if len(word) not in (3, 6):
            continue
    
        try:
            (ch for ch in word if ch not in letters).next()
        except StopIteration:
            yield word

if __name__ == "__main__":
    simple_words = list(colorwords(file("/usr/share/dict/words"), "abcdef"))
    for word in simple_words:
        print word,
    
    print
    print
    
    original_set = set(simple_words)
    
    for word in colorwords(file("/usr/share/dict/words"), "abcdefsoli"):
        if word not in original_set:
            print word,
    
    print
