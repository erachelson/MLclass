FROM jupyter/datascience-notebook
MAINTAINER Jonathan Sprauel
RUN conda install nltk nltk_data graphviz smt -y
RUN conda install -c anaconda py-xgboost  -y
EXPOSE 8888
CMD start-notebook.sh