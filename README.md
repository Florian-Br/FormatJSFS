usage: FormatJSFS.py [-h] -i INPUT -n1 N1 -n2 N2 [-d]  

Takes flattened output from 2D realsfs and creates a matrix output for use with fastsimcoal2  

options:  

    -h, --help                 show this help message and exit  
  
    -i INPUT, --Input INPUT    Input file from realSFS  
                        
    -n1 N1                     Number of haploid individuals in population 1  
  
    -n2 N2                     Number of haploid individuals in population 2  
  
    -d, --derived              Keep derived alleles (default off)  

When option -d is selsected derived alleles will be kept. If not they will be added to the d_0 class.
https://groups.google.com/g/fastsimcoal/c/QPSA0mxS-ZI/m/PYKQ50oYBQAJ
