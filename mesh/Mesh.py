import abc
import bpy


class Mesh(abc.ABC):
    """
    A class that represent a mesh object

    Attributes
    ----------
        obj : bpy.types.Object
            The mesh object
        location : tuple
            The location of the mesh object

    Methods
    -------
        create() -> None
            Create a mesh object
        translate(value: tuple) -> None
            Translate the object
        resize(value: tuple) -> None
            Scale the object
        rotate(value: tuple) -> None
            Rotate the object
        shear(value: tuple) -> None
            Shear the object
    """
    @abc.abstractmethod
    def __init__(self, location: tuple = (0, 0, 0)) -> None:
        """
        Initialize the mesh object

        Parameters
        ----------
            location : tuple
                    The location of the mesh object
        """
        self.obj = None
        self.location = location

    def translate(self, value: tuple = (0, 0, 0)) -> None:
        """
        Translate the object

        Parameters
        ----------
            value : tuple
                    The location to translate to

        Return
        ------
            None
        """
        bpy.ops.object.select_all(action='DESELECT')

        self.obj.select_set(True)
        bpy.context.view_layer.objects.active = self.obj

        bpy.ops.transform.translate(value=value)
        self.location = self.obj.location

    def resize(self, value: tuple = (1, 1, 1)) -> None:
        """
        Scale the object

        Parameters
        ----------
            value : tuple
                    The scale factor

        Return
        ------
            None
        """
        bpy.ops.object.select_all(action='DESELECT')

        self.obj.select_set(True)
        bpy.context.view_layer.objects.active = self.obj

        bpy.ops.transform.resize(value=value)
        self.location = self.obj.location

    def rotate(self, value: tuple = (0, 0, 0)) -> None:
        """
        Rotate the object

        Parameters
        ----------
            value : tuple
                    The rotation value

        Return
        ------
            None
        """
        bpy.ops.object.select_all(action='DESELECT')

        self.obj.select_set(True)
        bpy.context.view_layer.objects.active = self.obj

        bpy.ops.transform.rotate(value=value)
        self.location = self.obj.location

    def shear(self, value: tuple = (0, 0, 0)) -> None:
        """
        Shear the object

        Parameters
        ----------
            value : tuple
                    The shear value

        Return
        ------
            None
        """
        bpy.ops.object.select_all(action='DESELECT')

        self.obj.select_set(True)
        bpy.context.view_layer.objects.active = self.obj

        bpy.ops.transform.shear(value=value)
        self.location = self.obj.location
