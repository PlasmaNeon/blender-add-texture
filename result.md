import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

#~ PYTHON INTERACTIVE CONSOLE 3.7.0 (default, Jun 26 2019, 19:11:54)  [GCC 6.3.1 20170216 (Red Hat 6.3.1-3)]
#~ 
#~ Command History:     Up/Down Arrow
#~ Cursor:              Left/Right Home/End
#~ Remove:              Backspace/Delete
#~ Execute:             Enter
#~ Autocomplete:        Ctrl-Space
#~ Zoom:                Ctrl +/-, Ctrl-Wheel
#~ Builtin Modules:     bpy, bpy.data, bpy.ops, bpy.props, bpy.types, bpy.context, bpy.utils, bgl, blf, mathutils
#~ Convenience Imports: from mathutils import *; from math import *
#~ Convenience Variables: C = bpy.context, D = bpy.data
#~ 
file_path="/home/plasma/test_texture.png"
bpy.ops.image.open(filepath=file_path)
#~ {'FINISHED'}
#~ 
model_path = '/home/plasma/partnet/partnet_data/97/objs/new-1.obj'
bpy.ops.import_scene.obj(filepath = model_path)
#~ Progress:   0.00%
(  0.0001 sec |   0.0001 sec) Importing OBJ '/home/plasma/partnet/partnet_data/97/objs/new-1.obj'...
#~ Progress:   0.00%
  (  0.0011 sec |   0.0002 sec) Parsing OBJ file...
#~ Progress:   0.00%
    (  0.1439 sec |   0.1367 sec) Done, loading materials and images...
#~ Progress:  33.33%
    (  0.1453 sec |   0.1381 sec) Done, building geometries (verts:14398 faces:18455 materials: 1 smoothgroups:0) ...
#~ Progress:  66.67%
    (  0.2072 sec |   0.2000 sec) Done.
#~ Progress:  66.67%
Progress: 100.00%
  (  0.2093 sec |   0.2084 sec) Finished importing: '/home/plasma/partnet/partnet_data/97/objs/new-1.obj'
#~ Progress: 100.00%
Progress: 100.00%
#~ 
#~ {'FINISHED'}
#~ 
bpy.context.view_layer.objects.active=bpy.context.selected_objects[0]
bpy.ops.uv.smart_project()
#~ Smart Projection time: 0.79
#~ {'FINISHED'}
#~ 
mat = bpy.context.object.active_material
matnodes = mat.node_tree.nodes
texture=matnodes.new("ShaderNodeTexImage")
for m in matnodes:
    print(m)
    
#~ <bpy_struct, ShaderNodeOutputMaterial("Material Output")>
#~ <bpy_struct, ShaderNodeBsdfPrincipled("Principled BSDF")>
#~ <bpy_struct, ShaderNodeTexImage("Image Texture")>
#~ 
matnodes["Image Texture"].image=bpy.data.images['test_texture.png']
mat.node_tree.links.new(matnodes["Image Texture"].outputs[0],matnodes["Principled BSDF"].inputs[0])
#~ bpy.data.node_groups['Shader Nodetree']...NodeLink
#~ 