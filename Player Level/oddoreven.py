def separate_string(sentence):
     l1 = list(sentence)
     l2 = list()
     for letter in range(l1):
        index = l1.index(letter)
        if index % 2 != 0:
            l2.append(l[letter])
            l1.remove(letter)
if __name__ == '__main__':
    separate_string('abcedfg')
