from os import getcwd, chdir, path
from objtools import *

directory = getcwd()

# -----------------------------
# GLUTEUS MAX
# -----------------------------

print("\n----- Gluteus Max -----")

cam_gluteus = dict(
    position=(488.535, -228.916, 759.305),
    focal_point=(179.000, 287.500, 949.500),
    viewup=(-0.351876, -0.501907, 0.790109),
    distance=631.405,
    clipping_range=(114.342, 1283.80),
)
chdir(path.join(directory, "obj_generated_1"))
showFolderCam(".", cam_gluteus, z=1.65, save_image = False, show_3d = False, show_size = True, name = "gluteus_max")

# AUTRES FONCTIONS
# showObjCam("mesh_pylab.obj", cam_gluteus, z=2, save_image = False, show_3d = True)
# showFolder(".", yaw = -50, pitch = -50,z = 5, save_image = True, show_3d = False)
# showObj("mesh_pylab.obj", yaw = -50, pitch = -50,z = 5, save_image = True, show_3d = False)

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
showFolderCam(".", cam_sartorius, z=4.2, save_image = False, show_3d = False, show_size = True, name = "sartorius")