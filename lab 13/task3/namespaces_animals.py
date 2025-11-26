species = "Global Tiger"  # Global

def zoo():
    species = "Zoo Lion"  # Enclosing

    def inner():
        species = "Local Cat"  # Local
        print("Inside inner():", species)

    inner()

print("Global level:", species)
zoo()