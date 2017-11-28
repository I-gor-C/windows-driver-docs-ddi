---
UID: NF.usbdlib.UsbBuildInterruptOrBulkTransferRequest
title: UsbBuildInterruptOrBulkTransferRequest
author: windows-driver-content
description: The UsbBuildInterruptOrBulkTransferRequest macro formats an URB to send or receive data on a bulk pipe, or to receive data from an interrupt pipe.
old-location: buses\usbbuildinterruptorbulktransferrequest.htm
old-project: usbref
ms.assetid: 2500fa22-b3f9-419d-9e37-5060b83403fb
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UsbBuildInterruptOrBulkTransferRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: Usbdlib.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UsbBuildInterruptOrBulkTransferRequest
req.alt-loc: usbdlib.h
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

# UsbBuildInterruptOrBulkTransferRequest function



## -description
<p>The <b>UsbBuildInterruptOrBulkTransferRequest</b> macro formats an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> to send or receive data on a bulk pipe, or to receive data from an interrupt pipe.</p>


## -syntax

````
void UsbBuildInterruptOrBulkTransferRequest(
  _Inout_  PURB             Urb,
  _In_     USHORT           Length,
  _In_     USBD_PIPE_HANDLE PipeHandle,
  _In_opt_ PVOID            TransferBuffer,
  _In_opt_ PMDL             TransferBufferMDL,
  _In_     ULONG            TransferBufferLength,
  _In_     ULONG            TransferFlags,
  _In_     PURB             Link
);
````


## -parameters
<dl>

### -param <i>Urb</i> [in, out]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> to be formatted as an interrupt or bulk transfer request.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the size, in bytes, of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>.</p>
</dd>

### -param <i>PipeHandle</i> [in]

<dd>
<p>Specifies the handle for this pipe returned by the HCD when a configuration was selected.</p>
</dd>

### -param <i>TransferBuffer</i> [in, optional]

<dd>
<p>Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <i>TransferBufferMDL</i>. The contents of this buffer depend on the value of <i>TransferFlags</i>. If USBD_TRANSFER_DIRECTION_IN is specified, this buffer will contain data read from the device on return from the HCD. Otherwise, this buffer contains driver-supplied data to be transferred to the device.</p>
</dd>

### -param <i>TransferBufferMDL</i> [in, optional]

<dd>
<p>Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <i>TransferBuffer</i>. The contents of the buffer depend on the value of <i>TransferFlags</i>. If USBD_TRANSFER_DIRECTION_IN is specified, the described buffer will contain data read from the device on return from the HCD. Otherwise, the buffer contains driver-supplied data to be transferred to the device. The MDL must be allocated from nonpaged pool.</p>
</dd>

### -param <i>TransferBufferLength</i> [in]

<dd>
<p>Specifies the length, in bytes, of the buffer specified in <i>TransferBuffer</i> or described in <i>TransferBufferMDL</i>.</p>
</dd>

### -param <i>TransferFlags</i> [in]

<dd>
<p>Specifies zero, one, or a combination of the following flags:</p>
<p></p>
<dl>

### -param <a id="USBD_TRANSFER_DIRECTION_IN"></a><a id="usbd_transfer_direction_in"></a>USBD_TRANSFER_DIRECTION_IN

<dd>
<p>Is set to request data from a device. To transfer data to a device, this flag must be clear.</p>
</dd>

### -param <a id="USBD_SHORT_TRANSFER_OK"></a><a id="usbd_short_transfer_ok"></a>USBD_SHORT_TRANSFER_OK

<dd>
<p>Can be used if USBD_TRANSFER_DIRECTION_IN is set. If set, directs the HCD not to return an error if a packet is received from the device that is shorter than the maximum packet size for the endpoint. Otherwise, a short request returns an error condition.</p>
</dd>
</dl>
</dd>

### -param <i>Link</i> [in]

<dd>
<p>Reserved. Must be set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

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
<dt>Usbdlib.h (include Usbdlib.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539280">USB_DEVICE_DESCRIPTOR</a>
</dt>
<dt><a href="usb_reference.htm#client">USB device driver programming reference</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UsbBuildInterruptOrBulkTransferRequest routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
