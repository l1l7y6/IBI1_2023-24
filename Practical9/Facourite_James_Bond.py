def favor(a):
    # Bond actors by their active years
    bond_years = {
        (1973, 1986): "Roger Moore",
        (1987, 1994): "Timothy Dalton",
        (1995, 2005): "Pierce Brosnan",
        (2006, 2021): "Daniel Craig"
    }
    # Calculate when the person turned 18
    year18=a+18
    # Determine the favorite Bond actor
    for (start_year, end_year), actor in bond_years.items():
        if start_year <= year18 <= end_year:
            return actor
    return "No favorite Bond found"

# Example usage:
print(favor(1999))  # Expected: "Daniel Craig"