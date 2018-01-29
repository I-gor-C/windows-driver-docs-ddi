---
UID : NF:ntintsafe.RtlUInt8Mult
title : RtlUInt8Mult function
author : windows-driver-content
description : Multiplies one value of type UINT8 by another.
old-location : kernel\rtluint8mult.htm
old-project : kernel
ms.assetid : 3F9E47F5-1DE3-4949-BE92-8C8F571BFD3D
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlUInt8Mult, ntintsafe/RtlUInt8Mult, RtlUInt8Mult function [Kernel-Mode Driver Architecture], kernel.rtluint8mult
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


# RtlUInt8Mult function
Multiplies one value of type <b>UINT8</b> by another.

## Syntax

````
NTSTATUS RtlUInt8Mult(
  _In_  UINT8 u8Multiplicand,
  _In_  UINT8 u8Multiplier,
  _Out_ UINT8 *pu8Result
);
````

## Parameters

`u8Multiplicand`

The value to be multiplied by <i>u8Multiplier</i>.

`u8Multiplier`

The value by which to multiply <i>u8Multiplicand</i>.

`pu8Result`

A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.

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