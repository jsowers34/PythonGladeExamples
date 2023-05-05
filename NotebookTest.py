'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of GTKNotebook
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 05 MAY 2023
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of Window, Box, Button
 *      Incidental use of Label, Calendar, ColorButton
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class NotebookTest():
    
    def __init__(self):
        self.gladefile = "NotebookTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        
        # We're not going to do anything with the Calendar/Color/etc.  The purpose here
        # is to show the use of the Notebook.  Most of the actual work is done in Glade.
        
        # Set up the button bar
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        # Let'r rip!
        self.topLevel.show_all()
        
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    NotebookTest()
    gtk.main()   
