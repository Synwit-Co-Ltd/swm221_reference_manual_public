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

       BTIMER0		  BASE：0x40044000

       BTIMER1		  BASE：0x40044040

       BTIMER2		  BASE：0x40044080

       BTIMER3		  BASE：0x400440C0


   * - LOAD

     - 0x00

     - R/W

     - 0x00

     - 计数器初始值

   * - VALUE

     - 0x04

     - RO

     - 0x01

     - 计数器当前值。

   * - CR

     - 0x08

     - R/W

     - 0x00

     - 定时器控制寄存器

   * - IE

     - 0x10

     - R/W

     - 0x00

     - 定时器中断使能

   * - IF

     - 0x14

     - R/W1C

     - 0x00

     - 定时器中断状态。写1清零

   * - OCCR

     - 0x1C

     - R/W

     - 0x00

     - 输出PWM的控制信号。当PONO>x时才有效，否则该寄存器为只读，且为0

   * - OCMAT

     - 0x20

     - R/W

     - 0x00

     - PWM输出高电平宽度。当POTVAL0==0时，占空比为0；当POTVAL0>LDVALU时，占空比为100%

   * - PREDIV

     - 0x30

     - R/W

     - 0x00

     - 计数器预分频

   * - EN

     - 0x440

     - R/W

     - 0x00

     - 定时器使能



