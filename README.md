# Emerging Technologies Project
This repository contains code and information for my fourth-year (hons) undergraduate project for the module **Emerging Technologies .**
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics for the course [B.S.c. (Hons) in Software Developement.](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) The module outline can be viewed at https://emerging-technologies.github.io/ and additional information regarding the project can be viewed by following this [link](https://emerging-technologies.github.io/problems/project.html). The lecturer is  [Dr. Ian McLoughlin](https://ianmcloughlin.github.io/).

## Project Guidelines:
> In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

## What is MNIST:
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets.  

The MNIST database of handwritten digits has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image. Additional information can be viewed [here](https://en.wikipedia.org/wiki/MNIST_database) and the MNIST database [website](http://yann.lecun.com/exdb/mnist/).

## What is TensorFlow: 
TensorFlow™ is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

## What is Flask:  
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

## How to run:
All of the model code can be viewed inside `MNIST-Notebook.ipynb` along with the results of running the code by clicking this **[link](https://github.com/RicardsGraudins/Emerging-Technologies-Project/blob/master/MNIST-Notebook.ipynb)**.

**If you would like to run the *notebook* locally, do the following:**  
Download the repository and using the command console CD into the directory and launch jupyter notebook by typing `jupyter notebook` and in the browser window that pops up click on `MNIST-Notebook.ipynb`. To run the code click inside the coding blocks and press shift enter, the code should be run starting from step 1 onwards, otherwise if the code is run starting from the step 3 coding block for example, an error will be displayed as certain variables, imports etc. will not have been defined without running all the other exercises first.

Alternatively you can can just run the entire notebook by clicking `Cell` followed by `Run All`. Remember to change the directory of the image you would like to test in step 5 and keep in mind that the training in step 4 can take a while depending on your hardware.

**If you would like to run the project locally using *flask*, do the following:**  
Download the repository and using the command console CD into the directory/Project and type `python runme.py` or `py runme.py` depending on your version of Python. The application will then be accessable in your browser by going to the address displayed in the console window.

### Prerequisites:
When running the code locally the following prerequisites must be installed:  
* Python.  
  - Recommended version [3.6.1](https://www.python.org/downloads/release/python-361/).
* Jupyter.  
  - Installation guide available [here](http://jupyter.readthedocs.io/en/latest/install.html).
* Matplotlib.  
  - Installation guide available [here](https://matplotlib.org/downloads.html).
* Numpy.  
  - Installation guide available [here](http://www.numpy.org/).
* Tensorflow.
  - Installation guide available [here](https://www.tensorflow.org/install/).
  - Takes approx 5-10 minutes to install Tensorflow with CPU support.
* TFLearn.
  - Installation guide available [here](http://tflearn.org/installation/).
* Pillow.
  - Installation guide available [here](http://pillow.readthedocs.io/en/3.4.x/installation.html).
* Flask.
  - Installation guide available [here](http://flask.pocoo.org/docs/0.12/installation/).
  
**Alternatively** you can download [anaconda](https://anaconda.org/anaconda/python) which comes with the majority (excluding Tensorflow & TFLearn) of the above and other commonly used packages for scientific computing and data science. The Jupyter website has a quick guide on installing anaconda that is recommended for new users available [here](http://jupyter.readthedocs.io/en/latest/install.html). I recommended installing anaconda as it is a much faster and easier way to get this project up and running as fast as possible.

## References:
* [MNIST](https://en.wikipedia.org/wiki/MNIST_database)  
* [TensorFlow](https://www.tensorflow.org/)  
* [Flask](http://flask.pocoo.org/docs/0.12/)  

Code references can be found inside `MNIST-Notebook.ipynb` and `runme.py`.
