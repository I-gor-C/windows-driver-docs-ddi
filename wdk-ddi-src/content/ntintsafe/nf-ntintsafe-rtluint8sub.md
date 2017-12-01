---
UID: NF.ntintsafe.RtlUInt8Sub
title: RtlUInt8Sub
author: windows-driver-content
description: The RtlUInt8Sub routine subtracts one value of type UINT8 from another.
old-location: kernel\rtluint8sub.htm
old-project: kernel
ms.assetid: D8BD24AA-64CF-42CB-8AD2-2B6C77D4B195
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUInt8Sub
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
req.alt-api: RtlUInt8Sub
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

# RtlUInt8Sub function



## -description
<p>The <b>RtlUInt8Sub</b> routine subtracts one value of type <b>UINT8</b> from another.</p>


## -syntax

````
NTSTATUS RtlUInt8Sub(
  _In_  UINT8 u8Minuend,
  _In_  UINT8 u8Subtrahend,
  _Out_ UINT8 *pu8Result
);
````


## -parameters
<dl>

### -param <i>u8Minuend</i> [in]

<dd>
<p>The value from which <i>u8Subtrahend</i> is subtracted.</p>
</dd>

### -param <i>u8Subtrahend</i> [in]

<dd>
<p>The value to subtract from <i>u8Minuend</i>.</p>
</dd>

### -param <i>pu8Result</i> [out]

<dd>
<p>A pointer to the result. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -returns
<p><b>RtlUInt8Sub</b> returns STATUS_SUCCESS if the routine is successful. Possible error return values include the following status code.</p><dl>
<dt><b>STATUS_INTEGER_OVERFLOW</b></dt>
</dl><p>An arithmetic overflow occurred.</p>

<p> </p>

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