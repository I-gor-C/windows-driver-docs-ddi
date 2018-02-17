---
UID: NF:ntintsafe.RtlSizeTSub
title: RtlSizeTSub function
author: windows-driver-content
description: Subtracts one value of type SIZE_T from another.
old-location: kernel\rtlsizetsub.htm
old-project: kernel
ms.assetid: B7508B3B-DCE7-42F4-9257-E1E140625DA9
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: kernel.rtlsizetsub, RtlSizeTSub, ntintsafe/RtlSizeTSub, RtlSizeTSub function [Kernel-Mode Driver Architecture]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Ntintsafe.h
apiname:
-	RtlSizeTSub
product: Windows
targetos: Windows
req.typenames: PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
---


# RtlSizeTSub function
Subtracts one value of type <b>SIZE_T</b> from another.

## Syntax

````
NTSTATUS RtlSizeTSub(
  _In_  SIZE_T Minuend,
  _In_  SIZE_T Subtrahend,
  _Out_ SIZE_T *pResult
);
````

## Parameters

`Minuend`

The value from which <i>Subtrahend</i> is subtracted.

`Subtrahend`

The value to subtract from <i>Minuend</i>.

`pResult`

A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntintsafe.h |
| **Library** | NtosKrnl.exe |