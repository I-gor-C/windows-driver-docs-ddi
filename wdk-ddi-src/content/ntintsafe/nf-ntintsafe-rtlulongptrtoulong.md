---
UID: NF.ntintsafe.RtlULongPtrToULong
title: RtlULongPtrToULong function
author: windows-driver-content
description: Converts a value of type ULONG_PTR to a value of type ULONG.
old-location: kernel\rtlulongptrtoulong.htm
old-project: kernel
ms.assetid: 63F09DAA-C885-4A84-B0FF-249D8D6CA48C
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlULongPtrToULong
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
req.alt-api: RtlULongPtrToULong
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

# RtlULongPtrToULong function



## -description
Converts a value of type <b>ULONG_PTR</b> to a value of type <b>ULONG</b>.



## -syntax

````
NTSTATUS RtlULongPtrToULong(
  _In_  ULONG_PTR ulOperand,
  _Out_ ULONG     *pulResult
);
````


## -parameters

### -param ulOperand [in]

The value to be converted.


### -param pulResult [out]

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.


## -remarks
This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.


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