---
UID : NF:ntintsafe.RtlULongToUInt8
title : RtlULongToUInt8 function
author : windows-driver-content
description : Converts a value of type ULONG_PTR to a value of type UINT8.
old-location : kernel\rtlulongtouint8.htm
old-project : kernel
ms.assetid : 56A205A5-A7A8-440D-B28B-B925E2107AEE
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlULongToUInt8
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
req.alt-api : RtlULongToUInt8
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


# RtlULongToUInt8 function
Converts a value of type <b>ULONG_PTR</b> to a value of type <b>UINT8</b>.

## Syntax

````
NTSTATUS RtlULongToUInt8(
  _In_  ULONG_PTR ulOperand,
  _Out_ UINT8     *pui8Result
);
````

## Parameters

`ulOperand`

The value to be converted.

`pui8Result`

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

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