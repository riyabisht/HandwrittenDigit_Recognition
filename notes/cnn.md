1- Convolution operation

b) ReLU layer
2- Pooling
3- Flattening 
4 - Full Connection

Softmax and Cross Entropy

b and l 2 D array
0<= pixel value <= 255

colored image 

blue layer 
green
red

0 - white
1 - black

## Step 1 Convolution 

Introduction to Convolutional Neural Networking 
By Jianxin Wn( 2017)
[article](http://cn.nuj.edu.cn/wujx/paper/CNN.pdf)

### Feature Detector

- generally 3 X 3
- kernel / filter
- input X Featrue Detector = Feature MAp
- element wise nultiplycation
- feature reduces size of input image 
- create many feature maps 
- decide which map is more effective

### Rectified linear unit 

- input + convolutional Layer  + Rectifier  (increase non linearity in our network)
- [understanding Convolutional neural network with A mathematical Model](https://arxiv.org/pdf/1502.01852.pdf)
by : Kaiming he et al.

## Step2 Max Pooling

feature Map ----------max pooling ---> pooled feature Map
taking max of the pixel
- able to preserve feature 
- reducing size by 75%
- reducing no. of parameters
- preventing over fitting 
- [Evaluation of pooling Operation in Convolutions Architectures of Object Recognition](http://ais.uni-bonn.de/papers/icann2010_maxpool.pdf)

## step3 Flattening 

- pooled Feature Map --------- Flattening ----> input layer of a future Ann

input image ---- convolution --- pooling  -- flattening--->input layer of a future ANN

## Step 4 Full Connection

- adding ANN 
------> Flattening [input layer  ---- fully connected layer ---- output layer]-----output layer


### Softmax & Cross- Entropy

in order to make the sum of probabilities equal 1

Cross Entropy - 

### Error

- classification error
- Mean Squared Error
- cross-entropy
[reference ](https://rdipietro.github.io/friendly-into-to-cross-entropy-loss/) 


[CNN reference](https://data-flair.training/blogs/convolutional-neural-networks-tutorial/)
- One important feature of Convolutional Neural Network that sets it apart from other Machine Learning algorithms is its ability to pre-process the data by itself.
- During cold-start, the filters may require hand engineering but with progress in training, they are able to adapt to the learned features and develop filters of their own. Therefore, CNN is continuously evolving with growth in the data.

## CNN Working

- The convolutional neural network is different from the standard Neural Network in the sense that there is an explicit assumption of input as an image.

- unlike the linear arrangement of neurons in a simple neural network. These neurons have an overall structure of three dimensions – Length, Width, and Height.



