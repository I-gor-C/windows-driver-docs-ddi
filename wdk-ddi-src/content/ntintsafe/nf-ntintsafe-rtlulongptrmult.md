---
UID : NF:ntintsafe.RtlULongPtrMult
title : RtlULongPtrMult function
author : windows-driver-content
description : Multiplies one value of type ULONG_PTR by another.
old-location : kernel\rtlulongptrmult.htm
old-project : kernel
ms.assetid : 6E66CD0B-7CAD-4BF1-A6DD-56C5029A929E
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlULongPtrMult function [Kernel-Mode Driver Architecture], RtlULongPtrMult, ntintsafe/RtlULongPtrMult, kernel.rtlulongptrmult
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


# RtlULongPtrMult function
Multiplies one value of type <b>ULONG_PTR</b> by another.

## Syntax

````
NTSTATUS RtlULongPtrMult(
  _In_  ULONG_PTR Multiplicand,
  _In_  ULONG_PTR Multiplier,
  _Out_ ULONG_PTR *pResult
);
````

## Parameters

`ulMultiplicand`

TBD

`ulMultiplier`

TBD

`pulResult`

TBD


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