import streamlit as st
import kaggle

def carrega_dados_kaggle():
    kaggle.api.dataset_download_files('gpreda/covid-world-vaccination-progress', path='/', unzip=True)
    return 'done'


def main():
    st.text(carrega_dados_kaggle())






if __name__ == '__main__':
    main()