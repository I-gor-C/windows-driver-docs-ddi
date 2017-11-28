---
UID: NF.ks.KsDefaultDeviceIoCompletion
title: KsDefaultDeviceIoCompletion
author: windows-driver-content
description: The KsDefaultDeviceIoCompletion function is used to return a default response and to complete any device I/O control.
old-location: stream\ksdefaultdeviceiocompletion.htm
old-project: stream
ms.assetid: 6e466815-aef4-4602-b3cf-66b47b2e3f3b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsDefaultDeviceIoCompletion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDefaultDeviceIoCompletion
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

# KsDefaultDeviceIoCompletion function



## -description
<p>The <b>KsDefaultDeviceIoCompletion</b> function is used to return a default response and to complete any device I/O control. It can be used in the KSDISPATCH_TABLE and as the default response to unknown Ioctl's. It is important to use this function so that queries such as property requests return the correct value rather than just STATUS_INVALID_DEVICE_REQUEST when properties are not support for instance.</p>


## -syntax

````
NTSTATUS KsDefaultDeviceIoCompletion(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Specifies the device object dispatched to.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the IRP to return a default response to.</p>
</dd>
</dl>

## -returns
<p>The <b>KsDefaultDeviceIoCompletion</b> function returns the default response to the possible IOCTLs.</p>

## -remarks
<p>Note that this routine will complete the IRP.</p>

<p>Note that this routine will complete the IRP.</p>

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