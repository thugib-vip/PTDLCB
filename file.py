import streamlit as st
st.header('ja')
import streamlit as st

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit đầu tiên của bạn")

# Nhập dữ liệu
number = st.number_input("Nhập một số:")
st.write("Số bạn nhập là:", number)

# Thực hiện tính toán
square = number ** 2
st.write("Bình phương của số này là:", square)
