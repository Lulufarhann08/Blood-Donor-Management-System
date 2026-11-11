import streamlit as st
from DonorView import BloodDonorManager


donor_instance = BloodDonorManager()

tab1, tab2 ,tab3, tab4  = st.tabs(["Add Donor", "View Donors", "Update Donor", "Delete Donor"])


blood_groups = ["A+", "A-","B+","B-","AB+","AB-","O+","O-"]

        

with tab1:
    st.header("Add New Donor....!")
    name = st.text_input("Enter Donor Name")
    blood_group = st.selectbox("Select Blood Group", blood_groups)
    phone = st.text_input("Enter Donor Phone Number")
    city = st.text_input("Enter Donor City")
    last_donation = st.date_input("Enter Last Donation Date")
    if st.button("Submit"):
        donor_instance.post(name = name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor added successfully...!")


with tab2:
    st.header("View Blood donor Details...!")
    records = donor_instance.get()
    print(records)
    if records:
        st.table(records)
    else:
        st.warning("No records found...!")
        
        
       
with tab3:
    st.title("Update Donor Details...!")
    records = donor_instance.get()
   
    if records:
        donor_ids = [r[0] for r in records]
        # ids = [1,3,5,6]
        id = st.selectbox("Select Donor ID to Update", donor_ids, key="update_id")
    
        record = donor_instance.get_object(id=id)
        # record = 1, anu,O+,74725,kochi,2026-29-4
        name = st.text_input("Enter Donor Name :", value=record[1])
        phone = st.text_input("Enter Donor Phone Number", value =record[3])
        blood_group = st.selectbox("Select Blood Group",
                                   blood_groups,
                                   index= blood_groups.index(record[2]),
                                   key="update_group")
        city = st.text_input("Enter Donor City", value = record[4])
        last_donation = st.date_input("Enter Last Donation Date", value=record[5])
      
    if st.button("Update"):
        status, message = donor_instance.put(id=id,
                                            name=name,
                                            blood_group=blood_group,
                                            phone=phone,
                                            city=city,
                                            last_donation=last_donation)
        if status:
            st.success(message)
        else:
            st.error(message)
    else:
        st.warning("No Donor Found.....!")

with tab4:
    st.title("Delete Donor")
    records = donor_instance.get()

    if records:
        donor_ids = [record[0] for record in records]

        id = st.selectbox("Select Donor ID to Delete",donor_ids)

        if st.button("Delete Donor"):
            status, message = donor_instance.delete(id=id)

            if status:
                st.success(message)
                st.rerun()
            else:
                st.error(message)

    else:
        st.warning("No donor available to delete.")