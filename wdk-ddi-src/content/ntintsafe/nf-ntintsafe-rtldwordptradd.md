---
UID: NF.ntintsafe.RtlDWordPtrAdd
title: RtlDWordPtrAdd
author: windows-driver-content
description: Adds two values of type DWORD_PTR.
old-location: kernel\rtldwordptradd.htm
old-project: kernel
ms.assetid: 8364FC5F-1FF4-415F-B83C-4A866C860522
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlDWordPtrAdd
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
req.alt-api: RtlDWordPtrAdd
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

# RtlDWordPtrAdd function



## -description
<p>Adds two values of type <b>DWORD_PTR</b>.</p>


## -syntax

````
NTSTATUS RtlDWordPtrAdd(
  _In_  DWORD_PTR dwAugend,
  _In_  DWORD_PTR dwAddend,
  _Out_ DWORD_PTR *pdwResult
);
````


## -parameters
<dl>

### -param <i>dwAugend</i> [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param <i>dwAddend</i> [in]

<dd>
<p>The value to add to <i>dwAugend</i>.</p>
</dd>

### -param <i>pdwResult</i> [out]

<dd>
<p>A pointer to the sum. If the operation results in a value that overflows or underflows the capacity of the type, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
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