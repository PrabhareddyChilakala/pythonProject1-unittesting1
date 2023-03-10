from normal.searchfilein_dir import Searchfiles
obj=Searchfiles()
dir=input("enter dir path for ex:../normal:")
filename=input("enter the filename with file type extension:")
print(obj.search(dir,filename))