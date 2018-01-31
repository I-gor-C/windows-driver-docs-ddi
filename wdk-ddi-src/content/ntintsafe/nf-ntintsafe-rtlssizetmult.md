---
UID : NF:ntintsafe.RtlSSIZETMult
title : RtlSSIZETMult function
author : windows-driver-content
description : Multiplies one value of type SSIZE_T by another.
old-location : kernel\rtlssizetmult.htm
old-project : kernel
ms.assetid : 43FFE47F-C8A3-49B4-B61A-3EAF3841037D
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ntintsafe/RtlSSIZETMult, kernel.rtlssizetmult, RtlSSIZETMult, RtlSSIZETMult function [Kernel-Mode Driver Architecture]
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


# RtlSSIZETMult function
Multiplies one value of type <b>SSIZE_T</b> by another.

## Syntax

````
NTSTATUS RtlSSIZETMult(
  _In_  SSIZE_T Multiplicand,
  _In_  SSIZE_T Multiplier,
  _Out_ SSIZE_T *pResult
);
````

## Parameters

`Multiplicand`

The value to be multiplied by <i>Multiplier</i>.

`Multiplier`

The value by which to multiply <i>Multiplicand</i>.

`pResult`

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