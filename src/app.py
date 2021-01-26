import streamlit as st
import subprocess


def carrega_dados_kaggle():
    bash_command = 'kaggle datasets download -d gpreda/covid-world-vaccination-progress'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


def main():
    st.text(carrega_dados_kaggle())


if __name__ == '__main__':
    main()