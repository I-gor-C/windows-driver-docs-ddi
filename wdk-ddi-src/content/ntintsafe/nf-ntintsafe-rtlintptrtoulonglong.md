---
UID: NF.ntintsafe.RtlIntPtrToULongLong
title: RtlIntPtrToULongLong
author: windows-driver-content
description: Converts a value of type INT_PTR to a value of type ULONGLONG.
old-location: kernel\rtlintptrtoulonglong.htm
old-project: kernel
ms.assetid: FF5D7B10-86AE-4C01-AFA9-C0C94E566428
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlIntPtrToULongLong
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
req.alt-api: RtlIntPtrToULongLong
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
req.iface: 
---

# RtlIntPtrToULongLong function



## -description
<p>Converts a value of type <b>INT_PTR</b> to a value of type <b>ULONGLONG</b>.</p>


## -syntax

````
NTSTATUS RtlIntPtrToULongLong(
  _In_  INT_PTR   iOperand,
  _Out_ ULONGLONG *pullResult
);
````


## -parameters
<dl>

### -param <i>iOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pullResult</i> [out]

<dd>
<p>A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

<p>This function uses the following alternate name:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntintsafe.h</dt>
</dl>
</td>
</tr>
</table>