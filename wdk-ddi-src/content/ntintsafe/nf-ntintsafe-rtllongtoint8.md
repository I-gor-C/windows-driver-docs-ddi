---
UID: NF.ntintsafe.RtlLongToInt8
title: RtlLongToInt8
author: windows-driver-content
description: Converts a value of type LONG to a value of type INT8.
old-location: kernel\rtllongtoint8.htm
old-project: kernel
ms.assetid: 38BE4F80-DEF2-486B-8A37-BCFD7626325D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlLongToInt8
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
req.alt-api: RtlLongToInt8
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

# RtlLongToInt8 function



## -description
<p>Converts a value of type <b>LONG</b> to a value of type <b>INT8</b>.</p>


## -syntax

````
NTSTATUS RtlLongToInt8(
  _In_  LONG lOperand,
  _Out_ INT8 *pi8Result
);
````


## -parameters
<dl>

### -param lOperand [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param pi8Result [out]

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