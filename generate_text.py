import sys
import numpy as np
import random
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM, SimpleRNN
from keras.layers.wrappers import TimeDistributed
import os
import re
#generate_length = int(sys.argv[1]) #Number of chars to generate
#starter = sys.argv[2]



def generate_text(model, length,starter):
	

	vocab_size = len(chars)
	ix = []
	y_char = []

	starter_list = list("|\n" + starter + " ")
	x = np.zeros((1, length, vocab_size))
	for i in range(len(starter_list)):
		letter = starter_list[i]
		ix.append(char_to_ix[ letter ])
		y_char.append(letter)
		x[0, i, :][ix[-1]] = 1
	
	print("")
	for i in range(len(starter_list), length):
		
		#print ("(%i/%i)" % (i,length))
		
		j = i - 200
		if j <0:
			j=0
					
		x[0, i, :][ix[-1]] = 1
		#print(ix_to_char[ix[-1]], end = "")
		#ix = np.argmax(model.predict(x[:, :i+1, :])[0],1)

		ix = np.argmax(model.predict(x[:, j:i+1, :])[0],1)
		new_char = ix_to_char[ix[-1]]
		y_char.append(new_char)
		#print(new_char, end= "")
		
		status_message = "(%i/%i)" % (i,length)
		
		preview = ('').join(y_char)
		preview = preview.replace('\n', ' ').replace('\r', '')
		preview = preview + status_message
		try:
			cols, rows = os.get_terminal_size()
			if len(preview) > cols:
				preview = preview[cols * -1 :]
			print("\r" + preview ,end = "\r")
		except:
			if i % 20 == 0:
				print(preview)
				
	return('').join(y_char)

def loadText():
	data = open("buffy-summaries.txt", 'r').read()
	return data

def recreateNetwork():
	layer_num = 3
	hidden_dim = 500

	model = Sequential()

	model.add(LSTM(hidden_dim, input_shape = (None, vocab_size), return_sequences=True))
	for i in range(layer_num - 1):
		model.add(LSTM(hidden_dim, return_sequences=True))
	model.add(TimeDistributed(Dense(vocab_size)))
	model.add(Activation('softmax'))
	model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

	model.load_weights('checkpoint_500_epoch_62_.hdf5')
	return model

def get_first_words():
	first_words = []
	data_list = data.split("\n|\n")
	for entry in data_list:
		first_words.append( entry.split(" ")[0] )
	return list(dict.fromkeys(first_words))

def trim_generated(text):
		attempts = text.split("|")
		for i in range(len(attempts)):
			attempts[i] = attempts[i].strip()
			sentences = attempts[i].split(". ")
			while len( ". ".join(sentences) ) > 280:
				sentences = sentences[:-1]
			attempts[i] = ". ".join(sentences)
		output = "\n|\n".join(attempts) + "."
		output = re.sub(" +", " ", output)
		return output
		


#generate text
data = loadText()
chars = list(set(data))
chars.sort()
vocab_size = len(chars)
print("vocab size: ", vocab_size)
ix_to_char = {ix:char for ix, char in enumerate(chars)}
char_to_ix = {char:ix for ix, char in enumerate(chars)}

model = recreateNetwork()

first_words = get_first_words()


for i in range(len(first_words)):
	starter = first_words[i]
	print("starter: %s" % starter)
	text = generate_text(model, 350, starter)
	text = trim_generated(text)

	#output generated text
	print("")
	print ("run %i/%i: Recording:%s" % (i,len(first_words), text))
	with open("output.txt", 'a+') as file:
		file.write(text)

