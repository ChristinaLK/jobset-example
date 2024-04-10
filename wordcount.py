#!/usr/bin/env python3

import os
import sys
import operator
import time

start_time = time.perf_counter()

print('Analyzing {}'.format(input_filename))

words_dict = {}
with open("Alice_in_Wonderland.txt", 'r') as my_file:
    for line in my_file:
        line_words = line.split()
        for word in line_words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

sorted_words_list = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)

output_lines = ['{}\t{}'.format(word, count) for word,count in sorted_words_list]
output_text = '\n'.join(output_lines)

with open("Alice_in_Wonderland.tsv", 'w') as my_file:
    my_file.write(output_text)

stats = '''\
|  Total words = {total}
| Unique words = {uniq}'''.format(
    total=sum([count for word,count in sorted_words_list]),
    uniq=len(sorted_words_list)
)

print(stats)

end_time = time.perf_counter()

print('Elapsed time = {:.6f} secs'.format(end_time-start_time))
