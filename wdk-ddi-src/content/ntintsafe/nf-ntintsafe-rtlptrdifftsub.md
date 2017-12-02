---
UID: NF.ntintsafe.RtlPtrdiffTSub
title: RtlPtrdiffTSub
author: windows-driver-content
description: Subtracts one value of type PTRDIFF_T from another.
old-location: kernel\rtlptrdifftsub.htm
old-project: kernel
ms.assetid: C87E3BD5-8CA7-443E-8CC3-F863CD4F321A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlPtrdiffTSub
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
req.alt-api: RtlPtrdiffTSub
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

# RtlPtrdiffTSub function



## -description
<p>Subtracts one value of type <b>PTRDIFF_T</b> from another.</p>


## -syntax

````
NTSTATUS RtlPtrdiffTSub(
  _In_  PTRDIFF_T Minuend,
  _In_  PTRDIFF_T Subtrahend,
  _Out_ PTRDIFF_T *pResult
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