---
UID: NF:ntintsafe.RtlULongLongToULong
title: RtlULongLongToULong function
author: windows-driver-content
description: Converts a value of type ULONGLONG to a value of type ULONG.
old-location: kernel\rtlulonglongtoulong.htm
old-project: kernel
ms.assetid: 322A17F1-E767-44EF-837D-F9162C2D5237
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntintsafe/RtlULongLongToULong, RtlULongLongToULong, RtlULongLongToULong function [Kernel-Mode Driver Architecture], kernel.rtlulonglongtoulong
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
-	RtlULongLongToULong
product: Windows
targetos: Windows
req.typenames: PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
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

TBD


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntintsafe.h |
| **Library** | NtosKrnl.exe |