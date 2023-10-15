import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam

data = pd.read_csv('data(no5000).csv', encoding='cp949')

encoder = LabelEncoder()
data['발생유형'] = encoder.fit_transform(data['발생유형'])

X = data[['풍속(m/s)', 'GUST풍속(m/s)', '습도(%)', '기온(°C)', '현지기압(hPa)', '평균파고(m)']].values
y = data['발생유형'].values

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

train_size = int(len(X) * 0.7)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size,:], X[train_size:len(X),:]
y_train, y_test = y[0:train_size], y[train_size:len(y)]

model = Sequential()
model.add(LSTM(units=50, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

# 모델 학습
history = model.fit(X_train.reshape((X_train.shape[0], X_train.shape[1], 1)), y_train, epochs=100, batch_size=64, validation_data=(X_test.reshape((X_test.shape[0], X_test.shape[1], 1)), y_test))

# 검증 데이터셋에 대한 정확도 출력
print("Test Accuracy: %.2f%%" % (history.history['val_accuracy'][-1]*100))
model.save('lstm.h5')