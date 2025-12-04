import streamlit as st
import pandas as pd
from datetime import datetime

if 'employees' not in st.session_state:
    st.session_state.employees = pd.DataFrame([
        ["Google", "Розробник", "380991234567", "dev@google.com", 5000],
        ["Microsoft", "Менеджер", "380992345678", "manager@microsoft.com", 4500],
        ["Apple", "Дизайнер", "380993456789", "designer@apple.com", 5500]
    ], columns=["Фірма", "Посада", "Телефон", "Email", "Оклад"])

st.title(" База даних працівників")
st.write("**Група:** Кібербезпека")
st.write("**Студент:** Прізвище Ім'я")
st.write(f"**Дата:** {datetime.now().strftime('%d.%m.%Y %H:%M')}")

st.subheader(" Статистика")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Записів", len(st.session_state.employees))
with col2:
    unique_entries = st.session_state.employees.select_dtypes(include=['object']).nunique().sum()
    st.metric("Унікальних текстових", unique_entries)
with col3:
    salary_range = f"{st.session_state.employees['Оклад'].min()} - {st.session_state.employees['Оклад'].max()}"
    st.metric("Діапазон окладів", salary_range)

st.subheader(" Всі працівники")
st.dataframe(st.session_state.employees, use_container_width=True)

with st.sidebar:
    st.header(" Операції")

    st.subheader("➕ Додати працівника")
    with st.form("add_form"):
        company = st.text_input("Фірма")
        position = st.text_input("Посада")
        phone = st.text_input("Телефон")
        email = st.text_input("Email")
        salary = st.number_input("Оклад", min_value=0)

        if st.form_submit_button("Додати"):
            if all([company, position, phone, email]):
                new_row = pd.DataFrame([[company, position, phone, email, salary]],
                                       columns=st.session_state.employees.columns)
                st.session_state.employees = pd.concat([st.session_state.employees, new_row], ignore_index=True)
                st.success(" Працівника додано!")
                st.rerun()

    st.subheader(" Сортування")
    sort_col = st.selectbox("Сортувати за:", st.session_state.employees.columns)
    if st.button("Сортувати"):
        st.session_state.employees = st.session_state.employees.sort_values(sort_col)
        st.rerun()

    st.subheader(" Видалення за атрибутом")
    del_col = st.selectbox("Атрибут для видалення:", st.session_state.employees.columns)
    del_value = st.text_input("Значення для видалення")
    if st.button("Видалити"):
        if del_value:
            st.session_state.employees = st.session_state.employees[
                st.session_state.employees[del_col].astype(str) != del_value]
            st.rerun()

    st.subheader(" Видалення за індексом")
    del_idx = st.number_input("Індекс для видалення", min_value=0, max_value=len(st.session_state.employees) - 1,
                              step=1)
    if st.button("Видалити за індексом"):
        st.session_state.employees = st.session_state.employees.drop(index=del_idx).reset_index(drop=True)
        st.rerun()

    st.subheader(" Пошук за атрибутом")
    filter_col = st.selectbox("Фільтрувати за:", st.session_state.employees.columns)
    filter_value = st.text_input("Значення для пошуку")
    if st.button("Знайти"):
        if filter_value:
            result = st.session_state.employees[
                st.session_state.employees[filter_col].astype(str).str.contains(filter_value, case=False)
            ]
            st.subheader("Результати пошуку:")
            st.dataframe(result)

with st.expander(" Детальна статистика"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Текстові атрибути:**")
        for col in ["Фірма", "Посада", "Телефон", "Email"]:
            unique = st.session_state.employees[col].nunique()
            st.write(f"{col}: {unique} унікальних")

    with col2:
        st.write("**Числові атрибути:**")
        st.write(
            f"Оклад: {st.session_state.employees['Оклад'].min():,} - {st.session_state.employees['Оклад'].max():,}")
        st.write(f"Середній оклад: {st.session_state.employees['Оклад'].mean():,.0f}")
        st.write(f"Медіана: {st.session_state.employees['Оклад'].median():,.0f}")

st.sidebar.markdown("---")

