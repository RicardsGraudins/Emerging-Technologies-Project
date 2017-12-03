from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

import tensorflow as tf
import numpy as np
from PIL import Image
import tflearn
from tensorflow.examples.tutorials.mnist import input_data

app = Flask(__name__)

#Folder location for uploaded images
UPLOAD_FOLDER = 'C:/Users/Richard/Desktop/Images'
#Type of files that can be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'mysecret'

#Ref http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

#Setting allowed files
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		#Flash message & redirect if user tries to upload a file outside of the ALLOWED_EXTENSIONS
		if 'file' not in request.files:
			flash('This type of file cannot be uploaded.\n Please upload a file that uses one of the following formats .png .jpg .jpeg')
			return redirect(request.url)
		file = request.files['file']
		#Flash message & redirect if user clicks button without selecting a file to upload
		if file.filename == '':
			flash('No Selected File')
			return redirect(request.url)
		#If the file meets the criteria - upload to the UPLOAD_FOLDER & render template Uploaded.html
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return predict(filename)
	return render_template('Home.html')
	
#Restoring model, view jupyter notebook for further documentation, training & testing etc.
#Ref https://stackoverflow.com/questions/43887425/how-to-import-a-model-in-tensorflow
def predict(filename):
	#Placeholders
	#None means we can input any number of images
	#Input has 784 dimensional vector (28x28)
	#Output has to be 1 out of 10 outcomes, 0-9 digit
	x = tf.placeholder(tf.float32,shape=[None, 784])
	y_ = tf.placeholder(tf.float32,shape=[None, 10])

	#Input Layer: -1 meaning no fixed batch dimension
	#28x28 reshape and 1 for greyscale
	x_input = tf.reshape(x,[-1,28,28,1], name='input')

	#Layer 1: 32 output filters, filter size 5x5,
	#stride of 2, same padding and RELU activation
	layer1 = tflearn.layers.conv.conv_2d(x_input, nb_filter=32, filter_size=5, strides=[1,1,1,1],padding='same', activation='relu', regularizer="L2", name='layer1')

	#Pooling layer 1: Preforms max pooling 2x2 filter
	#and stride of 2 on layer 1
	out_layer1 = tflearn.layers.conv.max_pool_2d(layer1, 2)

	#Layer 2: 32 output filters, filter size 5x5,
	#stride of 2, same padding and RELU activation
	layer2 = tflearn.layers.conv.conv_2d(out_layer1, nb_filter=32, filter_size=5, strides=[1,1,1,1],padding='same', activation='relu',  regularizer="L2", name='layer2')

	#Pooling layer 2: Preforms max pooling 2x2 filter
	#and stride of 2 on layer 2
	out_layer2 = tflearn.layers.conv.max_pool_2d(layer2, 2)

	#Fully connected layer takes in layer 2 after pooling and has 1024 neurons
	fcl = tflearn.layers.core.fully_connected(out_layer2, 1024, activation='relu')

	#Dropout - simple way to prevent NN overfitting
	fcl_dropout = tflearn.layers.core.dropout(fcl, 0.8)

	#Predicted output using softmax
	y = tflearn.layers.core.fully_connected(fcl_dropout, 10, activation='softmax', name='output')

	#Loss function
	cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

	#Optimiser
	#train_step = tf.train.AdamOptimizer(0.01).minimize(cross_entropy)
	train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

	#Accuracy of the model
	correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	
	#Create the session
	sess = tf.InteractiveSession()
	#Initialize the variables
	tf.global_variables_initializer().run()

	#Restoring model - not working correctly..
	#model_path = "Model/mymodel"
	#saver = tf.train.import_meta_graph(model_path+'.meta')
	#saver.restore(sess, model_path)
	
	#Since the model doesn't restore correctly we train it, further documentation in readme
	#Get the MNIST data
	mnist = input_data.read_data_sets("MNIST_Data/", one_hot=True)
	#Short training session
	#Number of interations
	epoch=500
	#Batch size
	batch_size=50
	#Keep probability
	keep_prob = tf.placeholder(tf.float32)
	for i in range(epoch):
		batch = mnist.train.next_batch(batch_size)
		if i % 100 == 0:
			train_accuracy = accuracy.eval(feed_dict={
				x: batch[0], y_: batch[1], keep_prob: 1.0})
		train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

	img = Image.open(UPLOAD_FOLDER + "/" + filename)
	#Resize the image 28x28
	img = img.resize((28,28), Image.ANTIALIAS)
	#Convert to array
	img = np.array(img)
	#Normalise input
	imgN = img/np.max(img).astype(float)
	#Reshape to input layer shape
	test_myImage = np.reshape(imgN, [1,784])
	#Run the image through the session
	pred = (sess.run(y, feed_dict = {x:test_myImage}))
	predicted_class = np.argmax(pred)
	print("Predicted number: {}".format(predicted_class))
	displaymessage = "The predicted number is: {}".format(predicted_class)
	return render_template('Uploaded.html', displaymessage = displaymessage)

if __name__ == "__main__":
	app.run(debug=True)