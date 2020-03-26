### Import Libraries
import papermill as pm


### Execute a Notebook

input_path = "/vrep/vflow/tmp/DSP/R_Demo/02_make_prediction.ipynb" # A notebook with R-Coding
output_path = "/vrep/vflow/tmp/DSP/R_Demo/02_make_prediction_executed.ipynb"

_ = pm.execute_notebook(input_path, output_path)
                            
                            
### send output for shutdown
api.send("out", "end process")
