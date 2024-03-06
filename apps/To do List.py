import streamlit as st
import pandas as pd


# Function to load tasks or initialize an empty dataframe if no tasks are saved
def load_tasks(user):
    try:
        tasks = pd.read_csv(f'{user}_tasks.csv')
        # Ensure the 'Completed' column exists
        if 'Completed' not in tasks.columns:
            tasks['Completed'] = False  # Add 'Completed' column with default value False
    except FileNotFoundError:
        tasks = pd.DataFrame(columns=['Task', 'Completed'])
    return tasks


# Function to save tasks to a CSV file
def save_tasks(tasks, user):
    tasks.to_csv(f'{user}_tasks.csv', index=False)


# Load existing tasks for the authenticated user
tasks_df = load_tasks(st.session_state['user'])

# Streamlit application layout
st.title(f"{st.session_state['user']}'s To-Do List App")

# Input form to add a new task
with st.form(key='task_form'):
    new_task = st.text_input(label='Enter a new task')
    submit_button = st.form_submit_button(label='Add Task')

    # Add the new task to the dataframe and save if the submit button is pressed
if submit_button and new_task:
    new_task_row = pd.DataFrame({'Task': [new_task], 'Completed': [False]})
    tasks_df = pd.concat([tasks_df, new_task_row], ignore_index=True)
    save_tasks(tasks_df, st.session_state['user'])

# Display the tasks in a list with checkboxes to mark them as completed
st.subheader('Your Tasks:')
if not tasks_df.empty:
    for index, row in tasks_df.iterrows():
        completed = st.checkbox(f"{row['Task']}", key=index, value=row['Completed'])
        if completed != row['Completed']:  # Check if the status has changed
            tasks_df.at[index, 'Completed'] = completed
            save_tasks(tasks_df, st.session_state['user'])

        # Logout button
    if st.button('Logout'):
        st.session_state['authenticated'] = False
        st.experimental_rerun()

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
