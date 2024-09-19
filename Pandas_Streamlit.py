import pandas as pd
import streamlit as st
# import numpy as np
st.title("REF: Pandas Cheat Sheet")
"""
## Creating tables
There are two main objects in pandas: `DataFrame` (table) and `Series` (a sequence of values, such as a single column of a DataFrame). A table has row keys - indexes and column keys - columns. By default, the index is integer-based. Row indexes don't have to be unique. If they are the same, accessing the index with `df.loc[row]` will return a table with multiple rows.

The key difference from `numpy` arrays is that pandas `DataFrame` `columns` can be of different types (including class instances). A table can be transposed with df.T, so there's no fundamental difference between rows and columns. However, if the columns are of different types, transposing will convert all types into object.
``` py
import pandas as pd
 
df = pd.DataFrame()              # create an empty table
print(df.index, df.columns)      # Index( [] )  Index([])
 
df = pd.DataFrame([1,3,2],       # one column with 3 numbers named A 
                  columns=['A']) # default row indexes [0,1,2]
print(df.index)                  # RangeIndex(start=0,stop=3,step=1)
print(df.columns)                # Index(['A'])
 
df = pd.DataFrame()              # same as above
df['A'] = [1,2,3]                # create a column in the empty table
 
df = pd.DataFrame([[1,2],        # table from a 2D array
                   [3,4]])       # first row [1,2], second row [3,4]
```                   
    """
df = pd.DataFrame([[1,2], [3,4]]) 
st.dataframe(df)
"""
The table can be defined using a dictionary (its keys are the column names). If a key has a scalar value, it will be duplicated. When specifying row keys (index), you can mix str, int, Timestamp etc.:
``` py
import numpy as np 
cat = pd.Categorical(["a","b","a"])}        # categorical (not strings!)
df  = pd.DataFrame(
          {"Num":  1,                       #    | Num Name Age Cat
           "Name": ["Jon", "Mia", "Sam"],   #  --------------------
           "Age" : [43,     None, 56],      #  m | 1   Jon  43   a
           "Cat" : cat},                    #  f | 1   Mia  None b
           index=['m', 'f', 0])             #  0 | 1   Sam  56   a

```
"""
cat = pd.Categorical(["a","b","a"])        # categorical (not strings!)
df  = pd.DataFrame(
        {"Num":  1,                      #    | Num Name Age Cat
        "Name": ["Jon", "Mia", "Sam"],   #  --------------------
        "Age" : [43,    None, 56],       #  m | 1   Jon  43   a
        "Cat":  cat},                    #  f | 1   Mia  NaN  b
        index=['m', 'f', 0])             #  0 | 1   Sam  56   a

st.dataframe(df)
"""
A list of dictionaries represents a list of rows. Each new key generates a column:
``` py
pass                                        #    |  b   c   a
pd.DataFrame([{        'b': 1, 'c': 2},     #  ----------------
              {'a': 3, 'b': 4, 'c': 5}])    #  0 |  1   2   NaN
                                            #  1 |  3   4   5
df1 =  df.copy()                            # deepcopy of the table
```
"""
st.dataframe(pd.DataFrame([{'b': 1, 'c': 2},  {'a': 3, 'b': 4, 'c': 5}]))



def main():
    
    #st.write("Введіть повідомлення:")

    message = st.text_input("Ваше повідомлення")
    if st.button("Надіслати"):
        st.write("Ваше повідомлення:", message)
        st.write("Відповідь: Привіт! Як я можу допомогти?")

if __name__ == "__main__":
   # main()
   pass