---
UID: NF.ntintsafe.RtlULongPtrToLong
title: RtlULongPtrToLong
author: windows-driver-content
description: Converts a value of type ULONG_PTR to a value of type LONG.
old-location: kernel\rtlulongptrtolong.htm
ms.assetid: 7A5F39C8-DCA2-4684-801A-A334960AA523
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntintsafe.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlULongPtrToLong
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
ms.keywords: RtlULongPtrToLong
req.iface: 
---

# RtlULongPtrToLong function



## -description
<p>Converts a value of type <b>ULONG_PTR</b> to a value of type <b>LONG</b>.</p>


## -syntax

````
NTSTATUS RtlULongPtrToLong(
  _In_  ULONG_PTR ulOperand,
  _Out_ LONG      *plResult
);
````


## -parameters
<dl>

### -param <i>ulOperand</i> [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param <i>plResult</i> [out]

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