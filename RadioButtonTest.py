'''
 ***************************************************************************** 
 * PURPOSE
 *     Example of use of Radio Buttons
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers May 2, 2023
 ***************************************************************************** 
 *  DESIGN NOTES:
 *    Also demonstrates use of an entrytext and entrybuffer
 *         as well as the bottom buttonbar and Quit button
 *    Incidental use of GTKWindow, GTKGrid as containers
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class RadioButtonTest():
    
    def __init__(self):
        self.gladefile = "RadioButtonTest.glade"
        self.choices = ["Basic", "C++", "Java", "Python"]
        
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        self.results = builder.get_object('resultTXT')
        self.resultBUF = builder.get_object('entrybuffer1')
        
        # Grab the Radio Buttons
        self.radioButtons = [None]*4
        self.radioButtons[0] = builder.get_object('rb1')
        self.radioButtons[1] = builder.get_object('rb2')
        self.radioButtons[2] = builder.get_object('rb3')
        self.radioButtons[3] = builder.get_object('rb4')
        
        # Set the connect property 
        for i in range(0, 4):
            self.radioButtons[i].connect('toggled', self.checkRButtons,self.choices[i])

        # Set up the exit
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())     
        self.topLevel.show_all()
        
    def checkRButtons(self, button, txt):
        if button.get_active():
            self.resultBUF.set_text(txt, len(txt))
        else:
            self.resultBUF.set_text("", 0)
        
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    RadioButtonTest()
    gtk.main()   

