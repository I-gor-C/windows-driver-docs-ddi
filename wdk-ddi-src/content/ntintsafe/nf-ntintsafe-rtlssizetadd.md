---
UID : NF:ntintsafe.RtlSSIZETAdd
title : RtlSSIZETAdd function
author : windows-driver-content
description : Adds two values of type SSIZE_T.
old-location : kernel\rtlssizetadd.htm
old-project : kernel
ms.assetid : 1CBB3CDF-E7DD-4686-8EF6-FBCADE978A16
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlSSIZETAdd
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
req.alt-api : RtlSSIZETAdd
req.alt-loc : Ntintsafe.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
---


# RtlSSIZETAdd function
Adds two values of type <b>SSIZE_T</b>.

## Syntax

````
NTSTATUS RtlSSIZETAdd(
  _In_  SSIZE_T Augend,
  _In_  SSIZE_T Addend,
  _Out_ SSIZE_T *pResult
);
````

## Parameters

`Augend`

The first value in the equation.

`Addend`

The value to add to <i>Augend</i>.

`pResult`

A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.</p>

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