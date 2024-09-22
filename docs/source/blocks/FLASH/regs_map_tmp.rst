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

       FLASHCTL	        BASE：0x40045000

       


   * - DATA

     - 0x00

     - W

     - N/A

     - eFlash write FIFO

   * - ADDR

     - 0x04

     - W

     - 0

     - eFlash 写入地址

   * - ERASE

     - 0x08

     - RW

     - 0x0

     - 擦除操作请求

   * - CACHE

     - 0x0c

     - RW

     - 0x0

     - Cache 配置寄存器

   * - CFG0

     - 0x10

     - RW

     - 0x0

     - Flash 配置寄存器0

   * - CFG1

     - 0x14

     - WO

     - 0x0

     - Flash 配置寄存器1

   * - CFG2

     - 0x18

     - RW

     - 0x53

     - Flash 配置寄存器2

   * - CFG3

     - 0x1c

     - RW

     - 0x09C4_88B8

     - Flash 配置寄存器3

   * - CFG4

     - 0x20

     - RW

     - 0x2af8_ea60

     - Flash 配置寄存器4

   * - STAT

     - 0x24

     - RO

     - 0xA8

     - Flash 状态寄存器

   * - REMAP

     - 0x28

     - RW

     - 0x0

     - Remap寄存器



