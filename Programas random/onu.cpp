#include "iostream"
#include "string"
#include "stdlib.h"

using namespace std;

int main ()
{
	string password="";
	cout <<"Insert password:";
	cin >> password;
	if(password=="admin1234")
	{
		cout<< "Contraseña correcta. Bienvenido";
	}
	else
	{
		cout <<"¿Otra vez usted? Usted no aprende, ¿verdad? ¡Largo de aquí, coño!";
	}
	system("PAUSE");

	return 0;
}
