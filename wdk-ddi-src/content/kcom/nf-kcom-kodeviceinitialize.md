---
UID: NF.kcom.KoDeviceInitialize
title: KoDeviceInitialize
author: windows-driver-content
description: The KoDeviceInitialize function adds a kernel COM create-item entry to the specified device object.
old-location: stream\kodeviceinitialize.htm
old-project: stream
ms.assetid: 68ae87c5-7d71-4e85-8052-4e5c422340fb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KoDeviceInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: kcom.h
req.include-header: Kcom.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KoDeviceInitialize
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
---

# KoDeviceInitialize function



## -description
<p><i>This function is intended for internal use only.</i></p>
<p>The <b>KoDeviceInitialize</b> function adds a kernel COM create-item entry to the specified device object. </p>


## -syntax

````
NTSTATUS KoDeviceInitialize(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>Pointer to a device object. The device object is assumed to contain a KSOBJECT_HEADER in its device extension.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if successful. Otherwise, it returns a memory allocation error.</p>

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
<dt>Kcom.h (include Kcom.h)</dt>
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