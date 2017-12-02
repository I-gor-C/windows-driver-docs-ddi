---
UID: NF.ntintsafe.RtlULongSub
title: RtlULongSub
author: windows-driver-content
description: Subtracts one value of type ULONG from another.
old-location: kernel\rtlulongsub.htm
old-project: kernel
ms.assetid: 54776F17-C7EE-46DB-BA3F-2F545240FC61
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongSub
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
req.alt-api: RtlULongSub
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

# RtlULongSub function



## -description
<p>Subtracts one value of type <b>ULONG</b> from another.</p>


## -syntax

````
NTSTATUS RtlULongSub(
  _In_  UINT8 ulMinuend,
  _In_  UINT8 ulSubtrahend,
  _Out_ UINT8 *pulResult
);
````


## -parameters
<dl>

### -param ulMinuend [in]

<dd>
<p>The value from which <i>ulSubtrahend</i> is subtracted.</p>
</dd>

### -param ulSubtrahend [in]

<dd>
<p>The value to subtract from <i>ulMinuend</i>.</p>
</dd>

### -param pulResult [out]

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