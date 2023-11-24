import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

with open('dataset.txt', 'r') as f:
    dataset = f.read()

start_char = '^'
stop_char = '$'
empty_char = ' '
oov_char = '?'

chars = sorted(set(start_char + stop_char + empty_char + oov_char + dataset))
chars_size = len(chars)
char_to_index = {c: i for i, c in enumerate(chars)}
index_to_char = {i: c for i, c in enumerate(chars)}

lines = dataset.splitlines()
input_texts = lines[0::2]
output_texts = lines[1::2]

max_inp_len = max([len(inp) for inp in input_texts])
max_out_len = max([len(out) for out in output_texts])

train_size = int(len(input_texts) * 0.9)
train_inputs = input_texts[:train_size]
train_outputs = output_texts[:train_size]
test_inputs = input_texts[train_size:]
test_outputs = output_texts[train_size:]

embedding_size = 128
lstm_size = 256
batch_size = 64
epochs = 50


def text_to_seq(text):
    return [char_to_index[c] if c in char_to_index else char_to_index[oov_char] for c in text]


def seq_to_text(indices):
    return ''.join([index_to_char[i] if i in index_to_char else oov_char for i in indices])


def pad_seq(seq, max_len):
    return seq + [char_to_index[empty_char]] * (max_len - len(seq))


def prep_data(inputs, outputs):
    encoder_input_data = []
    decoder_input_data = []
    decoder_output_data = []
    for inp, out in zip(inputs, outputs):
        out = start_char + out + stop_char
        enc_inp = text_to_seq(inp)
        enc_inp = pad_seq(enc_inp, max_inp_len)
        dec_inp = out[:-1]
        dec_inp = text_to_seq(dec_inp)
        dec_inp = pad_seq(dec_inp, max_out_len + 1)
        dec_out = out[1:]
        dec_out = text_to_seq(dec_out)
        dec_out = pad_seq(dec_out, max_out_len + 1)
        encoder_input_data.append(enc_inp)
        decoder_input_data.append(dec_inp)
        decoder_output_data.append(dec_out)
    encoder_input_data = np.array(encoder_input_data)
    decoder_input_data = np.array(decoder_input_data)
    decoder_output_data = np.array(decoder_output_data)
    return encoder_input_data, decoder_input_data, decoder_output_data
