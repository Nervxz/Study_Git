"""
List operations demo
"""

def main():
    # Create a list
    fruits = ["apple", "banana", "cherry", "date", "date", "date", "date"]
    
    print("Original list:", fruits)
    
    # Add an item
    fruits.append("elderberry")
    print("After append:", fruits)
    
    # Remove an item
    fruits.remove("banana")
    print("After remove:", fruits)
    
    # Sort the list
    fruits.sort()
    print("After sort:", fruits)
    
    # Get list length
    print("List length:", len(fruits))

if __name__ == "__main__":
    main()
