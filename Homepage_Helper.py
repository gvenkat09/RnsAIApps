import streamlit
from PIL import Image
from app_utils import switch_page
from streamlit_option_menu import option_menu




def load_sidebar(st, authenticator):

    with st.sidebar:

        st.markdown(f'# Welcome *{st.session_state["name"]}*')

        selected = option_menu("RNS Apps", ["Mock Interview", 'Todo List'],
                               icons=['test', 'list'], default_index=0)

        st.markdown('## RNS Apps - V1.0.0')
        st.markdown(""" 
            #### Let's contact: [Venkat](https://www.linkedin.com/in/gvenkat09/)

            #### Please fill the form, we'd love to have your feedback: [Feedback Form]()

            #### Powered by -  [Rise n Shine](https://risenshinetechnologies.com)

                        """)
        st.markdown("""\n""")
        authenticator.logout('Logout', 'sidebar', key='unique_key')

    if selected == "Mock Interview":
        st.info("This is Mock Interview Section")
        load_mock_interview_simulator(st, authenticator)
    elif selected == 'Todo List':
        st.info("This is Todo list")
    else:
        st.info("Other Section")

    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )


def load_mock_interview_simulator(st, authenticator):

    im = Image.open("icon_old.png")
    st.image(im, width=50)
    st.markdown(f"""# RNS - Mock Interview Simulator <span style=color:#2E9BF5><font size=5>Beta</font></span>""",
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
            st.switch_page("Professional Screen")
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
            switch_page("Resume Screen")
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
            switch_page("Behavioral Screen")