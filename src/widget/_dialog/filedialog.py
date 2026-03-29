from .dialogs import Chooser, Directory, Open, SaveAs


def askopenfilename(**options):return Open(**options).show()
def asksaveasfilename(**options):return SaveAs(**options).show()
def askdirectory(**options):return Directory(**options).show()
def askcolor(color=None,**options):
 if color:options,options['initialcolor']=options.copy(),color
 return Chooser(**options).show()