#!/usr/bin/env python
# -*- coding:utf-8 -*-
# $Date$
# $Rev$

from atsFunc import atsFunc

import sys
import copy
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)


def main():
    print u"テスト開始"
    testGesdOutlierTest()
    testCorrcoef()
    testRootMeanSquareError()


def testRootMeanSquareError():
    myFunc = atsFunc()
    valList1 = []
    valList2 = []
    valList3 = []
    for val in range(0,10):
        valList1.append(val    )
        valList2.append(val + 1)
        valList3.append(val + 2)
    print valList1
    print myFunc.rootMeanSquareError(valList2, valList1, [1,1,0])
    print valList2
    print myFunc.rootMeanSquareError(valList2, valList2, [1,1,0])
    print valList3
    print myFunc.rootMeanSquareError(valList2, valList3, [1,1,0])

import numpy
import random
def testCorrcoef():
    myFunc = atsFunc()
    for testCount in range(0,10):
        valList1 = []
        valList2 = []
        random.seed(testCount)
        for idx in range(0,10):
            valList1.append(random.random())
            valList2.append(random.random())
        print valList1 
        print valList2
        corrcoefVal = myFunc.corrcoef(valList1 , valList2)
        print u"相関係数の値(numpy)  \t: " , numpy.corrcoef(valList1 , valList2)[0][1]
        print u"相関係数の値(atsFunc)\t: " , corrcoefVal
    valList1 = [10 , 11 , 12 , 13 , 14 , 15 , 14 , 13 , 12 , 11 , 10 , 11]
    valList2 = [10 , 11 , 12 , 13 , 14 , 15 , 14 , 13 , 12 , 11 , 10 , 11]
    corrcoefVal = myFunc.corrcoef(valList1 , valList2)
    print numpy.corrcoef(valList1 , valList2)
    print u"相関係数の値\t: " , corrcoefVal

def testGesdOutlierTest():
    valueList = [-0.25, 0.68, 0.94, 1.15, 1.20, 1.26, 1.26, \
                  1.34, 1.38, 1.43, 1.49, 1.49, 1.55, 1.56, \
                  1.58, 1.65, 1.69, 1.70, 1.76, 1.77, 1.81, \
                  1.91, 1.94, 1.96, 1.99, 2.06, 2.09, 2.10, \
                  2.14, 2.15, 2.23, 2.24, 2.26, 2.35, 2.37, \
                  2.40, 2.47, 2.54, 2.62, 2.64, 2.90, 2.92, \
                  2.92, 2.93, 3.21, 3.26, 3.30, 3.59, 3.68, \
                  4.30, 4.64, 5.34, 5.42, 6.01]
    correctRList         = [0, 3.118, 2.942, 3.179, 2.810, 2.815, 2.848, 2.279, 2.310, 2.101, 2.067]
    correctThresholdList = [0, 3.158, 3.151, 3.143, 3.136, 3.128, 3.120, 3.111, 3.103, 3.094, 3.085]
    print "valueList "    , valueList
    print "len(valueList) "    , len(valueList)
    print "R should have these values               : " , correctRList[1:]
    print "critical values should have these values : " , correctThresholdList[1:]
    testValueList = copy.deepcopy(valueList)
    maxOutlierCount = 10
    print u"-----^"
    myFunc = atsFunc()
    gesdResultList = myFunc.gesdOutlierTest(valueList , maxOutlierCount=maxOutlierCount , debugFlag=True)
    print u"外れ値とする値の個数の最大　　　　　:\t" , maxOutlierCount
    print u"外れ値ではないと判断された値のリスト:\t" , gesdResultList[0]
    print u"外れ値ではないと判断された値の個数　:\t" , len(gesdResultList[0])
    print u"外れ値となった値のリスト　　　　　　:\t" , gesdResultList[1]
    print u"外れ値となった値の個数　　　　　　　:\t" , len(gesdResultList[1])

main()
