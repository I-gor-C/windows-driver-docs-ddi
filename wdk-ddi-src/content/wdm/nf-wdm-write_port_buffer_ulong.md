---
UID : NF:wdm.WRITE_PORT_BUFFER_ULONG
title : WRITE_PORT_BUFFER_ULONG function
author : windows-driver-content
description : The WRITE_PORT_BUFFER_ULONG routine writes a number of ULONG values from a buffer to the specified port address.
old-location : kernel\write_port_buffer_ulong.htm
old-project : kernel
ms.assetid : 6f786456-344a-4fc3-bc13-8d4253f4039a
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : WRITE_PORT_BUFFER_ULONG
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
req.alt-api : WRITE_PORT_BUFFER_ULONG
req.alt-loc : Hal.lib,Hal.dll
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
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# WRITE_PORT_BUFFER_ULONG function
The <b>WRITE_PORT_BUFFER_ULONG</b> routine writes a number of ULONG values from a buffer to the specified port address.

## Syntax

````
 VOID WRITE_PORT_BUFFER_ULONG(
  _In_ PULONG Port,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````

## Parameters

`Port`

Pointer to the port, which must be a mapped memory range in I/O space.

`Buffer`

Pointer to a buffer from which an array of ULONG values is to be written.

`Count`

Specifies the number of ULONG values to be written to the port.


## Return Value

None

## Remarks

The size of the buffer must be large enough to contain at least the specified number of ULONG values.

Callers of <b>WRITE_PORT_BUFFER_ULONG</b> can be running at any IRQL, assuming the <i>Buffer</i> is resident and the <i>Port</i> is resident, mapped device memory.</p>

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