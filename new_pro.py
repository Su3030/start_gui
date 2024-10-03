import streamlit as st

# List of available devices
devices = [
    "FT232H 0x68",
    "FT232H 0x69",
    "FT232H 0x70",
    "FT232H 0x71"
]

def main():
    st.title("My Streamlit App")

    # Add a button for creating a new project
    if st.button("Add New Project"):
        add_new_project()

def add_new_project():
    st.subheader("Create a New Project")

    # Dropdown for device selection
    selected_device = st.selectbox("Please select a device:", devices)

    # Form for project details
    with st.form("new_project_form"):
        project_name = st.text_input("Project Name")
        project_description = st.text_area("Project Description")
        submit_button = st.form_submit_button("Create Project")

        if submit_button:
            # Handle project creation logic here
            st.success(f"Project '{project_name}' created successfully with device '{selected_device}'!")

if __name__ == "__main__":
    main()
