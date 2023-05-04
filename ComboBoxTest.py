'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of ComboBox and ComboBoxText
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 04 MAY 2023
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of TextView, Button
 *      Incidental use of GTKWindow, GTKBox, ButtonBox
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GObject

class ComboBoxTest():
    
    def __init__(self):
        self.gladefile = "ComboBoxTest.glade"
        self.languages = ["APL",    "Algol",   "Assembly", "Basic",  \
                          "C",      "C++",    "Clojure", "Cobol",  \
                          "Fortran", "GPSS",   "Java",   "Lisp",   \
                          "Lua",     "Pascal", "PL/I",   "Python", \
                          "R",       "Simscript", "Snobol", "SPSS", \
                          "SQL",     "T-SQL", "TeX", "Wolfram (Mathematica)"]
        
        self.opsystems = ["Fire OS", "DOS", "UNIX", "LINUX","Burroughs MCP", "macOS", \
                          "DG/UX", "CP/M", "VMS", "Multics", "HP-UX", "OS/360", "VM/370", \
                          "OpenSolaris", "Windows", "Plan 9", "CTOS"]

        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        self.combobox = builder.get_object('comboBX')
        self.comboboxtext = builder.get_object('comboboxTxt')
        self.resultTxt = builder.get_object('resultTxt')
        self.resultBUF = builder.get_object('textbuffer1')
        
        # Load the ComboBox with languages
        liststore1 = gtk.ListStore(GObject.TYPE_STRING)
        cell = gtk.CellRendererText()
        self.combobox.pack_start(cell,True)
        self.combobox.add_attribute(cell, 'text', 0)
        for i in self.languages:
            liststore1.append([i])        
        self.combobox.set_model(liststore1)
        self.combobox.connect('changed', lambda w:self.process_cb_selection())
        
        # Load the ComboBoxText with Operating Systems
        self.comboboxtext.set_entry_text_column(0)
        self.comboboxtext.connect("changed", self.on_comboboxtext_changed)
        for os in self.opsystems:
            self.comboboxtext.append_text(os)
        self.comboboxtext.set_active(0)

        
        # Set up the button bar
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        # Let'r rip!
        self.topLevel.show_all()
        
    def process_cb_selection(self):
        index = self.combobox.get_active()
        lang = self.languages[index]
        result = "Language selected = " + str(index) + ": " + lang
        self.resultBUF.set_text(result, len(result))
        
    def on_comboboxtext_changed(self, combotxt):
        text = combotxt.get_active_text()
        result = "Selected: Operating System = "
        if text is not None:
            result += text
            self.resultBUF.set_text(result, len(result))
            
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    ComboBoxTest()
    gtk.main()   
