import streamlit as st

st.title("Python")

st.write("""Python is a high-level, interpreted, and general-purpose programming language created by Guido van Rossum in 1991.  
It is known for its simplicity, readability, and versatility, making it one of the most widely used programming languages in the world.
""")

st.subheader("Key Features")
st.text("""1.Simple and Easy to Learn-Syntax is close to English, easy for beginners.  
2. Interpreted Language-No compilation required; code runs directly.  
3. Dynamically Typed-No need to declare variable data types.  
4. Object-Oriented-Supports classes, objects, and inheritance.  
5. Extensive Libraries-Rich standard library and thousands of external modules.  
6. Portable-Works on Windows, macOS, and Linux. """)


st.subheader("Core Concepts")
st.write("""1.Variables and Data Types-int, float, str, list, tuple, set, dict.  
2. Operators-Arithmetic, Logical, Comparison, Assignment.  
3. Control Statements-if, else, for, while, break, continue.  
4. Functions-Blocks of reusable code using `def`.  
5. Modules and Packages-For organizing and reusing code.  
6. File Handling-Read/write files using `open()`, `read()`, `write()`.  
7. Exception Handling-use of `try`, `except`, and `finally` for error control.  
8. OOP Concepts-Encapsulation, Inheritance, Polymorphism, Abstraction. """)



st.subheader("Commonly Used Built-in Functions")
st.write("""1. len()	Returns the length of an object.
2. type()	Returns the type of variable.
3. input()	Takes user input.
4. range()	Generates a sequence of numbers.
5. sum(), max(), min()	Mathematical operations.
6. sorted()	Sorts iterable items.""")

st.subheader("Data Structures")
st.write("""
1. List	[1, 2, 3]	Ordered, mutable.
2. Tuple	(1, 2, 3)	Ordered, immutable.
3. Set	{1, 2, 3}	Unordered, unique items.
4. Dictionary	{"name": "Ramya", "age": 20} Key-value pairs""")



st.subheader("Modules and Libraries")
st.write("""1. math → Mathematical functions
2. datetime → Date and time handling
3. os → Operating system tasks
4. random → Random number generation
5. re → Regular expressions
6. json → JSON handling
7. requests → HTTP requests
8. pandas / numpy / matplotlib → Data analysis & visualization""")


st.subheader("Python OOP Principles")
st.write("""1. Encapsulation	Hiding data within classes
2. Inheritance	Reusing code from parent classes
3. Polymorphism	One function behaves differently in different contexts
4. Abstraction	Hiding implementation details""")