https://www.youtube.com/watch?v=SiBw7os-_zI

Chess example
knight - position, captured, color ...

classes are templates for objects
Objects are instances of a class

class Knight

- move()
- position
- color

objects one Knight

# Encapsulation

(hiding information)

- bundling data with methods that can operate on that data within a class
- hiding data within class, preventing anything outside that class from directly interacting with it
- it is generally best to not allow external classes to directly edit an object's attributes
- each piece should not have access to or rely on the inner working of other sections of code
- members of other classes can interact with attributes of another object through its methods
- Getting methods : retrieving information
- setting method : changing information

chess: knight - piece.getColor() checks the color of any given piece from anywhere in the program

# Abstraction

- to only showing essential details and keeping everything else hidden
- car : steering wheel, gas pedal etc, not internal mechanism
- interface: the way section of code can comminicate with one another, by methods
- implementation : implementation of these methods or how these methods are coded, should be hidden
- if classes are entangled, then one change creates a ripple effect that cause many more changes
- creating an interface through which classes can intereact ensures that each piece can be individually developed

# Inheritance

- allow classes to derive from other classes
- superclass- subclasses
- access modifiers change which classes have access to other classes, methods, or attributes

* Public : can be accessed from anywhere
* Private : can be accessed within the same class that the member is defined
* Protected : can be accessed within the class it is defined, as well as any subclassess of the class

# Polymorphism

describes methods that are able to take on many forms

## dynamic polymorphism

- during runtime of the program
- describes when a method signature is in both a subclasses and a superclass
- the methods share the same name but have different implementation
- the implementation of the subclass that the object is an instance of overrides that of the superclass
- the form of the method is decided based on where in the class hierarchy it is called

## Static polymorphism

- occurs during compile-time rather than during runtime
- multiple methods with the same name but different arguments are defined in the same class
- ways to differentiate methods of the same name: i) different number of parameters ii) different types of paramaters iii) different order of parameters
- known as method overloading
- allows methods to take on many different forms

