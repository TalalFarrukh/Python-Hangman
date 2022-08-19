#include <iostream>
#include <cstdlib>
#include <ctime>
#include <stdlib.h>
using namespace std;

//variables declared globally
int i2=0, n2=0, d2=0, a2=0, l2=0, sto;
	string india, man, potato, car, key, name, hen, gear, open, close, store;
	string guess[10]={"india", "man", "potato", "car", "key", "name", "hen", "gear", "open", "close"};
	char inp;
//---------------------//

void pp1()
{
	if (store=="india"){
		cout<<"Hint: Its a country"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<4;){		
		cin>>inp;
		
		if (inp=='i' && i2<1){
			i2++;
			cout<<"i__i_"<<endl;
			chance2++;}
		else if (inp=='n' && n2<1){
			n2++;
			cout<<"_n___"<<endl;
			chance2++;}
		else if (inp=='d' && d2<1){
			d2++;
			cout<<"__d__"<<endl;
			chance2++;}
		else if (inp=='a' && a2<1){
			a2++;
			cout<<"____a"<<endl;
			chance2++;}
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: india"<<endl;
		break;	
			}
		else if (chance2==4){
		cout<<"india"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="car"){
		cout<<"Hint: A big object that has wheels"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<3;){		
		cin>>inp;
		
		if (inp=='c' && i2<1){
			i2++;
			cout<<"c__"<<endl;
			chance2++;}
		else if (inp=='a' && n2<1){
			n2++;
			cout<<"_a_"<<endl;
			chance2++;}
		else if (inp=='r' && d2<1){
			d2++;
			cout<<"__r"<<endl;
			chance2++;}
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: car"<<endl;
		break;	
			}
		else if (chance2==3){
		cout<<"car"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="man"){
		cout<<"Hint: One of the many genders"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<3;){		
		cin>>inp;
		
		if (inp=='m' && i2<1){
			i2++;
			cout<<"m__"<<endl;
			chance2++;}
		else if (inp=='a' && n2<1){
			n2++;
			cout<<"_a_"<<endl;
			chance2++;}
		else if (inp=='n' && d2<1){
			d2++;
			cout<<"__n"<<endl;
			chance2++;}
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: man"<<endl;
		break;	
			}
		else if (chance2==3){
		cout<<"man"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="key"){
		cout<<"Hint: A small object the gets lost when we need it"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<3;){		
		cin>>inp;
		
		if (inp=='k' && i2<1){
			i2++;
			cout<<"k__"<<endl;
			chance2++;}
		else if (inp=='a' && n2<1){
			n2++;
			cout<<"_e_"<<endl;
			chance2++;}
		else if (inp=='r' && d2<1){
			d2++;
			cout<<"__y"<<endl;
			chance2++;}
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: key"<<endl;
		break;	
			}
		else if (chance2==3){
		cout<<"key"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="name"){
		cout<<"Hint: Used to identify something"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<4;){		
		cin>>inp;
		
		if (inp=='n' && i2<1){
			i2++;
			cout<<"n___"<<endl;
			chance2++;}
		else if (inp=='a' && n2<1){
			n2++;
			cout<<"_a__"<<endl;
			chance2++;}
		else if (inp=='m' && d2<1){
			d2++;
			cout<<"__m_"<<endl;
			chance2++;}
		else if (inp=='e' && a2<1){
			a2++;
			cout<<"___e"<<endl;
			chance2++;}	
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: name"<<endl;
		break;	
			}
		else if (chance2==4){
		cout<<"name"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="potato"){
		cout<<"Hint: A vegetable"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<4;){		
		cin>>inp;
		
		if (inp=='p' && i2<1){
			i2++;
			cout<<"p_____"<<endl;
			chance2++;}
		else if (inp=='o' && n2<1){
			n2++;
			cout<<"_o___o"<<endl;
			chance2++;}
		else if (inp=='t' && d2<1){
			d2++;
			cout<<"__t_t_"<<endl;
			chance2++;}
		else if (inp=='a' && a2<1){
			a2++;
			cout<<"___a__"<<endl;
			chance2++;}	
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: potato"<<endl;
		break;	
			}
		else if (chance2==4){
		cout<<"potato"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="hen"){
		cout<<"Hint: A livestock animal"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<3;){		
		cin>>inp;
		
		if (inp=='h' && i2<1){
			i2++;
			cout<<"h__"<<endl;
			chance2++;}
		else if (inp=='e' && n2<1){
			n2++;
			cout<<"_e_"<<endl;
			chance2++;}
		else if (inp=='n' && d2<1){
			d2++;
			cout<<"__n"<<endl;
			chance2++;}
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: hen"<<endl;
		break;	
			}
		else if (chance2==3){
		cout<<"hen"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="open"){
		cout<<"Hint: We do this to a door"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<4;){		
		cin>>inp;
		
		if (inp=='o' && i2<1){
			i2++;
			cout<<"o___"<<endl;
			chance2++;}
		else if (inp=='p' && n2<1){
			n2++;
			cout<<"_p__"<<endl;
			chance2++;}
		else if (inp=='e' && d2<1){
			d2++;
			cout<<"__e_"<<endl;
			chance2++;}
		else if (inp=='n' && a2<1){
			a2++;
			cout<<"___n"<<endl;
			chance2++;}	
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: open"<<endl;
		break;	
			}
		else if (chance2==4){
		cout<<"open"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="gear"){
		cout<<"Hint: An essential component of a car that we use"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<4;){		
		cin>>inp;
		
		if (inp=='g' && i2<1){
			i2++;
			cout<<"g___"<<endl;
			chance2++;}
		else if (inp=='e' && n2<1){
			n2++;
			cout<<"_e__"<<endl;
			chance2++;}
		else if (inp=='a' && d2<1){
			d2++;
			cout<<"__a_"<<endl;
			chance2++;}
		else if (inp=='r' && a2<1){
			a2++;
			cout<<"___r"<<endl;
			chance2++;}	
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: gear"<<endl;
		break;	
			}
		else if (chance2==4){
		cout<<"gear"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}
	else if (store=="close"){
		cout<<"Hint: We do this to a door"<<endl;
		for (int chances=10,chance2=0; chances>0 || chance2<5;){		
		cin>>inp;
		
		if (inp=='c' && i2<1){
			i2++;
			cout<<"c____"<<endl;
			chance2++;}
		else if (inp=='l' && n2<1){
			n2++;
			cout<<"_l___"<<endl;
			chance2++;}
		else if (inp=='o' && d2<1){
			d2++;
			cout<<"__o__"<<endl;
			chance2++;}
		else if (inp=='s' && a2<1){
			a2++;
			cout<<"___s_"<<endl;
			chance2++;}
		else if (inp=='e' && l2<1){
			l2++;
			cout<<"____e"<<endl;
			chance2++;}		
		else 
			chances--;
	
		if (chances==0){
		cout<<"You have lost the game"<<endl<<"Correct word: close"<<endl;
		break;	
			}
		else if (chance2==5){
		cout<<"close"<<endl;	
		cout<<"You have won the game"<<endl;
		break;
			}
		}	
	}	
}

int rand();
int main()
{
	cout<<"-----HANGMAN-----"<<endl;
	cout<<"You have to guess each letter correctly to make up the country. Every wrong guess will decrease your chance by one"<<endl;
	cout<<"Play wisely!"<<endl;
	cout<<"Guess the letter"<<endl;
	
	srand(time(0));
	sto = (rand()%10);
	store = guess[sto];
	pp1();
	
	system("pause");
	return 0;
}
