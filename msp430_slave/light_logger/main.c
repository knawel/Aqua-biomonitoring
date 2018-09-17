#include <msp430.h> 


/**
 * main.c
 */

#define A1  BIT1
#define dv  0.0032258
/*  Global vars  */
float volts=0.0;

/*  functions  */
void ADC_init(void);



int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer


    ADC_init();

    for (;;) {
        ADC10CTL0 |= ADC10SC;   // start new ADC
        while ((ADC10CTL1 & ADC10BUSY) == 0x01); // wait for measurement
        volts=ADC10MEM*dv;  // convert to volts
    }

	return 0;
}

void ADC_init(void) {
            // Vcc and Vss
            // 16 x ADC10CLKs and turn on.
    ADC10CTL0 = SREF_0 + ADC10SHT_2 + ADC10ON;
            //  A1,  ADC10CLK = 1,one channel regime
    ADC10CTL1 =  INCH_1 + SHS_0 + ADC10SSEL_0 + ADC10DIV_0 + CONSEQ_0;
    ADC10AE0 = A1;      // Enable input A1 on P1.1

    ADC10CTL0 |= ENC;     // Enable convertion.
} // ADC_init

