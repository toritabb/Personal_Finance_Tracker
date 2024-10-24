# standard library
import os
import sys



# root path depending on if the program is run as an exe or as a script respectively
if getattr(sys, 'frozen', False): 
    ROOT_DIR = os.path.dirname(sys.executable)

else: 
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



def get_global_path(local_path: str) -> str:
    '''
    Gets the global path of a file from a local path.
    '''

    return os.path.join(ROOT_DIR, local_path)

