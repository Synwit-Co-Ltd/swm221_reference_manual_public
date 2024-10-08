.. ----------------------------------------------------------------------------------------------------

CR
^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - CR

     - 0x00

     - R/W

     - 0x00000303

     - 控制寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`2` --

     - :cspan:`4` CLKDIV

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`1` AVG

     - SEQ1DMAEN

     - SEQ0DMAEN

     - :cspan:`1` BITS

     - RESET

     - PWDN



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31:13

     - --

     - 

     - --

   * - 12:8

     - CLKDIV

     - R/W

     - ADC转换时钟 = core_clk / (CLKDIV + 1)

   * - 7:6

     - AVG

     - R/W

     - 0：关闭多次转换、硬件取平均功能

       1：一次启动连续采样、转换2次，并计算两次结果的平均值作为转换结果

       2：一次启动连续采样、转换4次，并计算四次结果的平均值作为转换结果

       3：一次启动连续采样、转换8次，并计算八次结果的平均值作为转换结果


   * - 5

     - SEQ1DMAEN

     - R/W

     - 0：转换结果通过对应通道的数据寄存器读取

       1：转换结果通过SEQ1DMA读取


   * - 4

     - SEQ0DMAEN

     - R/W

     - 0：转换结果通过对应通道的数据寄存器读取

       1：转换结果通过SEQ0DMA读取


   * - 3:2

     - BITS

     - R/W

     - 输出位宽配置

       00：12 bit

       01：10 bit

       10：8 bit

       11：6 bit

       非12 bit输出模式下，有效数据高位对齐，低位输出为0


   * - 1

     - RESET

     - R/W

     - ADCx模拟电路内部逻辑复位，高电平复位有效, 软件置1，硬件自动清零。

       退出powerdown模式后（ADCx_PWD由1写为0），硬件会自动执行一次复位操作。ADCx_PWD为1时，写ADCx_RESET为1后不会自动清零。

       此位写0无效


   * - 0

     - PWDN

     - R/W

     - 1 ：Power Down

       0 ：正常工作模式，写 0 后需等待 32 个采样周期




.. ----------------------------------------------------------------------------------------------------

IE
^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - IE

     - 0x04

     - R/W

     - 0x00000000

     - 中断使能寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`4` --

     - SEQ1MIN

     - SEQ1MAX

     - SEQ1EOC

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`4` --

     - SEQ0MIN

     - SEQ0MAX

     - SEQ0EOC



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 10

     - SEQ1MIN

     - R/W

     - 序列1转换结果小于MIN中断

   * - 9

     - SEQ1MAX

     - R/W

     - 序列1转换结果大于MAX中断

   * - 8

     - SEQ1EOC

     - R/W

     - 序列1转换完成中断

   * - 2

     - SEQ0MIN

     - R/W

     - 序列0转换结果小于MIN中断

   * - 1

     - SEQ0MAX

     - R/W

     - 序列0转换结果大于MAX中断

   * - 0

     - SEQ0EOC

     - R/W

     - 序列0转换完成中断



.. ----------------------------------------------------------------------------------------------------

IF
^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - IF

     - 0x08

     - R/W1C

     - 0x00000000

     - 中断标志寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` --

     - SEQ1BRK

     - SEQ1MIN

     - SEQ1MAX

     - SEQ1EOC

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`3` --

     - SEQ0BRK

     - SEQ0MIN

     - SEQ0MAX

     - SEQ0EOC



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 11

     - SEQ1BRK

     - R/W1C

     - 序列1 CPU启动采样被PWM触发打断，状态位，不产生中断

   * - 10

     - SEQ1MIN

     - R/W1C

     - 序列1转换结果小于MIN中断

   * - 9

     - SEQ1MAX

     - R/W1C

     - 序列1转换结果大于MAX中断

   * - 8

     - SEQ1EOC

     - R/W1C

     - 序列1转换完成中断

   * - 3

     - SEQ0BRK

     - R/W1C

     - 序列0 CPU启动采样被PWM触发打断，状态位，不产生中断

   * - 2

     - SEQ0MIN

     - R/W1C

     - 序列0转换结果小于MIN中断

   * - 1

     - SEQ0MAX

     - R/W1C

     - 序列0转换结果大于MAX中断

   * - 0

     - SEQ0EOC

     - R/W1C

     - 序列0转换完成中断



.. ----------------------------------------------------------------------------------------------------

SMPNUM
^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SMPNUM

     - 0x0C

     - R/W

     - 0x00000000

     - 采样次数寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` SEQ1

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` SEQ0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 15:8

     - SEQ1

     - R/W

     - 一次启动后，序列1连续转换次数，0表示1次，1表示2次，

   * - 7:0

     - SEQ0

     - R/W

     - 一次启动后，序列0连续转换次数，0表示1次，1表示2次，



.. ----------------------------------------------------------------------------------------------------

SMPTIM
^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SMPTIM

     - 0x10

     - R/W

     - 0x00000000

     - 采样时间寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` SEQ1

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` SEQ0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 15:8

     - SEQ1

     - R/W

     - ADC转换前对信号的采样时间，0表示4个时钟周期，1表示5个时钟周期，

   * - 7:0

     - SEQ0

     - R/W

     - ADC转换前对信号的采样时间，0表示4个时钟周期，1表示5个时钟周期，



.. ----------------------------------------------------------------------------------------------------

SEQTRG
^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQTRG

     - 0x14

     - R/W

     - 0x00000000

     - 序列触发源选择寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` SEQ1

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` SEQ0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 15:8

     - SEQ1

     - R/W

     - 序列1触发信号

   * - 7:0

     - SEQ0

     - R/W

     - 序列0触发信号

       0：无触发

       1：CPU触发

       2-4：timer0~timer2触发

       16-17：pwm0~pwm1触发




.. ----------------------------------------------------------------------------------------------------

SEQ0CHN
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ0CHN

     - 0x18

     - R/W

     - 0x00000000

     - 序列0通道选择寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`3` CH7

     - :cspan:`3` CH6

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`3` CH5

     - :cspan:`3` CH4

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` CH3

     - :cspan:`3` CH2

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`3` CH1

     - :cspan:`3` CH0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31:28

     - CH7

     - R/W

     - 序列0中第八个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 27:24

     - CH6

     - R/W

     - 序列0中第七个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 23:20

     - CH5

     - R/W

     - 序列0中第六个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 19:16

     - CH4

     - R/W

     - 序列0中第五个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 15:12

     - CH3

     - R/W

     - 序列0中第四个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 11:8

     - CH2

     - R/W

     - 序列0中第三个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 7:4

     - CH1

     - R/W

     - 序列0中第二个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 3:0

     - CH0

     - R/W

     - 序列0中第一个转换通道的通道号，取值0-9，0xF表示通道号查询终止



.. ----------------------------------------------------------------------------------------------------

SEQ1CHN
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ1CHN

     - 0x1C

     - R/W

     - 0x00000000

     - 序列1通道选择寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`3` CH7

     - :cspan:`3` CH6

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`3` CH5

     - :cspan:`3` CH4

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` CH3

     - :cspan:`3` CH2

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`3` CH1

     - :cspan:`3` CH0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31:28

     - CH7

     - R/W

     - 序列1中第八个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 27:24

     - CH6

     - R/W

     - 序列1中第七个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 23:20

     - CH5

     - R/W

     - 序列1中第六个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 19:16

     - CH4

     - R/W

     - 序列1中第五个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 15:12

     - CH3

     - R/W

     - 序列1中第四个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 11:8

     - CH2

     - R/W

     - 序列1中第三个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 7:4

     - CH1

     - R/W

     - 序列1中第二个转换通道的通道号，取值0-9，0xF表示通道号查询终止

   * - 3:0

     - CH0

     - R/W

     - 序列1中第一个转换通道的通道号，取值0-9，0xF表示通道号查询终止



.. ----------------------------------------------------------------------------------------------------

SEQ0CHK
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ0CHK

     - 0x20

     - R/W

     - 0x00000FFF

     - 序列0转换结果检查寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`3` --

     - :cspan:`3` MIN

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` MIN

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` --

     - :cspan:`3` MAX

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` MAX



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 27:16

     - MIN

     - R/W

     - 当转换结果小于此值时，可触发中断

   * - 11:0

     - MAX

     - R/W

     - 当转换结果大于此值时，可触发中断



.. ----------------------------------------------------------------------------------------------------

SEQ1CHK
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ1CHK

     - 0x24

     - R/W

     - 0x00000FFF

     - 序列1转换结果检查寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`3` --

     - :cspan:`3` MIN

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` MIN

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` --

     - :cspan:`3` MAX

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` MAX



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 27:16

     - MIN

     - R/W

     - 当转换结果小于此值时，可触发中断

   * - 11:0

     - MAX

     - R/W

     - 当转换结果大于此值时，可触发中断



.. ----------------------------------------------------------------------------------------------------

DATA0-9
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - DATA0

     - 0x30

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA1

     - 0x34

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA2

     - 0x38

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA3

     - 0x3C

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA4

     - 0x40

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA5

     - 0x44

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA6

     - 0x48

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA7

     - 0x4C

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA8

     - 0x50

     - RO

     - 0x00000000

     - 转换结果寄存器

   * - DATA9

     - 0x54

     - RO

     - 0x00000000

     - 转换结果寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`5` --

     - :cspan:`1` FLAG

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` --

     - :cspan:`3` DATA

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` DATA



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 17:16

     - FLAG

     - RO

     - 0 自上次读取无新数据   1 有新数据   2 发生过数据覆盖

   * - 11:0

     - DATA

     - RO

     - 通道转换结果



.. ----------------------------------------------------------------------------------------------------

SEQ0DMA
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ0DMA

     - 0x70

     - RO

     - 0x00000000

     - 序列0 DMA访问寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`5` --

     - :cspan:`1` FLAG

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` CHNUM

     - :cspan:`3` DATA

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` DATA



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 17:16

     - FLAG

     - RO

     - 0 自上次读取无新数据   1 有新数据   2 发生过数据覆盖

   * - 15:12

     - CHNUM

     - RO

     - 转换结果来自哪个通道

   * - 11:0

     - DATA

     - RO

     - 通道转换结果



.. ----------------------------------------------------------------------------------------------------

SEQ1DMA
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - SEQ1DMA

     - 0x74

     - RO

     - 0x00000000

     - 序列1 DMA访问寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`5` --

     - :cspan:`1` FLAG

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`3` CHNUM

     - :cspan:`3` DATA

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` DATA



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 17:16

     - FLAG

     - RO

     - 0 自上次读取无新数据   1 有新数据   2 发生过数据覆盖

   * - 15:12

     - CHNUM

     - RO

     - 转换结果来自哪个通道

   * - 11:0

     - DATA

     - RO

     - 通道转换结果



.. ----------------------------------------------------------------------------------------------------

START
^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - START

     - 0x200

     - R/W

     - 0x00000000

     - 转换启动寄存器



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-fields

   * - 31

     - 30

     - 29

     - 28

     - 27

     - 26

     - 25

     - 24

   * - :cspan:`7` --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - :cspan:`7` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`4` --

     - ADC1BUSY

     - ADC1SEQ1

     - ADC1SEQ0

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`4` --

     - ADC0BUSY

     - ADC0SEQ1

     - ADC0SEQ0



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 10

     - ADC1BUSY

     - RO

     - ADC1 busy flag

   * - 9

     - ADC1SEQ1

     - R/WAC

     - ADC1 SEQ1 启动位，写1启动ADC1 SEQ1转换，自动清零

   * - 8

     - ADC1SEQ0

     - R/WAC

     - ADC1 SEQ0 启动位，写1启动ADC1 SEQ0转换，自动清零

   * - 2

     - ADC0BUSY

     - RO

     - ADC0 busy flag

   * - 1

     - ADC0SEQ1

     - R/WAC

     - ADC0 SEQ1 启动位，写1启动ADC0 SEQ1转换，自动清零

   * - 0

     - ADC0SEQ0

     - R/WAC

     - ADC0 SEQ0 启动位，写1启动ADC0 SEQ0转换，自动清零



