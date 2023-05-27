'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of the Revealer Container.
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 26May23
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of Button
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class RevealerTest():
    
    def __init__(self):
        self.gladefile = "RevealerTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration

        self.revealer = builder.get_object('revealer')
        self.revealer.set_reveal_child(False)
        self.logo = builder.get_object('logoImg')
        
        # Set up the button bar
        self.revealBtn = builder.get_object('revealBtn')
        self.revealBtn.connect("clicked", self.onReveal)
        
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', lambda w: self.bye_bye())  
        
        # Let'r rip!
        self.topLevel.show_all()
        
    def onReveal(self, button):
        reveal = self.revealer.get_reveal_child()
        self.revealer.set_reveal_child(not reveal)
        if not reveal:
            button.set_label("Hide")
        else:
            button.set_label("Reveal")
        
    def bye_bye(self):
        gtk.main_quit()        

if __name__ == '__main__':
    RevealerTest()
    gtk.main()   
