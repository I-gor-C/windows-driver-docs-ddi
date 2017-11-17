---
UID: NF.ks.KsDispatchSetSecurity
title: KsDispatchSetSecurity
author: windows-driver-content
description: The KsDispatchSetSecurity function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor.
old-location: stream\ksdispatchsetsecurity.htm
ms.assetid: c1af342a-438d-4c83-be2d-a4c4c9f204b5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDispatchSetSecurity
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
ms.keywords: KsDispatchSetSecurity
req.iface: 
---

# KsDispatchSetSecurity function



## -description
<p>The <b>KsDispatchSetSecurity</b> function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor. The assumption is that the KSOBJECT_HEADER structure is being used in the <b>FsContext</b> data structure and that the <b>CreateItem</b> points to a valid item that optionally contains a security descriptor.</p>


## -syntax

````
NTSTATUS KsDispatchSetSecurity(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Specifies the device object associated with the IRP.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP that is being handled.</p>
</dd>
</dl>

## -returns
<p>The <b>KsDispatchSetSecurity</b> function returns the security set status and completes the IRP.</p>

## -remarks
<p>This security descriptor must be allocated in its own piece of pool memory, since <b>KsDispatchSetSecurity</b> will replace the existing descriptor with a new allocation. Therefore, it cannot be shared with <b>CreateItem</b>.</p>

<p>This security descriptor must be allocated in its own piece of pool memory, since <b>KsDispatchSetSecurity</b> will replace the existing descriptor with a new allocation. Therefore, it cannot be shared with <b>CreateItem</b>.</p>

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
<dt>Ks.h (include Ks.h)</dt>
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