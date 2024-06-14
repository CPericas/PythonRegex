#You have a list of product descriptions. Your task is to tag each product based on keywords in the description. For instance, tag 
# products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.
#Code Example:
#descriptions = [
#    "Smartphone with 6-inch screen and 128GB memory",
#    "Cotton t-shirt in medium size",
#    "Stainless steel kitchen knife set"
#]
# Tag each product based on keywords in the description
#Expected Outcome:
#Convert all price formats in the string to a standardized 'USD XX.XX' format.
#Use re.sub() to perform the necessary replacements and format transformations.
import re
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
tagged_descriptions = []
for desc in descriptions:
    if re.search(r'\bSmartphone\b|\bscreen\b|\bmemory\b', desc, re.IGNORECASE):
        tagged_descriptions.append(("Electronics", desc))
    elif re.search(r"\bCotton\b|\bT-?shirt\b|\bApparel\b", desc, re.IGNORECASE):
        tagged_descriptions.append(("Apperal", desc))
    elif re.search(r"\bKitchen\b|\bknife\b", desc, re.IGNORECASE):
        tagged_descriptions.append(("Home & Kitchen", desc))
    else:
        tagged_descriptions.append(("Uncategorized", desc))
for tag, desc in tagged_descriptions:
    print(f"{tag}: {desc}")

        