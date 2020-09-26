"""
This module demontrates the funcion polygonize() of bpypolyskel.

It cannot be used in Blender and is thought to be used by an interpreter
where the library mathutils is installed as standalone library.

Use 'pip install mathutils'
"""
import mathutils
# import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import time
import bpypolyskel

# uncomment one of the examples
from examples.rectangle import examplePoly
# from examples.rectangle_annex import examplePoly
# from examples.half_iron_cross import examplePoly
# from examples.holey import examplePoly

verts, numVerts, firstVertIndex, numVertsHoles = examplePoly()

faces = bpypolyskel.polygonize(verts, firstVertIndex, numVerts, numVertsHoles, 0.0, 0.5)

fig = plt.figure()
ax = fig.gca(projection='3d')
for face in faces:
	for edge in zip(face, face[1:] + face[:1]):
		p1 = verts[edge[0]]
		p2 = verts[edge[1]]
		ax.plot([p1.x,p2.x],[p1.y,p2.y],[p1.z,p2.z])
plt.show()
