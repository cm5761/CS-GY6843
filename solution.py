from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    mailserver = ("127.0.0.1", 1025)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mail_command = "MAIL FROM: &..6@gmail.com>\r\n"
    clientSocket.send(mail_command.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
       print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO: <cm5761@nyu.edu> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4)
    if recv4[:3] != '345':
        print('345 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: SMTP HW\r\n\r\n" 
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    recv_msg = clientSocket.recv(1024).decode()
    print(recv_msg)
    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024).decode()
    print (message)
    
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
