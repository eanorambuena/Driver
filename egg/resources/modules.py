import pip, sys, subprocess
import importlib as il
import importlib.util
from egg.resources.constants import white
from egg.resources.extensions import withoutFormat

def isntInstalled(package):
    spec=importlib.util.find_spec(package)
    loweredSpec=importlib.util.find_spec(package.lower())
    if (spec is None) and (loweredSpec is None): 
        return True
    return False

def install_option_1(name: str):
    #Implement pip as a subprocess
    if name=="$upgrade":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    else:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
    return "done"

def install_option_2(name: str):
    #Implement pip using pip package
    pip.main(['install', name])
    return "done"

def installFromRequests(requestOrPackages="requests",fromRequests=True):
    if fromRequests:
        requestOrPackages=withoutFormat.getLines(requestOrPackages)
    for package in requestOrPackages:
        if '\n' in package:
            package=package.rstrip('\n')
        if isntInstalled(package):
            install_option_1(package)

def install(name: str):
    try:
        installFromRequests(name,0)
        #raise Exception("error")
    except:
        print(white+"Install failed")
        print(white+"Retrying...")
        try:
            install_option_2(name)
        except:
            print(white+"Install failed")
            return "error"
    print(white+name+" succesfully installed")
    return "done"

def upgrade(name: str):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', name])
    except:
        print(white+name+" succesfully ugraded")
    return "done"

class Repo():
    def __init__(self,name: str):
        self.name=name
    def pull(self,package: str,functions: str = ""):
        funcs=functions.split(" ")
        try:
            package="github_com.PythonForChange."+self.name+"."+package
            _temp = il.__import__(package, globals(), locals(), funcs, 0)
            return _temp
        except:
            print(white+"Pull failed")
