
 folders =   ["folders1","folder2","folder3","folder4"]
  target = input("Enter the folder name:")
  found =  False
  for folder in folders:
      print(type(folder))
      if folder == target:
          print("folder name")
          found = True
      if not found:
          print("no match found")
    