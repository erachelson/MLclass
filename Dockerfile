FROM jupyter/datascience-notebook
MAINTAINER Jonathan Sprauel
RUN conda install nltk nltk_data graphviz -y
EXPOSE 8888
CMD start-notebook.sh