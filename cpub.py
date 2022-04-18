#Wirtten by John Hofmeyr
#04/16/2022

from multiprocessing import Process, Value, Array, Manager
import time
import numpy as np
import matplotlib.pyplot as plt
import os
import math
import random
import sys

def RunTest(CPU_Core, operation_time):
    operation = operation_time[CPU_Core]

    start = time.time()
    FindPrime(CPU_Core, 500)
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    FFT_BIG(CPU_Core, 300, 500) #Dataset Size, Run count
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    MatrixMultiply(CPU_Core, 300, 500) #Dataset Size, Run count
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    MatrixDivide(CPU_Core, 300, 500) #Dataset Size, Run count
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    Add(CPU_Core, 100000) #Run Count * 100
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    Subtract(CPU_Core, 100000) #Run Count * 100
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    Multiply(CPU_Core, 100000) #Run Count * 100
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    Divide(CPU_Core, 100000) #Run Count * 100
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

    operation = operation_time[CPU_Core]
    start = time.time()
    Exponent(CPU_Core, 500) #Run Count * 100
    end = time.time()
    operation.append(end-start)
    operation_time[CPU_Core] = operation

def FindPrime(CPU_Core, NumberOfPrimes):
    runs = 0
    while NumberOfPrimes >= runs:
        start = time.time()
        for num in range(0, NumberOfPrimes + 1):
            if num > 1:
                for i in range(2, num):
                    if(num%i) == 0:
                        break
                    else:
                        runs += 1
                        end = time.time()
                        if CPU_Core == 0:
                            print(" Prime Size = {} | Prime: {} | Time taken: {:.2f} sec".format(NumberOfPrimes, num, end-start), end = "\r")
                        runs += 1
    if CPU_Core == 0:
        print(" ") #next line

def FFT_BIG(CPU_Core, DataSetSize, RunCount):
    runs = 0

    while RunCount >= runs:
        start = time.time()

        t = np.random.rand(DataSetSize, DataSetSize)+random.random()
        freq = t
        x = 3*np.sin(2*np.pi*freq*t)

        t = np.random.rand(DataSetSize, DataSetSize)+random.random()
        freq = t
        x += np.sin(2*np.pi*freq*t)

        t = np.random.rand(DataSetSize, DataSetSize)+random.random()
        freq = t
        x += 0.5* np.sin(2*np.pi*freq*t)

        end = time.time()
        runs +=1
        if CPU_Core == 0:
            print(" FFT Size = {} | Time taken: {:.2f} msec".format(len(x), (end-start)*1000), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def MatrixMultiply(CPU_Core, Size, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        Matrix1 = np.random.rand(Size, Size)*(random.random() + random.uniform(1, 10))
        Matrix2 = np.random.rand(Size, Size)*(random.random() + random.uniform(1, 10))

        result = np.matmul(Matrix1, Matrix2)
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" MULTIPLY: Matrix Size = {} | Time taken: {:.2f} msec".format(Size, (end-start)*1000), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def MatrixDivide(CPU_Core, Size, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        Matrix1 = np.random.rand(Size, Size)*(random.random() + random.uniform(1, 10))
        Matrix2 = np.random.rand(Size, Size)*(random.random() + random.uniform(1, 10))

        result = np.divide(Matrix1, Matrix2)
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" DIVIDE: Matrix Size = {} | Time taken: {:.2f} msec".format(Size, (end-start)*1000), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def Add(CPU_Core, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        num1 = random.random() * (random.random() + random.uniform(0, 100000))
        num2 = random.random() * (random.random() + random.uniform(0, 100000))

        num3 = num1+num2
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" ADD, {:,} Runs".format(RunCount), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def Subtract(CPU_Core, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        num1 = random.random() * (random.random() + random.uniform(0, 100000))
        num2 = random.random() * (random.random() + random.uniform(0, 100000))

        num3 = num1-num2
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" Subtract, {:,} Runs".format(RunCount), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def Multiply(CPU_Core, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        num1 = random.random() * (random.random() + random.uniform(1000, 10000000))
        num2 = random.random() * (random.random() + random.uniform(1000, 10000000))

        num3 = num1*num2
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" Multiply, {:,} Runs".format(RunCount), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def Divide(CPU_Core, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        num1 = random.random() * (random.random() + random.uniform(1000, 10000000))
        num2 = random.random() * (random.random() + random.uniform(1000, 10000000))

        num3 = num1/num2
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" Divide, {:,} Runs".format(RunCount), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def Exponent(CPU_Core, RunCount):
    runs = 0
    while RunCount >= runs:
        start = time.time()
        num1 = random.random() * (random.random() + random.uniform(10000, 100000))
        num2 = random.random() * (random.random() + random.uniform(10000, 100000))

        num4 = int(num1)**int(num2)
        runs += 1
        end = time.time()
        if CPU_Core == 0:
            print(" Exponent, {} Runs".format(RunCount), end = "\r")
    if CPU_Core == 0:
        print(" ") #clear line

def readCoreInput(totalCoreCount):
    while True: #Makes sure you can only enter the right number of cores
        try:
            core_Count = int(input("Enter The Number of CPU Cores to test, Min of 1, Max of {}: ".format(totalCoreCount-1)))
            if (core_Count <= totalCoreCount) and (core_Count >= 0):
                break
            else:
                print("Number of CPU cores entered is invalid. Please Try again")
        except ValueError:
            print("Error, entered core count higher than available cores.")

    return(core_Count)

def createProcess(core_Count):
    for i in range(core_Count): #For the specified number of cores, append that number to CPU_
         core.append("CPU_"+str(i))
         operation_time.append([0])

    for i in range(core_Count): #For each core value create a new process
        core[i] = Process(target = RunTest, args=(i, operation_time)) #All other CPU cores can be used for the test

def start_and_run(core_Count):
    for i in range(core_Count): #Start each core process
        core[i].start()

    for i in range(core_Count): #Join each core process
        core[i].join()


if __name__ == "__main__":
    totalCoreCount = os.cpu_count()
    numCores = readCoreInput(totalCoreCount)
    core = []  #Array of Cores
    manager = Manager()
    operation_time = manager.list()
    createProcess(numCores)
    start_and_run(numCores)
    Score = 0
    for col in range(len(operation_time)):
        for row in range(col):
            Score += operation_time[row]

    print(Score)
