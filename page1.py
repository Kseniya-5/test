import streamlit as st

def run():
    st.title(":blue[Опросный лист]")

    # Вопрос 1
    if 'number' not in st.session_state:
        st.session_state.number = 1

    number = st.number_input(
        label=r"$\textbf{\large 1. Введите количество моделей}$",
        min_value=1,
        step=1,
        value=st.session_state.number
    )
    st.session_state.number = number
    st.write(f"Вы ввели: {int(number)}")


    # Вопрос 2
    if 'choice1' not in st.session_state:
        st.session_state.choice1 = None
    choice1_options = ["Да", "Нет"]
    choice1 = st.radio(
        label=r"$\textbf{\large 2. Есть ли наличие готовых промышленных витрин?}$",
        options=choice1_options,
        index=choice1_options.index(st.session_state.choice1) if st.session_state.choice1 else None,
        key='choice1_radio'
    )
    st.session_state.choice1 = choice1
    if choice1 == None:
        st.write("Вы ничего не выбрали")
    else:
        st.write(f"Вы выбрали: {choice1}")

    # Вопрос 3
    if 'choice2' not in st.session_state:
        st.session_state.choice2 = None
    choice2_options = ["Да", "Нет"]
    choice2 = st.radio(
        label=r"$\textbf{\large 3. Требуется ли внедрение модели в пром?}$",
        options=choice2_options,
        index=choice2_options.index(st.session_state.choice2) if st.session_state.choice2 else None,
        key='choice2_radio'
    )
    st.session_state.choice2 = choice2
    if choice2 == None:
        st.write("Вы ничего не выбрали")
    else:
        st.write(f"Вы выбрали: {choice2}")

    # Вопрос 4
    if 'choice3' not in st.session_state:
        st.session_state.choice3 = None
    choice3_options = ["Батч", "Онлайн"]
    choice3 = st.radio(
        label=r"$\textbf{\large 4. Выберите канал  внедрения}$",
        options=choice3_options,
        index=choice3_options.index(st.session_state.choice3) if st.session_state.choice3 else None,
        key='choice3_radio'
    )
    st.session_state.choice3 = choice3
    if choice3 == None:
        st.write("Вы ничего не выбрали")
    else:
        st.write(f"Вы выбрали: {choice3}")

