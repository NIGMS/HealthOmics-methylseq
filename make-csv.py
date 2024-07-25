import pandas as pd

# Initialize data to lists.
data = [{'sample': 'SRX202087_serum', 'fastq_1': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616795_sub_1.fastq.gz', 'fastq_2': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616795_sub_2.fastq.gz'},
        {'sample': 'SRX202088_2i', 'fastq_1': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616796_sub_1.fastq.gz', 'fastq_2': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616796_sub_2.fastq.gz'},
        {'sample': 'SRX271142_2i', 'fastq_1': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616802_sub_1.fastq.gz', 'fastq_2': 's3://danipan-nigms-sample-data/dna-methyl/SRR8616802_sub_2.fastq.gz'}]

# Creates DataFrame.
df = pd.DataFrame(data)
df.to_csv('samplesheet.csv', index=False)
