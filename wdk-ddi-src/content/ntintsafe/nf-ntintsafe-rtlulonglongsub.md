---
UID : NF:ntintsafe.RtlULongLongSub
title : RtlULongLongSub function
author : windows-driver-content
description : Subtracts one value of type ULONGLONG from another.
old-location : kernel\rtlulonglongsub.htm
old-project : kernel
ms.assetid : 3D0161C7-F99F-48EC-BE16-E5B857172C33
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.rtlulonglongsub, RtlULongLongSub, ntintsafe/RtlULongLongSub, RtlULongLongSub function [Kernel-Mode Driver Architecture]
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


# RtlULongLongSub function
Subtracts one value of type <b>ULONGLONG</b> from another.

## Syntax

````
NTSTATUS RtlULongLongSub(
  _In_  ULONGLONG ullMinuend,
  _In_  ULONGLONG ullSubtrahend,
  _Out_ ULONGLONG *pullResult
);
````

## Parameters

`ullMinuend`

The value from which <i>ullSubtrahend</i> is subtracted.

`ullSubtrahend`

The value to subtract from <i>ullMinuend</i>.

`pullResult`

A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


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