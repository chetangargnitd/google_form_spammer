import requests

i=0;
while(1):
	url='https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/formResponse'

	form_data = {
		'entry.410813173'	:	'Yes',
		'entry.1269816401'	:	'8',
		'entry.1963899682'	:	'6545',
		'entry.1616294512'	:	'6'
		}
	user_agent= {
		'Referer':'https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/viewform',
		'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
		}
        r=requests.post(url, data=form_data, headers=user_agent)
        i=i+1
        if(i%3==0):
		print(r)
		print('\nTotal Count = ')
		print(i)
        print('\n')
