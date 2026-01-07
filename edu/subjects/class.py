class Person:
    """
    A class to represent a person with basic information and functionality.
    
    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        email (str): The email address of the person
    """
    
    # Class variable
    species = "Human"
    
    def __init__(self, name: str, age: int, email: str = None):
        """
        Initialize a new Person instance.
        
        Args:
            name: The name of the person
            age: The age of the person
            email: Optional email address
        """
        self.name = name
        self.age = age
        self._email = email  # Using _ to indicate protected attribute
    
    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    @property
    def email(self) -> str:
        """Get the person's email address."""
        return self._email if self._email else "No email provided"
    
    @email.setter
    def email(self, value: str):
        """Set the person's email address.
        
        Args:
            value: The email address to set
        
        Raises:
            ValueError: If email doesn't contain '@'
        """
        if '@' not in value:
            raise ValueError("Invalid email format. Email must contain '@'")
        self._email = value
    
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int, email: str = None) -> 'Person':
        """Create a Person instance from birth year instead of age.
        
        Args:
            name: The name of the person
            birth_year: The birth year of the person
            email: Optional email address
            
        Returns:
            A new Person instance
        """
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age, email)
    
    @staticmethod
    def is_adult(age: int) -> bool:
        """Check if a person is an adult based on age.
        
        Args:
            age: The age to check
            
        Returns:
            bool: True if age is 18 or older, False otherwise
        """
        return age >= 18
    
    def __str__(self) -> str:
        """Return string representation of the Person."""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self) -> str:
        """Return official string representation of the Person."""
        return f"Person(name='{self.name}', age={self.age}, email='{self._email}')"
        
    @classmethod
    def is_a(cls, obj) -> bool:
        """Check if an object is an instance of Person.
        
        Args:
            obj: The object to check
            
        Returns:
            bool: True if obj is an instance of Person, False otherwise
        """
        return isinstance(obj, cls)