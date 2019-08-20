import commands
import getpass

def main():
	paths = dict()
	with open('urls.txt') as fp:
		for item in fp:
			temp = item.split('=')
			paths[temp[0]] = temp[1].strip('\n')
		
	user_name = getpass.getuser()
	
	#print user_name
	
	url_check = '/Users/' + user_name + paths['RUN_PATH']
	temp1 = paths['RUN_PATH'].replace(' ', '\ ')
	url = '/Users/' + user_name + temp1
	cmd = 'open ' + url
	
	#print cmd
	
	a = commands.getstatusoutput(cmd)
	pass
	


if __name__ == '__main__':
	main()