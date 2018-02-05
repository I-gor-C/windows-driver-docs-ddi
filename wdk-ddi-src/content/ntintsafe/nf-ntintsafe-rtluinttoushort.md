---
UID : NF:ntintsafe.RtlUIntToUShort
title : RtlUIntToUShort function
author : windows-driver-content
description : Converts a value of type UINT to a value of type USHORT.
old-location : kernel\rtluinttoushort.htm
old-project : kernel
ms.assetid : 3A9DB44E-ABAB-4808-9322-8ADA5AD39F75
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlUIntToUShort function [Kernel-Mode Driver Architecture], ntintsafe/RtlUIntToUShort, kernel.rtluinttoushort, RtlUIntToUShort
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


# RtlUIntToUShort function
Converts a value of type <b>UINT</b> to a value of type <b>USHORT</b>.

## Syntax

````
NTSTATUS RtlUIntToUShort(
  _In_  UINT   uOperand,
  _Out_ USHORT *pusResult
);
````

## Parameters

`uOperand`

The value to be converted.

`pusResult`

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

This function uses the following alternate name:
<ul>
<li>RtlUIntToUInt16
</li>
<li>RtlUIntToWord
</li>
<li>RtlUInt32ToUShort
</li>
<li>RtlUInt32ToUInt16
</li>
<li>RtlUInt32ToWord
</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntintsafe.h |
| **Library** | NtosKrnl.exe |