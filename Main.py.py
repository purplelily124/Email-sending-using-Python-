#Note : The term we used in program <VARIABLE> replace it with the variables you used in your program  
choice=int(input("1].sentiment\n2].Abusive\n"))
#Note : THE SENDER NEEDS TO GIVE ACCESS TO -->"Less secure apps " in Gmail account <--  
if choice==1:
    import mysql.connector as sql
    mail = sql.connect(
        host='',
        user='',
        password='',
        database=''
    )
    c = mail.cursor()
    sql_query = "SELECT column names FROM `table name` WHERE email_id column='VARIABLE';"
    c.execute(sql_query)
    result = c.fetchall()
    report=str(result)
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content(report)
    msg['From'] = "sender_@gmail.com"
    msg['To'] = "VARIABLE" # Here you should use the same variable as you used in your code for email_id 
    msg['Subject'] = 'This Is REPORT Of Sentiment Analysis'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("sender_@gmail.com", "sender_password")
        server.sendmail("sender_@gmail.com", "VARIABLE", msg.as_string())# Here you should use the same variable as you used in your code for email_id
        print("Email sent successfully")
    except Exception: # try to avoid catching Exception unless you have too
        print("Error 404!\nServer Is Not Responding!\nPlease Check Your Connection")
    finally:
        server.quit()
elif choice==2:
    import mysql.connector as sql
    mail = sql.connect(
        host='',
        user='',
        password='',
        database=''
    )
    c = mail.cursor()
    sql_query = "SELECT column names FROM `table name` WHERE email_id column='VAIRABLE';"
    c.execute(sql_query)
    result = c.fetchall()
    report=str(result)
    import smtplib
    from email.message import EmailMessage
    msg = EmailMessage()
    msg.set_content(report)
    msg['From'] = "sender_@gmail.com"
    msg['To'] = "VARIABLE" # Here you should use the same variable as you used in your code for email_id
    msg['Subject'] = 'This Is Your REPORT Of Abusive Words'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("sender_@gmail.com", "sender_password")
        server.sendmail("sender_@gmail.com", "VARIABLE", msg.as_string())# Here you should use the same variable as you used in your code for email_id
        print("Email sent successfully")
    except Exception: # try to avoid catching Exception unless you have too
        print("Error 404!\nServer Is Not Responding!\nPlease Check Your Connection")
    finally:
        server.quit()
elif choice!= 1 or choice!=2: 
    print("PLEASE CHOOSE FROM ABOVE MENTIONED")    
