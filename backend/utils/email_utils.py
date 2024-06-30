import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, recipient, body):
        sender_email = "your_email@example.com"
            sender_password = "your_password"
                
                    msg = MIMEMultipart()
                        msg['From'] = sender_email
                            msg['To'] = recipient
                                msg['Subject'] = subject
                                    
                                        msg.attach(MIMEText(body, 'plain'))
                                            
                                                try:
                                                            server = smtplib.SMTP('smtp.example.com', 587)
                                                                    server.starttls()
                                                                            server.login(sender_email, sender_password)
                                                                                    text = msg.as_string()
                                                                                            server.sendmail(sender_email, recipient, text)
                                                                                                    server.quit()
                                                                                                            return True
                                                                                                            except Exception as e:
                                                                                                                        print(f"Failed to send email: {e}")
                                                                                                                                return False

