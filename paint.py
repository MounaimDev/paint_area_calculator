import math
def paint_calc(height,width,cover):
  area  = height * width
  num_of_cans = math.ceil(area / cover)
  print(f"You will need {num_of_cans} of cans of paint.")

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w,cover=coverage)