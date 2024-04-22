import bpy
from mesh import Mesh


class Sphere(Mesh.Mesh):
    """
    A class that represent a sphere with a given radius and subdivisions

    Attributes
    ----------
        radius : int
            The radius of the sphere
        subdivisions : int
            The subdivisions of the sphere
        obj : bpy.types.Object
            The sphere object

    Methods
    -------
        create() -> None
            Create a sphere mesh with the given radius and subdivisions
    """
    def __init__(self, radius: int = 1, subdivisions: int = 5, location: tuple = (0, 0, 0), name: str = 'Sphere') -> None:
        """
        Parameters
        ----------
            radius : int
                    The radius of the sphere (default is 1)
            subdivisions : int
                    The subdivisions of the sphere (default is 5), range is 1 to 10, higher subdivisions will produce
                    smoother sphere
            location : tuple
                    The location of the cylinder (default is (0, 0, 0))

        Return
        ------
            None
        """
        self.radius = radius
        self.subdivisions = subdivisions
        self.location = location
        self.name = name
        self.obj = bpy.context.object
        self.__create()

    def __create(self) -> None:
        """
        Create a sphere mesh with the given radius and subdivisions

        Return
        ------
            None
        """
        bpy.ops.mesh.primitive_ico_sphere_add(radius=self.radius, subdivisions=self.subdivisions, location=self.location)
        self.obj = bpy.context.object
        bpy.context.object.name = self.name

    def __repr__(self):
        return f"Sphere(radius={self.radius})"

    def __str__(self):
        return f"Sphere(radius={self.radius})"
