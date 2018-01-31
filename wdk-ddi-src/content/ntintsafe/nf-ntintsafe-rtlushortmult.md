---
UID : NF:ntintsafe.RtlUShortMult
title : RtlUShortMult function
author : windows-driver-content
description : Multiplies one value of type USHORT by another.
old-location : kernel\rtlushortmult.htm
old-project : kernel
ms.assetid : 1727AD96-FC0B-4B52-92C5-5E7502433021
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.rtlushortmult, RtlUShortMult, RtlUShortMult function [Kernel-Mode Driver Architecture], ntintsafe/RtlUShortMult
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


# RtlUShortMult function
Multiplies one value of type <b>USHORT</b> by another.

## Syntax

````
NTSTATUS RtlUShortMult(
  _In_  USHORT usMultiplicand,
  _In_  USHORT usMultiplier,
  _Out_ USHORT *pusResult
);
````

## Parameters

`usMultiplicand`

The value to be multiplied by <i>usMultiplier</i>.

`usMultiplier`

The value by which to multiply <i>usMultiplicand</i>.

`pusResult`

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