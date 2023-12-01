from os import getcwd, chdir, path
from glob import glob
from objtools import *

import time
import nibabel as nib
from skimage import measure
import pymeshlab
import voxelfuse as vf       
import vtk
import numpy as np

print("\n\n---------------------------------------")
print("          TEST LIBRAIRIES - 3.11")
print("---------------------------------------\n\n")

# ------------------------------------------------------------------------------
#   FICHIER ORIGINAL
# ------------------------------------------------------------------------------

# Lire le fichier
directory = getcwd()
nom_fichier = "3d_source/gluteus_max.nii.gz"
lab = path.join(directory, nom_fichier)
test = nib.load(lab).get_fdata()

# (VTK) Read the nii file
nifti_vtk = vtk.vtkNIFTIImageReader()
nifti_vtk.SetFileName(nom_fichier)
nifti_vtk.Update()

chdir(path.join(directory, "obj_generated_1"))

#start_time = time.time()
#elapsed_time = time.time() - start_time 
#print(f"Elapsed time: {elapsed_time:.1f} seconds")

# ------------------------------------------------------------------------------
#   MARCHING CUBES
# ------------------------------------------------------------------------------

# Méthode 1 : Skimage-measure
verts, faces, normals, values = measure.marching_cubes(test)

# Méthode 3 : VTK 
model_vtk = vtk.vtkMarchingCubes()
model_vtk.SetInputConnection(nifti_vtk.GetOutputPort())
model_vtk.SetValue(0, 0.5)

# Méthode 4 : VoxelFuse (Voir section VoxelFuse)

# ------------------------------------------------------------------------------
#   CREATION DU MESH
# ------------------------------------------------------------------------------

# Méthode 1 : Pymeshlab
m_pymeshlab = pymeshlab.Mesh(verts, faces)

# Méthode 2 : Trimesh
m_trimesh = trimesh.Trimesh(vertices=verts, faces=faces, vertex_attributes={'normals': normals, 'values': values})

# ------------------------------------------------------------------------------
#   CALCUL DU VOLUME
# ------------------------------------------------------------------------------

# Volume "initial" = 3D numpy array
nbVoxels = np.count_nonzero(test)

# ------------------------------------------------------------------------------
#   MODIFICATION DU MESH
# ------------------------------------------------------------------------------

# -------------------------
#         PYMESHLAB 

print("\n--- Pymeshlab ---\n")
liste_pymeshlab = {}

# ------ Lissage -------- 

print("\nPas de lissage")
mesh_pylab = pymeshlab.MeshSet()
mesh_pylab.add_mesh(m_pymeshlab)
liste_pymeshlab["mesh_pylab"] = mesh_pylab

print("\nLaplacian 1")
mesh_pylab_lap01 = pymeshlab.MeshSet()
mesh_pylab_lap01.add_mesh(m_pymeshlab)
mesh_pylab_lap01.apply_coord_laplacian_smoothing(stepsmoothnum = 1) 
liste_pymeshlab["mesh_pylab_lap01"] = mesh_pylab_lap01

print("\nLaplacian 5")
mesh_pylab_lap05 = pymeshlab.MeshSet()
mesh_pylab_lap05.add_mesh(m_pymeshlab)
mesh_pylab_lap05.apply_coord_laplacian_smoothing(stepsmoothnum = 5) 
liste_pymeshlab["mesh_pylab_lap05"] = mesh_pylab_lap05

print("\nLaplacian 10")
mesh_pylab_lap10 = pymeshlab.MeshSet()
mesh_pylab_lap10.add_mesh(m_pymeshlab)
mesh_pylab_lap10.apply_coord_laplacian_smoothing(stepsmoothnum = 10) 
liste_pymeshlab["mesh_pylab_lap10"] = mesh_pylab_lap10

print("\nTaubin 10")
mesh_pylab_tau10 = pymeshlab.MeshSet()
mesh_pylab_tau10.add_mesh(m_pymeshlab)
mesh_pylab_tau10.apply_coord_taubin_smoothing()
liste_pymeshlab["mesh_pylab_tau10"] = mesh_pylab_tau10

# ------ DECIMATION (Simplification) -------- 

print("\nEdge Decimation (Marching Cubes)")
mesh_pylab_ed_mc = pymeshlab.MeshSet()
mesh_pylab_ed_mc.add_mesh(m_pymeshlab)
mesh_pylab_ed_mc.meshing_decimation_edge_collapse_for_marching_cube_meshes()
liste_pymeshlab["mesh_pylab_ed_mc"] = mesh_pylab_ed_mc

print("\nEdge Decimation (Quadratic Edge Collapse)")
mesh_pylab_ed_qe = pymeshlab.MeshSet()
mesh_pylab_ed_qe.add_mesh(m_pymeshlab)
mesh_pylab_ed_qe.meshing_decimation_quadric_edge_collapse()
liste_pymeshlab["mesh_pylab_ed_qe"] = mesh_pylab_ed_qe

# ------ SOLUTION RETENUE -------- 

print("\nEdge Decimation MC + Laplacian")
mesh_pylab_ed_xx = pymeshlab.MeshSet()
mesh_pylab_ed_xx.add_mesh(m_pymeshlab)
mesh_pylab_ed_xx.meshing_decimation_edge_collapse_for_marching_cube_meshes()
mesh_pylab_ed_xx.apply_coord_laplacian_smoothing()
liste_pymeshlab["mesh_pylab_ed_xx"] = mesh_pylab_ed_xx

print("\nEdge Decimation QE + Laplacian")
mesh_pylab_ed_yy = pymeshlab.MeshSet()
mesh_pylab_ed_yy.add_mesh(m_pymeshlab)
mesh_pylab_ed_yy.meshing_decimation_quadric_edge_collapse()
mesh_pylab_ed_yy.apply_coord_laplacian_smoothing()
liste_pymeshlab["mesh_pylab_ed_yy"] = mesh_pylab_ed_yy

# -------------------------
#         VOXELFUSE  

print("\n--- Voxelfuse ---\n")
liste_voxelfuse = {}

vf_test = vf.VoxelModel(test)

print("\nSans lissage")
mesh_vf_nonsmooth = vf.Mesh.marchingCubes(vf_test, False)
liste_voxelfuse["mesh_vf_nonsmooth"]=mesh_vf_nonsmooth

print("\nAvec lissage") #Prend 3 minutes ...
mesh_vf_smooth = vf.Mesh.marchingCubes(vf_test, True)
liste_voxelfuse["mesh_vf_smooth"]=mesh_vf_smooth

# ------------------------------------------------------------------------------
#    EXPORTATION DES MESH
# ------------------------------------------------------------------------------

print("Volume du nuage de points (Nombre de voxels):\n", nbVoxels)

# ---------------------------------------
# Pymeshlab

print("\n--- Pymeshlab ---\n")

for key, mesh in liste_pymeshlab.items():
    mesh.save_current_mesh(key+".obj")
    mesh.save_current_mesh(key+".stl")
    print("\n"+key)
    vol = pymeshlab_volume(mesh)
    print("Volume : ", vol)
    showError(nbVoxels, vol)

# ---------------------------------------
# Trimesh

print("\n--- Trimesh ---\n")

key = "mesh_trimesh"
m_trimesh.export(key+".stl", file_type='stl')
m_trimesh.export(key+".obj", file_type='obj')
print("\n"+key)
vol = trimesh_volume(m_trimesh)
print("Volume : ", vol)
showError(nbVoxels, vol)

# ---------------------------------------
# Voxelfuse

print("\n--- Voxelfuse ---\n")

key = "mesh_vf_nonsmooth"
# fichier .STL retiré car trop lourd
# mesh_vf_nonsmooth.export("mesh_vf_nonsmooth.stl")
mesh_vf_nonsmooth.export("mesh_vf_nonsmooth.obj")
print("\n"+key)
vol = voxelfuse_volume(mesh_vf_nonsmooth)
print("Volume : ", vol)
showError(nbVoxels, vol)

key = "mesh_vf_smooth"
# fichier .STL retiré car trop lourd
# mesh_vf_smooth.export("mesh_vf_smooth.stl") 
mesh_vf_smooth.export("mesh_vf_smooth.obj")
print("\n"+key)
vol = voxelfuse_volume(mesh_vf_smooth)
print("Volume : ", vol)
showError(nbVoxels, vol)

# ---------------------------------------
# VTK

print("\n--- VTK ---\n")

# Create a 3D model from the mesh
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(model_vtk.GetOutputPort())
# Create an actor for the model
actor = vtk.vtkActor()
actor.SetMapper(mapper)
# Create a renderer for the scene
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
# Create a render window for the scene
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
# Create an exporter object
export_vtk= vtk.vtkOBJExporter()
export_vtk.SetInput(render_window)
export_vtk.SetFilePrefix("mesh_vtk")
export_vtk.Write()

vol = vtk_volume(model_vtk)
print("Volume : ", vol)
showError(nbVoxels, vol)

# ------------------------------------------------------------------------------
#    Librairies et Fonctions obsolètes
# ------------------------------------------------------------------------------

"""
# ---------------------------------------
# Quadratic Mesh Simplification (Installation compliquée, et ne fonctionne pas !)

from quad_mesh_simplify.quad_mesh_simplify import simplify_mesh
num_nodes = verts.shape[0] # Combien de verts initialement
positions=verts.astype(np.double)
face=faces.astype(np.uint32)
final_num_nodes= int(num_nodes/2)
new_verts, new_faces = simplify_mesh(positions, face, final_num_nodes) 
# C'est cette fonction qui présente des erreurs, mair qi n'affiche aucune exception
# Les paramètres sont dans le bon format, confirmé sur la doc
mesh_qms = pymeshlab.Mesh(new_verts, new_faces)

# ---------------------------------------
# MESHPLEX (Fonctionne mais il faut payer la version premium)

# Exemple : calcul du volume
mesh = meshplex.MeshTri(verts, faces)
V = np.sum(mesh.cell_volumes)
print("Volume =", V)

# ---------------------------------------
# PYMESH (Trop d'erreurs, l'installation est impossible)

# Exemple : calcul du volume en utilisant l'"Outer Hull"
mesh = pymeshlab.Mesh(verts, faces)
volume = pymesh.outerhull.compute_outer_hull(mesh)

# --------- FONCTIONS -----------

# VOXELFUSE : Simplification ne fonctionne pas car dépend de la librairie quad_mesh_simplify

mesh_vf_simple_50 = mesh_vf_nonsmooth.simplify(50) # taux de réduction de 50% 

"""