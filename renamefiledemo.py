'''def rename(dir, pattern, titlePattern):
    i = 1
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        temp = titlePattern + str(i)
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,os.path.join(dir, temp % title + ext))
        i = i+ 1
var1="C:\\Users\\IBM_ADMIN\\Desktop\\dummy"
var1=var1.split("\\")
red=var1[-1]
#rename(r'C:\Users\IBM_ADMIN\Desktop\dummy_main', r'*.txt',str(red)+'_%s_')'''