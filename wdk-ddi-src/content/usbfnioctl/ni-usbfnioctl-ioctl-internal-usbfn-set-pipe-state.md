---
UID: NI.usbfnioctl.IOCTL_INTERNAL_USBFN_SET_PIPE_STATE
title: IOCTL_INTERNAL_USBFN_SET_PIPE_STATE
author: windows-driver-content
description: The class driver sends this request to set the stall state of the specified USB pipe.
old-location: buses\ioctl_internal_usbfn_set_pipe_state.htm
old-project: usbref
ms.assetid: EB44DE6F-6B88-4F6D-B9AC-3FF7A519C047
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_USB_STRING, USBFN_USB_STRING, *PUSBFN_USB_STRING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbfnioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_USBFN_SET_PIPE_STATE
req.alt-loc: usbfnioctl.h
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
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USBFN_SET_PIPE_STATE IOCTL



## -description
<p>The class driver sends this request to set the stall state of the specified USB pipe. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.</p>

### -input-buffer-length
<p>The size of a <b>USBFNPIPEID</b> type.</p>

<p>The size of a <b>USBFNPIPEID</b> type.</p>

### -output-buffer
<p>A pointer to <b>BOOLEAN</b> value that  specifies the stall state to set. If TRUE,  USB Function Class Extension (UFX) sets the  pipe to stall state; FALSE sets to clear state.
</p>

<p>A pointer to <b>BOOLEAN</b> value that  specifies the stall state to set. If TRUE,  USB Function Class Extension (UFX) sets the  pipe to stall state; FALSE sets to clear state.
</p>

<p>A pointer to <b>BOOLEAN</b> value that  specifies the stall state to set. If TRUE,  USB Function Class Extension (UFX) sets the  pipe to stall state; FALSE sets to clear state.
</p>

### -output-buffer-length
<p>The size of a <b>BOOLEAN</b>.</p>

<p>The size of a <b>BOOLEAN</b>.</p>

<p>The size of a <b>BOOLEAN</b>.</p>

<p>The size of a <b>BOOLEAN</b>.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>UFX completes the request with <b>STATUS_SUCCESS</b>.</p>

<p>UFX completes the request with <b>STATUS_SUCCESS</b>.</p>

<p>UFX completes the request with <b>STATUS_SUCCESS</b>.</p>

<p>UFX completes the request with <b>STATUS_SUCCESS</b>.</p>

<p>UFX completes the request with <b>STATUS_SUCCESS</b>.</p>

## -remarks
<p>This request must be sent after sending the <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="..\ufxclient\nf-ufxclient-ufxendpointcreate.md">UfxEndpointCreate</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbfnioctl.h</dt>
</dl>
</td>
</tr>
</table>