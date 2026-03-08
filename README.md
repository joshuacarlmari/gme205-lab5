# Gme205 Laboratory 5 Reflections
## 1. Where does polymorphism appear in your system?
### Polymorphism appears when spatial classes like Parcel, Building, and Road implement the same methods, such as area(), length(), or describe(). Each object handles the method according to its own behavior, allowing the program to call the same method on any object without needing to know its class. For example, feature.describe() outputs different results depending on whether the object is a Parcel, Building, or Road.

## 2. If you removed your algorithm planning step, how would your implementation likely change?

### Polymorphism lets each object handle its own behavior, so analysis.py doesn’t need if or elif checks. You can just call feature.area() or feature.length(), and the right method runs automatically, making the code simpler and less error-prone.

## 3. Where does spatial behavior live in your system, and why is that important?
### The OOP pillar that allows multiple classes to share a method name is polymorphism. Polymorphism lets different classes use the same method name while providing their own behavior. This way, it enables the system to treat all the objects consistenty, while each object handles its own behavior which are useful for features like parcels, roads, and buildings.

## 4. Why is it better for objects to compute their own area rather than using a condition to decide how?

### Objects should compute their own area because they have their own structure and rules. Encapsulation ensures each object protects its data—like parcels not having negative areas or buildings having realistic heights. This makes the code simpler, reduces errors, and avoids messy conditionals, keeping the system modular and easier to extend.

## 5. If you add a new class tomorrow (River), what changes are required in spatial.py?
### If a new class like River is added, only its definition and relevant methods (e.g., length() or describe()) need to be implemented in spatial.py. Existing scripts remain unchanged because polymorphism allows River objects to be used like any other spatial object, ensuring the system is clean, extensible, and maintainable.
