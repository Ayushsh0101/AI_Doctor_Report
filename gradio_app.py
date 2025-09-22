
# import gradio as gr
# from dotenv import load_dotenv
# import os
# import time
# from brain_of_the_doctor import encode_image, analyze_image_with_query
# from voice_of_the_patient import transcribe_with_groq
# from voice_of_the_doctor import text_to_speech_with_elevenlabs
# from authentication import register_user, login_user

# # Load env
# load_dotenv()

# # Global session
# user_session = {"username": None}

# system_prompt = """You have to act as a professional doctor..."""

# # ================= CORE DOCTOR LOGIC ================= #
# def process_inputs(audio_filepath, image_filepath):
#     if not user_session["username"]:
#         return "⚠️ Please login first!", "", None

#     speech_to_text_output = transcribe_with_groq(audio_filepath, "whisper-large-v3")

#     if image_filepath:
#         doctor_response = analyze_image_with_query(
#             query=system_prompt + speech_to_text_output,
#             encoded_image=encode_image(image_filepath),
#             model="meta-llama/llama-4-scout-17b-16e-instruct"
#         )
#     else:
#         doctor_response = "No image provided"

#     output_filename = f"doctor_voice_{int(time.time())}.mp3"
#     voice_of_doctor = text_to_speech_with_elevenlabs(
#         doctor_response, output_filename, "21m00Tcm4TlvDq8ikWAM"
#     )
#     return speech_to_text_output, doctor_response, voice_of_doctor


# # ================= AUTH HANDLERS ================= #
# def handle_register(username, email, phone, password):
#     if not username or not email or not phone or not password:
#         return "⚠️ All fields are required!", username, email, phone, password

#     msg = register_user(username, email, phone, password)
#     return msg, "", "", "", ""  # clear fields on success


# def handle_login(username, password):
#     if not username or not password:
#         return (
#             gr.update(visible=True),
#             gr.update(visible=False),
#             "",
#             "⚠️ Username and Password required!",
#             username, password
#         )

#     success, msg = login_user(username, password)
#     if success:
#         user_session["username"] = username
#         return (
#             gr.update(visible=False),
#             gr.update(visible=True),
#             f"<h2 id='welcome_text'>Welcome {username}!</h2>",
#             "",
#             "", ""
#         )
#     return (
#         gr.update(visible=True),
#         gr.update(visible=False),
#         "",
#         msg,
#         username, ""
#     )


# def handle_logout():
#     user_session["username"] = None
#     return (
#         gr.update(visible=True),
#         gr.update(visible=False),
#         "",
#         "",
#         "", ""
#     )


# def handle_forgot(username):
#     if not username:
#         return "⚠️ Please enter your username to reset password!"
#     return f"🔑 Password reset link sent to registered email/phone for {username} (demo)."


# # ================= GRADIO UI ================= #
# with gr.Blocks(
#     css="""
    
#     #welcome_text {
#         text-align: center;
#         font-size: 28px;
#         font-weight: bold;
#         margin: 10px 0;
#     }
#     #header_bar {
#         align-items: center;
#         justify-content: space-between;
#         background-color: #f8f9fa;
#         padding: 8px 15px;
#         border-radius: 6px;
#         margin-bottom: 10px;
#     }
#     #logout_col {
#         text-align: right;
#     }
#     button {
#         font-size: 16px !important;
#     }
#     """,
#     title="AI Doctor with Login"
# ) as demo:
#     ...


#     # ---------------- Authentication Forms ----------------
#     with gr.Group(visible=True) as auth_forms:
#         with gr.Tabs():
#             # Register
#             with gr.TabItem("📝 Register"):
#                 gr.Markdown("## Create Account")
#                 reg_username = gr.Textbox(label="Username")
#                 reg_email = gr.Textbox(label="Email")
#                 reg_phone = gr.Textbox(label="Phone")
#                 reg_password = gr.Textbox(label="Password", type="password")
#                 register_btn = gr.Button("Register")
#                 register_output = gr.Textbox(label="Register Status", interactive=False)
#                 register_btn.click(
#                     handle_register,
#                     [reg_username, reg_email, reg_phone, reg_password],
#                     [register_output, reg_username, reg_email, reg_phone, reg_password]
#                 )

#             # Login
#             with gr.TabItem("🔑 Login"):
#                 gr.Markdown("## Login")
#                 login_username = gr.Textbox(label="Username")
#                 login_password = gr.Textbox(label="Password", type="password")
#                 login_btn = gr.Button("Login")
#                 forgot_btn = gr.Button("Forgot Password")
#                 login_output = gr.Textbox(label="Login Status", interactive=False)
#                 forgot_btn.click(handle_forgot, [login_username], login_output)

#     # ---------------- Doctor Panel ----------------
#     # ---------------- Doctor Panel ----------------
#     with gr.Group(visible=False) as doctor_panel:
#         # Top header with Welcome + Logout
#         with gr.Row(elem_id="header_bar"):
#             with gr.Column(scale=3):
#                 welcome_text = gr.HTML("")  # dynamic welcome text
#             with gr.Column(scale=1, elem_id="logout_col"):
#                 logout_btn = gr.Button("Logout")

#         # Proper doctor panel heading
#         gr.HTML("<h3 style='text-align:left; margin-top:20px;'>🩺 Doctor Panel</h3>")

#         audio_in = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Speak here")
#         image_in = gr.Image(type="filepath", label="🖼️ Upload medical image")
#         text_out = gr.Textbox(label="Speech to Text")
#         doctor_out = gr.Textbox(label="Doctor's Response")
#         audio_out = gr.Audio(label="Doctor's Voice")
#         submit_btn = gr.Button("Ask Doctor")

#         submit_btn.click(
#             process_inputs,
#             [audio_in, image_in],
#             [text_out, doctor_out, audio_out]
#         )


#     # ---------------- Button Actions ----------------
#     login_btn.click(
#         handle_login,
#         [login_username, login_password],
#         [auth_forms, doctor_panel, welcome_text, login_output, login_username, login_password]
#     )

#     logout_btn.click(
#         handle_logout,
#         outputs=[auth_forms, doctor_panel, welcome_text, login_output, login_username, login_password]
#     )

# demo.launch(debug=True)
import gradio as gr
from dotenv import load_dotenv
import os
import time
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs
from authentication import register_user, login_user

# Load env
load_dotenv()

# Global session
user_session = {"username": None}

system_prompt = """You have to act as a professional doctor..."""

# ================= CORE DOCTOR LOGIC ================= #
def process_inputs(audio_filepath, image_filepath):
    if not user_session["username"]:
        return "⚠️ Please login first!", "", None

    # Speech to text
    speech_to_text_output = transcribe_with_groq(audio_filepath, "whisper-large-v3")

    # Doctor's analysis
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided"

    # Always overwrite the same file
    output_filename = "doctor_voice.mp3"

    voice_of_doctor = text_to_speech_with_elevenlabs(
        doctor_response, output_filename, "21m00Tcm4TlvDq8ikWAM"
    )

    return speech_to_text_output, doctor_response, voice_of_doctor



# ================= AUTH HANDLERS ================= #
def handle_register(username, email, phone, password):
    if not username or not email or not phone or not password:
        return "⚠️ All fields are required!", username, email, phone, password

    msg = register_user(username, email, phone, password)
    return msg, "", "", "", ""  # clear fields on success


def handle_login(username, password):
    if not username or not password:
        return (
            gr.update(visible=True),
            gr.update(visible=False),
            "",
            "⚠️ Username and Password required!",
            username, password
        )

    success, msg = login_user(username, password)
    if success:
        user_session["username"] = username
        return (
            gr.update(visible=False),
            gr.update(visible=True),
            f"<h2 id='welcome_text'>Welcome {username}!</h2>",
            "",
            "", ""
        )
    return (
        gr.update(visible=True),
        gr.update(visible=False),
        "",
        msg,
        username, ""
    )


def handle_logout():
    user_session["username"] = None
    return (
        gr.update(visible=True),
        gr.update(visible=False),
        "",
        "",
        "", ""
    )


def handle_forgot(username):
    if not username:
        return "⚠️ Please enter your username to reset password!"
    return f"🔑 Password reset link sent to registered email/phone for {username} (demo)."


# ================= GRADIO UI ================= #
with gr.Blocks(
    css="""
    #welcome_text {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin: 10px 0;
    }
    #header_bar {
        align-items: center;
        justify-content: space-between;
        background-color: #f8f9fa;
        padding: 8px 15px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    #logout_col {
        text-align: right;
    }
    #doctor_panel_title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin: 20px 0;
        color: #222;
    }
    button {
        font-size: 16px !important;
    }
    """,
    title="AI Doctor with Login"
) as demo:

    # ---------------- Authentication Forms ----------------
    with gr.Group(visible=True) as auth_forms:
        with gr.Tabs():
            # Register
            with gr.TabItem("📝 Register"):
                gr.Markdown("## Create Account")
                reg_username = gr.Textbox(label="Username")
                reg_email = gr.Textbox(label="Email")
                reg_phone = gr.Textbox(label="Phone")
                reg_password = gr.Textbox(label="Password", type="password")
                register_btn = gr.Button("Register")
                register_output = gr.Textbox(label="Register Status", interactive=False)
                register_btn.click(
                    handle_register,
                    [reg_username, reg_email, reg_phone, reg_password],
                    [register_output, reg_username, reg_email, reg_phone, reg_password]
                )

            # Login
            with gr.TabItem("🔑 Login"):
                gr.Markdown("## Login")
                login_username = gr.Textbox(label="Username")
                login_password = gr.Textbox(label="Password", type="password")
                login_btn = gr.Button("Login")
                forgot_btn = gr.Button("Forgot Password")
                login_output = gr.Textbox(label="Login Status", interactive=False)
                forgot_btn.click(handle_forgot, [login_username], login_output)

    # ---------------- Doctor Panel ----------------
    with gr.Group(visible=False) as doctor_panel:
        # Top header with Welcome + Logout
        with gr.Row(elem_id="header_bar"):
            with gr.Column(scale=3):
                welcome_text = gr.HTML("")  # dynamic welcome text
            with gr.Column(scale=1, elem_id="logout_col"):
                logout_btn = gr.Button("Logout")

        # ✅ Proper doctor panel heading (centered)
        gr.Markdown("##  Doctor Panel", elem_id="doctor_panel_title")

        audio_in = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Speak here")
        image_in = gr.Image(type="filepath", label="🖼️ Upload medical image")
        text_out = gr.Textbox(label="Speech to Text")
        doctor_out = gr.Textbox(label="Doctor's Response")
        audio_out = gr.Audio(label="Doctor's Voice")
        submit_btn = gr.Button("Ask Doctor")

        submit_btn.click(
            process_inputs,
            [audio_in, image_in],
            [text_out, doctor_out, audio_out]
        )

    # ---------------- Button Actions ----------------
    login_btn.click(
        handle_login,
        [login_username, login_password],
        [auth_forms, doctor_panel, welcome_text, login_output, login_username, login_password]
    )

    logout_btn.click(
        handle_logout,
        outputs=[auth_forms, doctor_panel, welcome_text, login_output, login_username, login_password]
    )

demo.launch(debug=True)
