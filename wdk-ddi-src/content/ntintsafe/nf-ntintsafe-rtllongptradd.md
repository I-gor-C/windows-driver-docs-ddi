---
UID: NF:ntintsafe.RtlLongPtrAdd
title: RtlLongPtrAdd function
author: windows-driver-content
description: Adds two values of type LONG_PTR.
old-location: kernel\rtllongptradd.htm
old-project: kernel
ms.assetid: D0036070-A23D-4525-AE80-E10B20330F97
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: RtlLongPtrAdd, RtlLongPtrAdd function [Kernel-Mode Driver Architecture], kernel.rtllongptradd, ntintsafe/RtlLongPtrAdd
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntintsafe.h
api_name:
-	RtlLongPtrAdd
product: Windows
targetos: Windows
req.typenames: PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
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

TBD

`lAddend`

TBD

`plResult`

TBD


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