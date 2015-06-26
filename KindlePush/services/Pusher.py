from mailthon import postman, email

from PushConf import pushConf
from exceptions import KindlePushError

class Pusher(object):
	
	def __init__(self, **kwargs):
		if kwargs:
			pushConf.update(kwargs)
		
	def push(self, receivers, attachments, *args, **kwargs):
		
		if not receivers:
			receivers = pushConf.receiver
		if not receivers:
			raise KindlePushError, "receiver empty"

		receivers_list = receivers.split(',')
		if not attachments:
			raise KindlePushError, "attachments empty"
		if isinstance(attachments, str):
			attachments = attachments.split(',')
		
		smtp = postman(host=pushConf.smtpHost, auth=(pushConf.username, pushConf.password))
		smtp.send(email(
			sender=pushConf.sender,
			receivers=receivers_list,
			attachments=attachments
		))
	
if __name__ == '__main__':
	pusher = Pusher()
	pusher.push("blandlove123@gmail.com", "test.txt")
