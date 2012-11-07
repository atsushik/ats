#!/usr/bin/env python
# -*- coding:utf-8 -*-

import copy
import sys
import numpy
from scipy import stats
from math  import sqrt
#import numpy

class atsFunc:

    #
    # 与えられた２つの数値のリストの相関係数を返す
    #from numpy import corrcoef
    def corrcoef(self , valList1 , valList2):
        print "valList1\t: " , valList1
        if self.nanstd(valList1) == 0:
            return Nan
        print "valList2\t: " , valList2
        if self.nanstd(valList2) == 0:
            return Nan
        print numpy.corrcoef(valList1 , valList2)
        return numpy.corrcoef(valList1 , valList2)[0][1]
    #
    # 与えられた数値のリストの平均値を返す
    def average(self , valList):
        return sum(valList) / float(len(valList))
    #
    # 与えられた数値のリストの不変分散を返す
    def nanstd(self , valList):
        return sqrt(sum((x - self.average(valList))**2 for x in valList) / float(len(valList) - 1))
    #
    # Generalized ESD Test for Outliers
    # http://www.itl.nist.gov/div898/handbook/eda/section3/eda35h3.htm
    # 数値のリストをvalueListとして与えると、「外れ値ではない数値のリスト」と「外れ値の数値のリスト」のリストを返す
    def gesdOutlierTest(self, valueList , maxOutlierCount = 10 , confidenceInterval =  0.95 , debugFlag = False):
        alpha = 1.0 - confidenceInterval
        #
        valueList.sort()
        #
        if debugFlag == True:
            print u"%s\t%s\t%s\t%s" % ("idx" , "R" , "gesdCriticalValue" , "outlierflag")
        outlierFlagList = []
        #outlierFlagList.append('')
        removeCount = 0
        R = [0]
        workingList = copy.deepcopy(valueList)
        for idx in range(1, maxOutlierCount + 1):
            maxIdx = -1
            maxR   = 0
            for idx2 in range(0, len(workingList)):
                avg = sum(workingList) / float(len(workingList))
                nanstd = sqrt(sum((x - avg)**2 for x in workingList) / float(len(workingList) - 1))
                Rval = abs(workingList[idx2] - avg) / nanstd
                if maxR < Rval:
                    maxR   = Rval
                    maxIdx = idx2
            workingList.remove(workingList[maxIdx])
            R.append(maxR)
            #
            p = (alpha / (2. * (len(valueList) - idx + 1.0)))
            tVal = stats.t.isf(p , len(valueList) - idx - 1.0)
            gesdCriticalValue = ((len(valueList) - idx) * (tVal))/sqrt((len(valueList) - idx - 1.0 + tVal**2.0)*(len(valueList) - idx + 1))
            #
            outLierFlag = "_"
            if R[idx] > gesdCriticalValue:
                outLierFlag = "*"
                removeCount = idx
            outlierFlagList.append(outLierFlag)
            if debugFlag == True:
                print u"%d\t%.6f\t%.6f\t%s" % (idx , R[idx] , gesdCriticalValue , outLierFlag)
        #
        outlierResultString = ""
        for result in outlierFlagList:
            outlierResultString += result
            outlierResultString += " "
        if debugFlag == True:
            print u"gesdOutlierTest[max=%d , confidenceInterval=%.2f]\toutlierFlagList\t%s" % (maxOutlierCount , 1-alpha , outlierResultString)
            sys.stdout.flush()
        workingList = copy.copy(valueList)
        workingList2 = []
        for idx in range(0, removeCount):
            maxIdx = -1
            maxR   = 0
            for idx2 in range(0, len(workingList)):
                avg = sum(workingList) / float(len(workingList))
                nanstd = sqrt(sum((x - avg)**2 for x in workingList) / float(len(workingList) - 1))
                Rval = abs(workingList[idx2] - avg) / nanstd
                if maxR < Rval:
                    maxR   = Rval
                    maxIdx = idx2
            workingList2.append(workingList[maxIdx])
            workingList.remove(workingList[maxIdx])
        workingList2.sort()
        return [workingList, workingList2]
