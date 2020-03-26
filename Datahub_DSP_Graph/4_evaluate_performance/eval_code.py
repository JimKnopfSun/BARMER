### Import Libraries
from git_clone import git_clone
import datetime
import os
import papermill as pm


### Create Timestamp for new Folder
now = str(datetime.datetime.now())


### Create new Folder for Git-Clone
datahub_path = "/vrep/vflow/tmp/DSP/FROM_GIT/" + now
os.mkdir(datahub_path)


### Clone a repository from Github to Datahub Filesystem
git_clone(  git_url="https://github.com/JimKnopfSun/BARMER.git", 
            path=datahub_path)
# FS: /files/vflow/tmp/DSP/FROM_GIT/2020-01-30 10:33:42.747468/BARMER.zip
# OP: /vrep/vflow/tmp/...


### Execute a Notebook
input_path = datahub_path + "/BARMER/04_evaluate_performance.ipynb"
output_path = "/vrep/vflow/tmp/DSP/EXECUTED/04_evaluate_performance.ipynb"

_ = pm.execute_notebook(    input_path=input_path, 
                            output_path=output_path)
                            
                            
### send output for shutdown
api.send("out", "end process")

