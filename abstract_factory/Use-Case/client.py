import furniture_factory as f

Product = f.FurnitureFactory.get_furniture('SmallChair')
print(Product.get_dimensions())

Product = f.FurnitureFactory.get_furniture('MediumTable') 
print(Product.get_dimensions())