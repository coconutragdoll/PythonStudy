fsrc = open(r'c:\Users\yyan18\python\src.txt','w+')
fsrc.writelines('How many seas must a white dove sail\n')
fsrc.writelines('Before she sleeps in the sand\n')
fsrc.seek(0,0)
src = fsrc.readlines()
fsrc.close()
fdest = open(r'c:\Users\yyan18\python\dest.txt','a+')
fdest.writelines(src)
fdest.seek(0,0)
fdest.writelines('How many roads must a man walk down\n')
fdest.writelines('Before they call him a man\n')