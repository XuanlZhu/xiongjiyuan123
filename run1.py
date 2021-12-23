import tensorflow as tf
import os
tf.compat.v1.disable_eager_execution()
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
message = tf.constant("hello world")
with tf.compat.v1.Session() as sess:
    print(sess.run(message).decode())