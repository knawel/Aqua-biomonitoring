#include <msp430.h> 


/**
 * main.c
 */

#define A1  BIT1
#define dv  0.0032258
/*  Глобальные переменные  */
float volts=0.0;

/*  Обьявление функций  */
void ADC_init(void);



int main(void)
{
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer


    ADC_init();

    for (;;) {
        ADC10CTL0 |= ADC10SC;   // начинаем новое преобразование
        while ((ADC10CTL1 & ADC10BUSY) == 0x01); // ждем, когда преобразование закончится
        volts=ADC10MEM*dv;  // конвертируем результат в напряжение и сохраняем

    }

	return 0;
}

void ADC_init(void) {
            // Используем Vcc/Vss(аналоговая земля) для верхнего/нижнего ИОН,
            // 16 x ADC10CLKs (выборка за 16 тактов), включаем АЦП.
    ADC10CTL0 = SREF_0 + ADC10SHT_2 + ADC10ON;
            // Вход A1, делитель ADC10CLK на 1, одноканальный режим.
    ADC10CTL1 =  INCH_1 + SHS_0 + ADC10SSEL_0 + ADC10DIV_0 + CONSEQ_0;
    ADC10AE0 = A1;      // Разрешаем вход АЦП на порту P1.1

    ADC10CTL0 |= ENC;     // Разрешаем преобразования.
} // ADC_init

