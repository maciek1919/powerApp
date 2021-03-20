/***************************************************
  Two phase quadrature encoder(Incremental)
* ****************************************************
   To determine motor with encode （CW OR CCW）

  @author Dong
  @version  V1.0
  @date  2016-5-26
  All above must be included in any redistribution
* ****************************************************/
#define  A_PHASE 2
#define  B_PHASE 3
unsigned int flag_A = 0;  //Assign a value to the token bit
unsigned int flag_B = 0;  
double t_probkowania = 100; //czas próbkowania w mili-sekundach !!!!

/** *  */
void setup() {
  pinMode(A_PHASE, INPUT);
  pinMode(B_PHASE, INPUT);
  Serial.begin(9600);   //Serial Port Baudrate: 9600
  attachInterrupt(digitalPinToInterrupt( A_PHASE), interrupt, RISING); //Interrupt trigger mode: RISING
}
void loop() {

  Serial.print("Kąt:  ");
  if((flag_A-flag_B)>6000){
    Serial.println(0);
  }else{
    Serial.println(flag_A-flag_B);
  } 
 
  delay(t_probkowania);// Direction judgement

}
void interrupt()// Interrupt function
{ 
  char i;
  i = digitalRead(  B_PHASE);
  if (i == 1)
    flag_A += 1;
  else
    flag_B += 1;
}   
