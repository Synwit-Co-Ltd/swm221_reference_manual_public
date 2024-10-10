.. ----------------------------------------------------------------------------------------------------

控制寄存器CR
^^^^^^^^^^^^^^^^^

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

     - WO

     - 0x00000000

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

   * - :cspan:`1` --

     - LINWKUP

     - LINABT

     - :cspan:`3` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - RETTO

     - :cspan:`2` --

     - STTTO

     - STPBRK

     - STTBRK

     - RSTSTA

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - TXDIS

     - TXEN

     - RXDIS

     - RXEN

     - RSTTX

     - RSTRX

     - :cspan:`1` --



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 21

     - LINWKUP

     - WO

     - 发送wakeup信号

   * - 20

     - LINABT

     - WO

     - 终止LIN传输

   * - 15

     - RETTO

     - WO

     - 重启接收超时检测

   * - 11

     - STTTO

     - WO

     - 开始接收超时检测

   * - 10

     - STPBRK

     - WO

     - 停止发送break

   * - 9

     - STTBRK

     - WO

     - 开始发送 break

   * - 8

     - RSTSTA

     - WO

     - 复位状态位

   * - 7

     - TXDIS

     - WO

     - 发送禁止

   * - 6

     - TXEN

     - WO

     - 发送使能

   * - 5

     - RXDIS

     - WO

     - 接收禁止

   * - 4

     - RXEN

     - WO

     - 接收使能

   * - 3

     - RSTTX

     - WO

     - 复位发送器

   * - 2

     - RSTRX

     - WO

     - 复位接收器



.. ----------------------------------------------------------------------------------------------------

模式寄存器MR
^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - MR

     - 0x04

     - R/W

     - 0x00000000

     - 模式寄存器



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

   * - :cspan:`3` --

     - OVER8

     - --

     - DATA9b

     - MSBF

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`1` --

     - :cspan:`1` NBSTOP

     - :cspan:`2` PARITY

     - --

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`1` NBDATA

     - :cspan:`1` CLKS

     - :cspan:`3` MODE



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 19

     - OVER8

     - R/W

     - 1 8x Oversampling，0 16x Oversampling

   * - 17

     - DATA9b

     - R/W

     - 1 数据位位数为9，0 数据位位数由NBDATA定义

   * - 16

     - MSBF

     - R/W

     - MSB first

   * - 13:12

     - NBSTOP

     - R/W

     - 停止位位数，0 1bit   1 1.5bit   2 2bit

   * - 11:9

     - PARITY

     - R/W

     - 校验位，0 Even parity   1 Odd parity   2 force 0   3 force 1   4 No parity

   * - 7:6

     - NBDATA

     - R/W

     - 数据位位数，0 5bit   1 6bit   2 7bit   3 8bit

   * - 5:4

     - CLKS

     - R/W

     - 时钟源选择

   * - 3:0

     - MODE

     - R/W

     - 0 UART   10 LIN Master   11 LIN Slave



.. ----------------------------------------------------------------------------------------------------

中断使能寄存器IER
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - IER

     - 0x08

     - WO

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

   * - HDRTO

     - --

     - NAKERR

     - CHKERR

     - IDERR

     - SYNCERR

     - BITERR

     - --

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

   * - DONE

     - ID

     - BRK

     - RXBFULL

     - TXBEMPTY

     - --

     - TXEMPTY

     - RXTO

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - PARITYERR

     - FRAMERR

     - OVRERR

     - :cspan:`1` --

     - RXBRK

     - TXRDY

     - RXRDY



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31

     - HDRTO

     - WO

     - LIN头超时中断

   * - 29

     - NAKERR

     - WO

     - LIN无从机响应错误中断

   * - 28

     - CHKERR

     - WO

     - LIN校验和错误中断

   * - 27

     - IDERR

     - WO

     - LIN ID校验错误中断

   * - 26

     - SYNCERR

     - WO

     - LIN同步域错误中断

   * - 25

     - BITERR

     - WO

     - 位错误中断

   * - 15

     - DONE

     - WO

     - LIN传输完成中断

   * - 14

     - ID

     - WO

     - 发送出或接收到LIN ID中断

   * - 13

     - BRK

     - WO

     - 发送出或接收到break中断

   * - 12

     - RXBFULL

     - WO

     - 接收缓冲满中断

   * - 11

     - TXBEMPTY

     - WO

     - 发送缓冲空中断

   * - 9

     - TXEMPTY

     - WO

     - 发送空中断

   * - 8

     - RXTO

     - WO

     - 接收超时中断

   * - 7

     - PARITYERR

     - WO

     - 接收奇偶校验错误中断

   * - 6

     - FRAMERR

     - WO

     - 接收帧错误中断

   * - 5

     - OVRERR

     - WO

     - 接收数据溢出中断

   * - 2

     - RXBRK

     - WO

     - 接收到break 中断

   * - 1

     - TXRDY

     - WO

     - 发送出数据中断，即THR为空

   * - 0

     - RXRDY

     - WO

     - 接收到数据中断，即 RHR 非空



.. ----------------------------------------------------------------------------------------------------

中断禁止寄存器IDR
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - IDR

     - 0x0C

     - WO

     - 0x00000000

     - 中断禁止寄存器



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

   * - HDRTO

     - --

     - NAKERR

     - CHKERR

     - IDERR

     - SYNCERR

     - BITERR

     - --

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

   * - DONE

     - ID

     - BRK

     - RXBFULL

     - TXBEMPTY

     - --

     - TXEMPTY

     - RXTO

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - PARITYERR

     - FRAMERR

     - OVRERR

     - :cspan:`1` --

     - RXBRK

     - TXRDY

     - RXRDY



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31

     - HDRTO

     - WO

     - LIN头超时中断

   * - 29

     - NAKERR

     - WO

     - LIN无从机响应错误中断

   * - 28

     - CHKERR

     - WO

     - LIN校验和错误中断

   * - 27

     - IDERR

     - WO

     - LIN ID校验错误中断

   * - 26

     - SYNCERR

     - WO

     - LIN同步域错误中断

   * - 25

     - BITERR

     - WO

     - 位错误中断

   * - 15

     - DONE

     - WO

     - LIN传输完成中断

   * - 14

     - ID

     - WO

     - 发送出或接收到LIN ID中断

   * - 13

     - BRK

     - WO

     - 发送出或接收到break中断

   * - 12

     - RXBFULL

     - WO

     - 接收缓冲满中断

   * - 11

     - TXBEMPTY

     - WO

     - 发送缓冲空中断

   * - 9

     - TXEMPTY

     - WO

     - 发送空中断

   * - 8

     - RXTO

     - WO

     - 接收超时中断

   * - 7

     - PARITYERR

     - WO

     - 接收奇偶校验错误中断

   * - 6

     - FRAMERR

     - WO

     - 接收帧错误中断

   * - 5

     - OVRERR

     - WO

     - 接收数据移除中断

   * - 2

     - RXBRK

     - WO

     - 接收到break 中断

   * - 1

     - TXRDY

     - WO

     - 发送出数据中断，即THR为空

   * - 0

     - RXRDY

     - WO

     - 接收到数据中断，即 RHR 非空



.. ----------------------------------------------------------------------------------------------------

中断屏蔽寄存器IMR
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - IMR

     - 0x10

     - RO

     - 0x00000000

     - 中断屏蔽寄存器



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

   * - HDRTO

     - --

     - NAKERR

     - CHKERR

     - IDERR

     - SYNCERR

     - BITERR

     - --

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

   * - DONE

     - ID

     - BRK

     - RXBFULL

     - TXBEMPTY

     - --

     - TXEMPTY

     - RXTO

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - PARITYERR

     - FRAMERR

     - OVRERR

     - :cspan:`1` --

     - RXBRK

     - TXRDY

     - RXRDY



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31

     - HDRTO

     - RO

     - LIN头超时中断

   * - 29

     - NAKERR

     - RO

     - LIN无从机响应错误中断

   * - 28

     - CHKERR

     - RO

     - LIN校验和错误中断

   * - 27

     - IDERR

     - RO

     - LIN ID校验错误中断

   * - 26

     - SYNCERR

     - RO

     - LIN同步域错误中断

   * - 25

     - BITERR

     - RO

     - 位错误中断

   * - 15

     - DONE

     - RO

     - LIN传输完成中断

   * - 14

     - ID

     - RO

     - 发送出或接收到LIN ID中断

   * - 13

     - BRK

     - RO

     - 发送出或接收到break中断

   * - 12

     - RXBFULL

     - RO

     - 接收缓冲满中断

   * - 11

     - TXBEMPTY

     - RO

     - 发送缓冲空中断

   * - 9

     - TXEMPTY

     - RO

     - 发送空中断

   * - 8

     - RXTO

     - RO

     - 接收超时中断

   * - 7

     - PARITYERR

     - RO

     - 接收奇偶校验错误中断

   * - 6

     - FRAMERR

     - RO

     - 接收帧错误中断

   * - 5

     - OVRERR

     - RO

     - 接收数据移除中断

   * - 2

     - RXBRK

     - RO

     - 接收到break 中断

   * - 1

     - TXRDY

     - RO

     - 发送出数据中断，即THR为空

   * - 0

     - RXRDY

     - RO

     - 接收到数据中断，即 RHR 非空



.. ----------------------------------------------------------------------------------------------------

中断状态寄存器ISR
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - ISR

     - 0x14

     - RO

     - 0x00000000

     - 中断状态寄存器



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

   * - HDRTO

     - --

     - NAKERR

     - CHKERR

     - IDERR

     - SYNCERR

     - BITERR

     - --

   * - 23

     - 22

     - 21

     - 20

     - 19

     - 18

     - 17

     - 16

   * - BUSSTA

     - :cspan:`6` --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - DONE

     - ID

     - BRK

     - RXBFULL

     - TXBEMPTY

     - --

     - TXEMPTY

     - RXTO

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - PARITYERR

     - FRAMERR

     - OVRERR

     - :cspan:`1` --

     - RXBRK

     - TXRDY

     - RXRDY



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 31

     - HDRTO

     - RO

     - LIN头超时中断

   * - 29

     - NAKERR

     - RO

     - LIN无从机响应错误中断

   * - 28

     - CHKERR

     - RO

     - LIN校验和错误中断

   * - 27

     - IDERR

     - RO

     - LIN ID校验错误中断

   * - 26

     - SYNCERR

     - RO

     - LIN同步域错误中断

   * - 25

     - BITERR

     - RO

     - 位错误中断

   * - 23

     - BUSSTA

     - RO

     - LIN总线当前状态

   * - 15

     - DONE

     - RO

     - LIN传输完成中断

   * - 14

     - ID

     - RO

     - 发送出或接收到LIN ID中断

   * - 13

     - BRK

     - RO

     - 发送出或接收到break中断

   * - 12

     - RXBFULL

     - RO

     - 接收缓冲满中断

   * - 11

     - TXBEMPTY

     - RO

     - 发送缓冲空中断

   * - 9

     - TXEMPTY

     - RO

     - 发送空中断

   * - 8

     - RXTO

     - RO

     - 接收超时中断

   * - 7

     - PARITYERR

     - RO

     - 接收奇偶校验错误中断

   * - 6

     - FRAMERR

     - RO

     - 接收帧错误中断

   * - 5

     - OVRERR

     - RO

     - 接收数据移除中断

   * - 2

     - RXBRK

     - RO

     - 接收到break 中断

   * - 1

     - TXRDY

     - RO

     - 发送出数据中断，即THR为空

   * - 0

     - RXRDY

     - RO

     - 接收到数据中断，即 RHR 非空



.. ----------------------------------------------------------------------------------------------------

接收保持寄存器RHR
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - RHR

     - 0x18

     - RO

     - 0x00000000

     - 接收保持寄存器



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

   * - :cspan:`6` --

     - DATA

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

   * - 8:0

     - DATA

     - RO

     - 接收到的数据



.. ----------------------------------------------------------------------------------------------------

发送保持寄存器THR
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - THR

     - 0x1C

     - WO

     - 0x00000000

     - 发送保持寄存器



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

   * - :cspan:`6` --

     - DATA

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

   * - 8:0

     - DATA

     - WO

     - 写入要发送的数据



.. ----------------------------------------------------------------------------------------------------

波特率寄存器BAUD
^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - BAUD

     - 0x20

     - R/W

     - 0x00000000

     - 波特率寄存器



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

   * - :cspan:`4` --

     - :cspan:`2` FDIV

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` IDIV

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` IDIV



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 18:16

     - FDIV

     - R/W

     - 小数分频部分

   * - 15:0

     - IDIV

     - R/W

     - 整数分频部分



.. ----------------------------------------------------------------------------------------------------

接收超时寄存器RXTO
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - RXTO

     - 0x24

     - R/W

     - 0x00000000

     - 接收超时寄存器



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

   * - :cspan:`7` Timeout

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` Timeout



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 15:0

     - Timeout

     - R/W

     - 接收超时时间



.. ----------------------------------------------------------------------------------------------------

LIN模式寄存器LINMR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - LINMR

     - 0x54

     - R/W

     - 0x00000000

     - LIN模式寄存器



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

     - SYNCDIS

     - --

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` DLC

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - WKUPTYP

     - FSMDIS

     - RDLMOD

     - CHKTYP

     - CHKDIS

     - PARDIS

     - :cspan:`1` NACT



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 17

     - SYNCDIS

     - R/W

     - 同步禁止

   * - 15:8

     - DLC

     - R/W

     - response data length is equal to DLC+1 bytes

   * - 7

     - WKUPTYP

     - R/W

     - 0 LIN 2.0 wakeup signal   1 LIN 1.3 wakeup signal

   * - 6

     - FSMDIS

     - R/W

     - Frame Slot Mode Disable

   * - 5

     - RDLMOD

     - R/W

     - 响应数据长度 defined by: 0 DLC field   1 the bits 5 and 6 of LINID register

   * - 4

     - CHKTYP

     - R/W

     - 校验类型，0 LIN 2.0 Enhanced Checksum   1 LIN 1.3 Classic Checksum

   * - 3

     - CHKDIS

     - R/W

     - 校验和禁止

   * - 2

     - PARDIS

     - R/W

     - 奇偶校验禁止

   * - 1:0

     - NACT

     - R/W

     - 节点动作，0 transmit the response   1 receive the response   2 ignore



.. ----------------------------------------------------------------------------------------------------

LIN ID寄存器LINID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - LINID

     - 0x58

     - R/W

     - 0x00000000

     - LIN ID寄存器



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

   * - :cspan:`7` --

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` ID



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 7:0

     - ID

     - R/W

     - LIN ID 字符



.. ----------------------------------------------------------------------------------------------------

LIN 波特率寄存器LINBR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. flat-table::
   :class: tight-table-reg-info
   :header-rows: 1

   * - 寄存器

     - 偏移

     - 类型

     - 复位值

     - 描述

   * - LINBR

     - 0x5C

     - RO

     - 0x00000000

     - LIN 波特率寄存器



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

   * - :cspan:`4` --

     - :cspan:`2` FDIV

   * - 15

     - 14

     - 13

     - 12

     - 11

     - 10

     - 9

     - 8

   * - :cspan:`7` IDIV

   * - 7

     - 6

     - 5

     - 4

     - 3

     - 2

     - 1

     - 0

   * - :cspan:`7` IDIV



.. ----------------------------------------------------------------------------------------------------

.. flat-table::
   :class: tight-table-reg-desc
   :header-rows: 1

   * - 位域

     - 名称

     - 类型

     - 描述

   * - 18:16

     - FDIV

     - RO

     - 小数分频部分

   * - 15:0

     - IDIV

     - RO

     - 整数分频部分，同步后读取返回当前波特率分频值



