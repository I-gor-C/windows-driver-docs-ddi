---
UID: NF.ntintsafe.RtlLongLongSub
title: RtlLongLongSub
author: windows-driver-content
description: Subtracts one value of type LONGLONG from another.
old-location: kernel\rtllonglongsub.htm
old-project: kernel
ms.assetid: A0D35ECE-5B7F-4F60-9178-75673C9A945F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlLongLongSub
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
req.alt-api: RtlLongLongSub
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

# RtlLongLongSub function



## -description
<p>Subtracts one value of type <b>LONGLONG</b> from another.</p>


## -syntax

````
NTSTATUS RtlLongLongSub(
  _In_  LONGLONG llMinuend,
  _In_  LONGLONG llSubtrahend,
  _Out_ LONGLONG *pllResult
);
````


## -parameters
<dl>

### -param llMinuend [in]

<dd>
<p>The value from which <i>llSubtrahend</i> is subtracted.</p>
</dd>

### -param llSubtrahend [in]

<dd>
<p>The value to subtract from <i>llMinuend</i>.</p>
</dd>

### -param pllResult [out]

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