from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Flatten, Conv3D, LSTM, MaxPool3D, TimeDistributed, Dense, Dropout

def build_model(input_shape = (10,244,244,3)):

    model = Sequential()
    model.add(Input(input_shape))
    model.add(Conv3D(
        filters=16,
        kernel_size=3,
        activation='relu',
        input_shape=input_shape
    ))
    model.add(Conv3D(
        filters=32,
        kernel_size=3,
        activation='relu',
        input_shape=input_shape
    ))
    model.add(Conv3D(
        filters=64,
        kernel_size=3,
        activation='relu',
        input_shape=input_shape
    ))
    model.add(Dropout(.3))
    model.add(Conv3D(
        filters=64,
        kernel_size=3,
        activation='relu',
        input_shape=input_shape
    ))
    model.add(MaxPool3D())
    model.add(TimeDistributed(Flatten()))
    model.add(LSTM(
        units=32
    ))
    model.add(Dense(40, activation='softmax'))
    model.summary()

    return model
    