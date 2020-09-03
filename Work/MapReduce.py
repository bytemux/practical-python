# source https://towardsdatascience.com/a-beginners-introduction-into-mapreduce-2c912bb5e6ac

# # Trivial way (1 full run) ~20 sec
# def find_longest_string(list_of_strings):
#     longest_string = None
#     longest_string_len = 0
#     for s in list_of_strings:
#         if len(s) > longest_string_len:
#             longest_string_len = len(s)
#             longest_string = s
#     return longest_string
# list_of_strings = ['abc', 'python', 'dima']
# large_list_of_strings = list_of_strings*100000000
# max_length = print(find_longest_string(large_list_of_strings))


# # Lambda way (slower, 2 full runs) ~40 sec
# list_of_strings = ['abc', 'python', 'dima']*100000000
# # step 1:
# list_of_string_lens = [len(s) for s in list_of_strings]
# list_of_string_lens = zip(list_of_strings, list_of_string_lens)
# #step 2:
# max_len = max(list_of_string_lens, key=lambda t: t[1])
# print(max_len)

# MapReduce way ~10 sec (scales with number of processes / chunks)
# “mapper” because it maps some value into some other value
# reducer because it gets a list of values and produces a single (in most cases) value.
from functools import reduce
from multiprocessing import Pool

list_of_strings = ['abc', 'python', 'dima', '1', '3','444','555']
mapper = len

def chunkify(seq, size):
    # seq[start:end:step]
    # seq[::n] is a sequence of each n-th item in the entire sequence.
    return (seq[i::size] for i in range(size))
# for debug & understanding:
# size = 2
# for i in range(size):
#     print(f'{i} {size}')

def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c

def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)

data_chunks = chunkify(list_of_strings, 2)
print(list(data_chunks))

# #step 1:
# mapped = pool.map(chunks_mapper, data_chunks)
# #step 2:
# reduced = reduce(reducer, mapped)
# print(reduced)


