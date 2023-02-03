class Circle:
    """
    The Circle class represents a circle with a radius.
    
    Attributes:
    - radius (float): the radius of the circle.
    
    Methods:
    - area(): returns the area of ​​the circle.
    """
    def __init__(self, radius):
        """
        The constructor for the Circle class.
        
        args:
        - radius (float): the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of ​​the circle.
        
        Returns:
        float: the area of ​​the circle.
        """
        return 3.14 * self.radius**2

