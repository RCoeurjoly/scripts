#!/usr/bin/env
# -*- coding: utf-8 -*-
# import uno
import glob
import nltk
# import re
import codecs
# import regex
# import string
# import os
from operator import itemgetter
dummyText = "".encode('utf-8')
bigrams_master = nltk.FreqDist(dummyText).most_common()
counter = 0
for filename in glob.glob('///home/rcl/Documents/test/*.txt'):
        stripedText = ''.join(
                c for c in codecs.open(
                        filename,
                        'r',
                        'utf-8-sig',q
                        'ignore').read() if u'\u4e00' <= c <= u'\u9fff')
        fdist = nltk.FreqDist(stripedText).most_common()
        hashTable = {}
        for item in fdist:
                hashTable[item[0]] = item[1] 
        '''for item in fdist:
                found = 0
                for i in xrange(len(bigrams_master)):
                        print bigrams_master[i]
                        if bigrams_master[i][0] == item[0]:
                                bigrams_master[i] = (
                                        item[0],
                                        bigrams_master[i][1] + item[1])
                                found = 1
                                break
                if found == 0:
                        bigrams_master.append(item)
        '''
        counter += 1
        print (str(counter) + " books analized. Looking for the next book.\n")
        bookName = filename.split("/")[7].split(".")[0]
        text = codecs.open(
                '///home/rcl/Documents/hashtable' + bookName + '.txt',
                'w',
                'utf-8-sig')
        fdist_master = sorted(fdist, key=itemgetter(1), reverse=True)
        for item in fdist:
                text.write(item[0][0])
                text.write(', ')
                text.write(item[0][1])
                text.write(str(item[1]) + '\n')
        text.close()
