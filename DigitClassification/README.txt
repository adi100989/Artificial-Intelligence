1. Naïve Bayes Classifier 
		
The problem was to categorize the handwritten digits according to the pixel values, into digit classes.
The data set given: 

Number of records:
5000 – training images
5000 – training labels
1000- test images
1000- training labels


Total Features:
28*28 pixel values of 3 types :
‘ ’ – blank or white space
‘+’ -  grey 
‘#’- black 

Digit Classes:
0-9 digit classification

Approach 
1.	Calculated the prior probability of each image in the training set using the labels assigned (#labels/#samples) per digit
2.	Calculated the likelihood function using a 3d matrix wherein for each pixel value per image, the counts were updated if 
    (‘  ’,’+’, ‘#’) values were found. These counts per digit were divided by the count of the number of images per sample.
3.	To take care of probabilities which were 0 for certain cases, a simple smoothening was applied, where a very small epsilon 
    value of 0.0005 was added to probabilities if it was 0, so as not to negate the whole probability when multiplied by 0.
4.	Steps 1-3 described the training. Now for the testing phase, I had to multiply the prior probability of every  digit x with 
    the probability that the pixel at position 1 has a certain value given it is digit x. 
5.	 This is done for every pixel value and every pixel and per image, per digit values is calculated. 
6.	For every image , the digit which has the highest probability value, most closely resembles the digit and thus the image 
    will be classified as this digit.
7.	The total number of correct classifications are counted and divided by the number of labels to find the accuracy value.
    In our case it was 78%.
8.	To Run the program simply place the training and test file s in a folder mentioned in the code or change the value to 
    read the correct file and run. Eg. Naive_Bayes/trainingimages.txt (line 29,30,34,35)


Result ( 78 % accuracy)

 
