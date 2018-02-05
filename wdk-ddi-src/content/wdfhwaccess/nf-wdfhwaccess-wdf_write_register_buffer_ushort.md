---
UID : NF:wdfhwaccess.WDF_WRITE_REGISTER_BUFFER_USHORT
title : WDF_WRITE_REGISTER_BUFFER_USHORT function
author : windows-driver-content
description : The WDF_WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register.
old-location : wdf\wdf_write_register_buffer_ushort.htm
old-project : wdf
ms.assetid : EE076D50-8E08-4D98-872F-DA6DBA27B9E5
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : WDF_WRITE_REGISTER_BUFFER_USHORT function, WDF_WRITE_REGISTER_BUFFER_USHORT, wdf.wdf_write_register_buffer_ushort, wdfhwaccess/WDF_WRITE_REGISTER_BUFFER_USHORT
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


# WDF_WRITE_REGISTER_BUFFER_USHORT function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_REGISTER_BUFFER_USHORT</b> routine writes a number of USHORT values from a buffer to the specified register.

## Syntax

````
void WDF_WRITE_REGISTER_BUFFER_USHORT(
  _In_ WDFDEVICE Device,
  _In_ PUSHORT   Register,
  _In_ PUSHORT   Buffer,
  _In_ ULONG     Count 
);
````

## Parameters

`Device`

A handle to a framework device object.

`Register`

A pointer to the register, which must be a mapped range in memory space.

`Buffer`

A pointer to a buffer into which an array of USHORT values is to be written.

`Count`

Specifies the number of USHORT values to write to the register.


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