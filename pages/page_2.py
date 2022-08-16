import streamlit as st

 #リロードの停止
with st.form(key='profile_form'):

            #テキストボックス
            name = st.text_input('名前')
            address = st.text_input('住所')
            #セレクトボックス
            #age_category = st.selectbox('年齢層',('子ども（１８才未満）','大人(18才以上)'))
            #ラジオボタン
            age_category = st.radio('年齢層',('子ども（１８才未満）','大人(18才以上)'))
            #マルチセレクト
            hobby = st.multiselect('趣味',('スポーツ','読書','プログラミング','アニメ映画','釣り','料理'))
            #ボタン
            submit_btn = st.form_submit_button('送信')
            cancel_btn = st.form_submit_button('キャンセル')
            print(f'sunbmit_btn: {submit_btn}')
            print(f'cancel_btn: {cancel_btn}')
            #応用
            if submit_btn:
                        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
                        st.text(f'年齢層{age_category}')
                        st.text(f'趣味:{",".join(hobby)}')