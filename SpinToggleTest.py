'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of the Slider and Spin Buttons and Toggle
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 04MAY23
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of Window, Box, Button, TextView
 ***************************************************************************** 
'''
import gi
from tkinter.test.support import widget_eq
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class SpinToggleTest():
    
    def __init__(self):
        self.languages = ["APL",    "Algol",   "Assembly", "Basic",  \
                          "C",      "C++",    "Clojure", "Cobol",  \
                          "Fortran", "GPSS",   "Java",   "Lisp",   \
                          "Lua",     "Pascal", "PL/I",   "Python", \
                          "R",       "Simscript", "Snobol", "SPSS", \
                          "SQL",     "T-SQL", "TeX", "Wolfram (Mathematica)"]
        
        self.gladefile = "SpinToggleTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        self.spinner = builder.get_object('spinBTN')
        self.spinner.set_range(0, len(self.languages)-1)     # Don't let it run past the number of languages
        self.spinnerBuf = builder.get_object('entrybuffer1')
        self.spinner.connect("value-changed", lambda w: self.spin_selected())
        
        
        self.toggle = builder.get_object('toggleBTN')
        self.toggle.connect("toggled", self.on_toggle)
        self.spinDisplay = builder.get_object('spinnerLBL')
        
        self.result = builder.get_object('resultTXT')
        self.resultBUF = builder.get_object('textbuffer1')
        
        # Initial display
        tmp = "0: " + self.languages[0]
        self.resultBUF.set_text(tmp, len(tmp))
        self.wheee_f  = False       # A flag to show when spin icon is active
        
        # Set up the button bar
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        # Let'r rip!
        self.topLevel.show_all()
        
    def bye_bye(self):
        gtk.main_quit()
        
    def spin_selected(self):
        bid = self.spinner.get_value_as_int()
        result = str(bid) + ": " + self.languages[bid]
        if not self.wheee_f:
            self.resultBUF.set_text(result, len(result))
        self.priorText = result       # Just in case we change the spin value while 'Wheee"-ing
        
    def on_toggle(self, widget, data=None):
        if widget.get_active():
            start_iter = self.resultBUF.get_start_iter()
            end_iter = self.resultBUF.get_end_iter()
            self.priorText = self.resultBUF.get_text(start_iter, end_iter, True)   # Save for return from "Wheee"
            self.spinDisplay.start()
            self.wheee_f = True
            self.resultBUF.set_text("Wheeee!", 7)
        else:
            self.spinDisplay.stop()
            self.wheee_f  = False
            self.resultBUF.set_text(self.priorText, len(self.priorText))  #Restore language
            
if __name__ == '__main__':
    SpinToggleTest()
    gtk.main()   
