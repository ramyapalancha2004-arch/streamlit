import streamlit as st
st.title("Students Details")
if "users" not in st.session_state:
    st.session_state.users=[]
form1=st.form("fill",clear_on_submit=True)
with form1:
    Firstname=st.text_input("Enter FirstName")
    Lastname=st.text_input("Enter LastName")
    Email=st.text_input("Enter Email")
    Phno=st.text_input("Enter PhoneNo")
    form1_submit=form1.form_submit_button("submit")
if form1_submit:
    # b={
    #     "first":Firstname,
    #     "last":Lastname,
    #     "email":Email
    # } 
    if not Firstname or not Lastname or not Email or not Phno:
        st.write("please fill all the fields before submitting")
    else:
        b={
        "first":Firstname,
        "last":Lastname,
        "email":Email,
        "phno":Phno
    }     
        if b: 
            if st.session_state.users:
                ex=False
                for i in st.session_state.users:
                    if i["last"]==b["last"] :
                        ex=True
                        break;
                if ex:
                    st.write("username is already present please use other name") 
                    
                else:
                    st.session_state.users.append(b)
                    st.write("successfully registerd") 
            else:
                st.session_state.users.append(b)  
                st.write("successfully registerd")     
if len(st.session_state.users)>0:
    st.table(st.session_state.users)