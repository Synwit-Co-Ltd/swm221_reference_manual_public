I2C总线控制器（I2C）
--------------------

概述
~~~~

SWM221系列所有型号I2C操作均相同，不同型号I2C模块数量可能不同。使用前需使能对应I2C模块时钟。

I2C模块提供了MASTER模式及SLAVE模式，基本操作及配置详见功能描述章节。

特性
~~~~

-  支持通过APB总线进行配置

-  支持master、slave两种模式

-  支持I2C输入信号数字滤波

-  支持Standard-mode（100kbps）、Fast-mode（400kbps）、Fast-mode
   Plus（1Mbps）、High-speed mode（3.4Mbps）

-  SCL/SDA线上数据可读

-  Master模式特性：

   -  支持clock synchronization

   -  支持多master总线仲裁

   -  支持clock stretching，slave器件可通过拉低SCL来hold总线

   -  支持SCL LOW超时报警

   -  支持读、写操作

   -  支持发出的SCL时钟周期最大为（2^17）\*pclk

   -  SCL时钟占空比可配置

-  Slave模式特性：

   -  支持多slave

   -  支持7位、10位两种地址模式

   -  支持地址mask，一个slave器件可以占用多个地址

      -  7位地址模式，一个slave器件最多可占用128个地址

      -  10位地址模式，一个slave器件最多可占用256个地址

   -  支持clock stretching，slave器件可通过拉低SCL来hold总线

   -  支持读、写操作

模块结构框图
~~~~~~~~~~~~

|image1|

图 6‑46 I2C模块结构框图

功能描述
~~~~~~~~

基本操作
^^^^^^^^

总线设置

I2C总线采用串行数据线(SDA)和串行时钟线(SCL)传输数据。I2C总线的设备端口为开漏输出，必须在接口外接上拉电阻。

数据在主从设备之间通过SCL时钟信号在SDA数据线上逐字节同步传输。每一个SCL时钟脉冲发送一位数据，高位在前。每发送一个字节的数据产生一个应答信号。在时钟线SCL高电平期间对数据的每一位进行采样。数据线SDA在时钟线SCL为低改变，在时钟线SCL为高电平时保持稳定。

协议介绍

通常情况下，一个标准的通信包含四个部分：开始信号、从机地址、数据传输、停止信号。如图
6‑47所示：

|image2|

图 6‑47 I2C通信示意图

起始位发送

当总线空闲时，表示没有主机设备占用总线（SCL和SDA都保持高电平），主机可以通过发送一个起始信号启动传输。启动信号，通常被称为S位。SCL为高电平时，SDA由高电平向低电平跳变。启动信号表示开始新的数据传输。

重新启动是没有先产生一个停止信号的启动信号。主机使用此方法与另一个从机或者在不释放总线的情况下与相同的从机改变数据传输方向（例如从写入设备到写入设备的转换）。

当命令寄存器的STA位被置位，同时RD或者WR位被置位时，系统核心产生一个启动信号。根据SCLK的当前的不同状态，生成启动信号或重复启动信号。

地址发送

在开始信号后，由主机传输的第一个字节数据是从机地址。包含7位的从设备地址和1位的RW指示位。RW指示位信号表示与从机的数据传输方向。在系统中的从机不可以具有相同的地址。只有从机地址和主机发送的地址匹配时才能产生一个应答位（在第九个时钟周期拉低SDA）进行响应。对于10位从机地址，模块通过产生两个从机地址支持。

发送从机地址为一次写操作，在传输寄存器中保存从机地址并对WR位置位，从机地址将被发送到总线上。

数据发送

一旦成功取得了从机地址，主机就可以通过R/W位控制逐字节的发送数据。每传输一个字节都需要在第九个时钟周期产生一个应答位。

如果从机信号无效，主机可以生成一个停止信号中止数据传输或生成重复启动的信号并开始一个新的传输周期。如果从机返回一个NACK信号，主机就会产生一个停止信号放弃数据传输，或者产生一个重新启动信号开始一个新的传输周期。

如果主机作为接收设备，没有应答从机，从机就会释放SDA，主机产生停止信号或者重新启动信号。

向从机写入数据，需把将要发送的数据存入传输寄存器中并设置WR位。从从机中读取数据，需设置RD位。在数据传输过程中系统核心设置TIP提示标志，指示传输正在进行。当传输完成后TIP提示标志会自动清除。当中断使能时，中断标志位IF被置位，并产生中断。当中断标志位IF被置位后，接收寄存器收到有效数据。当TIP提示标志复位后，用户可以发出新的写入或读取命令。

停止位发送

主机可以通过生成一个停止信号终止通信。停止信号通常被称为P位，被定义为SCL为高电平时，SDA由低电平向高电平跳变。

Master SCL周期配置
^^^^^^^^^^^^^^^^^^

|image3|

图 6‑48 Master SCL周期配置示意图

主机发送模式
^^^^^^^^^^^^

I2C模块作为主机，初始化配置操作如下：

-  配置PORTCON模块中端口对应PORTx_FUNC寄存器，将指定引脚切换为功能复用

-  配置PORTCON模块中端口对应PULLU_x上拉使能寄存器，使能端口内部上拉电阻（也可使用外部上拉电阻）

-  配置PORTCON模块中端口对应INEN_x输入使能寄存器，使能I2C数据线输入功能

-  配置CR寄存器的EN位，关闭I2C模块，确保配置寄存器过程中模块未工作

-  配置CR寄存器的MASTER位，将I2C模块设置为主机模式

-  配置CR寄存器的EN位，I2C模块总线使能

-  设置时序配置寄存器CLK，假设pclk=48M，希望I2C工作在Standard-mode（100kbps）速度下，则每个SCL
   480个pclk，可以设置SCLL=0Xa0，SCLH =0x50，DIV=0x01

-  查询SR.BUSY，如果为1，则等待直至其变为0；如果为0，则进行下一步

-  发送Start。设置MCR.STA=1，查询该位，直至其变为0

-  发slave地址字节

-  设置TXDATA为【7位slave地址字节左移一位】

-  设置MCR.WR=1，查询该位，直至其变为0（或查询到IF的TXDONE=1（发送成功）或AL=1（仲裁丢失总线），并写1清除）

-  如果TXDONE=1，读TR.RXACK，如果该位为0，表示slave地址匹配成功

-  如果AL=1，表示本master失去总线，不能再进行后续操作，需重新查询SR.BUSY位直至1，才可以重新发送Start位，重新申请总线操作

   -  向slave发送待写数据

-  设置TXDATA，准备待写入slave的数据

-  设置MCR.WR=1，查询该位，直至其变为0（或查询到RIST的TXDONE=1，并写1清除）

-  读TR.RXACK，如果该位为0，表示写数据成功

   -  发STOP。设置MCR.STO=1，查询该位，直至其变为0

示意图如图 6‑49所示：

|image4|

图 6‑49 Master 寄存器时序示意图

*注：*\ *图中红色部分表示软件操作*

主机接收模式
^^^^^^^^^^^^

I2C作为主机接收模式，需将I2C模块设置为MASTER，初始化过程与主发送模式相同。

I2C作为主机从从机接收数据操作流程如下：

-  配置PORTCON模块中端口对应PORTx_FUNC寄存器，将指定引脚切换为功能复用

-  配置PORTCON模块中端口对应PULLU_x上拉使能寄存器，使能端口内部上拉电阻（也可使用外部上拉电阻）

-  配置PORTCON模块中端口对应INEN_x输入使能寄存器，使能I2C数据线输入功能

-  配置CR寄存器的EN位，关闭I2C模块，确保配置寄存器过程中模块未工作

-  配置CR寄存器的MASTER位，将I2C模块设置为主机模式

-  配置CR寄存器的EN位，I2C模块总线使能

-  设置时序配置寄存器CLK，假设pclk=48M，希望I2C工作在Standard-mode（100kbps）速度下，则每个SCL
   480个pclk，可以设置SCLL=0Xa0，SCLH =0x50，DIV=0x01

-  查询SR.BUSY，如果为1，则等待直至其变为0；如果为0，则进行下一步

-  发送Start。设置MCR.STA=1，查询该位，直至其变为0

-  发slave地址字节

-  设置TXDATA为【7位slave地址字节地址右移1位】

-  设置MCR.WR=1，查询该位，直至其变为0（或查询到IF的TXDONE=1（发送成功）或AL=1（仲裁丢失总线），并写1清除）

-  如果TXDONE=1，读TR.RXACK，如果该位为0，表示slave地址匹配成功

-  如果AL=1，表示本master失去总线，不能再进行后续操作，需重新查询SR.BUSY位直至1，才可以重新发送Start位，重新申请总线操作

   -  从slave读数据

-  设置TR.TXACK=0

-  设置MCR.RD=1，查询直到IF.RXNE=1

-  读取RXDATA，得到slave数据

-  查询MCR.RD，直至其变为0（或查询到IF.RXDONE=1，并写1清除）

   -  发STOP。设置MCR.STO=1，查询该位，直至其变为0

从发送模式
^^^^^^^^^^

I2C作为从发送模式，需将I2C模块设置为SLAVE，具体软件配置操作如下：

-  配置PORTCON模块中端口对应PORTx_FUNC寄存器，将指定引脚切换为功能复用

-  配置PORTCON模块中端口对应PULLU_x上拉使能寄存器，使能端口内部上拉电阻（也可使用外部上拉电阻）

-  配置PORTCON模块中端口对应INEN_x输入使能寄存器，使能I2C数据线输入功能

-  配置CR寄存器的EN位，关闭I2C模块，确保配置寄存器过程中模块未工作

-  配置CR寄存器的MASTER位，将I2C模块设置为从机模式

-  配置CR寄存器的EN位，I2C模块总线使能

-  设置slave地址模式。SCR.SADDR10=0

-  设置slave地址SADDR

-  查询直至IF.RXSTA，表示检测到I2C总线上有start发出

-  查询直至IF.RXNE=1。表示有master选中本器件

-  如果SADDR中设置了地址mask，则读取RXDATA，判断master发送的实际地址

-  如果判断到TR.SLVRD=1，表示master希望从slave读取数据

-  准备数据，写TXDATA

-  查询直到RXDONE=1，表示之前地址匹配后，返回ACK结束

-  查询直到IF.TXE=1，就可以向TXDATA中写入新数据了

-  查询直到IF.TXDONE=1，表示数据发送完成。然后写1清除

-  查询TR.RXACK，如果为0，表示master希望继续接收数据，则可重新向TXDATA中写入数据；如果RXACK=1，表示master希望结束读操作，则设置TR.TXCLR，清除之前预准备到TXDATA中的最后一个数据。转入下一步

-  查询到IF.RXSTO，表示检测到I2C总线上有STOP发出。本次会话结束

示意图如图 6‑50所示：

|image5|

图 6‑50 Slave 寄存器时序示意图

*注1：图中红色部分表示软件操作*

*注2：图中t1= tLOW，由CLK寄存器设置*

从接收模式
^^^^^^^^^^

I2C作为从接收模式，需将I2C模块设置为SLAVE，操作流程如下：

-  配置PORTCON模块中端口对应PORTx_FUNC寄存器，将指定引脚切换为功能复用

-  配置PORTCON模块中端口对应PULLU_x上拉使能寄存器，使能端口内部上拉电阻（也可使用外部上拉电阻）

-  配置PORTCON模块中端口对应INEN_x输入使能寄存器，使能I2C数据线输入功能

-  配置CR寄存器的EN位，关闭I2C模块，确保配置寄存器过程中模块未工作

-  配置CR寄存器的MASTER位，将I2C模块设置为从机模式

-  配置CR寄存器的EN位，I2C模块总线使能

-  设置slave地址模式。SCR.SADDR10=0

-  设置slave地址SADDR

-  查询直至IF.RXSTA，表示检测到I2C总线上有start发出

-  查询直至IF.RXNE=1。表示有master选中本器件

-  如果SADDR中设置了地址mask，则读取RXDATA，判断master发送的实际地址

-  如果判断到TR.SLVWR=1，表示master希望向slave写入数据

-  查询直到RXDONE=1，表示之前地址匹配后，返回ACK结束。然后写1清除

-  设置TR.TXACK=0

-  查询直到IF.RXNE=1，表示slave接收到新数据，读取RXDATA

-  查询直到RXDONE=1，表示之前接收数据后，返回ACK结束。然后写1清除

-  可重复查询IF.RXNE位，继续接收数据，直到查询到IF.RXSTO，表示本次会话结束

时钟延展clock stretching
^^^^^^^^^^^^^^^^^^^^^^^^

clock
stretching通过将SCL线拉低来暂停一个传输，直到释放SCL线为高电平,传输才继续进行。

以master-receiver，slave-transmitter为例，具体软件配置操作如下：

-  配置PORTCON模块中端口对应PORTx_FUNC寄存器，将指定引脚切换为功能复用

-  配置PORTCON模块中端口对应PULLU_x上拉使能寄存器，使能端口内部上拉电阻（也可使用外部上拉电阻）

-  配置PORTCON模块中端口对应INEN_x输入使能寄存器，使能I2C数据线输入功能

-  配置CR寄存器的EN位，关闭I2C模块，确保配置寄存器过程中模块未工作

-  配置CR寄存器的MASTER位，将I2C模块设置为主机模式

-  配置CR寄存器的EN位，I2C模块总线使能

-  设置时序配置寄存器CLK，假设pclk=48M，希望I2C工作在Standard-mode（100kbps）速度下，则每个SCL
   480个pclk，可以设置SCLL=0Xa0，SCLH =0x50，DIV=0x01

-  查询SR.BUSY，如果为1，则等待直至其变为0；如果为0，则进行下一步

-  发送Start。设置MCR.STA=1，查询该位，直至其变为0

-  发slave地址字节

-  设置TXDATA为【7位slave地址字节左移一位】

-  设置MCR.WR=1，查询该位，直至其变为0（或查询到IF的TXDONE=1（发送成功）或AL=1（仲裁丢失总线），并写1清除）

-  如果TXDONE=1，读TR.RXACK，如果该位为0，表示slave地址匹配成功

-  如果AL=1，表示本master失去总线，不能再进行后续的步骤6~7，需查询直至SR.BUSY=1，才可以回到步骤4，重新发送Start位，重新申请总线操作

   -  向slave发送待写数据

-  设置TXDATA，准备待写入slave的数据

-  设置MCR.WR=1，查询该位，直至其变为0（或查询到RIST的TXDONE=1，并写1清除）

-  读TR.RXACK，如果该位为0，表示写数据成功

   -  发STOP。设置MCR.STO=1，查询该位，直至其变为0

HS-MODE
^^^^^^^

以master-transmitter为例

具体软件配置操作如下：

-  设置CR.HS=0，以普通模式发第一个字节

-  以主机发送模式的方式，先在F/S-mode下发送START和master
   code。在此过程中，可以进行multi-master的总线仲裁

-  如果本master获得了总线控制权。则进行如下步骤

-  设置CR.HS=1。才可以设置为高速模式

-  设置CLK寄存器。假设pclk=60M，希望I2C工作在HS-mode（3.4Mbps）速度下，则每个SCL
   14个pclk，可以设置SCLL=0x0A，SCLH=0x05，DIV=0x0

-  以主机发送模式的方式，以High-speed发送Sr和slave地址（不需要再判断IF.AL位）、写数据等

以slave-receiver为例

具体软件配置操作如下：

-  根据F/S-mode速度设置CLK寄存器

-  设置CR.MASTER=0（slave），CR.EN=1，CR.HS=0

-  设置slave SCR.MCDE=1，等待master发送master code

-  查询直到RXNE=1，表示接收到master code

-  读取RXDATA中的数据，判断是multi-master中的哪一个master获得了总线。（对于single-master情况，可以省略此判断，但RXDATA中的数据需要读走，否则会影响后续地址和数据的接收）

-  设置HS-mode，后续操作在HS-mode下进行。设置CR.HS=1；设置SCR.MCDE=0

-  根据HS-mode速度设置CLK寄存器

-  设置slave地址模式及地址。设置SCR.SADDR10，并相应设置SADDR

-  查询直到IF.RXSTA=1，表示接收到Sr

-  查询直到RXNE=1，表示接收到匹配的地址

-  根据从机接收模式的操作继续后续操作，直至结束本次会话

中断清除
^^^^^^^^

此模块中中断状态位详见寄存器中各个中断标志位属性，当其中断标志位属性为R/W1C时，如需清除此标志，需在对应标志位中写1清零（R/W1C），否则中断在开启状态下会一直进入；当其中断标志位属性为AC时，表示此中断状态位会自动清零；当其中断标志位属性为RO时，表示此标志位会随着水位的变化而改变，标志位只与其当前状态有关，不需要清除。具体详见寄存器描述。

.. |image1| image:: media/image1.emf
.. |image2| image:: media/image2.emf
.. |image3| image:: media/image3.emf
.. |image4| image:: media/image4.emf
.. |image5| image:: media/image5.emf
