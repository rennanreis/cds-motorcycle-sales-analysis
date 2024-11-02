import streamlit as st
import src.answers as asw
from src.extraction import load_data
import pandas as pd

st.set_page_config(layout="wide")

def create_dataframe_section(df):
    st.title("Sections - Database Description")

    # Splitting the screen into two equal columns
    col_1, col_2 = st.columns(2)

    # Verifica se df é realmente um DataFrame e contém dados
    if isinstance(df, pd.DataFrame) and not df.empty:
        col_1.header("Database")
        col_1.dataframe(df, height=530)  # Removido use_container_width=True
    else:
        st.warning("Warning: Data could not be loaded or is empty.")
        st.text(f"df type: {type(df)}")  # Exibe o tipo de df para depuração
        if isinstance(df, pd.DataFrame):
            st.text("DataFrame está vazio.")
        else:
            st.text("df não é um DataFrame.")

    # Displaying data description in the second column with Markdown and HTML for style control
    col_2.header("Data Description")

    data_description = """
    <style>
        table { width: 100%; }
        th, td { padding: 8px; text-align: left; }
    </style>

    | Column            | Description                                                    |
    | ----------------- | -------------------------------------------------------------- |
    | ID                | Row/Record Identifier                                          |
    | name              | Motorcycle Manufacturer and Model                              |
    | selling_price     | Selling Price                                                  |
    | year              | Year of Manufacture                                            |
    | seller_type       | Seller Type - Personal seller or dealership                    |
    | owner             | Ownership status (first, second, third, or fourth owner)       |
    | km_driven         | Kilometers traveled by the motorcycle                          |
    | ex_showroom_price | Motorcycle price excluding insurance and registration fees     |
    | age               | Years of usage                                                 |
    | km_class          | Mileage classification                                         |
    | km_per_year       | Kilometers driven per year                                     |
    | km_per_month      | Kilometers driven per month                                    |
    | company           | Motorcycle Manufacturer                                        |
    """

    col_2.markdown(data_description, unsafe_allow_html=True)

def create_answers_section(df):
    st.title("Main Questions and Answers")

    st.header("First Round")
    st.subheader("How many bikes are being sold by their owners versus distributors?")
    asw.rd1_question_9(df)

    st.subheader("How many bikes being sold have a unique owner?")
    asw.rd1_question_13(df)

    st.subheader("Are high-kilometer bikes more expensive than those with lower mileage?")
    asw.rd1_question_14(df)

    st.subheader("Are bikes with a unique owner more expensive on average than others?")
    asw.rd2_question_1(df)

    st.subheader("Do bikes with more owners have more kilometers traveled on average?")
    asw.rd2_question_2(df)

    st.subheader("Which company has the most bikes listed?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the most expensive bikes on average?")
    asw.rd3_question_2(df)

    st.subheader("Is the company with the most expensive bikes also the one with the most listings?")
    asw.rd3_question_5(df)

    st.subheader("Which bikes are good for purchasing?")
    asw.rd3_question_7(df)

def create_main_layout():
    df = load_data()
    # Verifica se o DataFrame foi carregado corretamente antes de prosseguir
    if isinstance(df, pd.DataFrame) and not df.empty:
        create_dataframe_section(df)
        create_answers_section(df)
    else:
        st.error("Error: Data could not be loaded. Please check the file path or data source.")
        st.text(f"df type: {type(df)}")  # Exibe o tipo de df para depuração
        if isinstance(df, pd.DataFrame):
            st.text("DataFrame está vazio.")
        else:
            st.text("df não é um DataFrame.")

if __name__ == "__main__":
    create_main_layout()
