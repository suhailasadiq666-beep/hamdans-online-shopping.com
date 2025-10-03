import streamlit as st
import time as tm




st.set_page_config(page_title="Hamdans online shop", page_icon = "icon.jpg")

placeholder = st.empty()
content_placeholder = st.empty()

if "clear_content" not in st.session_state:
    st.session_state.clear_content = False

if not st.session_state.clear_content:
    st.title("Hamdans online shop")
    st.markdown("---")



def clearall():
    st.session_state.clear_content = True
    if "clear_content2" not in st.session_state:
        st.session_state.clear_content2 = False
    if not st.session_state.clear_content2:
        st.markdown("### Do you want to buy this item?")
        st.button("Yes", key="yes", on_click = clearall2)

def clearall2():
    st.session_state.clear_content2 = True
    st.image("loading.jpg", width = 400, caption = "processing order...")
    tm.sleep(5)
    placeholder.empty()
    st.image("bought.jpg", width=400, caption="Order placed successfully!")
    



if not st.session_state.clear_content:
    st.image("akbar story.jpg", width=150) 
    st.markdown("### Akbar And Birbal Story Book")  
    st.markdown("### ₹200")
    st.button("Buy Now", key="book",on_click = clearall)
    st.markdown("---")



if not st.session_state.clear_content:
    st.image("bar magnet.jpeg", width=150)
    st.markdown("### Bar Magnet")
    st.markdown("### ₹150")
    st.button("Buy Now", key="bar_magnet",on_click = clearall)
    st.markdown("---")


if not st.session_state.clear_content:
    st.image("counter.jpeg", width=170) 
    st.markdown("###  4 Counters")
    st.markdown("### ₹240")
    st.button("Buy Now", key="counters",on_click = clearall)
    st.markdown("---")


if not st.session_state.clear_content:
    st.image("bata bag.jpeg", width=250)
    st.markdown("### Bata Bag")
    st.markdown("### ₹2250")
    st.button("Buy Now", key="bag",on_click = clearall)
    st.markdown("---")


if not st.session_state.clear_content:
    st.image("hotwheels.jpeg", width=200) 
    st.markdown("### Hot Wheels Cars. set of 25")
    st.markdown("### ₹200")
    st.button("Buy Now", key="hotwheels",on_click = clearall)
    st.markdown("---")


if not st.session_state.clear_content:
    st.image("shoes.jpg", width=200)
    st.markdown("### Shoes")
    st.markdown("### ₹2050")
    st.button("Buy Now", key="shoes",on_click = clearall)
    st.markdown("---")


if not st.session_state.clear_content:
    st.image("toy nerf.jpeg", width=200)
    st.markdown("### Toy Nerf Gun. pack of 50 darts")
    st.markdown("### ₹1550")
    st.button("Buy Now", key="toy_nerf",on_click = clearall)
    st.markdown("---")

if not st.session_state.clear_content:
    st.image("bedsheet.jpg", width=200)
    st.markdown("### Bedsheet")
    st.markdown("### ₹850")
    st.button("Buy Now", key="bedsheet",on_click = clearall)
    st.markdown("---")















