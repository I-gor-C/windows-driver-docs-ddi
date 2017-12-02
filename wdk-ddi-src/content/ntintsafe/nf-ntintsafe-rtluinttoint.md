---
UID: NF.ntintsafe.RtlUIntToInt
title: RtlUIntToInt
author: windows-driver-content
description: Converts a value of type UINT to a value of type INT.
old-location: kernel\rtluinttoint.htm
old-project: kernel
ms.assetid: 5C595F39-3F47-4B4D-B6C6-6CBC5848AA4B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlUIntToInt
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
req.alt-api: RtlUIntToInt
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

# RtlUIntToInt function



## -description
<p>Converts a value of type <b>UINT</b> to a value of type <b>INT</b>.</p>


## -syntax

````
NTSTATUS RtlUIntToInt(
  _In_  UINT uOperand,
  _Out_ INT  *piResult
);
````


## -parameters
<dl>

### -param uOperand [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param piResult [out]

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