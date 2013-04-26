#!/usr/bin/env python
# -*- coding: utf-8 -*-


class printStuffs():



    def printJointAngle(self, txtfile, digit_to_plot, data_path):
        j1List=[]
        j2List=[]
        j3List=[]
        indexList=[]
        
        for line in open(data_path+txtfile,  "r").readlines()[digit_to_plot::10]:  # read a row in every 10 rows, starting from the row =(digit_to_plot) 
            index, j1 ,  j2,  j3= line.split()
            j1 = float(j1)
            j2 = float(j2)
            j3 = float(j3)
            indexList.append(index)
            j1List.append(j1)   #joint1
            j2List.append(j2)   #joint2
            j3List.append(j3)  #joint3
        return j1List
        


if __name__ == '__main__':
    from pylab import *     
    import sys
    import scipy
    import numpy
    import matplotlib.pyplot    
    
    txtfile1 = 'output_20130408_171911_baseline.txt'
    txtfile2 = 'output_20130408_172728_index1.txt'
    txtfile3 = 'output_20130408_172825_index2.txt'
    txtfile4 = 'output_20130408_172952_middle1.txt'
    txtfile5 = 'output_20130408_173114_middle2.txt'
    txtfile6 = 'output_20130408_173251_both1.txt'
    txtfile7 = 'output_20130408_173401_both2.txt'
    txtfile8 = 'output_20130408_173546_MVC.txt'
    
#    txtfile1 = 'output_20130415_170806_baseline.txt'
#    txtfile2 = 'output_20130415_171138_indexOnly1.txt'
#    txtfile3 = 'output_20130415_171428_indexOnly2.txt'
#    txtfile4 = 'output_20130415_171531_middleOnly1.txt'
#    txtfile5 = 'output_20130415_171727_middleOnly2.txt'
#    txtfile6 = 'output_20130415_171822_both1.txt'
#    txtfile7 = 'output_20130415_171939_both2.txt'


#    DATA_PATH ="C:\\Code\\nerf_verilog\\source\\py\\data_parse\\glove_data\\20130415_ES\\"
    DATA_PATH ="C:\\Code\\nerf_verilog\\source\\py\\data_parse\\glove_data\\20130408_EL56\\"
    
    ps = printStuffs()
    ### digit_to_plot:  2- thumb, 3- index, 4 - middle....
    mcp_index1_index = ps.printJointAngle(txtfile2, 3, DATA_PATH)
    mcp_index1_middle = ps.printJointAngle(txtfile2, 4, DATA_PATH)
    mcp_index2_index = ps.printJointAngle(txtfile3, 3, DATA_PATH)
    mcp_index2_middle = ps.printJointAngle(txtfile3, 4, DATA_PATH)
    
    mcp_middle1_index = ps.printJointAngle(txtfile4, 3, DATA_PATH)
    mcp_middle1_middle = ps.printJointAngle(txtfile4, 4, DATA_PATH)
    mcp_middle2_index = ps.printJointAngle(txtfile5, 3, DATA_PATH)
    mcp_middle2_middle = ps.printJointAngle(txtfile5, 4, DATA_PATH)
    
    mcp_both1_index = ps.printJointAngle(txtfile6, 3, DATA_PATH)
    mcp_both1_middle = ps.printJointAngle(txtfile6, 4, DATA_PATH)
    mcp_both2_index = ps.printJointAngle(txtfile7, 3, DATA_PATH)
    mcp_both2_middle = ps.printJointAngle(txtfile7, 4, DATA_PATH)

    
##    fig = plt.figure()
#######################################################
#    num_of_subplots = 6
#    fig, axes = plt.subplots(num_of_subplots, 1, sharex=True, sharey=True)
#    axes[0].plot(mcp_index1_index, label = "move index only, index, t1")
#    axes[0].plot(mcp_index1_middle, color='r', label = "move index only, middle, t1")
#    axes[1].plot(mcp_index2_index,  label = "move index only, index, t2")
#    axes[1].plot(mcp_index2_middle, color = 'r',  label = "move index only, middle, t2")
#    
##    axes[2].plot(mcp_middle1_index, label = "move middle only, index, t1")
#    axes[2].plot(mcp_middle1_middle, color='r', label = "move middle only, middle, t1")
#    axes[3].plot(mcp_middle2_index,  label = "move middle only, index, t2")
#    axes[3].plot(mcp_middle2_middle, color = 'r',  label = "move middle only, middle, t2")
#    
#    axes[4].plot(mcp_both1_index, label = "move both, index, t1")
#    axes[4].plot(mcp_both1_middle, color='r', label = "move both, middle, t1")
#    axes[5].plot(mcp_both2_index,  label = "move both, index, t2")
#    axes[5].plot(mcp_both2_middle, color = 'r',  label = "move both, middle, t2")

#    axes[0].plot(mcp_index1_index, label = "move index only, index, t1")
#    axes[0].plot(mcp_index1_middle, color='r', label = "move index only, middle, t1")
#    axes[1].plot(mcp_index2_index,  label = "move index only, index, t2")
#    axes[1].plot(mcp_index2_middle, color = 'r',  label = "move index only, middle, t2")
##########################################################

    num_of_subplots = 6
    fig, axes = plt.subplots(num_of_subplots, 1, sharex=True, sharey=True)

    subplots_adjust(hspace=0.25)   # spacing between subplots
 
    mcp_index1_diff = []
    for a, b  in zip(mcp_index1_index,  mcp_index1_middle):
        mcp_index1_diff.append(abs(b-a))
    mcp_index2_diff = []
    for a, b  in zip(mcp_index2_index,  mcp_index2_middle):
        mcp_index2_diff.append(abs(b-a))
    mcp_middle1_diff = []
    for a, b  in zip(mcp_middle1_index,  mcp_middle1_middle):
        mcp_middle1_diff.append(abs(b-a))
    mcp_middle2_diff = []
    for a, b  in zip(mcp_middle2_index,  mcp_middle2_middle):
        mcp_middle2_diff.append(abs(b-a))
    mcp_both1_diff = []
    for a, b  in zip(mcp_both1_index,  mcp_both1_middle):
        mcp_both1_diff.append(abs(b-a))
    mcp_both2_diff = []
    for a, b  in zip(mcp_both2_index,  mcp_both2_middle):
        mcp_both2_diff.append(abs(b-a))
    
    axes[0].plot(mcp_index1_diff, label = "indexOnly, |diff|,  t1")
    axes[1].plot(mcp_index2_diff,  label = "indexOnly, |diff|,  t2")
    axes[2].plot(mcp_middle1_diff, label = "middleOnly, |diff|,  t1")
    axes[3].plot(mcp_middle2_diff,  label = "middleOnly, |diff|,  t2")
    axes[4].plot(mcp_both1_diff, label = "both, |diff|,  t1")
    axes[5].plot(mcp_both2_diff,  label = "both, |diff|,  t2")    
    
    ylim(0.0,  1.5)
#    plt.title('Eric Sohn')
#    axes[0].set_title('mcp_index1_index')
#    axes[1].set_title('mcp_index1_middle')
#    axes[2].set_title('mcp_index2_index')
#    axes[3].set_title('mcp_index2_middle')
    
    for i in range(num_of_subplots):
        axes[i].grid()
        axes[i].legend(loc='best')
        
    fig.suptitle("diff, EL56")
#    number_of_subplots =4
#    ax1 = fig.add_subplot(number_of_subplots,  1, 1)
#    ax2 = fig.add_subplot(number_of_subplots,  1,  2)
#    ax3 = fig.add_subplot(number_of_subplots,  1,  3)
#    ax4 = fig.add_subplot(number_of_subplots,  1,  4)
#    ax5 = fig.add_subplot(number_of_subplots,  1,  5)
#    ax6 = fig.add_subplot(number_of_subplots,  1,  6)

        
#    ax1.grid(True)
#    ax2.grid(True)
#    ax3.grid(True)
#    ax4.grid(True)
#    
#    ax1.plot(mcp_index1_index)
#    ax2.plot(mcp_index1_middle)
#    ax3.plot(mcp_index2_index)
#    ax4.plot(mcp_index2_middle)
#    
#    ax1.set_title('mcp_index1_index')
#    ax2.set_title('mcp_index1_middle')
#    ax3.set_title('mcp_index2_index')
#    ax4.set_title('mcp_index2_middle')

    show()
    
