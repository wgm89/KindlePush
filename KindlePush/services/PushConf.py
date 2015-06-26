import os
import json

from os.path import expanduser

class PushConf(object):

	defaultDir = ''

	confTpl = '''{
			"smtpHost":"smtp.qq.com",
			"username":"",
			"password":"",
			"sender":"",
			"receiver":""
		}'''
	confContent = {}

	def __init__(self):
		super(PushConf, self).__init__()
		self.defaultDir = os.path.join(expanduser("~"), '.kindlePush')
		if not os.path.exists(self.defaultDir):
			os.makedirs(self.defaultDir)
			self.setConfig(self.confTpl)
		self.get_conf_content()

	def __getattr__(self, key):
		return self.confContent.get(key, '')

	def __get_conf_file(self):
		return os.path.join(self.defaultDir, 'kindlePush.conf')

	def get_conf_content(self):
		if os.path.exists(self.__get_conf_file()):
			fd = open(self.__get_conf_file(), "r")
			try:
				self.confContent = json.load(fd)
			finally:
				fd.close()
		return self.confContent

	def setConfig(self, dic):
		if isinstance(dic, (str)):
			dic = json.loads(dic)
		file_content = self.get_conf_content()
		if file_content:
			try:
				file_content.update(dic)
				dic = file_content
			except ValueError:
				pass
		dic = json.dumps(dic)
		with open(self.__get_conf_file(), "w") as fd:
			fd.write(dic)

	def update(self, dic):
		for key, value in dic.items():
			setattr(self, key, value)

pushConf = PushConf()

if __name__ == '__main__':
	kindlePushConf = PushConf()
