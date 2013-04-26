if __name__ == '__main__':
    from cStringIO import StringIO
    from pylab import *
    s = StringIO()
  
  
     
#    df = pd.read_csv('output_20130321_163326.txt',  sep='\t')    
#    df = pd.read_csv('output_20130321_163326.txt',  sep='\t')    
    
#    s1 = StringIO()
#    s2 = StringIO()
    s3 = StringIO()
    s4 = StringIO()
    s5 = StringIO()
#    with open('output_20130321_163326.txt') as f:
#        for i,  line in f:
#            if i % 3 == 0:
#            if line.startswith('0'):
#                s.write(line)



f = open('output_20130321_163326.txt')
    for i,  line in enumerate(f):
            
        if i % 10  == 2:   # digit 1
                s1.append(line)
#            s1.write(line)
        if i % 10  == 3:   # digit 2
#            s2.write(line)
                s2.append(line)
#        if i % 10  == 4:   # digit 3
#            s3.write(line)
#        if i % 10  == 5:   # digit 4
#            s4.write(line)    
#        if i % 10  == 6:   # digit 5
#            s5.write(line)

#    s1.seek(0) # "rewind" to the beginning of the StringIO object
#    s2.seek(0) # "rewind" to the beginning of the StringIO object
#    s3.seek(0) # "rewind" to the beginning of the StringIO object
#    s4.seek(0) # "rewind" to the beginning of the StringIO object
#    s5.seek(0) # "rewind" to the beginning of the StringIO object
#    
    
    
#    print s1.getvalue()
#    s1_parsed = pd.read_csv(s1,  index_col = 0) # with further parameters…
#    print s1_parsed
#    frame = pd.DataFrame(s1_parsed) 
#    frame = pd.DataFrame(s2,  columns=['digit', 'joint1',  'joint2',  'joint3'])
#    print frame
    
