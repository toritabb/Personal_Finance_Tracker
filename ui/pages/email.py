import smtplib
import ui
from datetime import datetime


def send_question(question):
    unique_id = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S-%f")

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
''''
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

