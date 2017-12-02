---
UID: NF.ntintsafe.RtlIntAdd
title: RtlIntAdd
author: windows-driver-content
description: Adds two values of type INT.
old-location: kernel\rtlintadd.htm
old-project: kernel
ms.assetid: DF556961-D5BA-4A50-9E6A-DACE96D13B50
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlIntAdd
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
req.alt-api: RtlIntAdd
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

# RtlIntAdd function



## -description
<p>Adds two values of type <b>INT</b>.</p>


## -syntax

````
NTSTATUS RtlIntAdd(
  _In_  INT iAugend,
  _In_  INT iAddend,
  _Out_ INT *piResult
);
````


## -parameters
<dl>

### -param iAugend [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param iAddend [in]

<dd>
<p>The value to add to <i>iAugend</i>.</p>
</dd>

### -param piResult [out]

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