---
UID: NI.nfcradiodev.IOCTL_NFCRM_QUERY_RADIO_STATE
title: IOCTL_NFCRM_QUERY_RADIO_STATE
author: windows-driver-content
description: This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device.
old-location: nfpdrivers\ioctl_nfcrm_query_radio_state.htm
old-project: nfpdrivers
ms.assetid: BEFA6568-3E89-4626-AAC2-A0C628E5429F
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
req.alt-api: IOCTL_NFCRM_QUERY_RADIO_STATE
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

# IOCTL_NFCRM_QUERY_RADIO_STATE IOCTL



## -description
<p>This IOCTL is used by the radio management application or service to query the current radio power state of the proximity device.</p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-radio-state.md"> NFCRM_RADIO_STATE structure</a>
</p>

<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-radio-state.md"> NFCRM_RADIO_STATE structure</a>
</p>

<p>
<a href="..\nfcradiodev\ns-nfcradiodev--nfcrm-radio-state.md"> NFCRM_RADIO_STATE structure</a>
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
<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful.</p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful.</p>

## -remarks
<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

<p>The <b>STATUS_INVALID_PARAMETER</b> return code is no longer required. A bug was discovered in Windows 10 build 10240, that Windows would send a non-null input parameter with this IOCTL. This bug was fixed in later versions of Windows. To simplify code, drivers can ignore the input parameters in all versions of Windows 10.</p>

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