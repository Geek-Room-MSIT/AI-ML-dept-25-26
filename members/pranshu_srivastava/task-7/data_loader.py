class DataLoader:
  def __init__(self):
    self.num=[]
    a=int(input('Enter how many numbers you want to add in list:'))
    for i in range(a):
      b=int(input(f"Enter the value {i+1}:"))
      self.num.append(b)
  def get_data(self):
    return self.num
