---
UID : NF:ntintsafe.RtlIntAdd
title : RtlIntAdd function
author : windows-driver-content
description : Adds two values of type INT.
old-location : kernel\rtlintadd.htm
old-project : kernel
ms.assetid : DF556961-D5BA-4A50-9E6A-DACE96D13B50
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlIntAdd, kernel.rtlintadd, ntintsafe/RtlIntAdd, RtlIntAdd function [Kernel-Mode Driver Architecture]
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


# RtlIntAdd function
Adds two values of type <b>INT</b>.

## Syntax

````
NTSTATUS RtlIntAdd(
  _In_  INT iAugend,
  _In_  INT iAddend,
  _Out_ INT *piResult
);
````

## Parameters

`iAugend`

The first value in the equation.

`iAddend`

The value to add to <i>iAugend</i>.

`piResult`

A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## Return Value

None

## Remarks

This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.

This function uses the following alternate name:
<ul>
<li>RtlInt32Add
</li>
<li>RtlLong32Add
</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ntintsafe.h |
| **Library** | NtosKrnl.exe |