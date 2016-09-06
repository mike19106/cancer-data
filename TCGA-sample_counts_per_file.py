#!/bin/python

import collections
import os
import sys

import numpy #as np
import pandas #as pd

seqfile  = 'HiSeqV2.tsv'
clinfile = 'PANCAN_clinicalMatrix.tsv'
mutfile  = 'PANCAN_mutation.tsv'


# Clinical Matrix file
path = os.path.join('.', clinfile)

renamer = collections.OrderedDict([
    ('sampleID', 'sample_id'),
])

clinmat_df = (
    pandas.read_table(path)
    .rename(columns=renamer)
    [list(renamer.values())]
    .set_index('sample_id', drop=False)
)

cmcounts = clinmat_df['sample_id'].value_counts()
#print(cmcounts[0])
#print(type(cmcounts))
#print(cmcounts)


# Mutation data file
path = os.path.join('.', mutfile)

renamer = collections.OrderedDict([
    ('sample', 'sample_id'),
])

mut_df = (
    pandas.read_table(path)
    .rename(columns=renamer)
    [list(renamer.values())]
    .set_index('sample_id', drop=False)
)

mutcounts = mut_df['sample_id'].value_counts()
#print(mutcounts[0])
#print(type(mutcounts))
#print(mutcounts)


# Sequence data file
path = os.path.join('.', seqfile)

renamer = collections.OrderedDict([
    ('Sample', 'sample_id'),
])

seq_df = (
    pandas.read_table(path)
)

seqcounts = pandas.Series(data=list(seq_df.columns.values)).value_counts()
seqcounts.rename(columns=renamer)
#print(seqcounts[0])
#print(type(seqcounts))
#print(seqcounts)
print(seqcounts.get('TCGA-D3-A5GT-01'))

sys.exit(0)





cdf = pandas.DataFrame(data=cmcounts)
mdf = pandas.DataFrame(data=mutcounts)
cdf.merge(mdf, how='outer', left_on='sample_id', right_on='sample_id')
print(cdf)
sys.exit(0)


