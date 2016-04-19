#! /usr/bin/env pytho

import ipdb

from collections import Counter
from collections import defaultdict

filename = 'SP1.fq'

line_num = 0
#num_records = 0

#def reverse_complement(seq):
#    comps = []
#    empty = ''
#    for char in seq:
#        if char =='A':
#            comps.append('T')
#        if char =='C':
#            comps.append('G')
#        if char =='G':
#            comps.append('G')
#        if char =='T':
#            comps.append('A')
#        if char =='U':
#            comps.append('A')
#    rev_com = ''.join(reversed(comps))
#    print rev_com

#def sum_quals(qual):
    # val = sum([ord(i) for i in char])
#    sum = 0
#    for char in qual:
#        sum += ord(char)
#    return sum

def parse_fastq(filename):

    line_num = 0
    for line in open(filename):

        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()
        elif line_type == 1:
            seq = line.strip()
        elif line_type == 3:
            quals = line.strip()

            yield  name, seq, quals

        line_num += 1

num_rec = 0
max_num = 0

for name, seq, quals in parse_fastq(filename):

#    print seq
    counts = Counter(seq)
    r = counts['C']
#    print r
    if r  > max_num:
        max_num = r
        max_name = name

    num_rec += 1

    if num_rec > 9:
        break

print 'answer-3: ', name, max_num
#ipdb.set_trace()

large_qual = 0

def sum_quals(qual):
    sum = 0
    for char in qual:
        sum += ord(char)
    return sum

for name,seq,quals in parse_fastq(filename):
#    print sum_quals(quals)

    if sum_quals(quals) > large_qual:
        large_qual = sum_quals(quals)

print 'answer-4: ', large_qual


def reverse_complement(seq):
    comps = []
    empty = ''

    for char in seq:
        if char =='A':
            comps.append('T')
        if char =='C':
            comps.append('G')
        if char =='G':
            comps.append('C')
        if char =='T':
            comps.append('A')
        if char =='U':
            comps.append('A')

    rev_com = ''.join(reversed(comps))

    return rev_com

num_rec = 0
rv = 10

for name, seq, quals in parse_fastq(filename):
#    if reverse_complement(seq) > rv:
    if num_rec < 10:
        rv = reverse_complement(seq)
        print 'answer-5: ', rv
    num_rec += 1


bedfile= '/Users/Gaby/Desktop/bioinformatics WORKSHOP/datasets/data-sets/data-sets/bed/lamina.bed'


data = defaultdict(list)
chrom_counts = Counter()

starts_big = 0

for line in open(bedfile):
    if line.startswith('#'):
        continue

    fields = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    value = float(fields[3])

    if start > starts_big:
        starts_big = start
        chrom_big = chrom

print 'answer-1: %s:%s' %(chrom_big, starts_big)

large_end = 0

for line in open(bedfile):
    if line.startswith('#'):
        continue

    fields = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    value = float(fields[3])

    if  chrom == 'chrY':
        if end > large_end:
            large_end = end
            large_start = start

print 'answer-2: %s:%s-%s' % ("chrY", large_start, large_end)

