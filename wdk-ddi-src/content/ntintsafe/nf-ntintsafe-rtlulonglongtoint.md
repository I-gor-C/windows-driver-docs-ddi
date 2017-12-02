---
UID: NF.ntintsafe.RtlULongLongToInt
title: RtlULongLongToInt
author: windows-driver-content
description: Converts a value of type ULONGLONG to a value of type INT.
old-location: kernel\rtlulonglongtoint.htm
old-project: kernel
ms.assetid: C52CB40D-0B3D-4ED9-99FD-464D23481AD3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongLongToInt
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
req.alt-api: RtlULongLongToInt
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

# RtlULongLongToInt function



## -description
<p>Converts a value of type <b>ULONGLONG</b> to a value of type <b>INT</b>.</p>


## -syntax

````
NTSTATUS RtlULongLongToInt(
  _In_  ULONGLONG ullOperand,
  _Out_ INT       *piResult
);
````


## -parameters
<dl>

### -param ullOperand [in]

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