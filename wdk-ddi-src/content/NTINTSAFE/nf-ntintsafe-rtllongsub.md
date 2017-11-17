---
UID: NF.ntintsafe.RtlLongSub
title: RtlLongSub
author: windows-driver-content
description: Subtracts one value of type LONG from another.
old-location: kernel\rtllongsub.htm
ms.assetid: 5D98737C-0986-4DCB-9270-A0DF76CFCB5C
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlLongSub
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
ms.keywords: RtlLongSub
req.iface: 
---

# RtlLongSub function



## -description
<p>Subtracts one value of type <b>LONG</b> from another.</p>


## -syntax

````
NTSTATUS RtlLongSub(
  _In_  LONG lMinuend,
  _In_  LONG lSubtrahend,
  _Out_ LONG *plResult
);
````


## -parameters
<dl>

### -param <i>lMinuend</i> [in]

<dd>
<p>The value from which <i>lSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>lSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>lMinuend</i>.</p>
</dd>

### -param <i>plResult</i> [out]

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