from objtools import *
import os

dir = os.getcwd()
os.chdir("./obj_generated_1")
print(volume("mesh_vtk.obj"))
