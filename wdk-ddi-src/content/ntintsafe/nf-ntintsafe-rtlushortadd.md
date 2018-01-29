---
UID : NF:ntintsafe.RtlUShortAdd
title : RtlUShortAdd function
author : windows-driver-content
description : Adds two values of type USHORT.
old-location : kernel\rtlushortadd.htm
old-project : kernel
ms.assetid : 07167C7E-E8EB-41E3-B2E3-7B9E9CCC5465
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : ntintsafe/RtlUShortAdd, kernel.rtlushortadd, RtlUShortAdd function [Kernel-Mode Driver Architecture], RtlUShortAdd
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


# RtlUShortAdd function
Adds two values of type <b>USHORT</b>.

## Syntax

````
NTSTATUS RtlUShortAdd(
  _In_  USHORT usAugend,
  _In_  USHORT usAddend,
  _Out_ USHORT *pusResult
);
````

## Parameters

`usAugend`

The first value in the equation.

`usAddend`

The value to add to <i>usAugend</i>.

`pusResult`

A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


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