---
UID : NF:ntintsafe.RtlUInt8Add
title : RtlUInt8Add function
author : windows-driver-content
description : Adds two values of type UINT8.
old-location : kernel\rtluint8add.htm
old-project : kernel
ms.assetid : E93C8C7A-13E5-4089-931C-C56055FA3C90
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.rtluint8add, ntintsafe/RtlUInt8Add, RtlUInt8Add, RtlUInt8Add function [Kernel-Mode Driver Architecture]
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


# RtlUInt8Add function
Adds two values of type <b>UINT8</b>.

## Syntax

````
NTSTATUS RtlUInt8Add(
  _In_  UINT8 u8Augend,
  _In_  UINT8 u8Addend,
  _Out_ UINT8 *pu8Result
);
````

## Parameters

`u8Augend`

The first value in the equation.

`u8Addend`

The value to add to <i>u8Augend</i>.

`pu8Result`

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