---
UID: NF.ntintsafe.RtlUIntPtrToUInt16
title: RtlUIntPtrToUInt16
author: windows-driver-content
description: Converts a value of type UINT_PTR to a value of type UINT16.
old-location: kernel\rtluintptrtouint16.htm
old-project: kernel
ms.assetid: 405FB676-64FD-43DE-BCD9-233C8B43D851
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlUIntPtrToUInt16
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
req.alt-api: RtlUIntPtrToUInt16
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

# RtlUIntPtrToUInt16 function



## -description
<p>Converts a value of type <b>UINT_PTR</b> to a value of type <b>UINT16</b>.</p>


## -syntax

````
NTSTATUS RtlUIntPtrToUInt16(
  _In_  UINT_PTR uOperand,
  _Out_ UINT16   *pu16Result
);
````


## -parameters
<dl>

### -param <i>uOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>pu16Result</i> [out]

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