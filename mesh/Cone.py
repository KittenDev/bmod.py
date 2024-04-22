import bpy
from mesh import Mesh


class Cone(Mesh.Mesh):
    """
    A class that represent a cone with a given radius and depth

    Attributes
    ----------
        vertices : int
            The number of vertices of the cone
        radius : int
            The radius of the cone
        depth : int
            The depth of the cone
        location : tuple
            The location of the cone
        name : str
            The name of the cone
        obj : bpy.types.Object
            The cone object

    Methods
    -------
        create() -> None
            Create a cone mesh with the given radius and depth
    """
    def __init__(
            self,
            vertices: int = 32,
            radius: int = 1,
            depth: int = 1,
            location: tuple = (0, 0, 0),
            name: str = 'Cone'
    ) -> None:
        """
        Parameters
        ----------
            radius : int
                    The radius of the cone (default is 1)
        """
        self.vertices = vertices
        self.radius = radius
        self.depth = depth
        self.location = location
        self.name = name
        self.obj = None
        self.__create()

    def __create(self) -> None:
        """
        Create a cone mesh with the given radius and depth

        Return
        ------
            None
        """
        bpy.ops.mesh.primitive_cone_add(
            vertices=self.vertices,
            radius1=self.radius,
            depth=self.depth,
            location=self.location
        )
        self.obj = bpy.context.object
        bpy.context.object.name = self.name

    def __repr__(self):
        return f"Cone(radius={self.radius})"

    def __str__(self):
        return f"Cone(radius={self.radius})"
