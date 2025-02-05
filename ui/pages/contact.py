# local
import ui
import smtplib
from .page import Page, PageManagerBase
from datetime import datetime



class ContactPage(Page):
    STR = 'contact'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)


        '''
        def send_question(question):
        #unique_id = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S-%f")

        # Email Credentials
        sender_email = "<sender email>"
        sender_password = "<Google Code Password>"
        receiver_email = "<receiver email>"
        message = f"Subject: Help Request #{unique_id}\n\nQuestion from User: {question}"

        # Connect to SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        def display_qna_window(): 
            # New Window for Questions
            textbox1 = ui.Textbox(
                #self,
                ui.Pointer('Yap here'),
                ('Nunito', 20),
                (100, 100),
                (250, -1),
                padding=(7, 5),
                border_thickness=3,
                corner_radius=-1
                )
            
            # Add the question entry box and submit button
            question_label = tk.Label(qna_window, text="Send a Question or Suggestion to Our Developers\nInclude your email at the top of the message so we can get back to you", padx=100, pady=50, background=bg_color, font='Helvetica 10 bold')
            question_label.pack()

            question_box = tk.Text(qna_window, width=50, height=5, background=button_color)
            question_box.pack()

            def submit_question():
            question_text = question_box.get("1.0", "end").strip()

            # Check if question box is empty
            if question_text:
                send_question(question_text)
                question_box.delete("1.0", tk.END)  # Clear question box after submission
                success_label = tk.Label(qna_window, text="Question submitted successfully!", fg="green", background=button_color, font ='Helvetica 10 bold')
                success_label.pack(pady=30)
                root.after(5000, success_label.destroy)

            # Display the error label
            else:
                error_label = tk.Label(qna_window, text="Please enter your question.", fg="red", background=button_color, font='Helvetica 10 bold')
                error_label.pack(pady=30)
                root.after(5000, error_label.destroy)
            '''

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'Contact Page',
            ('Nunito', 40, True, False)
        )

        email = ui.Text(
            self,
            (300, 0),
            'falconfinancehelp@gmail.com',
            ('Nunito', 75)
        )
        ui.center(email, axis='x')
        ui.center(email, axis='y')
            

        contact = ui.Text(
            self,
            (0, email.top - 50),
            'Conatct us at',
            ('Nunito', 50)
        )

        ui.center(contact, axis='x') # center the text on the x

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=4
        )
            # you can remove these, they are just placeholders so you know what page it is and can return