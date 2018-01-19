---
UID : NF:ntintsafe.RtlLongToUShort
title : RtlLongToUShort function
author : windows-driver-content
description : Converts a value of type LONG to a value of type USHORT.
old-location : kernel\rtllongtoushort.htm
old-project : kernel
ms.assetid : A6D3E5D2-EB53-4F1D-B4E4-9E2D8D845E80
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlLongToUShort
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
req.alt-api : RtlLongToUShort
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


# RtlLongToUShort function
Converts a value of type <b>LONG</b> to a value of type <b>USHORT</b>.

## Syntax

````
NTSTATUS RtlLongToUShort(
  _In_  LONG   lOperand,
  _Out_ USHORT *pusResult
);
````

## Parameters

`lOperand`

The value to be converted.

`pusResult`

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

This function uses the following alternate name:</p>

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