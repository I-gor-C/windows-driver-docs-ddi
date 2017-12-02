---
UID: NF.ntintsafe.RtlSizeTSub
title: RtlSizeTSub
author: windows-driver-content
description: Subtracts one value of type SIZE_T from another.
old-location: kernel\rtlsizetsub.htm
old-project: kernel
ms.assetid: B7508B3B-DCE7-42F4-9257-E1E140625DA9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlSizeTSub
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
req.alt-api: RtlSizeTSub
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

# RtlSizeTSub function



## -description
<p>Subtracts one value of type <b>SIZE_T</b> from another.</p>


## -syntax

````
NTSTATUS RtlSizeTSub(
  _In_  SIZE_T Minuend,
  _In_  SIZE_T Subtrahend,
  _Out_ SIZE_T *pResult
);
````


## -parameters
<dl>

### -param Minuend [in]

<dd>
<p>The value from which <i>Subtrahend</i> is subtracted.</p>
</dd>

### -param Subtrahend [in]

<dd>
<p>The value to subtract from <i>Minuend</i>.</p>
</dd>

### -param pResult [out]

<dd>
<p>A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide arithmetic operations and perform validity checks with minimal impact on performance.</p>

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