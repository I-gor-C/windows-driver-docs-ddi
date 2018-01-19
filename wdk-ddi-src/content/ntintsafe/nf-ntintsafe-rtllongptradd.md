---
UID : NF:ntintsafe.RtlLongPtrAdd
title : RtlLongPtrAdd function
author : windows-driver-content
description : Adds two values of type LONG_PTR.
old-location : kernel\rtllongptradd.htm
old-project : kernel
ms.assetid : D0036070-A23D-4525-AE80-E10B20330F97
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlLongPtrAdd
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
req.alt-api : RtlLongPtrAdd
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


# RtlLongPtrAdd function
Adds two values of type <b>LONG_PTR</b>.

## Syntax

````
NTSTATUS RtlLongPtrAdd(
  _In_  UINT8 u8Augend,
  _In_  UINT8 u8Addend,
  _Out_ UINT8 *pu8Result
);
````

## Parameters

`lAugend`



`lAddend`



`plResult`




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