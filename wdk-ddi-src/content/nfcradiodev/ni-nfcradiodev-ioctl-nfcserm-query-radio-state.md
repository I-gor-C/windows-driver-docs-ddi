---
UID: NI.nfcradiodev.IOCTL_NFCSERM_QUERY_RADIO_STATE
title: IOCTL_NFCSERM_QUERY_RADIO_STATE
author: windows-driver-content
description: This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device.
old-location: nfpdrivers\ioctl_nfcserm_query_radio_state.htm
old-project: nfpdrivers
ms.assetid: 625E3B0B-78B4-4C12-B1FD-555FAA5E0E19
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NFCCX_DRIVER_GLOBALS, NFCCX_DRIVER_GLOBALS, *PNFCCX_DRIVER_GLOBALS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: nfcradiodev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_NFCSERM_QUERY_RADIO_STATE
req.alt-loc: nfcradiodev.h
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

# IOCTL_NFCSERM_QUERY_RADIO_STATE IOCTL



## -description
<p>This IOCTL is used by the SE radio management application or service to query the current radio power state of the proximity device.</p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-set-radio-state.md"> NFCRM_RADIO_STATE structure</a>
</p>

<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-set-radio-state.md"> NFCRM_RADIO_STATE structure</a>
</p>

<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-set-radio-state.md"> NFCRM_RADIO_STATE structure</a>
</p>

### -output-buffer-length
<p>sizeof(NFCRM_RADIO_STATE)</p>

<p>sizeof(NFCRM_RADIO_STATE)</p>

<p>sizeof(NFCRM_RADIO_STATE)</p>

<p>sizeof(NFCRM_RADIO_STATE)</p>

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

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfcradiodev.h</dt>
</dl>
</td>
</tr>
</table>