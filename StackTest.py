'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of the Stack Container
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 04 MAY 2023
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of StackSwitcher, Button
 *      Incidental use of GTKWindow, GTKCalendar, GTKTextView and GTKLabel as 
 *                        placeholders (no interactive use)
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class StackTest():
    
    def __init__(self):
        self.gladefile = "StackTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')

        # No real code here, the stack is handled and setup in Glade
        # Note the Stack Labels are set in Glade under the Packing tab for each of the contents of the stack.     
        
        # Set up the button bar
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        # Let'r rip!
        self.topLevel.show_all()
        
        
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    StackTest()
    gtk.main()   
