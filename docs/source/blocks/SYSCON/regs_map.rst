.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :header-rows: 1
   :class: tight-table-reg-map

   * - 名称

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - :cspan:`4` SYSCON		  BASE：0x40000000

   * - CLKSEL

     - 0x00

     - R/W

     - 0x01

     - 时钟选择控制寄存器

   * - CLKDIVX_ON

     - 0x04

     - R/W

     - 0x00

     - 源时钟控制寄存器

   * - CLKEN0

     - 0x08

     - R/W

     - 0x00

     - 时钟门控控制寄存器0

   * - SLEEP

     - 0x10

     - R/W

     - 0x00

     - 系统模式控制寄存器

   * - RSTSR

     - 0x24

     - R/W1C

     - 0x00

     - 芯片复位状态寄存器

   * - CHIP_ID0

     - 0x80

     - RO

     - —

     - 芯片128位ID寄存器0

   * - CHIP_ID1

     - 0x84

     - RO

     - —

     - 芯片128位ID寄存器1

   * - CHIP_ID2

     - 0x88

     - RO

     - —

     - 芯片128位ID寄存器2

   * - CHIP_ID3

     - 0x8C

     - RO

     - --

     - 芯片128位ID寄存器3

   * - PAWKEN

     - 0x100

     - R/W

     - 0x00

     - PORTA唤醒使能控制寄存器

   * - PBWKEN

     - 0x104

     - R/W

     - 0x00

     - PORTB唤醒使能控制寄存器

   * - PCWKEN

     - 0x108

     - R/W

     - 0x00

     - PORTC唤醒使能控制寄存器

   * - PAWKSR

     - 0x130

     - R/W1C

     - 0x00

     - PORTA唤醒状态寄存器

   * - PBWKSR

     - 0x134

     - R/W1C

     - 0x00

     - PORTB唤醒状态寄存器

   * - PCWKSR

     - 0x138

     - R/W1C

     - 0x00

     - PORTC唤醒状态寄存器

   * - IOFILT0

     - 0x400

     - R/W

     - 0x00

     - IO滤波窗口时间配置寄存器0

   * - IOFILT1

     - 0x404

     - R/W

     - 0x00

     - IO滤波窗口时间配置寄存器1

   * - PRSTEN

     - 0x720

     - R/W

     - 0x00

     - 芯片复位屏蔽寄存器

   * - PRSTR

     - 0x724

     - R/W

     - 0x00

     - 芯片复位配置寄存器0

   * - :cspan:`4` ANACON		  BASE：0400A5800

   * - RCCR

     - 0x08

     - R/W

     - 0x01

     - 内部RC振荡器配置寄存器

   * - XTALCR

     - 0x10

     - R/W

     - 0x00

     - 晶体振荡器控制寄存器

   * - XTALSR

     - 0x14

     - R/W1C

     - 0x00

     - 晶体振荡器状态寄存器

   * - PLLCR

     - 0x18

     - R/W

     - 0x00

     - PLL控制寄存器

   * - PLLST

     - 0x1C

     - R/W

     - 0x00

     - PLL状态寄存器

   * - PVDCR

     - 0x20

     - R/W

     - 0x00

     - PVD控制寄存器

   * - PVDSR

     - 0x24

     - R/W1C

     - 0x00

     - PVD中断状态寄存器

   * - LVRCR

     - 0x28

     - R/W

     - 0x00

     - LVR控制寄存器



