---
UID: NF.ntintsafe.RtlIntToUInt
title: RtlIntToUInt
author: windows-driver-content
description: Converts a value of type INT to a value of type UINT.
old-location: kernel\rtlinttouint.htm
old-project: kernel
ms.assetid: 9D2C7E0F-99E2-4B95-8CB6-9158DA1D906F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlIntToUInt
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
req.alt-api: RtlIntToUInt
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

# RtlIntToUInt function



## -description
<p>Converts a value of type <b>INT</b> to a value of type <b>UINT</b>.</p>


## -syntax

````
NTSTATUS RtlIntToUInt(
  _In_  INT  iOperand,
  _Out_ UINT *puResult
);
````


## -parameters
<dl>

### -param <i>iOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>puResult</i> [out]

<dd>
<p>A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

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