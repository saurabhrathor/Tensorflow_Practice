'''
Learning
1. tf.gather --> gathers elements from matrix, provided with indices
2. tf.where --> compares element wise, and output the indices
3. tf.range --> generate a range - start, end, gap
4. tf.diag --> make a diagnol matrix of input value

'''


import tensorflow as tf

sess = tf.Session()
x = tf.constant([29.05088806,  27.61298943,  31.19073486,  29.35532951,
  				30.97266006,  26.67541885,  38.08450317,  20.74983215,
  				34.94445419,  34.45999146,  29.06485367,  36.01657104,
  				27.88236427,  20.56035233,  30.20379066,  29.51215172,
  				33.71149445,  28.59134293,  36.05556488,  28.66994858])

print(sess.run(tf.gather(x, tf.where(x>30.,x=None,y=None))))
