import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
def load_(root):
    Data = pd.read_csv(root, delimiter= ',', encoding= 'utf-8', header= None)
    data = Data.to_numpy()
    trainloss = []
    validloss = []
    trainaccu = []
    validaccu = []

    for i in range(0, np.size(data, axis= 1)):
        trainloss.append(data[0][i])
        validloss.append(data[1][i])
        trainaccu.append(data[2][i])
        validaccu.append(data[3][i])

    return trainloss, validloss, trainaccu, validaccu

# Plot loss
def plotloss(train, valid):
    print(len(train), len(valid))
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.plot(range(0, len(train)), train, color = 'blue', label = 'training loss')
    plt.plot(range(0, len(valid)), valid, color = 'red', label = 'validation loss')
    plt.legend()
    plt.show()

# Plot accuracy
def plotaccu(train, valid):
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.plot(range(0, len(train)), train, color = 'blue', label = 'training accuracy')
    plt.plot(range(0, len(valid)), valid, color = 'red', label = 'validation accuracy')
    plt.legend()
    plt.show()

def main():
    trainloss, validloss, trainaccu, validaccu = load_(root= "/home/meng/model/output.csv")
    plotloss(trainloss, validloss)
    plotaccu(trainaccu, validaccu)
    
    # print(trainloss)
    # print(validloss)
    # print(trainaccu)
    # print(validaccu)


main()

