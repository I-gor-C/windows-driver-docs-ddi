---
UID : NF:wdfhwaccess.WDF_WRITE_PORT_UCHAR
title : WDF_WRITE_PORT_UCHAR function
author : windows-driver-content
description : The WDF_WRITE_PORT_UCHAR function writes a byte to the specified port address.
old-location : wdf\wdf_write_port_uchar.htm
old-project : wdf
ms.assetid : F7F40415-87E9-4870-8B10-83009159543E
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_WRITE_PORT_UCHAR, wdf.wdf_write_port_uchar, wdfhwaccess/WDF_WRITE_PORT_UCHAR, WDF_WRITE_PORT_UCHAR function
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdfhwaccess.h
req.include-header : 
req.target-type : Universal
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
req.product : Windows 10 or later.
---


# WDF_WRITE_PORT_UCHAR function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_PORT_UCHAR</b> function writes a byte to the specified port address.

## Syntax

````
void WDF_WRITE_PORT_UCHAR(
  _In_ WDFDEVICE Device,
  _In_ PUCHAR    Port,
  _In_ UCHAR     Value
);
````

## Parameters

`Device`

A handle to a framework device object.

`Port`

A pointer to the port, which must be a mapped memory range in I/O space.

`Value`

Specifies a byte to be written to the port.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Universal |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfhwaccess.h |
| **Library** | NtosKrnl.exe |