'''
# 1b: Create two 0-d tensors x and y randomly selected from the range [-1, 1).
# Return x + y if x < y, x - y if x > y, 0 otherwise.

Using Case

Learnings - 
1. tf.case
2. typecasting in tensorflow
3. tf.Interactivesession
'''

import tensorflow as tf

sess = tf.InteractiveSession()
x = tf.random_uniform([])
y = tf.random_uniform([])
out1 = tf.cond(tf.greater(x,y), lambda:tf.add(x,y), lambda:(tf.subtract(x,y)))
print(x.eval(), y.eval(), out1.eval())

x = tf.random_uniform([],-1,1)
y = tf.random_uniform([],-1,1)
def f1(): return tf.cast(tf.add(x,y), tf.float32)
def f2(): return tf.cast(tf.subtract(x,y), tf.float32)
def f3(): return tf.cast(tf.constant(0), tf.float32)
out2 = tf.case({tf.less(x, y):f2, tf.greater(x,y):f1}, default=f3)
print(x.eval(), y.eval(), out2.eval())
