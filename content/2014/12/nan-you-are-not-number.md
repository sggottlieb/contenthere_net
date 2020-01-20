Title: Nan, you are not a number
Date: 2014-12-10T07:06:00Z
Modified: 2015-01-06T19:28:49.173Z
Category: misc
Tags: python
Slug: 2014/12/nan-you-are-not-number
Authors: Seth Gottlieb

Here is a little programming oddity that we ran across yesterday.  

  

[onDemand](https://ondemand.lionbridge.com/) has a number of downloadable Excel reports.  To generate a useful Excel file, it is important to tell the Excel library what data type to make each cell.  To facilitate this, we had a little utility function called is_float:  

  

    
    def is_float(data):
    
        try:
            float(data)
            return True
        except Exception:
            return False
    

  

That seemed reasonable enough and it worked fine for quite some time. But then we had this customer named Nan (thanks for the business Nan!).  The problem with the name Nan is that float('Nan') doesn't return a ValueError like float('Bob').  float('Nan') successfully returns a float object with a value of 'nan.'  The reason for this is that Nan, in addition to a being fairly common name (I went to school with a girl named Nan), is Python shorthand for a "Not a Number."  Python's float function interpreted the input 'Nan' as an attempt to create a float object with a value of 'nan'.  This caused our logic to try to tell the Excel library that 'Nan' was a number and that created an error.  Incidentally, we would have had the same problem with someone named "Inf," which is Python shorthand for infinity.  

In case anyone is curious, the fix for this was quite simple:  

    
    def is_float(data):
    
        try:
            int(float(data))
            return True
        except Exception:
            return False
    

  

The int function doesn't try to be as clever.  It rejects cheeky floats like nan and inf.  You learn something new every day!
