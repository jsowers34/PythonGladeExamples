'''
 ***************************************************************************** 
 * PURPOSE
 *     Example of use of the About Box
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 13MAY23
 ***************************************************************************** 
 *  DESIGN NOTES:
 *     Note the use of 'show' instead of the usual 'show_all'.  If the show_all
 *     is used, the 'license' button (unresponsive) appears.  Known issue in GTK+3.
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class AboutBoxTest():
    
    def __init__(self):
        self.gladefile = "AboutBoxTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('topLevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration

        
        # Let'r rip!
        self.topLevel.show()
        
        response = self.topLevel.run()
        #self.displayResponses(response)
        if response == gtk.ResponseType.DELETE_EVENT:
            self.topLevel.destroy()

        
    def displayResponses(self, response):
        """ Debug Aid """
        if response == gtk.ResponseType.NONE:
            print("GTK_RESPONSE_NONE = %s"%response)
        elif response == gtk.ResponseType.REJECT:
            print("GTK_RESPONSE_REJECT = %s"%response)
        elif response == gtk.ResponseType.ACCEPT:
            print("GTK_RESPONSE_ACCEPT = %s"%response)
        elif response == gtk.ResponseType.DELETE_EVENT:
            print("GTK_RESPONSE_DELETE_EVENT = %s"%response)
        elif response == gtk.ResponseType.OK:
            print("GTK_RESPONSE_OK = %s"%response)
        elif response == gtk.ResponseType.CANCEL:
            print("GTK_RESPONSE_CANCEL = %s"%response)
        elif response == gtk.ResponseType.CLOSE:
            print("GTK_RESPONSE_CLOSE = %s"%response)
        elif response == gtk.ResponseType.YES:
            print("GTK_RESPONSE_YES = %s"%response)
        elif response == gtk.ResponseType.NO:
            print("GTK_RESPONSE_NO = %s"%response)
        elif response == gtk.ResponseType.APPLY:
            print("GTK_RESPONSE_APPLY = %s"%response)
        elif response == gtk.ResponseType.HELP:
            print("GTK_RESPONSE_HELP = %s"%response)
        else:
            print(response)
               
if __name__ == '__main__':
    AboutBoxTest()
    gtk.main()   
