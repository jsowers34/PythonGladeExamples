'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of Check Boxes
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers May 3, 2023
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of TextView
 *      Incidental use of GTKWindow, GTKGrid as containers
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class CheckBoxTest():
    
    def __init__(self):
        self.gladefile = "CheckBoxTest.glade"
        rows = 6
        columns = 4
        self.languages = ["APL",    "Algol",   "Assembly", "Basic",  \
                          "C",      "C++",    "Clojure", "Cobol",  \
                          "Fortran", "GPSS",   "Java",   "Lisp",   \
                          "Lua",     "Pascal", "PL/I",   "Python", \
                          "R",       "Simscript", "Snobol", "SPSS", \
                          "SQL",     "T-SQL", "TeX", "Wolfram (Mathematica)"]

        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        self.resultTxt = builder.get_object('resultTxt')
        self.resultBUF = builder.get_object('textbuffer1')
        
        # Grab the Checkboxes
        self.checkboxes = [None]*len(self.languages)
        for row in range(0, rows):
            for col in range(0, columns):
                boxname = "cb" + str(row + 1 ) + str(col + 1)
                indx = col + 4 * row
                self.checkboxes[indx] = builder.get_object(boxname)
        
        # Set up the button bar
        self.executeBtn = builder.get_object("executeBtn")
        self.executeBtn.connect('clicked', lambda w: self.checkBoxes())
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        self.topLevel.show_all()
        
    def checkBoxes(self):
        # Scan thru all the checkboxes and record the ones checked
        result = "Languages selected are "
        for i in range(0, len(self.languages)):
            if(self.checkboxes[i].get_active()):
                result += self.languages[i] + " "
        self.resultBUF.set_text(result, len(result))
            
        
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    CheckBoxTest()
    gtk.main()   
