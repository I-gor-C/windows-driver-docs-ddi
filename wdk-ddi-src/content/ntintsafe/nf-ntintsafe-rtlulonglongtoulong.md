---
UID : NF:ntintsafe.RtlULongLongToULong
title : RtlULongLongToULong function
author : windows-driver-content
description : Converts a value of type ULONGLONG to a value of type ULONG.
old-location : kernel\rtlulonglongtoulong.htm
old-project : kernel
ms.assetid : 322A17F1-E767-44EF-837D-F9162C2D5237
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlULongLongToULong
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
req.alt-api : RtlULongLongToULong
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


# RtlULongLongToULong function
Converts a value of type <b>ULONGLONG</b> to a value of type <b>ULONG</b>.

## Syntax

````
NTSTATUS RtlULongLongToULong(
  _In_  ULONGLONG ullOperand,
  _Out_ ULONG     *puResult
);
````

## Parameters

`ullOperand`

The value to be converted.

`pulResult`




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