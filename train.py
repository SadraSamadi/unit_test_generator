from shared import *
import tensorflow as tf

encoder_input_data, decoder_input_data, decoder_output_data = prep_data(train_inputs, train_outputs)

embedding = tf.keras.layers.Embedding(input_dim=chars_size, output_dim=embedding_size, name='embedding')

encoder_input = tf.keras.layers.Input(shape=(None,), name='encoder_input')
encoder_embedding = embedding(encoder_input)
encoder_lstm = tf.keras.layers.LSTM(units=lstm_size, return_state=True, name='encoder_lstm')
_, encoder_state_h, encoder_state_c = encoder_lstm(encoder_embedding)
encoder_states = [encoder_state_h, encoder_state_c]

decoder_input = tf.keras.layers.Input(shape=(None,), name='decoder_input')
decoder_embedding = embedding(decoder_input)
decoder_lstm = tf.keras.layers.LSTM(units=lstm_size, return_sequences=True, return_state=True, name='decoder_lstm')
decoder_output, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
decoder_dense = tf.keras.layers.Dense(units=chars_size, activation='softmax', name='decoder_dense')
decoder_output = decoder_dense(decoder_output)

model = tf.keras.models.Model([encoder_input, decoder_input], decoder_output)
model.compile(optimizer=tf.keras.optimizers.RMSprop(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit([encoder_input_data, decoder_input_data], decoder_output_data, batch_size=batch_size, epochs=epochs,
          validation_split=0.2)
model.save('model.keras')
