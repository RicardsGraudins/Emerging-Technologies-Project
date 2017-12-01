# Emerging Technologies Project
This repository contains code and information for my fourth-year (hons) undergraduate project for the module **Emerging Technologies .**
The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics for the course [B.S.c. (Hons) in Software Developement.](https://www.gmit.ie/software-development/bachelor-science-honours-software-development) The module outline can be viewed at https://emerging-technologies.github.io/ and additional information regarding the project can be viewed by following this [link](https://emerging-technologies.github.io/problems/project.html). The lecturer is  [Dr. Ian McLoughlin](https://ianmcloughlin.github.io/).

## What is MNIST:
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets.  

The MNIST database of handwritten digits has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image. Additional information can be viewed [here](https://en.wikipedia.org/wiki/MNIST_database) and the MNIST database [website](http://yann.lecun.com/exdb/mnist/).

## What is TensorFlow: 
TensorFlow™ is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

## What is Flask:  
Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

## References:
[MNIST](https://en.wikipedia.org/wiki/MNIST_database)  
[TensorFlow](https://www.tensorflow.org/)  
[Flask](http://flask.pocoo.org/docs/0.12/)

## Project Guidelines:
> In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

### Instructions:
>1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
>2. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
>3. Add a route to your application that accepts requests containing a user input image and responds with the digit.
>4. Connect the HTML page to the route using AJAX.
