import sys
import getopt
import logging
from services.Pusher import Pusher
from services.PushConf import pushConf

from services.exceptions import KindlePushError

class KindlePush(object):

	KPVersion = '0.1'
	logFile = 'KindlePush.log'

	def __init__(self):
		pass

	def usage(self):
		print "\n" + self.KPVersion + " by saeedwang"
		print "Usage: KindlePush <options>\n"
		print "Options:"
		print "-a <attachment>, --attachment=<attachment> upload an attachment"
		print "-c <configure>, --configure=<configure> create config file"
		print "-r <receivers>, --receiver=<receiver> kindle emails(tom@kindle.com, li@kindle.com)"
		print "-h help"


	def main(self, argv):
		options = self.parseOptions(argv)
		logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s',
				filename=self.logFile, filemode='w')
		Pusher().push(*options)

	def parseOptions(self, argv):
		attachment = ''
		receiver = ''
		try:
			opts, args = getopt.getopt(argv, "ha:cr:",
					["help", "attachment=", "configure", "receiver"])
			if not argv:
				raise getopt.GetoptError("no args")

			for opt, arg in opts:
				if opt in ("-h", "--help"):
					self.usage()
					sys.exit()
				elif opt in ("-a", "--attachment"):
					attachment = arg
				elif opt in ("-c", "--configure"):
					self.setConfig()
				elif opt in ("-r", "--receiver"):
					receiver = arg
				
			return [receiver, attachment]

		except getopt.GetoptError:
			self.usage()
			sys.exit(2)

	"""set config before first use"""
	def setConfig(self):
		smtpConf = {}
		requireParams = {
				"smtpHost", "username", "password", "sender", "receiver"
				}
		for param in requireParams:
			smtpConf[param] = raw_input("input %s:" % param)
		pushConf.setConfig(smtpConf)
		sys.exit()
		

def main():
	kindlePush = KindlePush()
	kindlePush.main(sys.argv[1:])
	
if __name__ == '__main__':
	main()
