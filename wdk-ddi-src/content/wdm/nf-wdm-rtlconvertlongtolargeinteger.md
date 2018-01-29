---
UID : NF:wdm.RtlConvertLongToLargeInteger
title : RtlConvertLongToLargeInteger function
author : windows-driver-content
description : The RtlConvertLongToLargeInteger routine converts the input signed integer to a signed large integer.
old-location : kernel\rtlconvertlongtolargeinteger.htm
old-project : kernel
ms.assetid : 8c1f6cd3-f54b-4104-bd14-63d2c284946c
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlConvertLongToLargeInteger routine [Kernel-Mode Driver Architecture], kernel.rtlconvertlongtolargeinteger, k109_f56a300b-e5d3-4f08-8d38-f124f73ada9f.xml, RtlConvertLongToLargeInteger, wdm/RtlConvertLongToLargeInteger
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
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# RtlConvertLongToLargeInteger function
The <b>RtlConvertLongToLargeInteger</b> routine converts the input signed integer to a signed large integer.

## Syntax

````
LARGE_INTEGER RtlConvertLongToLargeInteger(
  _In_ LONG SignedInteger
);
````

## Parameters

`SignedInteger`

Specifies an integer of type LONG.


## Return Value

<b>RtlConvertLongToLargeInteger</b> returns the large integer result.

## Remarks

This routine is not supported in Windows XP. Use native support for <b>__int64</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | Any level |
| **DDI compliance rules** |  |