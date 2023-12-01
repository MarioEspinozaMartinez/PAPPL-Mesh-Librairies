# PAPPL-Mesh-Libraries

## Introduction

A venir

## Importations

### Lecture des fichiers NIFTI
```python
import nibabel as nib
```

### Marching Cubes
```python
from skimage import measure
# --> pip install scikit-image
```

### Autres Méthodes
```python
import quad-mesh-simplify
# --> il faut l'installer manuellement et non pas avec pip/conda
# --> Assurez-vous d'avoir Microsoft Visual C++ > 14
```

### Manipulation de MESH
```python
import vtk
import pymeshlab
import trimesh
# --> Assurez-vous d'installer open3d, qui ne fonctionne pas avec Python 3.11 :
# --> pip install open3d
import voxelfuse as vf
# --> Assurez-vous d'avoir installé manuellement quad-mesh-simplify, qui ne peut pas s'installer directement avec pip
```


