import bpy
from mesh import Mesh


class Block(Mesh.Mesh):
    """
    A class that represent a block with a given length, width and height

    Attributes
    ----------
        length : int
            The length of the block
        width : int
            The width of the block
        height : int
            The height of the block
        obj : bpy.types.Object
            The block object

    Methods
    -------
        create() -> None
            Create a block mesh with the given length, width and height
    """
    def __init__(self, length: int = 1, width: int = 1, height: int = 1, name: str = 'Block') -> None:
        """
        Parameters
        ----------
            length : int
                    The length of the block (default is 1)
            width : int
                    The width of the block (default is 1)
            height : int
                    The height of the block (default is 1)
            name : str
                    The name of the block (default is 'Block')
        """
        self.length = length
        self.width = width
        self.height = height
        self.name = name
        self.obj = None
        self.__create()

    def __create(self):
        """
        Create a block mesh with the given length, width and height

        Return
        ------
            None
        """
        bpy.ops.mesh.primitive_cube_add(size=1)
        self.obj = bpy.context.object
        self.resize((self.length, self.width, self.height))
        bpy.context.object.name = self.name


    def __repr__(self):
        return f"Block(length={self.length}, width={self.width}, height={self.height})"

    def __str__(self):
        return f"Block(length={self.length}, width={self.width}, height={self.height})"
