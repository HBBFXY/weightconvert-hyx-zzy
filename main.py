#WeightConvert.py
WeightStr="10kg"
if WeightStr[-2:]=='kg':
  kg=float(WeightStr[:-2])
  pd=kg*2.2046
  print(f"10kg对应的英制重量为{pd:.3f}磅")
elif WeightStr[-2:]=='pd':
  pd=float(WeightStr[:-2])
  kg=pd/2.2046
  print(f"对应的公制重量为{kg:.3f}公斤")
else:
  print("输入格式错误")
WeightStr="10pd"
if WeightStr[-2:]=='kg':
  kg=float(WeightStr[:-2])
  pd=kg*2.2046
  print(f"10kg对应的英制重量为{pd:.3f}磅")
elif WeightStr[-2:]=='pd':
  pd=float(WeightStr[:-2])
  kg=pd/2.2046
  print(f"10pd对应的公制重量为{kg:.3f}公斤")
else:
  print("输入格式错误")
