# -*- coding: UTF-8 -*-
import datetime
import smtplib
import socket
from email.mime.text import MIMEText 

#========================================== 
# send_mail no proxy 
#========================================== 
def send_mail(to_list,sub,content): 
  me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEText(content) 
  msg['Subject'] = sub 
  msg['From'] = me 
  msg['To'] = ";".join(to_list) 
  try: 
    s = smtplib.SMTP() 
    s.connect(mail_host) 
    s.login(mail_user,mail_pass) 
    s.sendmail(me, to_list, msg.as_string()) 
    s.close() 
    return True
  except Exception, e: 
    print str(e) 
    return False

#========================================== 
# send mail  by proxy
#========================================== 
def recvline(sock):
    """Receives a line."""
    stop = 0
    line = ''
    while True:
        i = sock.recv(1)
        if i.decode('UTF-8') == '\n': stop = 1
        line += i.decode('UTF-8')
        if stop == 1:
            print('Stop reached.')
            break
    print('Received line: %s' % line)
    return line

class ProxySMTP(smtplib.SMTP):
    """Connects to a SMTP server through a HTTP proxy."""

    def __init__(self, host='', port=0, p_address='',p_port=0, local_hostname=None,
             timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """Initialize a new instance.

        If specified, `host' is the name of the remote host to which to
        connect.  If specified, `port' specifies the port to which to connect.
        By default, smtplib.SMTP_PORT is used.  An SMTPConnectError is raised
        if the specified `host' doesn't respond correctly.  If specified,
        `local_hostname` is used as the FQDN of the local host.  By default,
        the local hostname is found using socket.getfqdn().

        """
        self.p_address = p_address
        self.p_port = p_port

        self.timeout = timeout
        self.esmtp_features = {}
        self.default_port = smtplib.SMTP_PORT

        if host:
            (code, msg) = self.connect(host, port)
            if code != 220:
                raise IOError(code, msg)

        if local_hostname is not None:
            self.local_hostname = local_hostname
        else:
            # RFC 2821 says we should use the fqdn in the EHLO/HELO verb, and
            # if that can't be calculated, that we should use a domain literal
            # instead (essentially an encoded IP address like [A.B.C.D]).
            fqdn = socket.getfqdn()

            if '.' in fqdn:
                self.local_hostname = fqdn
            else:
                # We can't find an fqdn hostname, so use a domain literal
                addr = '127.0.0.1'

                try:
                    addr = socket.gethostbyname(socket.gethostname())
                except socket.gaierror:
                    pass
                self.local_hostname = '[%s]' % addr

        smtplib.SMTP.__init__(self)

    def _get_socket(self, port, host, timeout):
        # This makes it simpler for SMTP to use the SMTP connect code
        # and just alter the socket connection bit.
        print('Will connect to:', (host, port))
        print('Connect to proxy.')
        new_socket = socket.create_connection((self.p_address,self.p_port), timeout)

        s = "CONNECT %s:%s HTTP/1.1\r\n\r\n" % (port,host)
        s = s.encode('UTF-8')
        new_socket.sendall(s)

        print('Sent CONNECT. Receiving lines.')
        for x in range(2): recvline(new_socket)

        print('Connected.')
        return new_socket


mailto_list=["38643987@qq.com","787687312@qq.com"] 

mail_host="smtp.qq.com"  #ËÆæÁΩÆÊúçÂä°Âô®
mail_user="38643987"
mail_pass="xulei820729"
mail_postfix="qq.com"

if __name__ == '__main__':

  nowStr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  news="hello,world"
  isProxy=0   ##¥˙¿Ì”√1 ∑«¥˙¿Ì”√0
  proxy_host = "10.22.96.29"
  proxy_port = "8080"
  if isProxy==0:
	  if send_mail(mailto_list,nowStr,news): 
	    print "mail success"
	  else: 
	    print "mail fail"
  else:
	# Both port 25 and 587 work for SMTP
	conn = ProxySMTP(host="smtp.qq.com", port=587,
			 p_address=proxy_host, p_port=proxy_port)

	conn.ehlo()
	conn.starttls()
	conn.ehlo()

	r, d = conn.login("38643987@qq.com", "xulei820729")

	print('Login reply: %s' % r)

	sender = "38643987@qq.com"
	receivers = ["27119752@qq.com"]

	message = """From: From Person <from@fromdomain.com>
	To: To Person <to@todomain.com>
	Subject: SMTP e-mail test
	This is Xulei Test mail sender.
	"""

	print('Send email.')
	conn.sendmail(sender, receivers, message)

	print('Success.')
	conn.close()
