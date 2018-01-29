---
UID : NF:wdm.WRITE_PORT_UCHAR
title : WRITE_PORT_UCHAR function
author : windows-driver-content
description : The WRITE_PORT_UCHAR routine writes a byte to the specified port address.
old-location : kernel\write_port_uchar.htm
old-project : kernel
ms.assetid : 951b688f-21fa-4555-b877-e140e46a1700
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : k103_1495098b-03fb-4677-ac5a-2a1de9223f8b.xml, WRITE_PORT_UCHAR routine [Kernel-Mode Driver Architecture], WRITE_PORT_UCHAR, kernel.write_port_uchar, wdm/WRITE_PORT_UCHAR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Hal.lib
req.dll : 
req.irql : Any level (see Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# WRITE_PORT_UCHAR function
The <b>WRITE_PORT_UCHAR</b> routine writes a byte to the specified port address.

## Syntax

````
 VOID WRITE_PORT_UCHAR(
  _In_ PUCHAR Port,
  _In_ UCHAR  Value
);
````

## Parameters

`Port`

Pointer to the port, which must be a mapped memory range in I/O space.

`Value`

Specifies a byte to be written to the port.


## Return Value

None

## Remarks

Callers of <b>WRITE_PORT_UCHAR</b> can be running at any IRQL, assuming the <i>Port</i> is resident, mapped device memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | Any level (see Remarks section) |
| **DDI compliance rules** |  |