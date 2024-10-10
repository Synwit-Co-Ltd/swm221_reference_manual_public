
FLASH操作
^^^^^^^^^^^^^

FLASH操作可以通过寄存器进行操作，也可以通过IAP函数进行擦除及写入。

寄存器操作
~~~~~~~~~~~

**ERASE操作:**
   -  使能FLASH擦写使能位

   -  配置擦page的地址

   -  查询ERASE位等待擦完成，直至状态从1变为0，擦除完成。当Flash完成擦除操作后，方可进行其他操作
      

**PROGRAM 操作:**
   -  使能FLASH擦写使能位

   -  配置FLASH写地址，必须字对齐

   -  配置FLASH要写的数据

   -  查询PROEND位等待写完成


.. attention:: 以上操作流程均可在 FLASH 或 SRAM 中执行


.. attention::SWM221系列芯片FLASH每PAGE为512 Bytes ，每次最少写1 word

    
IAP操作
~~~~~~~~

IAP 函数作为片内驻留程序，其提供了针对flash 的相关操作IAP 函数为Thumb
代码，分为擦除函数（驻留地址为 0x1000401）和写入函数（驻留地址为 0x1000461），建议使用如下方式调用：

**擦除函数:**

.. list-table::
   :class: table-left-align

   * - **定义函数类型:**
   
   * - typedef uint32_t (\*IAPFunc1) (uint32_t PageNum);
       
       IAPFunc1 FLASH_PageErase = (IAPFunc1) 0x1000401;
   
   * - **变量定义如下：**
   
   * - PageNum： FLASH 擦除目标页码，以 page 为单位，0 为首地址，N 为 page * N 对应地址
   
   * - **返回值:**
       
   * - 0：擦除成功
       
       1：擦除失败，参数错误

   * - **调用**
   
   * - Result = FLASH_PageErase(10);

   * - 擦除第 10 * page 的内容。Result 返回 0 表示成功。


**写入函数:**

.. list-table::
   :class: table-left-align
     
   * - **定义函数类型:**
 
   * - typedef void (\*IAPFunc2) (uint32_t faddr, uint32_t raddr, uint32_t cnt);

       IAPFunc2 FLASH_PageWrite = (IAPFunc2) 0x1000461;

   * - **变量定义如下：**

   * - faddr： FLASH 写入目标地址，字对齐

       raddr： RAM 写入目标地址，字对齐

       cnt： 写入数量，字为单位，长度不超过1page
   
   * - **返回值:**

   * - 0：写入成功

       1：写入失败，参数错误
 
   * - **调用:**

   * - Result = FLASH_PageWrite(0x400, 0x20000400, 8)；

   * - 将 RAM 地址 0x20000400 开始的 8 * 4 个字节写入flash 地址 0x400 起始。Result 返回 0 表示成功。


调用 IAP 函数时，应保证栈空间剩余 24 个字节（byte）以上。执行写操作前，需确认对应目标地址已经执行过擦除操作。

.. note:: 详细IAP操作请参阅库函数。 


ISP（在系统编程）模式
^^^^^^^^^^^^^^^^^^^^^

当芯片上电后检测到 ISP 引脚持续 5ms 以上的高电平后，将会进入 ISP 模式。配合上位机及串口可执行程序更新操作，具体引脚请参考管脚定义章节。

.. attention:: ISP方式的串口烧录时，默认使用 C0 (UART1_TX) 以及 C1 (UART1_TX) 作为串口通讯使用。

.. note:: 详细ISP操作请参阅应用文档及库函数。

BOOT 自定义
^^^^^^^^^^^^^^

FLASH 地址空间支持将指定地址的 2KB 数据映射至 0x00000000 空间，通过 REMAP 寄存器实现。将地址（2KB 对齐）写入 REMAP 寄存器 BASEADD，并将 EN 位置1，则指定地址内容将被映射至 0x00000000 空间，可通过此功能实现向量表的重映射。

例如

BOOT： 0x00000000 ~ 0x00004000

USER： 0x00004000 ~ 0x00008000

在 BOOT 中配置 REMAP 寄存器地址为 0x00004000 并使能，并跳转至 USER 执行，当读取 0x00000000 地址时，返回内容为 0x00004000 地址内容。


加密方式
^^^^^^^^^^^^

控制器加密支持以下三种级别：

.. flat-table::
   :header-rows: 1
   :widths: 10 38 24

   - 

      - 级别
      - 说明
      - 关键字值
   - 

      - 级别1
      - 不加密，SWD可正常读写
      - 0x00000000
   - 

      - 级别2
      - SWD读取加密，SWD无法读取FLASH，只能执行擦除操作，连接SWD后，FLASH无法执行读操作，读取FLASH会进入Hardfault
      - 0x43211234
   - 

      - 级别3
      - SWD封锁，SWD无法执行读取及擦除工作，只能通过ISP读取
      - 0xABCD1234

.. hint:: 通过在用户程序中将 0x0000001C 偏移地址配置为指定关键字，即可实现指定级别的加密。程序下载后再次上电后，芯片将处于指定加密级别的状态。

