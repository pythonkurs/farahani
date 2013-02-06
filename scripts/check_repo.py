from farahani.session3 import CourseRepo, alter_directory
import sys,os




file_path = sys.argv[1]
surname = file_path.split("/")[-1]

with alter_directory(file_path):
    repos=CourseRepo(surname)
    if repos.check():
        print 'PASS'
    else:
        print 'FAIL'
        





