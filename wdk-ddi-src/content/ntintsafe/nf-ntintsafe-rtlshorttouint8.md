---
UID : NF:ntintsafe.RtlShortToUInt8
title : RtlShortToUInt8 function
author : windows-driver-content
description : Converts a value of type SHORT to a value of type UINT8.
old-location : kernel\rtlshorttouint8.htm
old-project : kernel
ms.assetid : B1B5AE37-23BC-444A-9014-529BAD50ED52
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlShortToUInt8
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
req.alt-api : RtlShortToUInt8
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


# RtlShortToUInt8 function
Converts a value of type <b>SHORT</b> to a value of type <b>UINT8</b>.

## Syntax

````
NTSTATUS RtlShortToUInt8(
  _In_  SHORT sOperand,
  _Out_ UINT8 *puiResult
);
````

## Parameters

`sOperand`

The value to be converted.

`pui8Result`




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