---
UID: NI.nfcsedev.IOCTL_NFCSE_GET_NFCC_CAPABILITIES
title: IOCTL_NFCSE_GET_NFCC_CAPABILITIES
author: windows-driver-content
description: The IOCTL_NFCSE_GET_NFCC_CAPABILITIES control code returns information about the current NFC controller capabilities, including the maximum Listen Mode Routing table size (defined in section 4.2 of the NFC Controller Interface (NCI) Technical Specification Version 1.1) and supported routing modes.
old-location: nfpdrivers\ioctl_nfcse_get_nfcc_capabilities.htm
old-project: nfpdrivers
ms.assetid: 4323FEDF-A7D0-4B67-BC3D-ECAA7AD1CC08
ms.author: windowsdriverdev
ms.date: 11/27/2017
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
req.alt-api: IOCTL_NFCSE_GET_NFCC_CAPABILITIES
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

# IOCTL_NFCSE_GET_NFCC_CAPABILITIES IOCTL



## -description
<p>The <b>IOCTL_NFCSE_GET_NFCC_CAPABILITIES</b> 
   control code returns information about the current NFC controller capabilities, including the  maximum Listen Mode Routing table size (defined in section 4.2 of the <i>NFC Controller Interface (NCI) Technical Specification Version 1.1) </i>and supported routing modes. </p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-nfcc-capabilities.md"> SECURE_ELEMENT_NFCC_CAPABILITIES</a> containing NFC controller capabilities.</p>

<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-nfcc-capabilities.md"> SECURE_ELEMENT_NFCC_CAPABILITIES</a> containing NFC controller capabilities.</p>

<p>
<a href="..\nfcsedev\ns-nfcsedev--secure-element-nfcc-capabilities.md"> SECURE_ELEMENT_NFCC_CAPABILITIES</a> containing NFC controller capabilities.</p>

### -output-buffer-length
<p>sizeof(SECURE_ELEMENT_NFCC_CAPABILITIES)</p>

<p>sizeof(SECURE_ELEMENT_NFCC_CAPABILITIES)</p>

<p>sizeof(SECURE_ELEMENT_NFCC_CAPABILITIES)</p>

<p>sizeof(SECURE_ELEMENT_NFCC_CAPABILITIES)</p>

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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>