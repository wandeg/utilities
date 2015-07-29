import csv
import os

def get_row_count():
    lines = 0
    with open('') as fil:
    	return fil.read()
        # lines += 1
    # return lines

# print get_row_count()


def split_file(batch=1000000):
	run = 0
	count = 0
	with open('') as fil:
		# for line in xrange(20000):
		reader = csv.reader(fil)
		init = run*batch
		fin = (run+1)*batch
		while count>= init and count< fin:
			count+=1
			print count, run
		run+=1

# split_file()

from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 1000000

with open('') as f:
	# header = f.readline()
	# print header
	reader = csv.reader(f)
	header = reader.next()
	for i, g in enumerate(grouper(n, reader, fillvalue=''), 1):
		file_name = '{0}.csv'.format(i)
		with open(file_name, 'w') as fout:
			wri = csv.writer(fout)
			wri.writerows([header])
		with open(file_name, 'a') as fout:
			# writer.writerow(haeder)
			wri = csv.writer(fout)
			wri.writerows(g)
			#    fout.writelines(g)
		# os.system("gzip {0}".format(file_name))

# from itertools import product
# import time




# # total = t1-t0
# # lists = [
# #     ['THE', 'A'],
# #     ['ELEPHANT', 'APPLE', 'CAR'],
# #     ['WALKED', 'DROVE', 'SAT']
# # ]

# lists = [
# xrange(10),
# xrange(10),
# xrange(10000)
# ]
# t0 = time.time()
# for items in product(*lists):
# 	pass
#     # print items
# t1 = time.time()

# for i in lists[0]:
# 	for j in lists[1]:
# 		for k in lists[2]:
# 			# print (i,j,k)
# 			pass
# t2 = time.time()

# print t1-t0
# print t2 - t1
# print type(range(10))
