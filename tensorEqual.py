#tf.equal 

import tensorflow as tf

sess = tf.Session()

x = tf.constant([[0, -2, -1], [0, 1, 2]])
y = tf.zeros(3,3)
print(sess.run(tf.equal(x,y, name="is_equal")))
