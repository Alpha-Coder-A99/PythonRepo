"""
A combination of two or more types of inheritance listed above 
(e.g., mixing multiple and multilevel inheritance
"""
class Base:
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A, B):  # Combines hierarchical and multiple structures
    pass
