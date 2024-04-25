import streamlit as st
import pandas as pd
from datetime import datetime
from st_pages import hide_pages

# Custom CSS to inject into the Streamlit page
hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {
                padding-top: 0rem;
            }
            .reportview-container .main .block-container{
                padding-top: 0rem;
            }
        </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


hide_pages(['Behavioral Interview'])
hide_pages(['Professional Interview'])
hide_pages(['Resume Interview'])
hide_pages(['ToDo List'])

# Initialize or load tasks from a user-specific CSV file for persistence
def load_tasks(username):
    try:
        return pd.read_csv(f'{username}_tasks.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['ID', 'Title', 'Description', 'Due Date', 'Due Time', 'Completed', 'Priority'])


# Save tasks to a user-specific CSV file for persistence
def save_tasks(username):
    st.session_state['tasks'].to_csv(f'{username}_tasks.csv', index=False)


# Function to add or update a task
def save_task(task_id, title, description, due_date, due_time, priority):
    # Ensure st.session_state['tasks'] is a DataFrame
    assert isinstance(st.session_state['tasks'], pd.DataFrame), "tasks is not a DataFrame"

    if task_id == -1:  # Add new task
        new_id = max(st.session_state['tasks']['ID'].max() + 1, 1) if not st.session_state['tasks'].empty else 1
        new_task = {'ID': new_id, 'Title': title, 'Description': description,
                    'Due Date': due_date, 'Due Time': due_time,
                    'Completed': False, 'Priority': priority}
        # Properly use append and assign the result
        st.session_state['tasks'] = st.session_state['tasks']._append(new_task, ignore_index=True)
    else:  # Update existing task
        task_index = st.session_state['tasks'].index[st.session_state['tasks']['ID'] == task_id].tolist()[0]
        st.session_state['tasks'].at[task_index, 'Title'] = title
        st.session_state['tasks'].at[task_index, 'Description'] = description
        st.session_state['tasks'].at[task_index, 'Due Date'] = due_date
        st.session_state['tasks'].at[task_index, 'Due Time'] = due_time
        st.session_state['tasks'].at[task_index, 'Priority'] = priority

    save_tasks(st.session_state['user'])


# Function to delete a task
def delete_task(task_id):
    st.session_state['tasks'] = st.session_state['tasks'][st.session_state['tasks']['ID'] != task_id]
    save_tasks(st.session_state['user'])


# Main application interface
def main_app():
    st.title(f"{st.session_state['user']}'s To-Do List Tasks")

    st.session_state['tasks'] = load_tasks(st.session_state['user'])
    # st.experimental_rerun()

    # Task input and edit form
    task_id = st.sidebar.selectbox('Select a task to edit', options=[-1] + st.session_state['tasks']['ID'].tolist(),
                                   format_func=lambda x: 'New Task' if x == -1 else f'Task {x}')
    if task_id != -1:
        task_data = st.session_state['tasks'][st.session_state['tasks']['ID'] == task_id].iloc[0]
        title = st.sidebar.text_input('Task Title', value=task_data['Title'])
        description = st.sidebar.text_area('Task Description', value=task_data['Description'])
        due_date = st.sidebar.date_input('Due Date', value=pd.to_datetime(task_data['Due Date']))
        due_time = st.sidebar.time_input('Due Time', value=pd.to_datetime(task_data['Due Time']).time())
        priority = st.sidebar.select_slider('Priority', options=['Low', 'Medium', 'High'], value=task_data['Priority'])
    else:
        title = st.sidebar.text_input('Task Title')
        description = st.sidebar.text_area('Task Description')
        due_date = st.sidebar.date_input('Due Date')
        due_time = st.sidebar.time_input('Due Time')
        priority = st.sidebar.select_slider('Priority', options=['Low', 'Medium', 'High'])

    if st.sidebar.button('Save Task'):
        save_task(task_id, title, description, due_date, due_time, priority)

    # Display tasks in a table with filter options
    st.write('Tasks:')
    filter_status = st.radio('Filter tasks by status', ('All', 'Completed', 'Incomplete'), horizontal=True)
    if filter_status == 'Completed':
        filtered_tasks = st.session_state['tasks'][st.session_state['tasks']['Completed']]
    elif filter_status == 'Incomplete':
        filtered_tasks = st.session_state['tasks'][~st.session_state['tasks']['Completed']]
    else:
        filtered_tasks = st.session_state['tasks']
    st.table(filtered_tasks)

    # Task interaction: completion and deletion
    for index, task in filtered_tasks.iterrows():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.checkbox(f"Completed Task - {task['Title']}", value=task['Completed'], key=f"completed_{task['ID']}"):
                st.session_state['tasks'].loc[st.session_state['tasks']['ID'] == task['ID'], 'Completed'] = True
                save_tasks(st.session_state['user'])
            else:
                st.session_state['tasks'].loc[st.session_state['tasks']['ID'] == task['ID'], 'Completed'] = False
                save_tasks(st.session_state['user'])
        with col2:
            if st.button(f"Delete Task - {task['Title']}", key=f"delete_{task['ID']}"):
                delete_task(task['ID'])


if st.session_state["authentication_status"]:
    main_app()

