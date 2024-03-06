from app_utils import switch_page
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from PIL import Image
from st_pages import Page, show_pages, hide_pages
from streamlit_option_menu import option_menu

im = Image.open("icon.png")
st.set_page_config(page_title="RNS AI Apps", layout="centered", page_icon=im, initial_sidebar_state="collapsed")

# Open YAML file

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.sidebar.empty()

# Create authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Render the login widget
name, authentication_status, username = authenticator.login('main',
                                                            fields={'Form name': 'Login', 'Username': 'Username',
                                                                    'Password': 'Password', 'Login': 'Login'})

show_pages([
    Page("Homepage.py", "Home Page"),
    Page("apps\\Behavioral Screen.py", "Behavioral Interview"),
    Page("apps\\Professional Screen.py", "Professional Interview"),
    Page("apps\\Resume Screen.py", "Resume Interview")
])

hide_pages(['Behavioral Interview'])
hide_pages(['Professional Interview'])
hide_pages(['Resume Interview'])


def load_sidebar():

    with st.sidebar:

        st.markdown(f'# Welcome *{st.session_state["name"]}*')

        selected = option_menu(None, ["Interview Simulator", 'Todo List'],
                               icons=['test', 'list'], default_index=0)

        st.markdown('## RNS Apps - V1.0.0')
        st.markdown(""" 
            #### Let's contact: [Venkat](https://www.linkedin.com/in/gvenkat09/)

            #### Please fill the form, we'd love to have your feedback: [Feedback Form]()

            #### Powered by -  [Rise n Shine](https://risenshinetechnologies.com)

                        """)
        st.markdown("""\n""")
        authenticator.logout('Logout', 'sidebar', key='unique_key')

    if selected == "Interview Simulator":
        load_mock_interview_simulator()
    elif selected == 'Todo List':
        st.info("This is Todo list")
    else:
        st.info("Other Section")

    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )


def load_mock_interview_simulator():

    im = Image.open("icon.png")
    st.image(im, width=50)
    st.markdown(f"""## 🏆 RNS - Mock Interview Simulator <span style=color:#2E9BF5><font size=5>Beta</font></span>""",
                unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown(
        "Welcome to RNS AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by Rise n Shine that conducts mock interviews. "
        "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions!")
    st.markdown("""\n""")
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")

    selected = option_menu(
        menu_title=None,
        options=["Professional", "Resume", "Behavioral"],
        icons=["cast", "cloud-upload", "cast"],
        default_index=0,
        orientation="horizontal",
    )
    if selected == 'Professional':
        st.info("""
                    📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
                    Note: The maximum length of your answer is 4097 tokens!
                    - Each Interview will take 10 to 15 mins.
                    - To start a new session, just refresh the page.
                    - Choose your favorite interaction style (chat)
                    - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Interview")
    if selected == 'Resume':
        st.info("""
                📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
                Note: The maximum length of your answer is 4097 tokens!
                - Each Interview will take 10 to 15 mins.
                - To start a new session, just refresh the page.
                - Choose your favorite interaction style (chat)
                - Start introduce yourself and enjoy！ """
                )
        if st.button("Start Interview!"):
            switch_page("Resume Interview")
    if selected == 'Behavioral':
        st.info("""
                📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
                Note: The maximum length of your answer is 4097 tokens!
                - Each Interview will take 10 to 15 mins.
                - To start a new session, just refresh the page.
                - Choose your favorite interaction style (chat)
                - Start introduce yourself and enjoy！ 
                """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Interview")

if __name__ == "__main__":
    # Authenticate users
    if st.session_state["authentication_status"]:

        home_title = "RNS Apps"
        home_introduction = "Welcome to RNS AI Interviewer, empowering your interview preparation with Simulator."
        load_sidebar()
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
        # st.sidebar.write("Please log in to see more options.")
    elif st.session_state["authentication_status"] is None:
        # st.sidebar.write("Please log in to see more options.")
        st.warning('Please enter your username and password')


