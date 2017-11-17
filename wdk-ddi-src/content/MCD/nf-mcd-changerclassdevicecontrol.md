---
UID: NF.mcd.ChangerClassDeviceControl
title: ChangerClassDeviceControl
author: windows-driver-content
description: The ChangerClassDeviceControl routine is called by a changer minidriver to allow the class driver perform device-independent aspects of a device control operation.
old-location: storage\changerclassdevicecontrol.htm
ms.assetid: 9107fa7b-b061-4505-aef7-be04587a4199
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerClassDeviceControl
req.alt-loc: mcd.h
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
ms.keywords: ChangerClassDeviceControl
req.iface: 
---

# ChangerClassDeviceControl function



## -description
<p>The <b>ChangerClassDeviceControl</b> routine is called by a changer minidriver to allow the class driver perform device-independent aspects of a device control operation. </p>


## -syntax

````
NTSTATUS ChangerClassDeviceControl(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object of the device. </p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the I/O request packet (IRP) that initiated the device control operation. </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the <b>ChangerClassDeviceControl</b> routine returns STATUS_SUCCESS. Otherwise the routine returns one of the following status values.</p><dl>
<dt><b>STATUS_NO_SUCH_DEVICE</b></dt>
</dl><p>The device object does not have a properly initialized device extension.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The length of the output buffer indicated in the IRP is too small to hold the return data.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The length of the input buffer indicated in the IRP is too small to hold the input data that is necessary to complete the operation.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The length of the input buffer is zero.</p>

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
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
</dl>
</td>
</tr>
</table>