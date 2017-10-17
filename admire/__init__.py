from datetime import datetime
from datetime import timedelta

from requests import post

class Captcha:
	def __init__(self, source, secret, is_package=False):
		self.source = source
		self.secret = secret
		self.is_package = is_package

	def verify_token(self, token, remote_ip='', expiration=None):
		payload = {
			'secret': self.secret,
			'response': token,
		}

		if remote_ip:
			payload['remoteip'] = remote_ip

		try:
			json = post('https://www.google.com/recaptcha/api/siteverify', data=payload, timeout=10).json()

			if json.get('success'):
				if (self.is_package and json.get('apk_package_name') == self.source) or (not self.is_package and json.get('hostname') == self.source):
					if expiration:
						timestamp = datetime.strptime(json.get('challenge_ts'), '%Y-%m-%dT%H:%M:%SZ')

						if datetime.utcnow() - timestamp < timedelta(seconds=expiration):
							return token
					else:
						return token
		except:
			pass

if __name__ == '__main__':
	captcha = Captcha('testkey.google.com', '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe')
	token = captcha.verify_token('6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI', expiration=600)

	if token:
		print('Verified token: {}'.format(token))
	else:
		print('Could not verify token.')
