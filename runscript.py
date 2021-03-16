import bitsv
from dotenv import load_dotenv
import os

load_dotenv()
my_key = bitsv.Key(os.environ.get('PRIVKEY'))
list_of_pushdata = ['$'.encode('utf-8'), 'useradd'.encode('utf-8'), '1Cr1yqxm7EJojG7caS1XYv5Za3TCRh9cyh'.encode('utf-8')]
my_key.send_op_return(list_of_pushdata)
print('done')
