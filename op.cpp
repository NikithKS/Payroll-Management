#include<iostream>
#include<sqlite3.h>
#include<string.h>
using namespace std;

static int callback(void* data, int argc, char** argv, char** azColName)
{
	int i;
	cout<<"NIL |";
	fprintf(stderr, "%s: ", (const char*)data);
	for (i = 0; i < argc; i++)
		{
		printf("%s|",argv[i] ? argv[i] : "NULL");
		}
	printf("\n");
	return 0;
}


class data
	{
	char pass,flag,EmpID;
	int status;
	sqlite3* DB;

	public:
	void opendb()
		{
		if (status!= SQLITE_OK)
			{
			status=sqlite3_open("oop.db",&DB);
			}
		}

	void verify(char EmpID0[])
		{
		char cmd[50];
		strcpy(cmd,"select Password from PASS where ID=");
		strcat(cmd,EmpID0);
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		}


	void display(char EmpID0[])
		{
		char cmd[50];
		strcpy(cmd,"select * from Payroll where EmpID=");
		strcat(cmd,EmpID0);
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		}
	void paysal(char EmpID0[])
		{
		char cmd[50];
		strcpy(cmd,"update Payroll set SalStatus='1' where EmpID=");
		strcat(cmd,EmpID0);
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		}

	void edit(char EmpID0[],char val[])
		{
		char cmd[200];
		strcpy(cmd,"delete from Payroll where EmpID=");
		strcat(cmd,EmpID0);
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		addnew(val);
		}

	void calc(char *a,char *b,char *c,char *d,char *e)
		{
		int sal;
		int salary=atoi(a);
		int OT=atoi(b);
		int OTsal=atoi(c);
		int Leave=atoi(d);
		int Deduct=atoi(e);
		sal=salary+(OT*OTsal)-(Leave*Deduct);
		cout<<sal;
		}


	void addnew(char val[])
		{
		cout<<val<<"qwe\n";
		char cmd[200];
		strcpy(cmd,"insert into Payroll values");
		strcat(cmd,val);
		cout<<cmd;
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		}
	void chpw(char EmpID0[],char pw[])
		{
		char cmd[100];
		strcpy(cmd,"delete from PASS where ID=");
		strcat(cmd,EmpID0);
		cout<<cmd<<"  1 \n";
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		strcpy(cmd,"insert into PASS values('");
		strcat(cmd,EmpID0);
		strcat(cmd,"','");
		strcat(cmd,pw);
		strcat(cmd,"')");
		cout<<cmd;
		sqlite3_exec(DB,cmd, callback, NULL, NULL);
		}
	};




int main(int argc,char *argv[])
{
if(argc>1)
{
	int command;
	char *c,x[200];
	data obj;
	c=argv[1];
	command=atoi(argv[1]);
	obj.opendb();
		if(command==0)
			{
			obj.display(argv[2]);
			}
		else if(command==1)
			{
			obj.verify(argv[2]);
			}

		else if(command==2)
			{
			obj.paysal(argv[2]);
			}

		else if(command==3)
			{
			obj.calc(argv[2],argv[3],argv[4],argv[5],argv[6]);
			}

		else if(command==4)
			{
			obj.addnew(argv[2]);
			}
		else if(command==5)
			{
			obj.chpw(argv[2],argv[3]);
			}
		else
			{
			cout<<"Unidentified input";
			}
}
else
	{
	cout<<argv[1];
	cout<<"\nInsufficient Arguments provided\n";
	}
return 0;

}
