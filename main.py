#!/usr/bin/env python

"""code template"""

import cv2
import glob


crosswalk_cascade = cv2.CascadeClassifier('cascade.xml')
lista_zd = glob.glob('test\\images\\*.png')
for zdj in lista_zd:
        image = cv2.imread(zdj)
        h, w, c = image.shape
        i=1
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cwlk = crosswalk_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=45, minSize=(50,50))
        print(zdj)
        for (x, y, w, h) in cwlk:
                print('Znak',i)
                cv2.rectangle(image, (x, y), (x + w, y + h), (190, 0, 0), 2)
                print('X1: ',x)
                print('X2: ',x + w)
                print('Y1: ',y)
                print('Y1: ',h+y)
                i+=1
        cv2.imshow('img', image)
        cv2.waitKey()

