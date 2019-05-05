import numpy as np
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM, SimpleRNN
from keras.layers.wrappers import TimeDistributed


def generate_text(model, length):
	ix = [vocab_size - 1]
	y_char = [ix_to_char[ix[-1]]]
	x = np.zeros((1, length, vocab_size))
	for i in range(length):
		x[0, i, :][ix[-1]] = 1
		print(ix_to_char[ix[-1]], end = "")
		ix = np.argmax(model.predict(x[:, :i+1, :])[0],1)
		y_char.append(ix_to_char[ix[-1]])
	return('').join(y_char)

data = open("buffy-summaries.txt", 'r').read()
chars = list(set(data))
chars.sort()
vocab_size = len(chars)

print("vocab size: ", vocab_size)
print(chars)

hidden_dim = 500
seq_length = 50
layer_num = 3
batch_size = 50
generate_length = 50000

#######PREPARE THE TRAINING DATA ###########


ix_to_char = {ix:char for ix, char in enumerate(chars)}
char_to_ix = {char:ix for ix, char in enumerate(chars)}

x = np.zeros( ( int( len(data)/seq_length ), seq_length, vocab_size ) )
y = np.zeros( ( int( len(data)/seq_length ), seq_length, vocab_size ) )

for i in range(0, int ( len(data)/seq_length ) ):
	x_sequence = data[i * seq_length:(i+1)*seq_length] #Get the i'th sequence from data
	# encode the sequence
	x_sequence_ix = [char_to_ix[value] for value in x_sequence]

	input_sequence = np.zeros((seq_length, vocab_size))
	for j in range(seq_length):
		input_sequence[j][x_sequence_ix[j]] = 1.
	x[i] = input_sequence
	
	y_sequence = data[i*seq_length+1:(i+1)*seq_length+1]
	y_sequence_ix = [char_to_ix[value] for value in y_sequence]
	
	target_sequence = np.zeros((seq_length, vocab_size))
	for j in range (seq_length):
		target_sequence[j][y_sequence_ix[j]] = 1.
	y[i] = target_sequence


#######CREATE THE NETWORK ###########

model = Sequential()
model.add(LSTM(hidden_dim, input_shape = (None, vocab_size), return_sequences=True))
for i in range(layer_num - 1):
	model.add(LSTM(hidden_dim, return_sequences=True))
model.add(TimeDistributed(Dense(vocab_size)))
model.add(Activation('softmax'))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")
model.load_weights('checkpoint_500_epoch_120_.hdf5')


text = generate_text(model, generate_length)

print (text)

