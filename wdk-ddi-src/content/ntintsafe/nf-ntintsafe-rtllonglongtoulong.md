---
UID: NF.ntintsafe.RtlLongLongToULong
title: RtlLongLongToULong function
author: windows-driver-content
description: Converts a value of type LONGLONG to a value of type ULONG.
old-location: kernel\rtllonglongtoulong.htm
old-project: kernel
ms.assetid: EA5C57D3-E4EF-49B2-9B0E-DB99CD32C888
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlLongLongToULong
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
req.alt-api: RtlLongLongToULong
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

# RtlLongLongToULong function



## -description
Converts a value of type <b>LONGLONG</b> to a value of type <b>ULONG</b>.


## -syntax

````
NTSTATUS RtlLongLongToULong(
  _In_  LONGLONG llOperand,
  _Out_ ULONG    *pulResult
);
````


## -parameters

### -param llOperand [in]

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