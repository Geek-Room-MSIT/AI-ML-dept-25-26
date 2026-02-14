class SimpleModel:
  def __init__(self):
    self.avg=0
  def train(self,data):
    Sum=0
    for i in data:
      Sum=Sum+i
    Len=len(data)
    self.avg=Sum/Len 
  def predict(self,x):
    if(x<self.avg):
      return "Below Average"
    elif(x>self.avg):
      return "Above Average"
    else:
      return "Average"
