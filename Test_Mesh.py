from os import getcwd, chdir, path
from objtools import *

directory = getcwd()

# -----------------------------
# GLUTEUS MAX
# -----------------------------

# Si vous voulez visualiser l'objet 3D, il faut passer en 3.8

print("\n----- Gluteus Max -----")
cam_gluteus = dict(
    position=(488.535, -228.916, 759.305),
    focal_point=(179.000, 287.500, 949.500),
    viewup=(-0.351876, -0.501907, 0.790109),
    distance=631.405,
    clipping_range=(114.342, 1283.80),
)
chdir(path.join(directory, "obj_generated_1"))
showFolderCam(".", cam_gluteus, z=1.65, save_image = True, show_3d = False, show_size = True, name = "gluteus_max")

# AUTRES FONCTIONS
# showObjCam("mesh_pylab.obj", cam_gluteus, z=2, save_image = False, show_3d = True)
# showFolder(".", yaw = -50, pitch = -50,z = 5, save_image = True, show_3d = False)
# showObj("mesh_pylab.obj", yaw = -50, pitch = -50,z = 5, save_image = True, show_3d = False)

print("\n----- Gluteus Max (nii2mesh) -----")

cam_gluteus_nii2mesh = dict(
    position=(-513.212, 526.481, -134.669),
    focal_point=(-101.008, -55.4613, 82.8040),
    viewup=(0.316167, 0.520385, 0.793245),
    distance=745.562,
    clipping_range=(452.939, 1115.71),
)
chdir(path.join(directory, "obj_generated_1_nii2mesh"))
showFolderCam(".", cam_gluteus_nii2mesh, z=1.65, save_image = True, show_3d = False, show_size = True, name = "gluteus_max_n2m")

# -----------------------------
# SARTORIUS
# -----------------------------

print("\n------ Sartorius ------")

cam_sartorius = dict(
    position=(366.587, 915.348, 32.8812),
    focal_point=(116.500, 164.000, 588.000),
    viewup=(-0.956402, 0.122439, -0.265150),
    distance=967.070,
    clipping_range=(107.728, 2051.14),
)
chdir(path.join(directory, "obj_generated_2"))
showFolderCam(".", cam_sartorius, z=4.2, save_image = True, show_3d = False, show_size = True, name = "sartorius")

print("\n----- Sartorius (nii2mesh) -----")

cam_sartorius_nii2mesh = dict(
    position=(-306.210, -866.426, -802.396),
    focal_point=(-66.6119, 12.5647, -116.207),
    viewup=(0.962399, -0.0546056, -0.266094),
    distance=1140.56,
    clipping_range=(651.441, 1759.02),
)
chdir(path.join(directory, "obj_generated_2_nii2mesh"))
showFolderCam(".", cam_sartorius_nii2mesh, z=4.2, save_image = True, show_3d = False, show_size = True, name = "sartorius_n2m")



# Noter les changments de positions


"""

---------------------------------------
          TEST LIBRAIRIES - 3.11
---------------------------------------



--- Pymeshlab ---


Pas de lissage

Laplacian 1

Laplacian 5

Laplacian 10

Taubin 10

Edge Decimation (Marching Cubes)

Edge Decimation (Quadratic Edge Collapse)

Edge Decimation MC + Laplacian

Edge Decimation QE + Laplacian

--- Voxelfuse ---


Sans lissage

Avec lissage
Volume du nuage de points (Nombre de voxels):
 11823403

--- Pymeshlab ---


mesh_pylab
Volume :  11822987.04
Erreur volumétrique:
 0.00352 %

mesh_pylab_lap01
Volume :  11822158.84
Erreur volumétrique:
 0.01052 %

mesh_pylab_lap05
Volume :  11819247.3
Erreur volumétrique:
 0.03515 %

mesh_pylab_lap10
Volume :  11815649.69
Erreur volumétrique:
 0.06558 %

mesh_pylab_tau10
Volume :  1182323Erreur volumétrique:
 0.00139 %       

mesh_pylab_ed_mc 
Volume :  11794455.06
Erreur volumétrique:
 0.24484 %       
mesh_pylab_ed_mc

Volume :  11794455.06
Erreur volumétrique:
 0.24484 %      

mesh_pylab_ed_qe

Volume :  11822987.04
65.66
Erreur volumétrique:
 0.05106 %

--- Trimesh ---


mesh_trimesh
Volume :  11822987.04
Erreur volumétrique:
 0.00352 %

--- Voxelfuse ---


mesh_vf_nonsmooth
Volume :  11822985.54
Erreur volumétrique:
 0.00353 %

mesh_vf_smooth
Volume :  11819179.15
Erreur volumétrique:
 0.03572 %

--- VTK ---

Volume :  1995419.27
Erreur volumétrique:
 83.12314 %
(py38) PS C:\Users\sacha\Documents\VSCodeProjects\PAPPL\Mesh_Source>     



"""