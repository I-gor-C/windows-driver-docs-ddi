---
UID : NF:ntintsafe.RtlLongLongToInt8
title : RtlLongLongToInt8 function
author : windows-driver-content
description : Converts a value of type LONGLONG to a value of type INT8.
old-location : kernel\rtllonglongtoint8.htm
old-project : kernel
ms.assetid : C7BFDEA1-E0E9-4909-A543-94D047B1F1A9
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ntintsafe/RtlLongLongToInt8, RtlLongLongToInt8, kernel.rtllonglongtoint8, RtlLongLongToInt8 function [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntintsafe.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
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
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
---


# RtlLongLongToInt8 function
Converts a value of type <b>LONGLONG</b> to a value of type <b>INT8</b>.

## Syntax

````
NTSTATUS RtlLongLongToInt8(
  _In_  LONGLONG llOperand,
  _Out_ INT8     *pi8Result
);
````

## Parameters

`llOperand`

The value to be converted.

`pi8Result`

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

This function uses the following alternate name:
<ul>
<li>
RtlLong64ToInt8
</li>
<li>RtlInt64ToInt8
</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntintsafe.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |