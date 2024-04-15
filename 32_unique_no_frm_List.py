listabc=[10,20,30,10,20]

unique_elements = []

for element in listabc:
    if element not in unique_elements:
        unique_elements.append(element)

print(unique_elements)
