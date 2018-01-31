---
UID : NF:wdfhwaccess.WDF_WRITE_REGISTER_UCHAR
title : WDF_WRITE_REGISTER_UCHAR function
author : windows-driver-content
description : The WDF_WRITE_REGISTER_UCHAR routine writes a byte to the specified address.
old-location : wdf\wdf_write_register_uchar.htm
old-project : wdf
ms.assetid : 5738654A-83B1-44B4-BA45-52E2B60C852D
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdfhwaccess/WDF_WRITE_REGISTER_UCHAR, wdf.wdf_write_register_uchar, WDF_WRITE_REGISTER_UCHAR function, WDF_WRITE_REGISTER_UCHAR
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


# WDF_WRITE_REGISTER_UCHAR function
<p class="CCE_Message">[Applies to UMDF only]

The <b>WDF_WRITE_REGISTER_UCHAR</b> routine writes a byte to the specified address.

## Syntax

````
void WDF_WRITE_REGISTER_UCHAR(
  _In_ WDFDEVICE Device,
  _In_ PUCHAR    Register,
  _In_ UCHAR     Value
);
````

## Parameters

`Device`

A handle to a framework device object.

`Register`

A pointer to the register, which must be a mapped range in memory space.

`Value`

Specifies a byte to write to the register.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfhwaccess.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |