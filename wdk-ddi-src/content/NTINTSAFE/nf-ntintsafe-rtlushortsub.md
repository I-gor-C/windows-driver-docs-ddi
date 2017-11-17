---
UID: NF.ntintsafe.RtlUShortSub
title: RtlUShortSub
author: windows-driver-content
description: Subtracts one value of type USHORT from another.
old-location: kernel\rtlushortsub.htm
ms.assetid: 1C0392AE-F3BD-4F42-9094-87228B7C3E10
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
req.alt-api: RtlUShortSub
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
ms.keywords: RtlUShortSub
req.iface: 
---

# RtlUShortSub function



## -description
<p>Subtracts one value of type <b>USHORT</b> from another.</p>


## -syntax

````
NTSTATUS RtlUShortSub(
  _In_  USHORT usMinuend,
  _In_  USHORT usSubtrahend,
  _Out_ USHORT *pusResult
);
````


## -parameters
<dl>

### -param <i>usMinuend</i> [in]

<dd>
<p>The value from which <i>usSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>usSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>usMinuend</i>.</p>
</dd>

### -param <i>pusResult</i> [out]

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