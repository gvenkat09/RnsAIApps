
# Password reset widget
# if authentication_status:
#     try:
#         if authenticator.reset_password(username, fields='Reset password'):
#             with open('config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)

# Register new user
# try:
#     if authenticator.register_user(preauthorization=False, fields={'Form name': 'Register User', 'Email': 'Email', 'Username': 'Username', 'Password': 'Password', 'Repeat password': 'Repeat password', 'Register': 'Register'}):
#         with open('config.yaml', 'w') as file:
#             yaml.dump(config, file, default_flow_style=False)
#         st.success('User registered successfully')
# except Exception as e:
#     st.error(e)

# Forgot password widget
# try:
#     username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password(
#         fields={'Form name': 'Forgot password', 'Username': 'Username', 'Submit': 'Submit'})
#     if username_of_forgotten_password:
#         st.success('New password sent securely')
#         # Random password to be transferred to user securely
#     else:
#         st.error('Username not found')
# except Exception as e:
#     st.error(e)

# Forgot username
# try:
#     username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username(
#         'Forgot username')
#     if username_of_forgotten_username:
#         st.success('Username sent securely')
#         # Username to be transferred to user securely
#     else:
#         st.error('Email not found')
# except Exception as e:
#     st.error(e)

# Update user details
# if authentication_status:
#     try:
#         if authenticator.update_user_details(username, 'Update user details'):
#             with open('config.yaml', 'w') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#             st.success('Entries updated successfully')
#     except Exception as e:
#         st.error(e)

# Hash passwords and store them in the YAML file. Only do this once
# hasehd_pwd = stauth.Hasher(['123', '12345']).generate()
#
# st.write(hasehd_pwd)