import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
import random

st.set_page_config(layout="wide",)

# st.write(st.__version__)
st.logo('ios-color.svg',size='large')

changes = list(rng(5).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

@st.fragment(run_every=1.0)
def diagnostic_data():

    lst = [0.581835, 2.955541, 0.00002, 2.12043, 0.17064, 48515.0, 61.21929, 1.84033, 4.57031, 2.30859, 3.99023, 0.27539, 2.46973, 2.38184, 1.83984, 1.98926, 51.30, 20.44075]

    df = pd.DataFrame(
            {
                "Параметр": [
                    "Статус",
                    "Флаги тока",
                    "Ток",
                    "Гармоника 0",
                    "Гармоника 1",
                    "Гармоника 2",
                    "Гармоника 4",
                    "Max. Current",
                    "Контраст",
                    "Фи",
                    "Umod",
                    "Max.First Amp",
                    "Max. ADC",
                    "Mod. Ret.",
                    "Uref DAC",
                    "Mod U15",
                    "Analog U12",
                    "Input U12",
                    "Tin",
                    "Тем. Коррекции",
                    ],
                "Фаза А": [0, 128, ] + [i + random.random() for i in lst],
                "Фаза В": [0, 128, ] + [i + random.random() for i in lst],
                "Фаза С": [0, 128, ] + [i + random.random() for i in lst],
            },
        )

    st.dataframe(df, width="stretch", height="content", hide_index=True,)

with st.sidebar:
    with st.container(border=True):
        c1, c2 = st.columns(2, vertical_alignment="bottom")

        with c1:
            st.selectbox('COM-порт', ['COM-1','COM-2'])

        with c2:
            st.button('Обновить', width="stretch")

        st.button('Подключение', width="stretch")

    # st.space('small')

    with st.container(border=True):
        st.button('Поиск устройств', width="stretch")
        st.selectbox('COM-порт', [1,2], label_visibility="collapsed")
        st.checkbox('Без авторизации')
        st.button('Подключиться к устройсву', width="stretch")

    with st.container(border=True):
        st.selectbox('Роль', ['','Админ'], width="stretch")
        st.text_input('Пароль', key='pass-1', width="stretch")
        st.button('Авторизация', key='auth-1', width="stretch")


    with st.container(border=True):
        st.selectbox('Подроль', ['','Factory'], width="stretch")
        st.text_input('Пароль', key='pass-2', width="stretch")
        st.button('Авторизация', key='auth-2', width="stretch")

    st.space('medium')

    with st.container(vertical_alignment="top"):
        st.selectbox('Язык', ['RUS','ENG'])

    st.write('`Версия 1.0.1`')


row = st.container(horizontal=True, horizontal_alignment="right")
with row:
    st.button('Заблокировать поля', key='general_close_btn',)
    st.button('Разблокировать поля', key='general_open_btn',)

mtabs = st.tabs(["Общие данные", "Конфигурация", "Прошивки", "Модуль тока", "Модуль напряжения", "Модуль термометра", "Модуль оцифровки напряжения", "Модуль аналоговых выходов", "Самописец", "Дашборд"])

with mtabs[3]:

    c1, c2, c3 = st.columns([3,1.5,1], gap="small", border=True)

    with c1:
        stab1, stab2, stab3, stab4 = st.tabs(["Конфигурация", "Оптический тракт", "Коррекция по току", "Коррекция по температуре"])

        with stab1:
        
            sс1, sс2 = st.columns(2, gap="small", border=True)

            with sс1:
                st.write("``Настройка алгоритма обработки данных:``")
                df1 = pd.DataFrame(
                    {
                        "Параметр": [
                            "Correction by Q",
                            "AC",
                            "Deviation Stabilization",
                            "In-Phase settings OFF",
                            "61850 Phase Correction",
                            "DAC Phase Correction",
                            "Lock current 0.3%",
                            "Linear Correction",
                            "24-bit amplifier",
                            "Alg Correction Drop",
                            "500 Hz filter",
                            "Large Current",
                            "Correction Poly Large Current",
                            "Large Current Alg Fix",
                            ],
                        "Фаза А": [True, False, False, True, False, False, False, False, False, False, False, False, False, False],
                        "Фаза В": [True, False, False, True, False, False, False, False, False, False, False, False, False, False],
                        "Фаза С": [True, False, False, True, False, False, False, False, False, False, False, False, False, False],
                    },
                )

                st.data_editor(
                    df1,
                    column_config={
                        "Фаза А": st.column_config.CheckboxColumn(),
                        "Фаза В": st.column_config.CheckboxColumn(),
                        "Фаза С": st.column_config.CheckboxColumn(),
                    },
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            with sс2:
                st.write("``Настройка алгоритма коррекции температуры:``")

                df2 = pd.DataFrame(
                    {
                        "Параметр": [
                            "Полиномиальная по Твнеш",
                            "Полиномиальная по Твнут ",
                            "Линейная по Твнеш",
                            "Перезагрузка амплитуды",
                            ],
                        "Фаза А": [True, False, False, False,],
                        "Фаза В": [True, False, False, False,],
                        "Фаза С": [True, False, False, False,],
                    },
                )

                st.data_editor(
                    df2,
                    column_config={
                        "Фаза А": st.column_config.CheckboxColumn(default=False,),
                        "Фаза В": st.column_config.CheckboxColumn(default=False,),
                        "Фаза С": st.column_config.CheckboxColumn(default=False,),
                    },
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

                st.write('`Выбор источника температуры:`')
                row = st.container(horizontal=False, border=False)
                with row:
                    st.selectbox('Фаза А', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'], key='temp_PhaseA')
                    st.selectbox('Фаза В', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'], key='temp_PhaseB')
                    st.selectbox('Фаза С', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'], key='temp_PhaseC')

        # st.button("Записать настройки алгоритмов")
        # st.space('xxsmall')
        # row = st.container(horizontal=True)
        # with row:
        #     st.button('Считать параметры', key='curr_read_btn', width='stretch')
        #     st.button('Записать параметры', key='curr_set_btn', width='stretch')
    

        with stab2:
            cols = st.columns([2,1], border=True)
            with cols[0]:
                st.write("``Оптические параметры:``")
                df4 = pd.DataFrame(
                    {
                        "Параметр": [
                            "Част. модуляции",
                            "Значение ЦАП",
                            "Амп. модуляции",
                            "Смещение 0",
                            "Смещение 1",
                            "Смещение 2",
                            "Смещение 4",
                            "Сдвиг фазы",
                            "K0",
                            "K1",
                            "K2",
                            "K4",
                            "V",
                            "FI",
                            "U2 Low",
                            "U4 Low",
                            "Усил. фотоприемника",
                            ],
                        "Фаза А": [64.6, 0.9, 0.25, 2.16,0,0,0,0,1.3665,2.9542,3.16588,3.3725,0.7,0,0.5,0.05,16],
                        "Фаза В": [64.6, 0.9, 0.25, 2.16,0,0,0,0,1.3665,2.9542,3.16588,3.3725,0.7,0,0.5,0.05,16],
                        "Фаза С": [64.6, 0.9, 0.25, 2.16,0,0,0,0,1.3665,2.9542,3.16588,3.3725,0.7,0,0.5,0.05,16],
                    },
                )

                st.data_editor(
                    df4,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            with cols[1]:
                st.write("``Автонастройка:``")
                with st.container(border=True):
                    st.checkbox('Установить параметры по умолчанию перед автонастройкой', width='stretch')
                    st.checkbox('Настройка усилителя фотоприемника', width='stretch')
                    st.checkbox('Настройка частоты модуляции', width='stretch')
                    st.checkbox('Настройка смещения гармоник', width='stretch')
                    st.checkbox('Сохранить результаты в резервное хранилище', width='stretch')
                    st.checkbox('Выбрать все', width='stretch')
                    st.button('Автонастройка', width='stretch')

                st.button('Настройка квадратурной компоненты', width='stretch')

                with st.container(border=False):
                    st.write("``Поднастройка:``")
                    st.button('Калибровка Гармоники 1', width='stretch')
                    st.button('Переворот фазы', width='stretch')
        

            # st.space('xxsmall')
            # row = st.container(horizontal=True)
            # with row:
            #     st.button('Считать параметры', key='optic_read_btn', width='stretch')
            #     st.button('Записать параметры', key='optic_set_btn', width='stretch')

        with stab3:

            col31, col32, col33 = st.columns(3, gap="small", border=True)

            with col31:
                st.write('`Калибровочные параметры:`')

                df5 = pd.DataFrame(
                {
                    "Параметр": [
                        "K1",
                        "K2",
                        "N",
                        "Масштаб DAC",
                        "Номинал",
                        "Фазовая коррекция",
                        "AmpMax",
                        ],
                    "Фаза А": [1, 1, 1, 10500,1000,0,1000000,],
                    "Фаза В": [1, 1, 1, 10500,1000,0,1000000,],
                    "Фаза С": [1, 1, 1, 10500,1000,0,1000000,],
                },
            )

                st.data_editor(
                    df5,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            with col32:
                st.write('`Полнином малых токов:`')

                df5 = pd.DataFrame(
                {
                    "Параметр": [
                        "PA0",
                        "PA1",
                        "PA2",
                        "PA3",
                        "PA4",
                        "MA0",
                        "MA1",
                        "MA2",
                        "MA3",
                        "MA4",
                        "KLinP",
                        "KLinM",
                        ],
                    "Фаза А": [0,1,0,0,0,0,1,0,0,0,1,1],
                    "Фаза В": [0,1,0,0,0,0,1,0,0,0,1,1],
                    "Фаза С": [0,1,0,0,0,0,1,0,0,0,1,1],
                },
            )

                st.data_editor(
                    df5,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )     
    

            with col33:
                st.write('`Полнином больших токов:`')

                df6 = pd.DataFrame(
                {
                    "Параметр": [
                        "Kch_ABT",
                        "PB1",
                        "PB2",
                        "PB3",
                        "PB4",
                        "PB5",
                        "MB0",
                        "MB1",
                        "MB2",
                        "MB3",
                        "MB4",
                        "MB5",
                        ],
                    "Фаза А": [1,0,1,0,0,0,0,0,1,0,0,0],
                    "Фаза В": [1,0,1,0,0,0,0,0,1,0,0,0],
                    "Фаза С": [1,0,1,0,0,0,0,0,1,0,0,0],
                },
            )

                st.data_editor(
                    df6,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            # st.space('xxsmall')
            # row = st.container(horizontal=True)
            # with row:
            #     st.button('Считать параметры', key='curr_cor_read_btn', width='stretch')
            #     st.button('Записать параметры', key='curr_cor_set_btn', width='stretch')

            # col31, col32, col33 = st.columns(3, gap="large")
            # with col31:
            #     st.button('Записать параметры', key='mainCal',)
            # with col32:
            #     st.button('Записать параметры', key='smallCal', )
            # with col33:
            #     st.button('Записать параметры', key='bigCal')

        with stab4:

            col41, col42 = st.columns(2, gap="small", border=True)

            with col41:

                st.write('`Границы коррекции по температуре`')

                df7 = pd.DataFrame(
                {
                    "Параметр": [
                        "Нижняя граница",
                        "Верхняя граница",
                        ],
                    "Фаза А": [-60, +60,],
                    "Фаза В": [-60, +60,],
                    "Фаза С": [-60, +60,],
                },
            )
                st.data_editor(
                    df7,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            
            with col42:
                st.write('`Линейная коррекция температуры`')

                df8 = pd.DataFrame(
                {
                    "Параметр": [
                        "Temp0",
                        "TempAlpha0",
                        "TempAlpha1",
                        ],
                    "Фаза А": [20, 0, 0,],
                    "Фаза В": [20, 0, 0,],
                    "Фаза С": [20, 0, 0,],
                },
            )
                st.data_editor(
                    df8,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )


            # col41, col42 = st.columns(2, gap="large",)

            # with col41:
            #     st.button('Записать параметры', key='mainTemp',)
            # with col42:
            #     st.button('Записать параметры', key='LiniarTemp',)

            col41, col42 = st.columns(2, gap="small", border=True)

            with col41:

                st.write('`Полином коррекции по внешней температуре`')

                df9 = pd.DataFrame(
                {
                    "Параметр": [
                        "K0",
                        "K1",
                        "K2",
                        "K3",
                        "K4",
                        "K5",
                        "K6",
                        "K7",
                        "K8",
                        ],
                    "Фаза А": [0,0,0,0,0,0,0,0,0,],
                    "Фаза В": [0,0,0,0,0,0,0,0,0,],
                    "Фаза С": [0,0,0,0,0,0,0,0,0,],
                },
            )
                st.data_editor(
                    df9,
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            with col42:
                st.write('`Полином коррекции по внутренней температуре`')

                df10 = pd.DataFrame(
                {
                    "Параметр": [
                        "K0",
                        "K1",
                        "K2",
                        "K3",
                        "K4",
                        "K5",
                        "K6",
                        "K7",
                        "K8",
                        ],
                    "Фаза А": [0,0,0,0,0,0,0,0,0,],
                    "Фаза В": [0,0,0,0,0,0,0,0,0,],
                    "Фаза С": [0,0,0,0,0,0,0,0,0,],
                },
            )
                st.data_editor(
                    df10,
                    key='ExtTempCorr',
                    hide_index=True,
                    width="stretch",
                    height="content"
                )

            # col41, col42 = st.columns(2, gap="large",)

            # with col41:
            #     st.button('Записать параметры', key='ExtPolTemp',)
            # with col42:
            #     st.button('Записать параметры', key='IntPolTemp',)

            # st.space('xxsmall')
            # row = st.container(horizontal=True)
            # with row:
            #     st.button('Считать параметры', key='curr_term_read_btn', width='stretch')
            #     st.button('Разблокировать параметры', key='curr_term_open_btn', width='stretch')
            #     st.button('Записать параметры', key='curr_term_set_btn', width='stretch')

    with c2:
        st.write('``Диагностические параметры:``')
        diagnostic_data()

    with c3:
        st.write('``Дашборд:``')
        with st.container(height=700, border=False):
            options = ["Фаза А", "Фаза В", "Фаза С", ]
            selection = st.pills("Фазы:", options, key='verticalbar', selection_mode="multi", default=["Фаза С"])
            
            st.metric(
                "Гармоника 0", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Гармоника 1", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Гармоника 2", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
        )
            st.metric(
                "Гармоника 4", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
        )

    c1, c2, c3 = st.columns([3,1.5,1], gap="small", border=True)
    with c1:
        # st.space('xxsmall')
        row = st.container(horizontal=True)
        with row:
            st.button('Записать ', key='curr_set_btn', width='stretch')
            st.button('Считать', key='curr_read_btn', width='stretch')
            st.button('Считать из резерва', key='curr_read_from_reserv_btn', width='stretch')
            

with mtabs[4]:

    c1, c2, c3 = st.columns([3,1.5,1], gap="small", border=True)

    with c1:
        stab1, stab2 = st.tabs(["Конфигурация", "Коррекция",])

        with stab1:
            # st.write("``Настройка алгоритма обработки данных:``")
            st.write('`Настройка алгоритма DSP`')
            df = pd.DataFrame(
                {
                    "Параметр": [
                        "ФНЧ 16 кГц",
                        "ФНЧ 5 кГц",
                        "ФНЧ 2.5 кГц",
                        "Вычитание пост.сост",
                        "Работа с синхроимпульсом",
                        "Фаз.коррекция усилителя",
                        "Фаз.коррекция SYNC",
                        "Коррекция выбросов",
                        "Коррекция полиномом",
                        "Постоянное напряжение",

                        ],
                    "Фаза А": [False, False, False, False, False, False, True, False, False, False,],
                    "Фаза В": [False, False, False, False, False, False, True, False, False, False,],
                    "Фаза С": [False, False, False, False, False, False, True, False, False, False,],
                },
            )

            st.data_editor(
                df,
                column_config={
                    "Фаза А": st.column_config.CheckboxColumn(),
                    "Фаза В": st.column_config.CheckboxColumn(),
                    "Фаза С": st.column_config.CheckboxColumn(),
                },
                hide_index=True,
                width="stretch",
                height="content"
            )

            st.write('`Настройка алгоритма ARM`')

            df = pd.DataFrame(
                {
                    "Параметр": [
                        "Коррекция по температуре ВМ",
                        "Коррекция по температуре колонны",
                        "Коррекция смещения по напряжению",
                        "Коррекция смещения АЦП",

                        ],
                    "Фаза А": [False, True, False, True,],
                    "Фаза В": [False, True, False, True,],
                    "Фаза С": [False, True, False, True,],
                },
            )

            st.data_editor(
                df,
                column_config={
                    "Фаза А": st.column_config.CheckboxColumn(),
                    "Фаза В": st.column_config.CheckboxColumn(),
                    "Фаза С": st.column_config.CheckboxColumn(),
                },
                hide_index=True,
                width="stretch",
                height="content"
            )

            st.write('`Настройка источника температуры`')

            row = st.container(horizontal=True)
            with row:
                st.selectbox('Фаза А', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'])
                st.selectbox('Фаза В', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'])
                st.selectbox('Фаза С', ['По умолчанию', 'Фаза А','Фаза В','Фаза С'])

            st.space('small')
            # st.write('---')

            row = st.container(horizontal=True)
            with row:
                st.button('Считать параметры', key='volt_read_btn', width='stretch')
                st.button('Записать параметры', key='volt_set_btn', width='stretch')

        with stab2:
            with st.container(height=700, border=False):
                cc1, cc2 = st.columns(2, gap='small', border=True,)
                with cc1:
                    st.write('`Коррекция напряжения:`')
                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Коэф. деления колонны",
                            "Коэф. деления ВМ",
                            "Коэф. коррекции",
                            ],
                        "Фаза А": [1000,13.1951,1],
                        "Фаза В": [1000,13.1951,1],
                        "Фаза С": [1000,13.1951,1],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )
                    st.write('`Полином. коррекция напряжения c делителя`')
                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "U(U) K0",
                            "U(U) K1",
                            "U(U) K2",
                            "U(U) K3",
                            "U(U) K4",
                            ],
                        "Фаза А": [0,1,0,0,0,],
                        "Фаза В": [0,1,0,0,0,],
                        "Фаза С": [0,1,0,0,0,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    st.write('`Линейная коррекция напряжения по Тcol`')
                    
                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "U(Tcol)K(t<T0)",
                            "U(Tcol)K(t>T0)",
                            "U(Tcol)T0",
                            ],
                        "Фаза А": [0,0,20,],
                        "Фаза В": [0,0,20,],
                        "Фаза С": [0,0,20,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    st.write('`Линейная коррекция напряжения по Тvm`')

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "U(Tvm)K(t<T0)",
                            "U(Tvm)K(t>T0)",
                            "U(Tvm)T0",
                            ],
                        "Фаза А": [0,0,20,],
                        "Фаза В": [0,0,20,],
                        "Фаза С": [0,0,20,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )
                    # st.button('Записать параметры', key='volt_params_btn')

                with cc2:

                    st.write('`Смещение АЦП`')

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Смещение U в отсчетах АЦП",
                            "OffsetADC(Tvm)K(t<T0)",
                            "OffsetADC(Tvm)K(t<T0)",
                            "OffsetADC(Tvm)T0"
                            ],
                        "Фаза А": [0,0,0,20],
                        "Фаза В": [0,0,0,20],
                        "Фаза С": [0,0,0,20],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    st.write('`Параметры ЦАПН:`')

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Номинал DAC",
                            "Масштаб DAC",
                            "Фаз. корр. DAC",
                            ],
                        "Фаза А": [0,1,0],
                        "Фаза В": [0,1,0],
                        "Фаза С": [0,1,0],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    # st.button('Записать параметры', key='volt_params_dac_btn')

                    st.write('`Коррекция фазы:`')

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Offset0",
                            "Offset(U)K",
                            "Offset DAC",
                            ],
                        "Фаза А": [7,0,0,],
                        "Фаза В": [7,0,0,],
                        "Фаза С": [7,0,0,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Offset(Tcol)K(t<T0)",
                            "Offset(Tcol)K(t>T0)",
                            "Offset(Tcol)T0",
                            ],
                        "Фаза А": [0,0,20,],
                        "Фаза В": [0,0,20,],
                        "Фаза С": [0,0,20,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

                    df = pd.DataFrame(
                    {
                        "Параметр": [
                            "Offset(Tvm)K(t<T0)",
                            "Offset(Tvm)K(t>T0)",
                            "Offset(Tvm)T0",
                            ],
                        "Фаза А": [0,0,20,],
                        "Фаза В": [0,0,20,],
                        "Фаза С": [0,0,20,],
                    },
                )

                    st.data_editor(
                        df,
                        hide_index=True,
                        width="stretch",
                        height="content"
                    )

            # st.button('Записать параметры', key='volt_params_phase_btn')
            # st.space('xxsmall')
            row = st.container(horizontal=True)
            with row:
                st.button('Считать параметры', key='volt_cor_read_btn', width='stretch')
                st.button('Записать параметры', key='volt_cor_set_btn', width='stretch')


    with c2:
        st.write('``Диагностические параметры:``')

        df = pd.DataFrame(
            {
                "Параметр": [
                    "Статус",
                    "Напряжение",
                    "Частота",
                    "Температура ВМ",
                    "Температура колонны",
                    "Влажность",
                    "Напряжение 27",
                    "Ток 27",
                    "Напряжение 24",
                    "Ток 24",
                    "Счетчик ошибок",
                    "Флаги"
                    ],
                "Фаза А": [0,7154.5443,50.00,37.67,23.87,13.0,27.84,75.00,25.309,19.00,0,16],
                "Фаза В": [0,7154.5443,50.00,37.67,23.87,13.0,27.84,75.00,25.309,19.00,0,16],
                "Фаза С": [0,7154.5443,50.00,37.67,23.87,13.0,27.84,75.00,25.309,19.00,0,16],
            },
        )

        st.data_editor(
            df,
            key='volt_params_general',
            hide_index=True,
            width="stretch",
            height="content"
        )

    with c3:
        st.write('``Дашборд:``')

        with st.container(height=800, border=False):
            options = ["Фаза А", "Фаза В", "Фаза С", ]
            selection = st.pills("Фазы:", options, key='verticalbar_volt', selection_mode="multi", default=["Фаза С"])
            
            st.metric(
                "Статус", round(changes[-1],3), delta, chart_data=data, chart_type="bar", border=True
            )
            st.metric(
                "Напряжение", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Частота", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
            st.metric(
                "Температура ВМ", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )

with mtabs[5]:
    c1, c2, c3 = st.columns([3,1.5,1], gap="small", border=True)

    with c1:
        st.write("`Настроечные параметры:`")

        df = pd.DataFrame(
            {
                "Параметр": [
                    "Усиление опорного канала",
                    "Усиление измерительного канала",
                    "P",
                    "V",
                    "Usource",
                    ],
                "Фаза А": [1,1,1,1,1],
                "Фаза В": [1,1,1,1,1],
                "Фаза С": [1,1,1,1,1],
            },
        )

        st.data_editor(
            df,
            key='termo_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.space('xxsmall')
        row = st.container(horizontal=True)
        with row:
            st.button('Считать параметры', key='termo_params_read_btn', width='stretch')
            st.button('Считать параметры из резерва', key='termo_params_reserv_read_btn', width='stretch')
            st.button('Записать параметры', key='termo_params_set_btn', width='stretch')

        st.write("`Калибровка:`")

        scol1, scol2, scol3 = st.columns(3, border=True)

        with scol1:
            st.number_input('Верхняя точка Фаза А', width='stretch')
            st.button('Калибровать',key='up_phA', width='stretch')
            st.number_input('Нижняя точка Фаза А', width='stretch')
            st.button('Калибровать',key='down_phA', width='stretch')


        with scol2:
            st.number_input('Верхняя точка Фаза В', width='stretch')
            st.button('Калибровать',key='up_phB', width='stretch')
            st.number_input('Нижняя точка Фаза В', width='stretch')
            st.button('Калибровать',key='down_phB', width='stretch')

        with scol3:
            st.number_input('Верхняя точка Фаза С', width='stretch')
            st.button('Калибровать',key='up_phC', width='stretch')
            st.number_input('Нижняя точка Фаза С', width='stretch')
            st.button('Калибровать',key='down_phC', width='stretch')

    with c2:
        st.write("`Диагностические параметры:`")

        st.caption("Общие параметры:")
        df = pd.DataFrame(
            {
                "Параметр": [
                    "Внетренняя температура",
                    "Опора ЦАП0",
                    "Опора ЦАП1",
                    "Опора ЦАП2",
                    "Питание 5 Вольт",
                    ],
                "Фаза А": [38.3741,1.24512,1.24512,1.24512,1.24512],
                "Фаза В": [38.3741,1.24512,1.24512,1.24512,1.24512],
                "Фаза С": [38.3741,1.24512,1.24512,1.24512,1.24512],
            },
        )

        st.data_editor(
            df,
            key='termo_params_general',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.caption("Фазные параметры:")
        df = pd.DataFrame(
            {
                "Параметр": [
                    "Флаги ТК",
                    "ТК",
                    "Напряжение Оп.канала",
                    "Напряжение Изм.канала",
                    ],
                "Фаза А": [0,25.05,2243,1467,],
                "Фаза В": [0,25.05,2243,1467,],
                "Фаза С": [0,25.05,2243,1467,],
            },
        )

        st.data_editor(
            df,
            key='termo_params_phase',
            hide_index=True,
            width="stretch",
            height="content"
        )

    with c3:
        st.write("`Дашборд:`")
        with st.container(height=800, border=False):
            options = ["Фаза А", "Фаза В", "Фаза С", ]
            selection = st.pills("Фазы:", options, key='verticalbar_term', selection_mode="multi", default=["Фаза С"])
            
            st.metric(
                "Напряжение Оп.канала", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Напряжение Изм.канала", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Флаги ТК", round(changes[-1],3), delta, chart_data=data, chart_type="bar", border=True
        )
            st.metric(
                "ТК", round(changes[-1],3), delta, chart_data=data, chart_type="bar", border=True
        )

with mtabs[6]:
    c1, c2, c3 = st.columns([3,1.5,1], gap="small", border=True)

    with c1:
        st.write("`Настройка алгоритма обработки данных:`")
        df1 = pd.DataFrame(
            {
                "Параметр": [
                    "Фазовая коррекция SYNC",
                    "Коррекция выбросов",
                    "Постоянное напряжение",
                    ],
                "Фаза А": [True, False, False,],
                "Фаза В": [True, False, False,],
                "Фаза С": [True, False, False,],
            },
        )

        st.data_editor(
            df1,
            column_config={
                "Фаза А": st.column_config.CheckboxColumn(),
                "Фаза В": st.column_config.CheckboxColumn(),
                "Фаза С": st.column_config.CheckboxColumn(),
            },
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.write("`Настройка параметров:`")
        df = pd.DataFrame(
            {
                "Параметр": [
                    "Коэф.деления InterADC",
                    "Коэф.деления колонны",
                    "Коэф.коррекции",
                    "Смещение нуля",
                    "U(T)K(t>T0)",
                    "U(T)K(t<T0)",
                    "U(T)K(T0)",
                    ],
                "Фаза А": [101,1000,1,0,0,0,20],
                "Фаза В": [101,1000,1,0,0,0,20],
                "Фаза С": [101,1000,1,0,0,0,20],
            },
        )

        st.data_editor(
            df,
            key='volt_adc_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        row = st.container(horizontal=True,)
        with row:
            st.button('Записать параметры', key='volt_adc_write_btn', width='stretch')
            st.button('Считать параметры', key='volt_adc_params_read_btn', width='stretch')
            st.button('Считать параметры из резерва', key='volt_adc_params_reserv_read_btn', width='stretch')
            
    with c2:
        st.write("`Диагностические параметры:`")

        df = pd.DataFrame(
            {
                "Параметр": [
                    "Стартовое состояние",
                    "Напряжение",
                    "Температура",
                    "Статус",
                    "Ошибки",
                    ],
                "Фаза А": [0,942.267,49.3125,1,0],
                "Фаза В": [0,942.267,49.3125,1,0],
                "Фаза С": [0,942.267,49.3125,1,0],
            },
        )

        st.data_editor(
            df,
            key='volt_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

    with c3:
        st.write("`Дашборд:`")
        with st.container(height=800, border=False):
            options = ["Фаза А", "Фаза В", "Фаза С", ]
            selection = st.pills("Фазы:", options, key='verticalbar_volt_adc', selection_mode="multi", default=["Фаза С"])
            
            st.metric(
                "Напряжение", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Температура", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
            )
            st.metric(
                "Статус", round(changes[-1],3), delta, chart_data=data, chart_type="bar", border=True
        )
            st.metric(
                "Ошибки", round(changes[-1],3), delta, chart_data=data, chart_type="bar", border=True
        )

with mtabs[7]:

    cols = st.columns(4, border=True)

    with cols[0]:
        st.write("`Общие параметры:`")
        df = pd.DataFrame(
        {
            "Параметр": [
                # "Номинал Фаза А, [А]",
                # "Номинал Фаза B, [А]",
                # "Номинал Фаза C, [А]",
                "Значение ЦАП0",
                "Значение ЦАП1",
                "Значение ЦАП2",
                "Прямой ток",
                "Обратный ток",
                "Температура ЧЭ",
                "Пользовательский коэф.",
                "Нижний порог измеряемого тока, %",
                "Верхний порог измеряемого тока, %",
                "Гистерезис превышения тока, %"
                ],
            "Значение": [0,0,0,0,0,0,0,0,0,0],
        },
        )

        st.data_editor(
            df,
            key='clem_general_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.write("`Суммирование выходов:`")

        df = pd.DataFrame(
            {
                "Параметр": [
                    "Т1",
                    "Т2",
                    "Т3",
                    "Т4",
                    ],
                "Фаза А": [False, False, False, False,],
                "Фаза В": [False, False, False, False,],
                "Фаза С": [True, True, True, True,],
            },
        )

        st.data_editor(
            df,
            column_config={
                "Фаза А": st.column_config.CheckboxColumn(default=False,),
                "Фаза В": st.column_config.CheckboxColumn(default=False,),
                "Фаза С": st.column_config.CheckboxColumn(default=False,),
            },
            hide_index=True,
            width="stretch",
            height="content"
        )

    with cols[1]:
        st.write("`Токовые выходы:`")
        df = pd.DataFrame(
        {
            "Параметр": [
                "Номинал вых., [А]",
                ],
            "Т1": [0,],
            "Т2": [0,],
            "Т3": [0,],
            "Т4": [0,],
        },
        )

        st.write("`Параметры:`")

        st.data_editor(
            df,
            key='clem_curr_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        df = pd.DataFrame(
        {
            "Параметр": [
                "K0",
                "K1",
                "K2",
                "K3",
                "K4",
                "K5",
                "K6",
                "K7",
                "K8",
                ],
            "Т1": [0,1,0,0,0,0,0,0,0],
            "Т2": [0,1,0,0,0,0,0,0,0],
            "Т3": [0,1,0,0,0,0,0,0,0],
            "Т4": [0,1,0,0,0,0,0,0,0],
        },
        )

        st.write("`Коррекция:`")

        st.data_editor(
            df,
            key='clem_curr_cal',
            hide_index=True,
            width="stretch",
            height="content"
        )

    with cols[2]:
        st.write("`Потенциальные выходы:`")
        st.write("`Параметры:`")
        df = pd.DataFrame(
        {
            "Параметр": [
                "Номинал вых., [А]",
                ],
            "П1": [0,],
        },
        )

        st.data_editor(
            df,
            key='clem_poten_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.write("`Коррекция:`")

        df = pd.DataFrame(
        {
            "Параметр": [
                "K0",
                "K1",
                "K2",
                "K3",
                "K4",
                "K5",
                "K6",
                "K7",
                "K8",
                ],
            "П1": [0,1,0,0,0,0,0,0,0],
        },
        )

        st.data_editor(
            df,
            key='clem_poten_cal',
            hide_index=True,
            width="stretch",
            height="content"
        )

    with cols[3]:
        st.write("`Частотные выходы:`")
        st.write("`Параметры:`")
        df = pd.DataFrame(
        {
            "Параметр": [
                "Номинал вых., [А]",
                "Верхняя частота, [Гц]",
                "Нижняя частота, [Гц]",
                ],
            "Ч1": [0,0,0],
            "Ч2": [0,0,0],
            "Ч3": [0,0,0],
        },
        )

        st.data_editor(
            df,
            key='clem_freq_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.write("`Импульсные выходы:`")
        st.write("`Параметры:`")
        df = pd.DataFrame(
        {
            "Параметр": [
                "Номинал вых., [А]",

                ],
            "И1": [0,],
        },
        )

        st.data_editor(
            df,
            key='clem_impl_set',
            hide_index=True,
            width="stretch",
            height="content"
        )

        st.write("`ModBUS:`")
        # st.write("`Параметры:`")

        # df = pd.DataFrame(
        #     {
        #         "Адрес": ['',],
        #         "Скорость бит/c": ['',],
        #         "Четность": ['',],
        #         "Стоп биты": ['',],
        #     },
        # )

        # st.data_editor(
        #     df,
        #     column_config={
        #         "Адрес": st.column_config.SelectboxColumn(options=[5,10]),
        #         "Скорость бит/c": st.column_config.SelectboxColumn(options=[5,10]),
        #         "Четность": st.column_config.SelectboxColumn(options=[5,10]),
        #         "Стоп биты": st.column_config.SelectboxColumn(options=[5,10]),
        #     },
        #     hide_index=True,
        #     width="stretch",
        #     height="content"
        # )

        scols = st.columns(2)
        with scols[0]:
            st.selectbox('Адрес', [5])
            st.selectbox('Скорость бит/c',[''])
        with scols[1]:
            st.selectbox('Четность',[''])
            st.selectbox('Стоп биты',[''])

    cols = st.columns(4, border=True)
    with cols[0]:
        # st.write('---')
        row = st.container(horizontal=True,)
        with row:
            st.button('Записать', key='clem_general_write_btn', width='stretch')
            st.button('Считать', key='clem_general_params_read_btn', width='stretch')
            st.button('Считать из резерва', key='clem_general_params_reserv_read_btn', width='stretch')
    with cols[1]:
        # st.write('---')
        row = st.container(horizontal=True,)
        with row:
            st.button('Записать', key='clem_curr_write_btn', width='stretch')
            st.button('Считать', key='clem_curr_params_read_btn', width='stretch')
            st.button('Считать из резерва', key='clem_curr_params_reserv_read_btn', width='stretch')
    with cols[2]:
        # st.write('---')
        row = st.container(horizontal=True,)
        with row:
            st.button('Записать', key='clem_ponent_write_btn', width='stretch')
            st.button('Считать', key='clem_ponent_params_read_btn', width='stretch')
            st.button('Считать из резерва', key='clem_ponent_params_reserv_read_btn', width='stretch')
    with cols[3]:
        # st.write('---')
        row = st.container(horizontal=True,)
        with row:
            st.button('Записать', key='clem_4_write_btn', width='stretch')
            st.button('Считать', key='clem_4_params_read_btn', width='stretch')
            st.button('Считать из резерва', key='clem_4_params_reserv_read_btn', width='stretch')

with mtabs[8]:
    cols = st.columns([1,3,1.5], border=True)

    with cols[0]:
        st.write('`Конфигурация:`')
        st.text_input('Путь к каталогу')
        st.text_input('Имя каталога')
        st.selectbox('Период обновления данных:', ['1 сек', '3 сек','5 сек','10 сек',])
        st.write('Время')
        st.write('Ошибки(удалено точек)')

        st.button('Запись', width='stretch')

    with cols[1]:
        st.write('`Настройка параметров для отображения на графике:`')
        row = st.container(horizontal=True, border=True)
        labels = [
            "",
            "Время", 
            "Ток",
            "Гармоника 0",
            "Гармоника 1",
            "Гармоника 2",
            "Гармоника 4",
            "Max. Current",
            "Контраст",
            "Фи",
            "Umod",
            "Max.First Amp",
            "Max. ADC",
            "Uref DAC",
            "Mod U15",
            "Analog U12",
            "Input U12",
            "Tin",
            "Тем. Коррекции",
        ]

        with row:
            st.selectbox('Ось Х', key='recorder_ax', options=labels, width='stretch')
            st.multiselect('Ось Y1', key='recorder_ay1', options=labels, width='stretch')
            st.multiselect('Ось Y2', key='recorder_ay2', options=labels, width='stretch')
            options = ["Фаза А", "Фаза В", "Фаза С",]
            selection = st.segmented_control("Отобразить", options, selection_mode="multi")
        st.space('small')
        with st.container(border=True):
            df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
            st.scatter_chart(df, width='stretch', height=600)

    with cols[2]:
        st.write('``Диагностические параметры:``')
        
        diagnostic_data()

with mtabs[9]:
    options = ["Фаза А", "Фаза В", "Фаза С", ]
    selection = st.pills("Фазы:", options, selection_mode="multi", default=["Фаза С"])

    # st.space(size="small")

    row = st.container(horizontal=True)
    with row:
        st.metric(
            "Ток Raw", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
        )
        st.metric(
            "Ток с ТС", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
        )
        st.metric(
            "Ток с СС", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
    )
        st.metric(
            "Ток усредненый", round(changes[-1],3), delta, chart_data=data, chart_type="area", border=True
    )
    
    row = st.container(horizontal=True)
    with row:
        st.metric(
            "Гармоника 0", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Гармоника 1", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Гармоника 2", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )
        st.metric(
            "Гармоника 4", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )

    row = st.container(horizontal=True)
    with row:
        st.metric(
            "Ток излучателя", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Мощность источника", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Температура излучателя", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )
        st.metric(
            "Внутренняя температура", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )

    row = st.container(horizontal=True)
    with row:
        st.metric(
            "Контраст", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Напряжение модуляции", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Девиация", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )
        st.metric(
            "Макс АЦП", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )

    row = st.container(horizontal=True)
    with row:
        st.metric(
            "Vоп", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Vизм", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )
        st.metric(
            "Температура термометра", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
    )
        st.metric(
            "Температура с коррекцией", round(changes[-1],3), delta, chart_data=data, chart_type="line", border=True
        )

# st.write('---')

