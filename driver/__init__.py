from egg.resources.modules import installFromRequests, install_option_1

def init():
    install_option_1("$upgrade") #Upgrade pip
    installFromRequests()