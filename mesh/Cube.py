import bpy
from mesh import Mesh


class Cube(Mesh.Mesh):
    """
    A class that represent a cube with a given size

    Attributes
    ----------
        size : int
            The size of the cube
        obj : bpy.types.Object
            The cube object

    Methods
    -------
        create() -> None
            Create a cube mesh with the given size
    """
    def __init__(self, size: int = 1, location: tuple = (0, 0, 0), name: str = 'Cube') -> None:
        """
        Parameters
        ----------
            size : int
                    The size of the cube (default is 1)
            location : tuple
                    The location of the cube (default is (0, 0, 0))

        Return
        ------
            None
        """
        self.size = size
        self.location = location
        self.name = name
        self.obj = None
        self.__create()

    def __create(self) -> None:
        """
        Create a cube mesh with the given size

        Return
        ------
            None
        """
        bpy.ops.mesh.primitive_cube_add(size=self.size, location=self.location)
        self.obj = bpy.context.object
        bpy.context.object.name = self.name

    def __repr__(self):
        return f"Cube(size={self.size})"

    def __str__(self):
        return f"Cube(size={self.size})"
