import streamlit as st
import pandas as pd
import math


def run():
    st.title(":blue[Расчётная итоговая оценка по трудозатратам на разработку и внедрение ML-модели]")

    # Достаем сохраненные состояния
    number = int(st.session_state.number)
    choice1 = st.session_state.choice1
    choice2 = st.session_state.choice2
    choice3 = st.session_state.choice3

    # Расчет коэффициентов
    if number == 1:
        ratio1 = 1
    else:
        ratio1 = 1 + (number - 1) * 0.75

    if choice1 == "Да":
        ratio2 = 0.5
    else:
        ratio2 = 1

    if choice2 == "Да":
        ratio3 = 1
    else:
        ratio3 = 0

    if choice3 == "Батч":
        ratio4 = 1.5
    else:
        ratio4 = 0.8

    st.write(r"$\textbf{\large Таблица трудозатрат по этапу}$")
    stage_name = pd.DataFrame({
        "Наименование этапа": ["01. Построение витрины", "02. Разработка модели", "03. Адаптация и внедрение модели"],
        "Среднее значение трудозатрат, Ч/Д": [63, 32, 47]
    })
    st.dataframe(stage_name)

    st.write(r"$\textbf{\large Таблица расчета}$")
    df = pd.DataFrame({
        "Вопрос": ["Кол-во моделей (>1 для каскадов и ансамблей моделей)", "Наличие готовых промышленных витрин",
                   "Требуется ли внедрение модели в пром", "Канал  внедрения"],
        "Ответ": [number, choice1, choice2, choice3],
        "Коэффициент": [ratio1, ratio2, ratio3, ratio4],
        "Влияние на этап": ["02", "01", "03", "03"]
    })
    st.dataframe(df)

    st.write(r"$\textbf{\large Формула итоговой оценки}$")
    st.write(
        "Итоговая оценка = ср.знач.Трудозатрат по этапу 01 * коэффициент + ср.знач.Трудозатрат по этапу 02 * коэффициент "
        "+ ср.знач.Трудозатрат по этапу 03 * коэффициенты")

    answer = 63 * ratio2 + 32 * ratio1 + 47 * ratio3 * ratio4

    st.write(r"$\textbf{\large Подсчет итоговой оценки с округлением вверх}$")
    st.write(f"Итоговая оценка = 63 * {ratio2} + 32 * {ratio1} + 47 * {ratio3} * {ratio4} = {math.ceil(answer)} Ч/Д")
