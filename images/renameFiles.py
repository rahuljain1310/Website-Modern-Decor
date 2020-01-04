import os 

def rename(folder):
  i = 0
  for filename in os.listdir(folder): 
      dst = str(i) + ".jpg"
      src = folder + "/"+ filename 
      dst = folder + "/"+ dst 
      os.rename(src, dst) 
      i += 1

directories = ['Project'+str(i) for i in range(1,7)]
for d in directories:
  rename(d)