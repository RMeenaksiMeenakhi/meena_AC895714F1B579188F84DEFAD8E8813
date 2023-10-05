def linear_search_product(productlist,tar):
  indices=[]
  for index, prouct in enumerate(productlist):
    if prouct==tar:
      indices.append(index)

  return indices

product= ["rice","nuts""dal","nuts","fruits","vegetable"]
target="nuts"
result=linear_search_product(product,target)
print(result)