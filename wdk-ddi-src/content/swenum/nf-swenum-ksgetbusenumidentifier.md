---
UID: NF.swenum.KsGetBusEnumIdentifier
title: KsGetBusEnumIdentifier
author: windows-driver-content
description: The KsGetBusEnumIdentifier function retrieves the software bus enumerator identifier for the bus device associated with the given IRP.
old-location: stream\ksgetbusenumidentifier.htm
old-project: stream
ms.assetid: 50e14e01-5879-4a84-a8c2-f03c953dbeec
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsGetBusEnumIdentifier
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetBusEnumIdentifier
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
req.iface: 
req.product: Windows 10 or later.
---

# KsGetBusEnumIdentifier function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KsGetBusEnumIdentifier</b> function retrieves the software bus enumerator identifier for the bus device associated with the given IRP. </p>


## -syntax

````
NTSTATUS KsGetBusEnumIdentifier(
  _Inout_ PIRP Irp
);
````


## -parameters
<dl>

### -param Irp [in, out]

<dd>
<p>Pointer to the IRP that specifies the address and size of the user output buffer to receive the requested bus enumerator identifier.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the bus enumerator identifier was retrieved successfully. Otherwise, it returns one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The specified device is not valid</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The specified buffer was not large enough</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>No buffer was specified (the required buffer size is returned in the Irp).</p>

<p> </p>

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