FROM jupyter/scipy-notebook:0ce64578df46

RUN pip install torch==1.9.0+cpu torchvision==0.10.0+cpu torchtext==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN conda install hyperopt

RUN conda install xgboost

RUN conda install scikit-learn

RUN conda install imbalanced-learn

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

RUN echo "export PYTHONPATH=/home/jovyan/work" >> ~/.bashrc

WORKDIR /home/jovyan/work