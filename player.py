def createToken(self):
	token_url = 'https://lhediscoverysandbox.service-now.com/oauth_token.do'
	client_id = 'ff4cff6dd79dc70025b6f8fe2738b9a1'
	client_secret = 'VvSHW)(reC'
	usr = ''
	pwd = ''
	oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
	token = oauth.fetch_token(
		token_url=token_url,
		username=usr, 
		password=pwd, 
		client_id=client_id,
		client_secret=client_secret
		)
	auth_token = token['access_token']
	self._headers['Authorization'] = 'Bearer {}'.format(auth_token)
	from oauthlib.oauth2 import LegacyApplicationClient
	from requests_oauthlib import OAuth2Session