from subprocess import Popen, PIPE

def get_all_users():
  grep_process = Popen(["grep","/bin/bash","/etc/passwd"], stdout=PIPE, stderr=PIPE)
  #python3.5
  #user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split(b'\n')
  #python2.7
  user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  #print(user_list)
  return filter(None,user_list)
