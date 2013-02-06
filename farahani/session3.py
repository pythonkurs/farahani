import os

class alter_directory(object):
    
    
    def __init__(self,new_path):
        self.neue_path = new_path
        self.cu_path = os.getcwd()
        os.chdir(self.neue_path)
        
        
    def __exit__(self):
        os.chdir(self.cu_path)



class CourseRepo(object):
    def __init__(self, lastname):
        self.required=[]
        self.surname = lastname


    @property
    def surname(self):
        return self._surname


    @surname.setter
    def surname(self,n_name):
        self._surname=n_name
        self.required.append(".git") 
        self.required.append("setup.py") 
        self.required.append("README.md")
        self.required.append("scripts/getting_data.py")
        self.required.append("scripts/check_repo.py")
        self.required.append(n_name + "/__init__.py")
        self.required.append(n_name + "/session3.py")



    def check(self):
        for p in self.required:
            if not os.path.exists(p):
                return False
        return True
