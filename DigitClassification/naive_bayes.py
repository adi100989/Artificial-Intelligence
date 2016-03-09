from __future__ import division
__author__ = 'adi100989'
import sys
import time
import argparse
import math

global score
accuracy=0.000000000000
global prior_prob
prior_prob = [0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000,
              0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000]
global features_count
features_count = [[[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]],
                  [[0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)], [0.000000000000 for x in range(0, 784)]]]


def main(args):
    global prior_prob

    images = read_images_file("Naive_Bayes/trainingimages.txt", 5000)  # list of features for each label list
    values = read_labels_file("Naive_Bayes/traininglabels.txt", 5000)  # list of labels

    training(images, values, 5000)

    test_images = read_images_file("Naive_Bayes/testimages.txt", 1000)  # list of features for each label list
    test_values = read_labels_file("Naive_Bayes/testlabels.txt", 1000)  # list of labels

    #print features_count
    test(test_images, test_values, 1000)
    #print_digit( test_images[1])

    print "The accuracy attained ==",accuracy



############################################################################
#                                Training                                    #
###########################################################################



def training(images, values, max):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    global prior_prob
    global features_count

    # print values[0]
    # print count[values[0]]
    for i in range(0, max):
        count[values[i]] += 1  # number of images per label

    for i in range(0, 10):
        prior_prob[i] = (count[i] / max)
    print "The Prior Probability is \n",prior_prob


    # max_likelihood
    for i in range(0, max):
        for j in range(0, 784):
            if images[i][j] == ' ':
                features_count[values[i]][0][j] = features_count[values[i]][0][
                                                      j] + 1  # no of images for which pixel i is white
            elif images[i][j] == '+':
                features_count[values[i]][1][j] = features_count[values[i]][1][
                                                      j] + 1  # no of images for which pixel i is grey
            elif images[i][j] == '#':
                features_count[values[i]][2][j] = features_count[values[i]][2][
                                                      j] + 1  # no of images for which pixel i is black

    for i in range(0, 10):
        for j in range(0, 784):
            features_count[i][0][j] = (features_count[i][0][j]  / count[i])
            features_count[i][1][j] = (features_count[i][1][j]  / count[i])
            features_count[i][2][j] = (features_count[i][2][j]  / count[i])

    #smoothening

    for i in range(0, 10):
        for j in range(0, 784):
            if(features_count[i][0][j]==0):
                features_count[i][0][j]=0.0005
            if(features_count[i][1][j]==0):
                features_count[i][1][j]=0.0005
            if(features_count[i][2][j]==0):
                features_count[i][2][j]=0.0005


    return



############################################################################
#                                TEST                                    #
###########################################################################

def test(images,values,max):
    global features_count
    global prior_prob
    global accuracy
    prob=1
    digit_class_test=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    test_classify=[-1 for x in range(0, max)]
    '''
    digit_pixel_score=[[-1 for x in range(0, 784)],[-1 for x in range(0, 784)],[-1 for x in range(0, 784)],
                       [-1 for x in range(0, 784)],[-1 for x in range(0, 784)],[-1 for x in range(0, 784)],
                       [-1 for x in range(0, 784)],[-1 for x in range(0, 784)],[-1 for x in range(0, 784)],
                       [-1 for x in range(0, 784)]]
    '''
    for digit in range(0,10):
        digit_class_test[digit]=prior_prob[digit]


    #print "digit class test =",digit_class_test

    for image_data in range (0,max): #find probablity of digit * prob(pixel1=blank|digit)*...* etc

        for digit in range(0,10):
            prob=1
            for pixel in range(0,784):
                if images[image_data][pixel]==' ':
                    prob*=(features_count[digit][0][pixel])
                elif images[image_data][pixel]=='+':
                    prob*=(features_count[digit][1][pixel])
                elif images[image_data][pixel]=='#':
                    prob*=(features_count[digit][2][pixel])
            digit_class_test[digit]=prior_prob[digit]*prob
        #print digit_class_test
        test_classify[image_data]=find_max(digit_class_test)

    #classify done in the same loop above

    #print test_classify[0:100]
    print "\n The digits classified in the test round are \n",test_classify
    for label_entry in range(0,max):
        if test_classify[label_entry]==values[label_entry]:
            accuracy+=1

    accuracy=(accuracy/10)
    return

def find_max(digit_class_test):
    max=-1.00000

    for digit in range(0,10):
        if max<digit_class_test[digit] :
            max=digit_class_test[digit]
            digit_class=digit
    #print "max returned is",digit_class
    return digit_class



############################################################################
#                                read testfile                             #
###########################################################################
def read_images_file(filename, total):
    training = ()
    temp_list = []
    temp = []
    fileHandle = open(filename, 'r')
    line = " "
    str = ''
    while line != "":
        line = fileHandle.readline().strip('\n')
        str = str + line
        # temp=list(line)
        # temp_list.append(temp)
        # print temp
    c = 0
    while c < total:
        temp_list.append(list(str[(784 * (c)):(784 * (c + 1))]))
        c = c + 1
        # print str
        # print (temp_list)

    # print_digit(temp_list[3])
    '''
    c = 28*3
    for i in range(0, 28):
        print (str[(28 * (c)):(28 * (c + 1))])
        c = c + 1
    '''
    # print ("length is ", len(temp_list[4999]))
    return (temp_list[0:total])


def read_labels_file(filename, total):
    temp_list = []
    fileHandle = open(filename, 'r')
    line = "  "
    while line != "":
        line = fileHandle.readline().strip('\n')
        if line != '':
            temp_list.append(int(line))

    # print "\n the length of list is",len(temp_list)

    return temp_list[0:total]


def print_digit(temp_list):
    str = ''
    for i in range(0, 28):
        for j in range(0, 28):
            str = str + temp_list[(i * 28) + j]
        str = str + '\n'

    #print str


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HomeWork Five")
    parser.add_argument("--input", type=str)
    args = parser.parse_args()
    main(args)
