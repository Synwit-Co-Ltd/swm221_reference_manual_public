.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :header-rows: 1
   :class: tight-table-reg-map

   * - 名称

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - :cspan:`4` 

       UART0		  BASE：0x40040000

       UART1		  BASE：0x40040800


   * - DATA

     - 0x00

     - R/W

     - 0x00000000

     - UART数据寄存器

   * - CTRL

     - 0x04

     - R/W

     - 0x00000001

     - UART 控制及状态寄存器

   * - BAUD

     - 0x08

     - R/W

     - 0xF0184000

     - UART 波特率控制寄存器

   * - FIFO

     - 0x0C

     - R/W

     - 0x00000000

     - UART 数据队列寄存器

   * - LINCR

     - 0x10

     - R/W

     - 0x00000000

     - LIN Frame 控制寄存器

   * - FCCTRL

     - 0x14

     - R/W

     - 0x00000000

     - 自动流控控制寄存器

   * - CFG

     - 0x18

     - RO

     - 0x00000334

     - CFG 寄存器

   * - TOCTRL

     - 0x1C

     - RO

     - 0x00000000

     - 接收超时控制寄存器



