import os

#Works for linux paths. Not tested for windows.
#Script to rename all *jpg files to a RequiredName-xx.jpg in a specified directory.

def main():
   directory="/path/to/dir"
   i = 0

   for filename in os.listdir(directory):
     if filename.endswith(".jpg"):
        originalpath = os.path.join(directory, filename)
        #print 'originalpath : {}'.format(originalpath)
        newname = 'RequiredName-{}.jpg'.format(i)
        newpath = os.path.join(directory, newname)
        #print 'newpath : {}'.format(newpath)
        os.rename(originalpath, newpath)
        i += 1

if __name__=="__main__":
    main()
