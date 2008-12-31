#!/usr/bin/env python
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
