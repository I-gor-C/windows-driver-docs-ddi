---
UID : NF:wdfhwaccess.WDF_WRITE_REGISTER_BUFFER_UCHAR
title : WDF_WRITE_REGISTER_BUFFER_UCHAR function
author : windows-driver-content
description : The WDF_WRITE_REGISTER_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified register.
old-location : wdf\wdf_write_register_buffer_uchar.htm
old-project : wdf
ms.assetid : A2BFF042-8358-4F82-B15D-7AD130C95DE3
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_WRITE_REGISTER_BUFFER_UCHAR function, WDF_WRITE_REGISTER_BUFFER_UCHAR, wdf.wdf_write_register_buffer_uchar, wdfhwaccess/WDF_WRITE_REGISTER_BUFFER_UCHAR
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


# WDF_WRITE_REGISTER_BUFFER_UCHAR function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_REGISTER_BUFFER_UCHAR</b> function writes a number of bytes from a buffer to the specified register.

## Syntax

````
void WDF_WRITE_REGISTER_BUFFER_UCHAR(
  _In_ WDFDEVICE Device,
  _In_ PUCHAR    Register,
  _In_ PUCHAR    Buffer,
  _In_ ULONG     Count 
);
````

## Parameters

`Device`

A handle to a framework device object.

`Register`

A pointer to the register, which must be a mapped range in memory space.

`Buffer`

A pointer to a buffer from which an array of UCHAR values is to be written.

`Count`

Specifies the number of bytes to write to the register.


## Return Value

This function does not return a value.

## Remarks

The size of the buffer must be large enough to contain at least the specified number of bytes.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Universal |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfhwaccess.h |
| **Library** | NtosKrnl.exe |