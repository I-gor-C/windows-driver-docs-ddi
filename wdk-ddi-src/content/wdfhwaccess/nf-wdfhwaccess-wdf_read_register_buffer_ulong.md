---
UID: NF:wdfhwaccess.WDF_READ_REGISTER_BUFFER_ULONG
title: WDF_READ_REGISTER_BUFFER_ULONG function
author: windows-driver-content
description: The WDF_READ_REGISTER_BUFFER_ULONG function reads a number of ULONG values from the specified register address into a buffer.
old-location: wdf\wdf_read_register_buffer_ulong.htm
old-project: wdf
ms.assetid: 249D8FCF-6B63-467B-AEAA-BCF4900CFA48
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: WDF_READ_REGISTER_BUFFER_ULONG, wdf.wdf_read_register_buffer_ulong, WDF_READ_REGISTER_BUFFER_ULONG function, wdfhwaccess/WDF_READ_REGISTER_BUFFER_ULONG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfhwaccess.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Wdfhwaccess.h
apiname:
-	WDF_READ_REGISTER_BUFFER_ULONG
product: Windows
targetos: Windows
req.typenames: WDF_FILE_INFORMATION_CLASS, *PWDF_FILE_INFORMATION_CLASS
req.product: Windows 10 or later.
---


# WDF_READ_REGISTER_BUFFER_ULONG function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_READ_REGISTER_BUFFER_ULONG</b> function reads a number of ULONG values  from the specified register address into a buffer.

## Syntax

````
void WDF_READ_REGISTER_BUFFER_ULONG(
  _In_  WDFDEVICE Device,
  _In_  PULONG    Register,
  _Out_ PULONG    Buffer,
  _In_  ULONG     Count 
);
````

## Parameters

`Device`

A handle to a framework device object.

`Register`

A pointer to the register, which must be a mapped range in memory space.

`Buffer`

A pointer to a buffer into which an array of ULONG values is read.

`Count`

Specifies the number of ULONG values to be read into the buffer.


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