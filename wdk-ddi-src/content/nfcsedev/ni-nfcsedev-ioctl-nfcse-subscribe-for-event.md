---
UID: NI.nfcsedev.IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT
title: IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT
author: windows-driver-content
description: The IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT control code is issued by a client to subscribe to a specific event.
old-location: nfpdrivers\ioctl_nfcse_subscribe_for_event.htm
old-project: nfpdrivers
ms.assetid: 3A184392-A68C-4AFC-AE9F-36247153ADD2
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NFCRM_SET_RADIO_STATE, NFCRM_SET_RADIO_STATE, *PNFCRM_SET_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT
req.alt-loc: nfcsedev.h
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

# IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT IOCTL



## -description
<p>The <b>IOCTL_NFCSE_SUBSCRIBE_FOR_EVENT</b> 
   control code is issued by a client to subscribe to a specific event. </p>


## -ioctlparameters

### -input-buffer
<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-event-subscription-info.md"> SECURE_ELEMENT_EVENT_SUBSCRIPTION_INFO</a> structure.
</p>

### -input-buffer-length

<text></text>

### -output-buffer
<p>None</p>

<p>None</p>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

## -remarks
<p>The following are requirements that the driver must adhere to.<ul>
<li>This IOCTL must be called on a handle with a <b>SEEvents</b> file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE.</li>
<li><b>GUID_NULL</b> can be specified by the client as a wild card to subscribe for a specific event from all enumerated secure elements.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>This IOCTL must be called on a handle with a <b>SEEvents</b> file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE.</li>
<li><b>GUID_NULL</b> can be specified by the client as a wild card to subscribe for a specific event from all enumerated secure elements.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>This IOCTL must be called on a handle with a <b>SEEvents</b> file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE.</li>
<li><b>GUID_NULL</b> can be specified by the client as a wild card to subscribe for a specific event from all enumerated secure elements.</li>
</ul>
</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>This IOCTL must be called on a handle with a <b>SEEvents</b> file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE.</li>
<li><b>GUID_NULL</b> can be specified by the client as a wild card to subscribe for a specific event from all enumerated secure elements.</li>
</ul>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>