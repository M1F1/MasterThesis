# Python program to
# demonstrate merging
# of two files

data = data2 = ""

# Reading data from file1
print("Read data from literature.bib ...")
with open('literature.bib') as fp:
	data = fp.read()

# Reading data from file2
print("Read data from literature_non_arxiv.bib ...")
with open('literature_non_arxiv.bib') as fp:
	data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += data2
print('Merge files into literature_all.bib')
with open ('literature_all.bib', 'w') as fp:
	fp.write(data)
