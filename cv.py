import streamlit as st

st.set_page_config(
    page_title="Lopez, Alejandro",
    page_icon="profile_pic.jpg",
    layout="centered"
)

c1, c2 = st.columns([1, 4])
with c1:
    st.image("profile_pic.jpg", width=100)
with c2:
    st.title("Alejandro Lopez Albertos")
    
st.divider()

c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([30,108,30,210,30,85,30,130])
with c1:
    st.image("call.png", width=25)
with c2:
    st.write("+34665346865")
with c3:
    st.image("mail.png", width=25)
with c4:
    st.markdown("alexlopezalbertos@gmail.com")
with c5:
    st.image("linkedin.png", width=25)
with c6:
    st.markdown('[Alejandro](https://www.linkedin.com/in/alejandro-l%C3%B3pez-albertos-090a08206/)', unsafe_allow_html=True)
with c7:
    st.image("location.png", width=25)
with c8:
    st.markdown("Brussels, Belgium")

st.divider()

st.subheader("SKILLS", divider="blue")
st.markdown("**Languages:** Spanish (native), English (C2), French (B1), Catalan/Valenciano (B2).")
st.markdown("**Programming:** Python, CSS, Java, Swift, DAX.")
st.markdown("**Frameworks/Libraries:** Pandas, scikit-learn,Matplotlib, NumPy.")
st.markdown("**Software:** Microsoft Office, PowerBI, Xcode, autoCAD, Inventor Professional.")
st.markdown("**Soft Skills:** Project Managing, Conflict resolution, Critical thinking.")

st.write("")
st.subheader("EXPERIENCE", divider="blue")

c1,c2 = st.columns([1,16.5])
with c1:
    st.image("pg.png", width=30)
with c2:
    st.markdown("**Procter & Gamble**")

c0, c1,c2 = st.columns([0.83,10,2.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**Packaging & Making Manager**")
with c2:
    st.markdown("Jan 2024 - Present")

c0, c1 = st.columns([0.83, 12.6])
with c0:
        st.markdown("")
with c1:
    st.markdown("Technical Project Manager at Procter & Gamble’s Brussels Innovation Center, I oversee the development and implementation of packaging and liquid manufacturing lines for external production facilities which make P&G products at external plants.")

c0, c1,c2 = st.columns([0.83,9.6,2.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**MPD Engineer Internship**")
with c2:
    st.markdown("Jul 2023 - Dec 2023")

c0, c1 = st.columns([0.83, 12.6])
with c0:
        st.markdown("")
with c1:
    st.markdown("Development and implementarion of a Python + Power Bi tool that calculates the department’s Supply Chain Resilience via Machine Learning and other data processing models.")
    st.markdown("Implementation of Sustainable Solutions to align with European Comission packaging waste regulations. Directly worked on: resizing of products, increase of fill levels and changing packaging materials to recyclable alternatives.")

st.write("")
c1,c2 = st.columns([1,16.5])
with c1:
    st.image("ford.jfif", width=30)
with c2:
    st.markdown("**Ford**")

c0, c1,c2 = st.columns([0.83,9.3,2.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**Body Exterior Engineer**")
with c2:
    st.markdown("Feb 2023 - Jun 2023")

c0, c1 = st.columns([0.83, 12.6])
with c0:
        st.markdown("")
with c1:
    st.markdown("PVT (Plant Vehicle Team). Find and implement engineering solutions to manufacturing and warranty issues related to Ford Kuga at Ford Valencia plant.")

st.write("")
st.subheader("EDUCATION", divider="blue")

st.write("")
c1,c2 = st.columns([1,16.5])
with c1:
    st.image("upv.jfif", width=30)
with c2:
    st.markdown("**Universitat Politècnica de València (UPV)**")

c0, c1,c2 = st.columns([0.83,10.3,1.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**Master's Degree in Industrial Engineering**")
with c2:
    st.markdown("2021 - 2023")

c0, c1 = st.columns([0.83, 12.6])
with c0:
        st.markdown("")
with c1:
    st.markdown("Specialization in Industrial Organization and Management")

c0, c1,c2 = st.columns([0.83,10.3,1.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**Bachelor's Degree in Industrial Engineering**")
with c2:
    st.markdown("2015 - 2020")

    st.write("")
c1,c2 = st.columns([1,16.5])
with c1:
    st.image("cambridge.jfif", width=30)
with c2:
    st.markdown("**Cambridge House Community College**")

c0, c1,c2 = st.columns([0.83,10.3,1.6])
with c0:
    st.markdown("")
with c1:
    st.markdown("**Primary and Secondary School**")
with c2:
    st.markdown("2000 - 2015")

c0, c1 = st.columns([0.83, 12.6])
with c0:
        st.markdown("")
with c1:
    st.markdown("Bilingual education program, enhancing students' language proficiency")


st.divider()

