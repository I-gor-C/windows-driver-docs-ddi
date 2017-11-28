---
UID: NF.ntintsafe.RtlIntToUShort
title: RtlIntToUShort
author: windows-driver-content
description: Converts a value of type INT to a value of type USHORT.
old-location: kernel\rtlinttoushort.htm
old-project: kernel
ms.assetid: 52571477-80F5-4848-8BCC-AFA70140FABE
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlIntToUShort
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
req.alt-api: RtlIntToUShort
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

# RtlIntToUShort function



## -description
<p>Converts a value of type <b>INT</b> to a value of type <b>USHORT</b>.</p>


## -syntax

````
NTSTATUS RtlIntToUShort(
  _In_  INT    iOperand,
  _Out_ USHORT *pusResult
);
````


## -parameters
<dl>

### -param <i>iOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pusResult</i> [out]

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