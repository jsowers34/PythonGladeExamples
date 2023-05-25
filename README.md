# PythonGladeExamples
A set of examples of the use of Python 3 and GTK+3 using Glade as a designer.

In trying to create a number of project using both Glade and Python 3, I have spent many frustrating hours 
searching the web to find useful, and simple, examples for the use of various containers, widgets, etc..

This repository is my effort to provide some straightforward samples of the use of common tools, such as
Comboboxes, TextViews, CheckButtons (CheckBoxes), RadioButtons, and so forth.
Each sample is setup as a Python3 file and a corresponding Glade file; as such they have the same file names with only the extension changed.
For example, RadioButtonTest.py makes use of RadioButtonTest.glade.

Since part of my frustrations have included downloading samples (when found) and having them fail to run, here is a word of warning:
These samples work under Debian 10,  Python 3 and Glade 3.22.1 and GTK+3.   They are purposely kept minimal so that any changes should be relatively easy
to fix when they become obsolete such as changing to newer version of python, GTK or Glade.

At present there are examples for:
    Radio Buttons
    Check Boxes (or Buttons)
    ComboBoxes and ComboBoxText
    
Some of the samples use other elements of GTK+3 by necessity or as a placeholder (where interaction is absent).  For example, GTKWindow, various containers and widgets may be used.   Specifically, a TextView or Entry may be present to reflect selections made from the primary objects of the sample.

Note that the png files, except for the rff_logo.png, are used in the Assistant example.  The rff_logo.png is used in the About example.
