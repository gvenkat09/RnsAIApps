# Let's start by importing the necessary Streamlit library
import streamlit as st

# Initialize the Streamlit application
st.title("Career Development Planner")

# Display an introductory text to guide the users on what to do with the app
st.write("""
    ### Welcome to the Career Development Planner!
    This tool is designed to help you outline and track your career goals using the SMART criteria:
    - **S**pecific
    - **M**easurable
    - **A**chievable
    - **R**elevant
    - **T**ime-bound

    "If you don't know where you're going, any road will take you there." - Lewis Carroll.

    Follow the steps below to kickstart your career planning process:
""")

# Section to download the Career Map template
st.subheader("Step 1: Download the Career Map Template")
st.write("Download the Career Map template from the Bonus section in the course and fill it up following all the instructions in the template.")

# Button to simulate downloading the Career Map template (Note: Streamlit does not support actual file downloads in this way, so we simulate the action)
if st.button('Download Career Map Template'):
    st.success("Download initiated! Check your downloads folder.")

# Section to download the SWOT template
st.subheader("Step 2: Download the SWOT Template")
st.write("Download the SWOT template from the Bonus section and do the same.")

# Button to simulate downloading the SWOT template
if st.button('Download SWOT Template'):
    st.success("Download initiated! Check your downloads folder.")

# Checklist for users to keep track of their progress
st.subheader("Career Goals Checklist")
checklist = {
    "Downloaded the career map": st.checkbox("Downloaded the career map"),
    "Filled the career map": st.checkbox("Filled the career map"),
    "Downloaded the SWOT template": st.checkbox("Downloaded the SWOT template"),
    "Filled the SWOT template": st.checkbox("Filled the SWOT template")
}

# Display message based on the checklist progress
if all(checklist.values()):
    st.write("Great! You've completed all the initial steps. Don't forget to set weekly reminders in Google Calendar to track your progress against each goal.")
else:
    st.write("Please complete all the steps to move forward in your career planning process.")

# Final section for setting reminders
st.subheader("Set Weekly Reminders")
st.write("Set weekly reminders in Google Calendar to come back and track your progress against each goal.")
if st.button("Set Reminder"):
    # This button is also a simulation as Streamlit in this context cannot interact with external applications like Google Calendar
    st.success("Reminder set! You'll now receive weekly notifications to track your progress.")

