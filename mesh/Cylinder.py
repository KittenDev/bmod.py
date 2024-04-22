import bpy
from mesh import Mesh


class Cylinder(Mesh.Mesh):
    """
    A class that represent a cylinder with a given radius and depth

    Attributes
    ----------
        radius : int
            The radius of the cylinder
        depth : int
            The depth of the cylinder
        obj : bpy.types.Object
            The cylinder object

    Methods
    -------
        create() -> None
            Create a cylinder mesh with the given radius and depth
    """
    def __init__(self, radius: int = 1, depth: int = 1, location: tuple = (0, 0, 0), name: str = 'Cylinder') -> None:
        """
        Parameters
        ----------
            radius : int
                    The radius of the cylinder (default is 1)
            depth : int
                    The depth of the cylinder (default is 1)
            location : tuple
                    The location of the cylinder (default is (0, 0, 0))
        """
        self.radius = radius
        self.depth = depth
        self.location = location
        self.name = name
        self.obj = None
        self.__create()

    def __create(self):
        """
        Create a cylinder mesh with the given radius and depth

        Return
        ------
            None
        """
        bpy.ops.mesh.primitive_cylinder_add(radius=self.radius, depth=self.depth, location=self.location)
        self.obj = bpy.context.object
        bpy.context.object.name = self.name

    def __repr__(self):
        return f"Cylinder(radius={self.radius})"

    def __str__(self):
        return f"Cylinder(radius={self.radius})"
