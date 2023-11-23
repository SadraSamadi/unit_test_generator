from shared import *
import tensorflow as tf
import random

encoder_input_data, decoder_input_data, decoder_output_data = prep_data(test_inputs, test_outputs)

model = tf.keras.models.load_model('model.keras')

embedding = model.get_layer('embedding')

encoder_input = model.get_layer('encoder_input')
encoder_lstm = model.get_layer('encoder_lstm')
_, encoder_state_h, encoder_state_c = encoder_lstm.output
encoder_states = [encoder_state_h, encoder_state_c]
encoder_model = tf.keras.Model(encoder_input.input, encoder_states)

decoder_input = model.get_layer('decoder_input')
decoder_embedding = embedding(decoder_input.input)
decoder_input_state_h = tf.keras.layers.Input(shape=(lstm_size,))
decoder_input_state_c = tf.keras.layers.Input(shape=(lstm_size,))
decoder_input_states = [decoder_input_state_h, decoder_input_state_c]
decoder_lstm = model.get_layer('decoder_lstm')
decoder_output, decoder_state_h, decoder_state_c = decoder_lstm(decoder_embedding, initial_state=decoder_input_states)
decoder_dense = model.get_layer('decoder_dense')
decoder_output = decoder_dense(decoder_output)
decoder_model = tf.keras.models.Model([decoder_input.input] + decoder_input_states,
                                      [decoder_output, decoder_state_h, decoder_state_c])

loss, accuracy = model.evaluate([encoder_input_data, decoder_input_data], decoder_output_data,
                                batch_size=batch_size, verbose=0)

print(f'[Evaluation] Loss: {loss:.3f} | Accuracy: %{accuracy * 100:.2f}')
print('-' * 80)


def sample(preds, temperature):
    scaled = preds / temperature
    exp = np.exp(scaled - np.max(scaled))
    dist = exp / np.sum(exp)
    return np.random.choice(len(dist), p=dist)


def generate(inp_txt):
    out_txt = ''
    enc_inp = text_to_seq(inp_txt)
    enc_inp = pad_seq(enc_inp, max_len=max_inp_len)
    enc_inp = np.array([enc_inp])
    dec_inp = [char_to_index[start_char]]
    dec_inp = np.array([dec_inp])
    pred_state = encoder_model.predict(enc_inp, verbose=0)
    while len(out_txt) < max_out_len:
        decoder_pred, decoder_h, decoder_c = decoder_model.predict([dec_inp] + pred_state, verbose=0)
        index = sample(decoder_pred[0, -1], 0.02)
        char = index_to_char[index]
        if char == stop_char:
            break
        out_txt += char
        dec_inp = text_to_seq(char)
        dec_inp = np.array([dec_inp])
        pred_state = [decoder_h, decoder_c]
    return out_txt


for inp in random.choices(test_inputs, k=10):
    print('[Input ]', inp)
    out = generate(inp)
    print('[Output]', out)
    print('-' * 80)
