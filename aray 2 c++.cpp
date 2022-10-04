#include <iostream>
 using namespace std;
 int main(){
 	int angka[20];
 	cout<<"Masukan Nilai Ke 20 Mahasiswa Kela 2D Informatika"<<endl;
 	cout<<"===================================================="<<endl;
 	int jml_array = sizeof(angka)/sizeof(*angka);
 	
 	for(int a =0; a < jml_array; a++){
 		cout<<"Masukan nilai Mahasiswa ke-"<<a<<" :";
 		cin>>angka[a];
	 }
	 cout<<"==========================================="<<endl;
	 cout<<"Nilai Mahasiswa yang telah dimasukan"<<endl;
	 cout<<"==========================================="<<endl;
	 for(int b=0;b<jml_array; b++){
	 	cout<<"index ke-"<<b<<":"<<angka[b]<<endl;
	 }
 }
  
 
