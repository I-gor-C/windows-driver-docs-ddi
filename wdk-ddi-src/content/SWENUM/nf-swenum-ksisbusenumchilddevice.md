---
UID: NF.swenum.KsIsBusEnumChildDevice
title: KsIsBusEnumChildDevice
author: windows-driver-content
description: The KsIsBusEnumChildDevice function determines if the given device object is a child device of the demand-load bus enumerator object.
old-location: stream\ksisbusenumchilddevice.htm
ms.assetid: 7b9aa600-dd47-4ef1-acc8-02fb1b4f51ce
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsIsBusEnumChildDevice
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
ms.keywords: KsIsBusEnumChildDevice
req.iface: 
req.product: Windows 10 or later.
---

# KsIsBusEnumChildDevice function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsIsBusEnumChildDevice</b> function determines if the given device object is a child device of the demand-load bus enumerator object. </p>


## -syntax

````
NTSTATUS KsIsBusEnumChildDevice(
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PBOOLEAN       ChildDevice
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to a device object.</p>
</dd>

### -param <i>ChildDevice</i> [out]

<dd>
<p>Pointer to a BOOLEAN to receive the result. <b>KsIsBusEnumChildDevice</b> sets this to <b>TRUE</b> if the given device object is a child device of the demand-load bus enumerator object, or <b>FALSE</b> otherwise.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the given device object's device extension is valid; otherwise, it returns an error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Swenum.h (include Swenum.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>