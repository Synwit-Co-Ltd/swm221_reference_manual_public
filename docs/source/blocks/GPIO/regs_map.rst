.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :header-rows: 1
   :class: tight-table
   :widths: 12 9 6 10 33

   * - 名称

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - :cspan:`4` 

       GPIOA		  BASE：0x40003800

       GPIOB		  BASE：0x40004000

       GPIOC		  BASE：0x40004800


   * - ODR

     - 0x00

     - R/W

     - 0x00

     - GPIO写数据寄存器

   * - DIR

     - 0x04

     - R/W

     - 0x00

     - GPIO方向寄存器

   * - INTLVLTRG

     - 0x08

     - R/W

     - 0x00

     - GPIO中断触发条件

   * - INTBE

     - 0x0c

     - R/W

     - 0x00

     - GPIO中断沿触发配置寄存器

   * - INTRISEEN

     - 0x10

     - R/W

     - 0x00

     - GPIO 中断触发极性

   * - INTEN

     - 0x14

     - R/W

     - 0x00

     - GPIO中断使能

   * - INTRAWSTAT

     - 0x18

     - R

     - 0x00

     - GPIO中断原始状态

   * - INTSTAT

     - 0x1c

     - R

     - 0x00

     - GPIO中断状态

   * - INTCLR

     - 0x20

     - W

     - 0x00

     - GPIO中断清除

   * - IDR

     - 0x30

     - R

     - 0x00

     - GPIO读数据寄存器

   * - DATAPIN0

     - 0x40

     - R/W

     - 0x00

     - GPIO PIN0数据寄存器

   * - DATAPIN1

     - 0x44

     - R/W

     - 0x00

     - GPIO PIN1数据寄存器

   * - DATAPIN2

     - 0x48

     - R/W

     - 0x00

     - GPIO PIN2数据寄存器

   * - DATAPIN3

     - 0x4c

     - R/W

     - 0x00

     - GPIO PIN3数据寄存器

   * - DATAPIN4

     - 0x50

     - R/W

     - 0x00

     - GPIO PIN4数据寄存器

   * - DATAPIN5

     - 0x54

     - R/W

     - 0x00

     - GPIO PIN5数据寄存器

   * - DATAPIN6

     - 0x58

     - R/W

     - 0x00

     - GPIO PIN6数据寄存器

   * - DATAPIN7

     - 0x5c

     - R/W

     - 0x00

     - GPIO PIN7数据寄存器

   * - DATAPIN8

     - 0x60

     - R/W

     - 0x00

     - GPIO PIN8数据寄存器

   * - DATAPIN9

     - 0x64

     - R/W

     - 0x00

     - GPIO PIN9数据寄存器

   * - DATAPIN10

     - 0x68

     - R/W

     - 0x00

     - GPIO PIN10数据寄存器

   * - DATAPIN11

     - 0x6c

     - R/W

     - 0x00

     - GPIO PIN11数据寄存器

   * - DATAPIN12

     - 0x70

     - R/W

     - 0x00

     - GPIO PIN12数据寄存器

   * - DATAPIN13

     - 0x74

     - R/W

     - 0x00

     - GPIO PIN13数据寄存器

   * - DATAPIN14

     - 0x78

     - R/W

     - 0x00

     - GPIO PIN14数据寄存器

   * - DATAPIN15

     - 0x7c

     - R/W

     - 0x00

     - GPIO PIN15数据寄存器



