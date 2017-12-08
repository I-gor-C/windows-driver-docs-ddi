---
UID: NF.ntintsafe.RtlULongPtrAdd
title: RtlULongPtrAdd function
author: windows-driver-content
description: Adds two values of type ULONG_PTR.
old-location: kernel\rtlulongptradd.htm
old-project: kernel
ms.assetid: 26A9A0B6-07A3-4D42-A5A1-C4CDD541A3FA
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlULongPtrAdd
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
req.alt-api: RtlULongPtrAdd
req.alt-loc: Ntintsafe.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# RtlULongPtrAdd function



## -description
Adds two values of type <b>ULONG_PTR</b>.


## -syntax

````
NTSTATUS RtlULongPtrAdd(
  _In_  ULONG_PTR ulAugend,
  _In_  ULONG_PTR ulAddend,
  _Out_ ULONG_PTR *pulResult
);
````


## -parameters

### -param ulAugend [in]

The first value in the equation.

### -param ulAddend [in]

The value to add to <i>ulAugend</i>.

### -param pulResult [out]

A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntintsafe.h</dt>
</dl>
</td>
</tr>
</table>