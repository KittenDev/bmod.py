import bpy


def translate(obj: bpy.types.Object, value: tuple = (0, 0, 0)) -> None:
    """
    Translate the object

    Parameters
    ----------
    obj : bpy.types.Object
            The object to translate
    value : tuple
            The location to translate to
    """
    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.transform.translate(value=value)


def resize(obj: bpy.types.Object, value: tuple = (1, 1, 1)) -> None:
    """
    Scale the object

    Parameters
    ----------
    obj : bpy.types.Object
            The object to scale
    value : tuple
            The scale factor
    """
    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.transform.resize(value=value)


def rotate(obj: bpy.types.Object, value: tuple = (0, 0, 0)) -> None:
    """
    Rotate the object

    Parameters
    ----------
    obj : bpy.types.Object
            The object to rotate
    value : tuple
            The rotation value
    """
    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.transform.rotate(value=value)


def shear(obj: bpy.types.Object, value: tuple = (0, 0, 0)) -> None:
    """
    Shear the object

    Parameters
    ----------
        obj : bpy.types.Object
                The object to shear
        value : tuple
                The shear value

    Return
    ------
        None
    """
    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    bpy.ops.transform.shear(value=value)
