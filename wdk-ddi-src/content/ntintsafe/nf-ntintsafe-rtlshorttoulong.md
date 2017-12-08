---
UID: NF.ntintsafe.RtlShortToULong
title: RtlShortToULong function
author: windows-driver-content
description: Converts a value of type SHORT to a value of type ULONG.
old-location: kernel\rtlshorttoulong.htm
old-project: kernel
ms.assetid: A69F7F0E-3A71-4F29-9B56-A9B34D112F6C
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlShortToULong
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
req.alt-api: RtlShortToULong
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

# RtlShortToULong function



## -description
Converts a value of type <b>SHORT</b> to a value of type <b>ULONG</b>.


## -syntax

````
NTSTATUS RtlShortToULong(
  _In_  SHORT sOperand,
  _Out_ ULONG *pulResult
);
````


## -parameters

### -param sOperand [in]

The value to be converted.

### -param pulResult [out]

A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.

## -remarks
This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.

This function uses the following alternate name:

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