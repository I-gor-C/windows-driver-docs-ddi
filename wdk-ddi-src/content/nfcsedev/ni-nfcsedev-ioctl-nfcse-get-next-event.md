---
UID: NI.nfcsedev.IOCTL_NFCSE_GET_NEXT_EVENT
title: IOCTL_NFCSE_GET_NEXT_EVENT
author: windows-driver-content
description: The IOCTL_NFCSE_GET_NEXT_EVENT control code returns the next event available in the buffer, or if there are no more buffered events remains pending until a secure element event is available. The event details must then be returned to the caller.
old-location: nfpdrivers\ioctl_nfcse_get_next_event.htm
old-project: nfpdrivers
ms.assetid: B142BB21-D70E-4BA2-B2C1-60468FA8378E
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
req.alt-api: IOCTL_NFCSE_GET_NEXT_EVENT
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

# IOCTL_NFCSE_GET_NEXT_EVENT IOCTL



## -description
<p>The <b>IOCTL_NFCSE_GET_NEXT_EVENT</b> 
   control code returns the next event available in the buffer, or if there are no more buffered events remains pending until a secure element event is available. The event details must then be returned to the caller.  </p>


## -ioctlparameters

### -input-buffer
<p>None</p>

### -input-buffer-length
<p>None</p>

<p>None</p>

### -output-buffer
<p>
                A <b>DWORD</b> indicating the size of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn905590">SECURE_ELEMENT_EVENT_INFO</a> structure plus its payload, immediately followed by the <b>SECURE_ELEMENT_EVENT_INFO</b> structure itself. </p>

<p>
                A <b>DWORD</b> indicating the size of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn905590">SECURE_ELEMENT_EVENT_INFO</a> structure plus its payload, immediately followed by the <b>SECURE_ELEMENT_EVENT_INFO</b> structure itself. </p>

<p>
                A <b>DWORD</b> indicating the size of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn905590">SECURE_ELEMENT_EVENT_INFO</a> structure plus its payload, immediately followed by the <b>SECURE_ELEMENT_EVENT_INFO</b> structure itself. </p>

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

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p> </p>

## -remarks
<p>The following are requirements that the driver must adhere to.<ul>
<li>
<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>
</li>
<li>
<p>This driver must support CancelIO for this pending IOCTL.</p>
</li>
<li>
<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>
</li>
<li>
<p>The following conditions must be met when this IOCTL is received in the driver:</p>
<ul>
<li>
<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>
</li>
<li>
<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>
</li>
</ul>
</li>
<li>
<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>
</li>
<li>
<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>
</li>
</ul>
</p>

<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>

<p>This driver must support CancelIO for this pending IOCTL.</p>

<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>

<p>The following conditions must be met when this IOCTL is received in the driver:</p>

<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>

<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>

<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>

<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>
<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>
</li>
<li>
<p>This driver must support CancelIO for this pending IOCTL.</p>
</li>
<li>
<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>
</li>
<li>
<p>The following conditions must be met when this IOCTL is received in the driver:</p>
<ul>
<li>
<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>
</li>
<li>
<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>
</li>
</ul>
</li>
<li>
<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>
</li>
<li>
<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>
</li>
</ul>
</p>

<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>

<p>This driver must support CancelIO for this pending IOCTL.</p>

<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>

<p>The following conditions must be met when this IOCTL is received in the driver:</p>

<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>

<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>

<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>

<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>
<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>
</li>
<li>
<p>This driver must support CancelIO for this pending IOCTL.</p>
</li>
<li>
<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>
</li>
<li>
<p>The following conditions must be met when this IOCTL is received in the driver:</p>
<ul>
<li>
<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>
</li>
<li>
<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>
</li>
</ul>
</li>
<li>
<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>
</li>
<li>
<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>
</li>
</ul>
</p>

<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>

<p>This driver must support CancelIO for this pending IOCTL.</p>

<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>

<p>The following conditions must be met when this IOCTL is received in the driver:</p>

<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>

<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>

<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>

<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>
<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>
</li>
<li>
<p>This driver must support CancelIO for this pending IOCTL.</p>
</li>
<li>
<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>
</li>
<li>
<p>The following conditions must be met when this IOCTL is received in the driver:</p>
<ul>
<li>
<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>
</li>
<li>
<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>
</li>
</ul>
</li>
<li>
<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>
</li>
<li>
<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>
</li>
</ul>
</p>

<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>

<p>This driver must support CancelIO for this pending IOCTL.</p>

<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>

<p>The following conditions must be met when this IOCTL is received in the driver:</p>

<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>

<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>

<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>

<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>

<p>The following are requirements that the driver must adhere to.<ul>
<li>
<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>
</li>
<li>
<p>This driver must support CancelIO for this pending IOCTL.</p>
</li>
<li>
<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>
</li>
<li>
<p>The following conditions must be met when this IOCTL is received in the driver:</p>
<ul>
<li>
<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>
</li>
<li>
<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>
</li>
</ul>
</li>
<li>
<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>
</li>
<li>
<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>
</li>
</ul>
</p>

<p>This IOCTL must be called on a handle that has an <b>SEEvents</b> relative file name; otherwise, the driver returns STATUS_INVALID_DEVICE_STATE</p>

<p>This driver must support CancelIO for this pending IOCTL.</p>

<p>This driver must maintain a received queue of the received secure element events that match the subscription type.</p>

<p>The following conditions must be met when this IOCTL is received in the driver:</p>

<p>If the received queue is empty, then the driver must pend the IOCTL for later completion.</p>

<p>If the received queue is non-empty, then the driver must de-queue one event, copy the message buffer to the IOCTL’s output buffer, and complete the IOCTL with <b>STATUS_SUCCESS</b> immediately.</p>

<p>If the driver completes this IOCTL with STATUS_SUCCESS, the first DWORD [4 bytes] of the output buffer must contain the size of the SECURE_ELEMENT_EVENT_INFO structure plus its payload.</p>

<p>If a received secure element event info is too large to be copied into this IOCTL’s buffer, the driver must copy the required buffer size into the first 4 bytes of the output buffer, set the IOCTL’s information field to sizeof(DWORD), and complete the IOCTL with <b>STATUS_BUFFER_OVERFLOW</b>. The event must then be left in the received queue.</p>

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