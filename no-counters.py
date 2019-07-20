from gi.repository import GObject, Liferea

class NrNoCountersPlugin (GObject.Object, Liferea.ShellActivatable):
    __gtype_name__ = 'NrNoCountersPlugin'

    shell = GObject.property (type=Liferea.Shell)

    def do_activate (self):
        self.treeview = self.shell.lookup ("feedlist")
        self.counter_column = self.treeview.get_column (1)
        self.counter_column.set_visible (False)
        self.treeview.queue_draw ()
        return

    def do_deactivate (self):
        self.counter_column.set_visible (True)
        self.treeview.queue_draw ()
        return
