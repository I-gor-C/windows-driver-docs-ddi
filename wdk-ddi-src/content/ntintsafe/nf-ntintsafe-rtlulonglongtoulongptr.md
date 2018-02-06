---
UID: NF:ntintsafe.RtlULongLongToULongPtr
title: RtlULongLongToULongPtr function
author: windows-driver-content
description: Converts a value of type ULONGLONG to a value of type ULONG_PTR.
old-location: kernel\rtlulonglongtoulongptr.htm
old-project: kernel
ms.assetid: D170649F-D0CE-454B-8F2B-18C66F58CAF7
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: ntintsafe/RtlULongLongToULongPtr, RtlULongLongToULongPtr function [Kernel-Mode Driver Architecture], kernel.rtlulonglongtoulongptr, RtlULongLongToULongPtr
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
-	RtlULongLongToULongPtr
product: Windows
targetos: Windows
req.typenames: PUBLIC_OBJECT_TYPE_INFORMATION, *PPUBLIC_OBJECT_TYPE_INFORMATION
---


# RtlULongLongToULongPtr function
Converts a value of type <b>ULONGLONG</b> to a value of type <b>ULONG_PTR</b>.

## Syntax

````
NTSTATUS RtlULongLongToULongPtr(
  _In_  ULONGLONG ullOperand,
  _Out_ ULONG_PTR *puResult
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