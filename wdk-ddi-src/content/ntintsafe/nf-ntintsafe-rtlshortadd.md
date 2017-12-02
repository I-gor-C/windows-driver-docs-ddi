---
UID: NF.ntintsafe.RtlShortAdd
title: RtlShortAdd
author: windows-driver-content
description: Adds two values of type SHORT.
old-location: kernel\rtlshortadd.htm
old-project: kernel
ms.assetid: 6CCBDECB-D52A-409D-91CA-6635E6D02545
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlShortAdd
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
req.alt-api: RtlShortAdd
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

# RtlShortAdd function



## -description
<p>Adds two values of type <b>SHORT</b>.</p>


## -syntax

````
NTSTATUS RtlShortAdd(
  _In_  SHORT sAugend,
  _In_  SHORT sAddend,
  _Out_ SHORT *psResult
);
````


## -parameters
<dl>

### -param sAugend [in]

<dd>
<p>The first value in the equation.</p>
</dd>

### -param sAddend [in]

<dd>
<p>The value to add to <i>sAugend</i>.</p>
</dd>

### -param psResult [out]

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