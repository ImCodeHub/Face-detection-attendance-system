import tensorflow as tf

with tf.compat.v1.Session() as sess:

    node1=tf.constant(3.0, tf.float32)
    node2=tf.constant(4.0, tf.float32)

    print(sess.run([node1,node2]))