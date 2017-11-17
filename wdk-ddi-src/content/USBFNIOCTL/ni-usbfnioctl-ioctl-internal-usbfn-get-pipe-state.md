---
UID: NI.usbfnioctl.IOCTL_INTERNAL_USBFN_GET_PIPE_STATE
title: IOCTL_INTERNAL_USBFN_GET_PIPE_STATE
author: windows-driver-content
description: The class driver sends this request to get the stall state of the specified pipe.
old-location: buses\ioctl_internal_usbfn_get_pipe_state.htm
ms.assetid: CFBFC5E4-852C-4287-A85E-2EF3C89FE474
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbfnioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_USBFN_GET_PIPE_STATE
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
ms.keywords: USBFN_USB_STRING, USBFN_USB_STRING, *PUSBFN_USB_STRING
req.iface: 
req.product: Windows 10 or later.
---

# IOCTL_INTERNAL_USBFN_GET_PIPE_STATE IOCTL



## -description
<p>The class driver sends this request to get the stall state of the specified pipe.</p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <b>USBFNPIPEID</b> type that specifies the pipe ID.</p>

### -input-buffer-length
<p>The size of a <b>USBFNPIPEID</b> type.</p>

<p>The size of a <b>USBFNPIPEID</b> type.</p>

### -output-buffer
<p>A pointer to <b>BOOLEAN</b> value that  is set by USB Function Class Extension (UFX) to indicate whether or not the specified pipe is stalled. TRUE, indicates the pipe is in stall state; FALSE indicates the pipe is in clear state.
</p>

<p>A pointer to <b>BOOLEAN</b> value that  is set by USB Function Class Extension (UFX) to indicate whether or not the specified pipe is stalled. TRUE, indicates the pipe is in stall state; FALSE indicates the pipe is in clear state.
</p>

<p>A pointer to <b>BOOLEAN</b> value that  is set by USB Function Class Extension (UFX) to indicate whether or not the specified pipe is stalled. TRUE, indicates the pipe is in stall state; FALSE indicates the pipe is in clear state.
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
<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

<p>This request must be sent after sending the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187891">IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS</a> request.</p>

<p>When stalled, the pipe sends STALL transaction packets to the host. See the Universal Serial Bus (USB) specification for more information.</p>

<p>UFX forwards this IOCTL request to the transfer queue created for the endpoint by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187965">UfxEndpointCreate</a>.</p>

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