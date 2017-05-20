# Used Python 3
# Created by Robson Aristóteles Campos de Souza
# At 2017/05

import codecs
import cx_Oracle
import os
import string
import sys
import time

os.environ["NLS_LANG"] = ".AL32UTF8" 
START_VALUE = u"Unicode \u3042 3" 
END_VALUE = u"Unicode \u3042 6"

def main():
	# Build connection string
	user = "USUARIO"
	host = "host.com.br"
	port = "1521"
	sid = "adm"
	pswd = "senha"
	dsn = cx_Oracle.makedsn (host, port, sid)
		    
	# Connect to Oracle and test
	con = cx_Oracle.connect (user, pswd, dsn)
	start = time.time()
	if (con):
	    print("Connection successful")
	    print(con.version)
	    print("--------------------------")
	    cur = con.cursor()
	    cur.execute('select * from emp order by empno')
	    res = cur.fetchall()
    
	    elapsed = (time.time() - start)
	    print(elapsed, " seconds")
	    
	    for result in cur:
	        print(result)

	    print("----------Fet----------------")
	    
	    for r in res:
	        print(r)
	    
	    print("------------Fim--------------")
	    cur.close()
 	else:
    	print("Connection not successful")

  con.close()

def grava_registro_bd(param):
	# Build connection string
	user = "USUARIO"
	host = "host.com.br"
	port = "1521"
	sid = "adm"
	pswd = "senha"
	dsn = cx_Oracle.makedsn (host, port, sid)
	con = cx_Oracle.connect (user, pswd, dsn)
	start = time.time()

 	if (con):
		cur = con.cursor() 
		cur.execute("INSERT INTO TB1 (COLUMN1, COLUMN2) VALUES ("+str(param[0])+", '"+param[4]+"')")
 	else:
    	print("Connection not successful")
  
  	con.commit()
  	con.close()

def lista_diretorios():
    print("Listing arcives in directory.")
    path = "/Users/robson.aristoteles/Documents/workspace/project/"
    for filename in os.listdir(path):
        print("Starting file import '",filename,"' size:",round(os.stat(path+filename).st_size/1024/1024,2),"MB")
        with open(path+filename, encoding = "UTF-8") as f:
            for line in f:
                valor_linha = line.replace('"', '').strip('\n').split(';')
                grava_registro_bd(valor_linha)
        f.close()
        print("Finish...",filename)

        
if __name__ == '__main__':
	start = time.time()
	# main()
	lista_diretorios()
	elapsed = (time.time() - start)
	print(elapsed, " seconds")
