elders={
        5000 :['budha1',{'amar':'+','jyoti':'-','jawan':'+'}],
        1000 :['budha2',{'amar':'+','jawan':'+','jyoti':'+'}]
                }

carers={
        1000:['amar',3,{'budha1':'+' , 'budha2':'+' }],
        5000 :['jyoti',4,{'budha1':'-' , 'budha2':'+' }],
        2000:['jawan',1,{'budha1':'+' , 'budha2':'-' }]
              }

print("Welcome to CareGiving");
import time
time.sleep(0);
import sys
def basic():
	print("welcome");
	top=0;
	print"(1)Are you an elder in need of carer or (2)Carer who wishes to earn money or (3) other info";
	top=raw_input('Enter 1 or 2:');
	if(top=='1'):
		print("Enter your name");
		nameE=raw_input();
		print("Your funds");
		funds=raw_input();
		funds=int(funds);
		elders[funds]=[nameE,{}];
		print"would you like to go farwards 0/1 (No/Yes)";
		choice=raw_input();
		if(choice=='0'):
			sys.exit(0);
		elif(choice=='1'):
			elderFarward(funds);
	if(top=='2'):
		print"Enter your name";
		nameC=raw_input();
		print("Your price");
		price=raw_input();
		price=int(price);
		carers[price]=[nameC,0,{}];
		print"would you like to go farwards 0/1 (No/Yes)";
		choice=raw_input();
		if choice=='0':
			sys.exit(0);
		elif choice=='1':
			if carers[price][1]<4:
				carerFarward(price);
			else:
				print"you have reached the max count";
	if(top=='3'):
		print "To see which of the carers has all carer slots filled press 0 or press 1 to see enquire who a carer  is taking carer of ";
		c=int(raw_input());
		if c!=0 | c!=1:
			print "wrong key presssed";
			sys.exit(0);
		if c==0:
			for slots in carers:
				if carers[slots][1]==4:
					print carers[slots][0],"is all hike";
		if c==1:
			print "Enter a name to enquire about";
			N=raw_input();
			for slots in carers:
				if N==carers[slots][0]:
					print "Mr.",carers[slots][0],"is taking care of :";
					carers[slots][-1].keys();

def elderFarward(funds):
	bestkey=funds;
	print"looking for carers under the range of ", funds;
	if funds not in carers.keys():
		print "sorry, no one is available under this range now. kindly try other platform."
		sys.exit(0);
	for key in carers:
		print carers[funds][0],"carer cost",key;
		if key>funds:
			continue;
		elif carers[key][1]>=4:
			continue;
		else:
			R=checkReview(key,carers);
			print "rating is",R;
			if R=='-':
				continue;
			if R=='+':
				bestprice=key;
				print"here";
				if key<bestprice:
					bestkey=key;
					
	print "Going for the carer:",carers[bestkey][0];
	carers[bestkey][1]= carers[bestkey][1] + 1;
	print "Do you want to go back to home Yes==1| No==0";
	again=raw_input();
	again=int(again);
	if again==0:
		sys.exit(0);
	else:
		basic();



def carerFarward(price):
	print"looking for carers under the range of ",price;
	for key in elders:
			if key<price:
				continue;
			else:
				R=checkReview(key,elders);
				if R=='-':
					continue;
				if R=='+':
					print "Assigning",elders[key][0];
					carers[price][1]= carers[price][1] + 1;
					print "Do you want to go back to home Yes==1| No==0";
					again=raw_input();
					again=int(again);
					if again==0:
						sys.exit(0);
					else:
						basic();
	print "no elder has this amount of funds available. kindly condider lowering a bit or choose a diff platform";

def checkReview(key,dictionary):
	rarray=dictionary[key][-1].values();
	pluscount=0;
	minuscount=0;
	for item in rarray:
		if item=='+':
			pluscount=pluscount+1;
		if item=='-':
			minuscount=minuscount+1;
	if pluscount > minuscount:
		return '+';
	else:
		return '-';

basic();
