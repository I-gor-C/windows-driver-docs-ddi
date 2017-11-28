---
UID: NF.ntintsafe.RtlUIntAdd
title: RtlUIntAdd
author: windows-driver-content
description: Adds two values of type UINT.
old-location: kernel\rtluintadd.htm
old-project: kernel
ms.assetid: ABF392BD-7B05-417E-AFD8-4EE7E64F9FC2
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUIntAdd
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
req.alt-api: RtlUIntAdd
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

# RtlUIntAdd function



## -description
<p>Adds two values of type <b>UINT</b>.</p>


## -syntax

````
NTSTATUS RtlUIntAdd(
  _In_  UINT uAugend,
  _In_  UINT uAddend,
  _Out_ UINT *puResult
);
````


## -parameters
<dl>

### -param <i>uAugend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>uAddend</i> [in]

<dd>
<p>The value to add to <i>uAugend</i>.</p>
</dd>

### -param <i>puResult</i> [out]

<dd>
<p>A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
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