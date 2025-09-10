#WeightConvert.py
WeightStr=input()
if WeightStr[-2:]=='kg':
  kg=float(WeightStr[:-2])
  pd=kg*2.2046
  print(f"对应的英制重量为{pd:.3f}磅")
elif WeightStr[-2:]=='pd':
  pd=float(WeightStr[:-2])
  kg=pd/2.2046
  print(f"对应的公制重量为{kg:.3f}公斤")
else:
  print("输入格式错误")
