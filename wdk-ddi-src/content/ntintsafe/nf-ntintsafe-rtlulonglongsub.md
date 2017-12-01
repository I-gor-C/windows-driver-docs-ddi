---
UID: NF.ntintsafe.RtlULongLongSub
title: RtlULongLongSub
author: windows-driver-content
description: Subtracts one value of type ULONGLONG from another.
old-location: kernel\rtlulonglongsub.htm
old-project: kernel
ms.assetid: 3D0161C7-F99F-48EC-BE16-E5B857172C33
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongLongSub
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
req.alt-api: RtlULongLongSub
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

# RtlULongLongSub function



## -description
<p>Subtracts one value of type <b>ULONGLONG</b> from another.</p>


## -syntax

````
NTSTATUS RtlULongLongSub(
  _In_  ULONGLONG ullMinuend,
  _In_  ULONGLONG ullSubtrahend,
  _Out_ ULONGLONG *pullResult
);
````


## -parameters
<dl>

### -param <i>ullMinuend</i> [in]

<dd>
<p>The value from which <i>ullSubtrahend</i> is subtracted.</p>
</dd>

### -param <i>ullSubtrahend</i> [in]

<dd>
<p>The value to subtract from <i>ullMinuend</i>.</p>
</dd>

### -param <i>pullResult</i> [out]

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