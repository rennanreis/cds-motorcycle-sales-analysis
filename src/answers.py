import pandas as pd
import plotly.express as px
import streamlit as st
from io import BytesIO

def rd1_question_9(df):
    df_grouped = df[["id", "seller_type"]].groupby("seller_type").count().reset_index()
    df_grouped = df_grouped.rename(columns={"id": "count"})

    fig = px.bar(
        df_grouped,
        x="seller_type",
        y="count",
        labels={"seller_type": "Seller Type", "count": "Quantity"},
        color="seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd1_question_13(df):
    df_grouped = (
        df.groupby("owner")
        .agg(qty=pd.NamedAgg("id", "count"))
        .sort_values("qty")
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="owner",
        y="qty",
        labels={"owner": "Owner Types", "qty": "Quantity"},
        color="owner",
        text="qty",
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd1_question_14(df):
    st.text("As we can see, bikes with higher mileage tend to be cheaper.")

    fig = px.scatter(
        df,
        x="km_driven",
        y="selling_price",
        labels={"km_driven": "Kilometers", "selling_price": "Selling Price"},
    )

    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd2_question_1(df):
    df_grouped = (
        df.groupby("owner")
        .agg(
            avg_price=pd.NamedAgg("selling_price", "mean"),
            qty=pd.NamedAgg("owner", "count"),
        )
        .sort_values("avg_price", ascending=False)
        .reset_index()
    )

    df_grouped["avg_price"] = df_grouped["avg_price"].round(2)

    fig = px.bar(
        df_grouped,
        x="owner",
        y="avg_price",
        labels={"owner": "Owner Types", "avg_price": "Average Price"},
        text="avg_price",
        color="owner",
    )

    fig.update_traces(texttemplate="$ %{text:.2f}", textposition="inside")
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd2_question_2(df):
    df_grouped = (
        df[["owner", "km_driven"]]
        .groupby("owner")
        .mean()
        .sort_values("km_driven", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="owner",
        y="km_driven",
        labels={"owner": "Owner Types", "km_driven": "Average Kilometers"},
        text="km_driven",
        color="owner",
    )

    fig.update_traces(texttemplate="%{text:.2f} Km", textposition="inside")
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd2_question_3(df):
    df_grouped = (
        df[["owner", "age"]]
        .groupby("owner")
        .mean()
        .sort_values("age", ascending=False)
        .reset_index()
    )

    df_grouped["age"] = df_grouped["age"].astype(int)

    fig = px.bar(
        df_grouped,
        x="owner",
        y="age",
        labels={"owner": "Owner Types", "age": "Average Age"},
        text="age",
        color="owner",
    )

    fig.update_traces(texttemplate="%{text:.0f} Years", textposition="inside")
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd2_question_7(df):
    df_grouped = (
        df[["company", "id"]]
        .groupby("company")
        .count()
        .sort_values("id", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="company",
        y="id",
        labels={"company": "Companies", "id": "Quantity"},
        text="id",
        color="company",
    )

    fig.update_traces(textposition="outside")
    fig.update_xaxes(tickangle=-80)
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd3_question_2(df):
    df_grouped = (
        df[["company", "selling_price"]]
        .groupby("company")
        .agg(
            avg_price=pd.NamedAgg("selling_price", "mean"),
            median_price=pd.NamedAgg("selling_price", "median"),
            std_price=pd.NamedAgg("selling_price", "std"),
            qty=pd.NamedAgg("company", "count"),
        )
        .sort_values("avg_price", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x="company",
        y="avg_price",
        labels={"company": "Companies", "avg_price": "Average Price"},
        text="avg_price",
        color="company",
        title="Company Average Price",
    )

    fig.update_traces(texttemplate="$ %{text:.2f}", textposition="outside")
    fig.update_xaxes(tickangle=-80)
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd3_question_5(df):
    df_grouped = (
        df[["id", "selling_price", "company"]]
        .groupby("company")
        .agg(
            max_selling_price=pd.NamedAgg("selling_price", "max"),
            quantity=pd.NamedAgg("id", "count"),
        )
        .reset_index()
        .sort_values("max_selling_price", ascending=False)
    )

    fig = px.scatter(
        df_grouped,
        x="company",
        y="max_selling_price",
        labels={"company": "Company", "max_selling_price": "Selling Price"},
        text="quantity",
        color="quantity",
    )

    fig.update_traces(marker={"size": 20}, textposition="top center")
    fig.update_xaxes(tickangle=-80)
    fig.update_layout(width=700, height=400, margin=dict(l=0, r=0, t=40, b=40))

    with st.container():
        st.plotly_chart(fig, use_container_width=True)

    return None

def rd3_question_7(df):
    # Filtros
    year = df["year"] >= 2018
    sale = df["selling_price"] < df["ex_showroom_price"]
    single_owner = df["owner"] == "1st owner"
    individual_seller = df["seller_type"] == "Individual"
    low_mileage = df["km_driven"] <= 40000

    # Colunas para exibir
    columns = ["id", "name", "selling_price", "km_driven", "year"]

    # Seleção de dados
    df_selected = df.loc[
        year & low_mileage & single_owner & individual_seller & sale, columns
    ].sort_values("selling_price", ascending=False)

    # Renderizar o DataFrame como HTML com largura completa
    st.markdown(df_selected.to_html(index=False), unsafe_allow_html=True)

    # Converte o dataframe para o formato Excel
    df_xlsx = to_excel(df_selected)

    # Botão de download
    st.download_button(
        label="📥 Download Buying Suggestions",
        data=df_xlsx,
        file_name="buying_suggestions.xlsx",
    )

    return None

# Função auxiliar para converter dataframe em formato Excel
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    output.seek(0)
    return output.getvalue()
