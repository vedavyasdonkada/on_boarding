#!/usr/bin/env python
# coding: utf-8

# In[39]:


import click
@click.command()
@click.argument("input_file_path",type=click.Path(exists=True))

def count_vowel(input_file_path):
    
    """ This function expects a proper text file path and prints out the count of vowels in it """
    
    from collections import Counter
    try:
        vow=["a","e","i","o","u"]
        file=open(input_file_path,"r")
        file=file.read()
        file=file.lower().replace(" ","")
        print ({key:Counter(file)[key] for key in Counter(file).keys()if key in vow})
    except:
        print("Path doesnot exist")
if __name__ == "__main__" :
    count_vowel()

