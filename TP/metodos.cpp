#include "metodos.hpp"


float calculoTrapezio(int subIntervalos, float a, float b){
	//VARIAVEIS
	int TAM = subIntervalos+1;
	float h;
	float soma = 0;
	float integral;
	float vetorX[TAM];
	float vetorY[TAM];
	int vetorCI[TAM];

	//DISTANCIA ENTRE OS VALORES DE X
 	h = (b-(a))/subIntervalos;

 	//VETOR DOS VALORES DE X E CI
	vetorX[0] = a; 
	vetorCI[0] = 1;
	for (int i = 1; i<=TAM; i++){
		vetorX[i] = vetorX[i-1]+h;
		vetorCI[i] = 2;
	}
	vetorX[subIntervalos] = b;
	vetorCI[subIntervalos] = 1;
	
	// FUNÇOES QUE USEI PARA TESTE
	//pow(10,vetorX[i]) - 10^x
	// 1/vetorX[i] - 1/x 
	// sqrt(vetorX[i])
	//VETOR DOS VALORES DE Y
	for(int i=0; i<TAM; i++){
		vetorY[i] = 1/vetorX[i];
	}

	for(int i = 0; i<TAM; i++){
		soma += (vetorCI[i]*vetorY[i]);
	}

	//CALCULO DA INTEGRAL
	integral = (h*soma)/2;

/*	for(int j = 0; j<TAM;j++){
		cout<<" x: "<<vetorX[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" y: "<<vetorY[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" CI: "<<vetorCI[j]<<endl;
	}
	cout<<"--------------"<<endl;
	cout<<"Soma:"<<soma<<endl;
	cout<<"--------------"<<endl;
	cout<<"Integral:"<<integral<<endl;
*/
	return integral;
}

float calculoPrimeiraSimpson(int subIntervalos, float a, float b){
	//VERIFICAR SE SUBINTERVALOS É PAR

	//VARIAVEIS
	int TAM = subIntervalos+1;
	float h;
	float soma = 0;
	float integral;
	float vetorX[TAM];
	float vetorY[TAM];
	int vetorCI[TAM];
	
	//DISTANCIA ENTRE OS VALORES DE X
 	h = (b-(a))/subIntervalos;

 	//VETOR DOS VALORES DE X
	vetorX[0] = a; 
	for (int i = 1; i<=TAM; i++){
		vetorX[i] = vetorX[i-1]+h;
	}
	vetorX[subIntervalos] = b;
	
	// FUNÇOES QUE USEI PARA TESTE
	//1/(1+(pow(vetorX[i],2))) - 1/1+x^2
	//VETOR DOS VALORES DE Y
	for(int i=0; i<TAM; i++){
		vetorY[i] = 1/(1+(pow(vetorX[i],2)));
	}

	//VETOR DOS VALORES DE CI
	vetorCI[0] = 1; 
	for (int i = 1; i<=TAM; i = i+2){
		vetorCI[i] = 4;
	}
	for (int i = 2; i<=TAM; i = i+2){
		vetorCI[i] = 2;
	}
	vetorCI[subIntervalos] = 1;
	
	for(int i = 0; i<TAM; i++){
		soma += (vetorCI[i]*vetorY[i]);
	}

	//CALCULO DA INTEGRAL
	integral = (h*soma)/3;

	for(int j = 0; j<TAM;j++){
		cout<<" x: "<<vetorX[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" y: "<<vetorY[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" CI: "<<vetorCI[j]<<endl;
	}
	cout<<"--------------"<<endl;
	cout<<"Soma:"<<soma<<endl;
	cout<<"--------------"<<endl;
	cout<<"Integral:"<<integral<<endl;

	return integral;

}

float calculoSegundaSimpson(int subIntervalos, float a, float b){
	//VERIFICAR SE SUBINTERVALOS É MULTIPLO DE 3

	//VARIAVEIS
	int TAM = subIntervalos+1;
	float h;
	float soma = 0;
	float integral;
	float vetorX[TAM];
	float vetorY[TAM];
	int vetorCI[TAM];
	
	//DISTANCIA ENTRE OS VALORES DE X
 	h = (b-(a))/subIntervalos;

 	//VETOR DOS VALORES DE X E CI
	vetorX[0] = a; 
	vetorCI[0] = 1; 
	for (int i = 1; i<=TAM; i++){
		vetorX[i] = vetorX[i-1]+h;
		vetorCI[i] = 3;
	}
	vetorX[subIntervalos] = b;
	vetorCI[subIntervalos] = 1;
	

	// FUNÇOES QUE USEI PARA TESTE
	//1/vetorX[i] - 1/x	
	//VETOR DOS VALORES DE Y
	for(int i=0; i<TAM; i++){
		vetorY[i] = 1/vetorX[i];
	}

	for(int i = 0; i<TAM; i++){
		soma += (vetorCI[i]*vetorY[i]);
	}
/*
	//CALCULO DA INTEGRAL
	integral = (3*h*soma)/8;

	for(int j = 0; j<TAM;j++){
		cout<<" x: "<<vetorX[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" y: "<<vetorY[j]<<endl;
	}
	cout<<"--------------"<<endl;
	for(int j = 0; j<TAM;j++){
		cout<<" CI: "<<vetorCI[j]<<endl;
	}
	cout<<"--------------"<<endl;
	cout<<"Soma:"<<soma<<endl;
	cout<<"--------------"<<endl;
	cout<<"Integral:"<<integral<<endl;
*/
	return integral;

}