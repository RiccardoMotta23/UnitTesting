import math

class MathUtils:
  """
  Class that implements mathematical operations.
  """

  @staticmethod
  def add(a: int | float, b: int | float) -> int | float:
    """
    Just adds two numbers together.
    """
    return a + b

  @staticmethod
  def subtract(a: int | float, b: int | float) -> int | float:
    """
    Just subtracts two numbers.
    """
    return a - b

  @staticmethod
  def divide(a: int | float, b: int | float) -> float:
    """
    Just divides two numbers.
    """
    if b == 0:
      raise ValueError("You cannot divide by zero!")
    return a / b
  
  def multiply(a: int | float, b: int | float) -> int | float:
    """
    Just multiply two numbers
    """
    return a * b

  def sqrt(a: int | float) -> int | float:
    """
    Just square root a number
    """
    return math.sqrt(a)

  def power_of(a: int | float, b: int | float) -> int | float:
    """
    Just power_of a number
    """
    return a**b

  def cos_value(a: int | float) -> float:
    """
    Returns the cosine of a number (in radians)
    """
    return math.cos(a)
    """"""

  def sin_value(a: int | float) -> float:
    """
    Returns the sine of a number (in radians)
    """
    return math.sin(a)

  def tan_value(a: int | float) -> float:
    """
    Returns the tangent of a number (in radians)
    """
    return math.tan(a)

  def log_value(a: int | float, base: int | float = math.e) -> float:
    """
    Returns the logarithm of a number with the given base (default: natural logarithm)
    """
    return math.log(a, base)

  def factorial_value(a: int) -> int:
    """
    Returns the factorial of an integer
    """
    return math.factorial(a)