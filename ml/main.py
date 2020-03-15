#from __future__ import absolute_import, division, print_function, unicode_literals
#!pip install -q tensorflow-gpu=2.0.0-rc1
import tensorflow as tf

# MNIST 데이터셋을 로드하여 준비합니다
# 다운로드 위치: C:\Users\cskuu\.keras\datasets
mnist = tf.keras.datasets.mnist

# 샘플 값을 정수에서 부동소수로 변환합니다
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 층을 차례대로 쌓아 tf.keras.Sequential 모델을 만듭니다
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')])

# 훈련에 사용할 옵티마이저(optimizer)와 손실 함수를 선택합니다
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# 학습 데이터 세트를 사용하여 모델을 훈련합니다. 5번 반복합니다. 
model.fit(x_train, y_train, epochs=5)

# 테스트 데이터 세트를 사용하여 모델을 평가합니다. 
model.evaluate(x_test,  y_test, verbose=2)