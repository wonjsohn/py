#!/usr/bin/env python
# -*- coding: utf-8 -*-       

### this script removes the last line of the raw text files in order to avoid parsing error of the incomplete line

if __name__ == "__main__":           
    
    txtfile = 'output_20130327_123509.txt'
    lines = file(txtfile,  'r').readlines()
    del lines[-1] 
    file(txtfile, 'w').writelines(lines) 

  
  ## remove the last line of the file ##
#    lines = file(txtfile, 'r').readlines() 
#    del lines[-1] 
#    file(txtfile, 'w').writelines(lines) 
    #########################
