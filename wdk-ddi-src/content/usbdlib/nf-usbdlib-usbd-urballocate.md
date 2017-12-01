---
UID: NF.usbdlib.USBD_UrbAllocate
title: USBD_UrbAllocate
author: windows-driver-content
description: The USBD_UrbAllocate routine allocates a USB Request Block (URB).
old-location: buses\usbd_urballocate.htm
old-project: usbref
ms.assetid: 384E04BE-794F-4F87-81E5-35B974EB6172
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_UrbAllocate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_UrbAllocate
req.alt-loc: Usbdex.lib,Usbdex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbdex.lib
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBD_UrbAllocate function



## -description
<p>The <b>USBD_UrbAllocate</b> routine allocates a USB Request Block (URB).</p>


## -syntax

````
NTSTATUS USBD_UrbAllocate(
  _In_  USBD_HANDLE USBDHandle,
  _Out_ PURB        *Urb
);
````


## -parameters
<dl>

### -param <i>USBDHandle</i> [in]

<dd>
<p>USBD handle that is retrieved by the client driver in a previous call to  the <a href="..\usbdlib\nf-usbdlib-usbd-createhandle.md">USBD_CreateHandle</a> routine.</p>
</dd>

### -param <i>Urb</i> [out]

<dd>
<p>Pointer to the newly allocated <a href="..\usb\ns-usb--urb.md">URB</a> structure. All members of the structure are set to zero. The client driver must free the URB when the driver has finished using it by calling <a href="..\usbdlib\nf-usbdlib-usbd-urbfree.md">USBD_UrbFree</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>USBD_UrbAllocate</b> routine returns STATUS_SUCCESS if the request is successful. Otherwise,  <b>USBD_UrbAllocate</b> sets <i>Urb</i> to NULL and returns a failure code. </p>

<p>Possible values include, but are not limited to, STATUS_INVALID_PARAMETER, which  indicates the caller passed in NULL to <i>USBDHandle</i> or <i>Urb</i>.</p>

## -remarks
<p>The <b>USBD_UrbAllocate</b> routine enables the underlying USB driver stack to allocate an opaque URB context for the URB. By using the URB context, the USB driver stack can process requests more efficiently and reliably. Those optimizations are provided by the USB 3.0 driver stack that is included in Windows 8. The client driver cannot access the URB context; the context is used internally by the bus driver. </p>

<p>Regardless of the USB protocol version of the host controller, the underlying USB driver stack, the target operating system, the client driver must always call <b>USBD_UrbAllocate</b> to allocate an <a href="..\usb\ns-usb--urb.md">URB</a> structure.  <b>USBD_UrbAllocate</b> replaces earlier allocation mechanisms, such as  <a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>, or allocating them on the stack. </p>

<p>The client driver must <i>not</i> use <b>USBD_UrbAllocate</b>, </p>

<p>For more information about replacement routines, see <a href="buses.how_to_add_xrb_support_for_client_drivers">Allocating and Building URBs</a>.</p>

<p>You must call <a href="..\usbdlib\nf-usbdlib-usbd-urbfree.md">USBD_UrbFree</a> to release the URB allocated by <b>USBD_UrbAllocate</b>. </p>

<p>The following code example shows how to allocate, submit, and release a URB. The example submits the URB synchronously.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbdlib\nf-usbdlib-usbd-urbfree.md">USBD_UrbFree</a>
</dt>
<dt>
<a href="buses.how_to_add_xrb_support_for_client_drivers">Allocating and Building URBs</a>
</dt>
<dt>
<a href="buses.communicating_with_a_usb_device">Sending Requests to a USB Device</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_UrbAllocate routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
