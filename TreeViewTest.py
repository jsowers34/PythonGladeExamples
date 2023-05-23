'''
 ***************************************************************************** 
 * PURPOSE
 *          Example of use of TreeView.
 ***************************************************************************** 
 * MODIFICATIONS
 * @author JL Sowers 20MAY23
 ***************************************************************************** 
 *  DESIGN NOTES:
 *      Also shows use of ListStore, TreeStore, ScrolledWindow and TreeModel
 *      and ToggleButton, TreeViewColumn.
 ***************************************************************************** 
'''
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GObject as gobj

class TreeViewTest():
    
    stars = [['Orion',       ['Betelguise', ['M2', 650,  0.92]]],
             ['Scorpio',     ['Antares',    ['M1', 400,  0.92]]],
             ['Ursa Major',  ['Dubhe',      ['K0', 145,  1.81]]],
             ['Canis Minor', ['Sirius',     ['A0', 8.6, -1.33]]],
             ['Cygnus',      ['Deneb',      ['A2', 2615, 1.25]]],
             ['Taurus',      ['Aldebaran',  ['K5', 65,   0.86]]]
            ]
    headers = ["Constellation", "Star", "Spectral Class", "DistanceLY", "Magnitude"]
    
    def __init__(self):
        self.gladefile = "TreeViewTest.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        self.topLevel = builder.get_object('toplevel')
        self.topLevel.connect("delete-event", gtk.main_quit) # Handle the decoration
        self.toggleBtn = builder.get_object('viewToggle')
        self.toggleBtn.connect('toggled', self.togglebutton_cb)
        self.scrollable_treelist = builder.get_object('scrolledWindow')
        self.treeView = builder.get_object('treeView')
        self.treeView.connect('row_activated', self.onSelect)
        self.listModel = gtk.ListStore(gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING)
        self.treeModel = gtk.TreeStore(gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING, gobj.TYPE_STRING)
        self.state = 0
        self.loadTreeModel()
        
        # Set up the button bar
        self.quitBtn = builder.get_object("quitBtn")
        self.quitBtn.connect('clicked', self.bye_bye)  
        
        # Let'r rip!
        self.topLevel.show_all()
        
    def onSelect(self, tree, path, column):
        """ Print the value selected from the model. """
        data = None
        model, xiter = tree.get_selection().get_selected()        
        if iter is not None:
            if self.state == 0:  # Tree
                data = model.get_value(xiter, 0)
            else:  # List -- Table
                ix = self.headers.index(column.get_title())
                data = model.get_value(xiter, ix)
            print("The selected value is ", data)

    def loadListModel(self):
        """ Populate and Load the List Model version. """
        self.populateList()
        i = 0
        for column_title in self.headers:
            renderer = gtk.CellRendererText()
            column = gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeView.append_column(column)
            i = i + 1
            
    def populateList(self):
        """
            Populate the List Model with Constellation, Star, Spectral Class, Distance(Ly), Magnitude
        """
        for x in self.stars:
            constellation = x[0]
            sublist = self.flatten(x[1])
            newlist = [constellation]
            newlist.append(sublist)
            newlist = self.flatten(newlist)
            self.listModel.append(newlist)
        self.scrollable_treelist.set_vexpand(True)
        self.treeView.set_model(self.listModel)
        
    def printInput(self):
        """ Dump the Data Structure for debug purposes. """
        for x in self.stars:
            print(x[0])
            for i in range(1, len(x)):
                stardata = x[i:]
                for data in stardata:
                    data = self.flatten(data)
                    print(data[0])
                    for y in range(1,len(data)):
                        print("        ", data[y])
                print()
         
    def loadTreeModel(self):
        """ Populate and Load the TreeModel version. """
        self.populateTree()
        renderer = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Constellation", renderer, text=0)
        self.treeView.append_column(column)
        self.scrollable_treelist.set_vexpand(True)
        self.treeView.set_model(self.treeModel)
                
    def populateTree(self):
        """
            Populate the Tree Model with Constellation, Star, Spectral Class, Distance(Ly), Magnitude
        """
        for x in self.stars:
            iter_level_1 = self.append_tree(x[0])
            for i in range(1, len(x)):
                stardata = x[i:]
                for data in stardata:
                    data = self.flatten(data)
                    iter_level_2 = self.append_tree(data[0], iter_level_1)
                    for y in range(1,len(data)):
                        if type(data[y]) != str:
                            data[y] = str(data[y])
                        self.append_tree(data[y], iter_level_2) 

    def append_tree(self, name, parent=None):
        """
            Append to the treeview if parent is null append to root level.
            if parent is a valid iter (possibly returned from previous append) then append under the parent
        """
        myiter = self.treeModel.insert_after(parent, None)
        self.treeModel.set_value(myiter, 0, name)
        return myiter
    
    def clearTree(self):
        """ Empty the Tree in preparation for loading the differing version. """
        num_columns = len(self.treeView.get_columns())
        for _ in range(0, num_columns):
            column = self.treeView.get_column(0) # Since we are removing, it will always be 0
            self.treeView.remove_column(column)
        self.listModel.clear()
        self.treeModel.clear()
        self.treeView.set_model(None)


    def togglebutton_cb(self, widget):
        """ Callback for the ToggleButton Click. """
        self.clearTree()
        self.state = widget.get_active()
        labels = ['Using Tree Model', 'Using List Model']
        widget.set_label(labels[self.state])
        if self.state == 0:
            self.loadTreeModel()
        else:
            self.loadListModel()
        
    def flatten(self, items, seqtypes=(list, tuple)):
        """ Collapse a nested list into a simple list. """
        for i, _ in enumerate(items):
            while i < len(items) and isinstance(items[i], seqtypes):
                items[i:i+1] = items[i]
        return items
        
    def bye_bye(self, widget):
        """ You are the weakest link. Goodbye. """
        gtk.main_quit()        

if __name__ == '__main__':
    TreeViewTest()
    gtk.main()   
