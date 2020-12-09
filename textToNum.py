import numpy as np
import collections
from numpy import random
import sys

import docx
import matplotlib.pyplot as plt

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

filename = "manual.docx"
raw_text = getText(filename)
raw_text_splited_to_words = raw_text.split(" ")

# #each word to a random number
# number_words = []
# for word in raw_text_splited_to_words:
#     number_words.append([np.float64(ord(character)) for character in word])
#
# rand_number_words = []
# for wornum_list in number_words:
#     new_wornum_list = []
#     for wornum in wornum_list:
#         elem_to_append = random.random()
#         new_wornum_list.append(elem_to_append)
#     rand_number_words.append(new_wornum_list)
#
# max_len = max([len(word) for word in rand_number_words])
# for word in rand_number_words:
#     for i in range(max_len - len(word)):
#         word.append(0)
#
# img = plt.imshow(rand_number_words[:38], interpolation='nearest')
# img.set_cmap('hot')
# plt.axis('off')
# plt.show()

#one type of plot
raw_text_splited_to_words_to_numbers = []
for word in raw_text_splited_to_words:
    raw_text_splited_to_words_to_numbers.append([np.float64(ord(character)) for character in word])

number_words = raw_text_splited_to_words_to_numbers
max_len = max([len(word) for word in number_words])
for word in number_words:
    for i in range(max_len - len(word)):
        word.append(0)

data = np.array(number_words)
img = plt.imshow(data[:max_len], interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
plt.savefig("test2.png", bbox_inches='tight')
plt.show()

img = plt.imshow(data, interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
plt.savefig("testALL.png", bbox_inches='tight')
plt.show()

start = 0
stop = max_len
while stop < len(number_words):
    print(start,stop)
    data = np.array(number_words)[start:stop]
    img = plt.imshow(data, interpolation='nearest')
    img.set_cmap('hot')
    plt.axis('off')
    plt.savefig("images/words_{}.png".format(stop), bbox_inches='tight')
    start = stop+1
    stop += max_len
print(start,stop)
data = np.array(number_words)[start:stop]
img = plt.imshow(data, interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
plt.savefig("images/words_{}.png".format(stop), bbox_inches='tight')
# #one kind of plot
# text_to_numbers = [ord(character) for character in raw_text]
# text_to_numbers = [number for number in text_to_numbers if number < 8000.]
# def CountFrequency(arr):
#     return collections.Counter(arr)
#
# frequencies = CountFrequency(text_to_numbers)
# print(len(text_to_numbers), len(frequencies))
# text_to_numbers = [[elem, frequencies[elem]] for elem in text_to_numbers]
# fig = plt.figure()
# plt.axis('off')
# plt.plot(text_to_numbers,marker = '.',  markersize = 400/fig.dpi,mec = 'None', ls = 'None',color='black')
# plt.show()

# #example
# data = random.random((38,38))
# img = plt.imshow(data, interpolation='nearest')
# img.set_cmap('hot')
# plt.axis('off')
# plt.show()
# plt.savefig("test.png", bbox_inches='tight')

# # sys.exit()
# freqs = [frequencies[elem] for elem in text_to_numbers]
# plt.scatter(text_to_numbers, freqs, c ='black')
# plt.plot(numbersInstead[1], 'o', color='black')
# plt.plot(numbersInstead[2], 'o', color='black')
# plt.show()

# x = np.array(text_to_numbers)
# y = np.array(freqs)
# m, b = np.polyfit(x, y, 1)
# m2, b2, c3 = np.polyfit(x,y,2)
# plt.plot(x,m*x+b)
# plt.plot(x,m2*x**2 + b2*x + c3, 'o' )
# plt.show()