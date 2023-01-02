import streamlit as st
import datetime

with st.form(key='profile_form'):

    # テキストボックス
    name = st.text_input('名前')
    addres = st.text_input('住所')

    # セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ("大人", "子供")
    )

    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('写真', '自転車', 'プログラミング', '英語', '読書', '映画鑑賞', '旅行')
    )

    # ラジオボタン
    age_category = st.radio(
        '年齢層',
        ("大人", "子供")
    )

    # 日付
    start_date = st.date_input(
        '開始日',
        datetime.date(2023, 1, 1)
    )

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ、{name}さん! {addres}に書籍をおくりました')
        st.text(f'年齢層:{age_category}')
        st.text(f'趣味:{",".join(hobby)}')
