---
UID: NF.ntintsafe.RtlUIntSub
title: RtlUIntSub
author: windows-driver-content
description: Subtracts one value of type UINT from another.
old-location: kernel\rtluintsub.htm
old-project: kernel
ms.assetid: 0886578A-C1CF-4A48-86A3-407A0C16ADEC
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUIntSub
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
req.alt-api: RtlUIntSub
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

# RtlUIntSub function



## -description
<p>Subtracts one value of type <b>UINT</b> from another.</p>


## -syntax

````
NTSTATUS RtlUIntSub(
  _In_  UINT uMinuend,
  _In_  UINT uSubtrahend,
  _Out_ UINT *puResult
);
````


## -parameters
<dl>

### -param uMinuend [in]

<dd>
<p>The value from which <i>u8Subtrahend</i> is subtracted.</p>
</dd>

### -param uSubtrahend [in]

<dd>
<p>The value to subtract from <i>u8Minuend</i>.</p>
</dd>

### -param puResult [out]

<dd>
<p>A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.</p>

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