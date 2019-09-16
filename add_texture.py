import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

## Import texture images, saved in Blender 
texture_path="examples/test_texture.png"
bpy.ops.image.open(filepath=texture_path) 

'''
for i in bpy.data.images:
    print(i)
    
#~ <bpy_struct, Image("Render Result")>
#~ <bpy_struct, Image("test_texture.png")>
#~ <bpy_struct, Image("Viewer Node")>
#~ 
'''

## Import .obj model 
model_path = 'examples/new-1.obj'
bpy.ops.import_scene.obj(filepath = model_path)

# Activate objects, selected objects are rounded by dim orange, while active objects are rounded by bright orange
bpy.context.view_layer.objects.active=bpy.context.selected_objects[0]

# Set up uv smart project
bpy.ops.uv.smart_project()

# Add textures
mat = bpy.context.object.active_material
matnodes = mat.node_tree.nodes

# Add a new node to include image textures
texture=matnodes.new("ShaderNodeTexImage")

'''
for m in matnodes:
    print(m)
    
#~ <bpy_struct, ShaderNodeOutputMaterial("Material Output")>
#~ <bpy_struct, ShaderNodeTexImage("Image Texture")>
#~ <bpy_struct, ShaderNodeBsdfPrincipled("Principled BSDF")>
#~ 
'''

matnodes["Image Texture"].image=bpy.data.images['test_texture.png']

# Add link
mat.node_tree.links.new(matnodes["Image Texture"].outputs[0],matnodes["Principled BSDF"].inputs[0])
