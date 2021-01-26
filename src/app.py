import streamlit as st
import subprocess
import zipfile
import os


def baixar_dados():
    bash_command = 'kaggle datasets download -d gpreda/covid-world-vaccination-progress'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output, error


def baixar_dados_2():
    os.system('kaggle datasets download -d gpreda/covid-world-vaccination-progress')
    return 'done'


def extrair_dados():
    with zipfile.ZipFile('./covid-world-vaccination-progress.zip', 'r') as zip_ref:
        zip_ref.extractall('./dados/')


def main():
    st.text(baixar_dados_2())
    extrair_dados()


if __name__ == '__main__':
    main()