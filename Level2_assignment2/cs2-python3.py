import os
import sys
from glob import glob

class ClassDependencies:
    def get_subclasses(self,cls):
        #find subclasses of the class
        if len(cls.__subclasses__())<=0:
            return 
        print (cls.__name__ , " [",classes[cls],".py ]")
        for subclass in cls.__subclasses__():
            print ("\t",subclass.__name__ ," [",classes[subclass],".py ]")
        print ("\n")
    def analyse_all_files(self,path):
        #analyse all files in directory and return dict where key=class value=filename
        classes = {}
        filename = path + "*.py"
        for file in glob(filename):
            name = os.path.splitext(os.path.basename(file))[0]
            module = __import__(name)
            for objname in dir(module):
                obj = eval("module." + objname)
                if type(obj) is type:
                    classes.update({obj:name})
        return classes
    def printClassesWithItsSubclasses(self,classes):
        #iterate dict and call method get_subclasses
        for obj in classes:
           self.get_subclasses(obj)

if __name__ == "__main__":
    try:
        path = sys.argv[1]
        sys.path.append(path)
        obj1 = ClassDependencies()
        classes = obj1.analyse_all_files(path)
        obj1.printClassesWithItsSubclasses(classes)
    except Exception as e:
        print (e)





   
