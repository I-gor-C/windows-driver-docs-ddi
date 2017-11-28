---
UID: NF.ntintsafe.RtlUIntToChar
title: RtlUIntToChar
author: windows-driver-content
description: Converts a value of type UINT to a value of type CHAR.
old-location: kernel\rtluinttochar.htm
old-project: kernel
ms.assetid: 1E4620A9-5CAA-4E45-9D43-1E183D7EB572
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUIntToChar
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
req.alt-api: RtlUIntToChar
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

# RtlUIntToChar function



## -description
<p>Converts a value of type <b>UINT</b> to a value of type <b>CHAR</b>.</p>


## -syntax

````
NTSTATUS RtlUIntToChar(
  _In_  UINT uOperand,
  _Out_ CHAR *pch
);
````


## -parameters
<dl>

### -param <i>uOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pch</i> [out]

<dd>
<p>A pointer to the converted value. In the case where the conversion causes a truncation of the original value, the function returns STATUS_INTEGER_OVERFLOW and this parameter is not valid.</p>
</dd>
</dl>

## -remarks
<p>This is one of a set of inline functions designed to provide type conversions and perform validity checks with minimal impact on performance.</p>

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