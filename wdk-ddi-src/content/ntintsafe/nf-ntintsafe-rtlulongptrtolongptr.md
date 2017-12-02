---
UID: NF.ntintsafe.RtlULongPtrToLongPtr
title: RtlULongPtrToLongPtr
author: windows-driver-content
description: Converts a value of type ULONG_PTR to a value of type LONG_PTR.
old-location: kernel\rtlulongptrtolongptr.htm
old-project: kernel
ms.assetid: 5231A8BC-2F7A-4A2C-931C-D3A81563754A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlULongPtrToLongPtr
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
req.alt-api: RtlULongPtrToLongPtr
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

# RtlULongPtrToLongPtr function



## -description
<p>Converts a value of type <b>ULONG_PTR</b> to a value of type <b>LONG_PTR</b>.</p>


## -syntax

````
NTSTATUS RtlULongPtrToLongPtr(
  _In_  ULONG_PTR ulOperand,
  _Out_ LONG_PTR  *plResult
);
````


## -parameters
<dl>

### -param ulOperand [in]

<dd>
<p>The value to be converted.</p>
</dd>

### -param plResult [out]

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