# OOP
creates a program based on object not functions
* link
https://www.youtube.com/watch?v=5SWKbS87p98

1. Object (instance of class)
court - attributes - color, surface, dimention (variables, data members)
      - functionality - doCourtBooking(), courtCleaning(functions)

2. class
specification of object
    student {
        attributes
        functions
    }
Changes in attribute changes function within inside class

3. abstraction
taking the necessary details and ignoring the rest
class{
    some attributes out of all possible
    some functions out of all possible
}

you do not need to know what you do not need to know fprintf (I do not know what is inside of this function)

4. encapsulation

think about capsul. (medicine can reaction with air)

protection, to protect data to go outside. variables should not be accesable which are generaly private, no one outside of the class should be able to read data.

but the functions are public (interface). functions can access the data, the data is acceseable through functions. So we have control over with function,

5. inheritance

One object acquiring the properties of another object through relationship

Object(Papa) <---- Object(child)

relationship and object
relationship of program and softwares...

6. Polymorphism (Many forms)

facilitate the use of the software, to make ease use of the user
Means: same function when applied on the different objects gives different results

    1. Example: age of emprires attacking of soldiers in different ways by one click of attack.
    2. Example: wash function for vegatables : wash spanich different than okras... wash function behaves differently for each object.

- - - -
- - - -

# SOLID principles
Concepts/Desing/Practices

software always changes. Designers think about future changes to desing.

## Principles

### DRY (donot repeat yourself)
if you copy and paste a functionality in 5 places, and when code changes in future, you have to change everything in 5 places instead of one.

### Divide & Conquer
if program get bigger, think this

### Expect Change
Design should be able to accomodate change without destroying the existing working functionality

1. Single Responsibility Principle
A class should have one and only one reason to change
in term context : is about the regarding one thing (booking or member)
Example: A sportman only thinks sport and the other things in his life is taken care by his/her wife.
Example: Court example:
Member can only do C:create, R:read, U:update, D:delete
Not booking.

2. Open for extension / closed for modification
    1. Booking Class [payment method] should not have details inside, should only call one function p.payment()
    2. Payment Class should have payment.method and under there should be 3 class for cash_payment, card_payment etc...
So when there is new method of payment created, we only add this method as a class, the rest of the code changes as it is because we do not update booking and payment class. We only extent and do not modify.

3. Liskov's substitution Principles
Child should be able to substitute the parent for providing the functionality promised by the parent

A kartel's son is elected after his father died. But he was neighbors son and does not know the kartel's rules. This violates the principle

4. Interface Segregation Principle
Any client should not be forced to implement any interface which is irrelevant to it
Parent's goes to restaurant and faced with bar menu. But they came for eating dinner.

Booking class (bookingDetails(memberdetaials), paymentDetails())
if you pay cash you should not have card detail class...
Card detail class should be a new interface.

5. Dependency Inversion Principle
For different payment method in booking Class,
Booking class should not decide which method by if clauses

But instead, the instance of class booking, we should provide the payment method
Booking b = Booking(member, CardPayment())
Booking b = Booking(member, CashPayment())


# Class

Court Member
    1. Data Members
    2. Member functions

 (data types, int, string, char, float)
