# FineTuningBert
Fine tuning BERT to perform sequence classification on tweets regarding cryptocurrencies

# Run Jupyter Notbeook on GPU (https://www.techentice.com/how-to-make-jupyter-notebook-to-run-on-gpu/) 
Ensure the following are installed 
- Python 
- Anaconda 
- Cuda toolkit 
Open command prompt with Admin privileges 
 conda create -n gpu2 python=3.6
 conda info -e
 conda activate -n gpu2
 pip install tensorflow-gpu==2.3.0
 conda install -c anaconda ipykernel
 python -m ipykernel install –user –name=gpu2
