import tensorflow as tf

#This is our dataset
mnist = tf.keras.datasets.mnist #28x28 images of hand-written digits 0-9

#This destructures the dataset into tuples
(x_train, y_train), (x_test, y_test) = mnist.load_data()