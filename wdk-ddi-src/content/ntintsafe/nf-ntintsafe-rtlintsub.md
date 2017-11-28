---
UID: NF.ntintsafe.RtlIntSub
title: RtlIntSub
author: windows-driver-content
description: Subtracts one value of type INT from another.
old-location: kernel\rtlintsub.htm
old-project: kernel
ms.assetid: 68BBD6B8-5C7C-4FE5-97F7-473A9510400F
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlIntSub
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
req.alt-api: RtlIntSub
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

# RtlIntSub function



## -description
<p>Subtracts one value of type <b>INT</b> from another.</p>


## -syntax

````
NTSTATUS RtlIntSub(
  _In_  INT iMinuend,
  _In_  INT iSubtrahend,
  _Out_ INT *pu8Result
);
````


## -parameters
<dl>

### -param <i>iMinuend</i> [in]

<dd>
<p>The value from which <i>iSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>iSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>iMinuend</i>.</p>
</dd>

### -param <i>pu8Result</i> [out]

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