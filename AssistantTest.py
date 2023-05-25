'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of the Gtk.Assistant Top level dialog.
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 25MAY23
 ***************************************************************************** 
 *  DESIGN NOTES:
 *
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class AssistantTest():
    
    def __init__(self):
        self.gladefile = "AssistantTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('topLevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        
        self.topLevel.connect("cancel", gtk.main_quit)
        self.topLevel.connect("close", gtk.main_quit)
        self.topLevel.connect("apply", self.topLevel.next_page)
        
        self.introPage = builder.get_object('introPage')
        self.topLevel.set_page_complete(self.introPage, True)
        self.page1 = builder.get_object('page1')             # List of Samples
        self.topLevel.set_page_complete(self.page1, True)
        self.page2 = builder.get_object('page2')             # About
        self.topLevel.set_page_complete(self.page2, True)
        self.page3 = builder.get_object('page3')             # Assistant
        self.topLevel.set_page_complete(self.page3, True)
        self.page4 = builder.get_object('page4')             # Check Box
        self.topLevel.set_page_complete(self.page4, True)
        self.page5 = builder.get_object('page5')             # ComboBox
        self.topLevel.set_page_complete(self.page5, True)
        self.page6 = builder.get_object('page6')             # Notebook
        self.topLevel.set_page_complete(self.page6, True)
        self.page7 = builder.get_object('page7')             # RadioButton
        self.topLevel.set_page_complete(self.page7, True)
        self.page8 = builder.get_object('page8')             # Spin & Toggle 
        self.topLevel.set_page_complete(self.page8, True)
        self.page9 = builder.get_object('page9')             # Stack
        self.topLevel.set_page_complete(self.page9, True)    
        self.page10 = builder.get_object('page10')           # TreeView 
        self.topLevel.set_page_complete(self.page10, True)
        self.page11 = builder.get_object('page11')           # MenuBar 
        self.topLevel.set_page_complete(self.page11, True)    
        
        self.finalPage= builder.get_object('finalPage')      # Goodbye
        self.topLevel.set_page_complete(self.finalPage, True)        
        
        # Let'r rip!
        self.topLevel.show_all()

if __name__ == '__main__':
    AssistantTest()
    gtk.main()   
