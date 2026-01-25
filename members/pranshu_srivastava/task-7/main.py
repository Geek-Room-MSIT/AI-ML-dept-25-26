from data_loader import DataLoader 
from simple_model import SimpleModel 
loader = DataLoader()
data = loader.get_data()
model = SimpleModel()
model.train(data)
test_val = [10,20,25]
for val in test_val:
  result = model.predict(val)
  print(f"value {val} -> {result}")
