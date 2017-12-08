---
UID: NF.usbdlib.USBD_UrbAllocate
title: USBD_UrbAllocate function
author: windows-driver-content
description: The USBD_UrbAllocate routine allocates a USB Request Block (URB).
old-location: buses\usbd_urballocate.htm
old-project: usbref
ms.assetid: 384E04BE-794F-4F87-81E5-35B974EB6172
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.product: Windows 10 or later.
---

# USBD_UrbAllocate function



## -description
The <b>USBD_UrbAllocate</b> routine allocates a USB Request Block (URB).


## -syntax

````
NTSTATUS USBD_UrbAllocate(
  _In_  USBD_HANDLE USBDHandle,
  _Out_ PURB        *Urb
);
````


## -parameters

### -param USBDHandle [in]

USBD handle that is retrieved by the client driver in a previous call to  the <a href="buses.usbd_register">USBD_CreateHandle</a> routine.

### -param Urb [out]

Pointer to the newly allocated <a href="buses.urb">URB</a> structure. All members of the structure are set to zero. The client driver must free the URB when the driver has finished using it by calling <a href="buses.usbd_urbfree">USBD_UrbFree</a>.

## -returns
The <b>USBD_UrbAllocate</b> routine returns STATUS_SUCCESS if the request is successful. Otherwise,  <b>USBD_UrbAllocate</b> sets <i>Urb</i> to NULL and returns a failure code. 

Possible values include, but are not limited to, STATUS_INVALID_PARAMETER, which  indicates the caller passed in NULL to <i>USBDHandle</i> or <i>Urb</i>.

## -remarks
The <b>USBD_UrbAllocate</b> routine enables the underlying USB driver stack to allocate an opaque URB context for the URB. By using the URB context, the USB driver stack can process requests more efficiently and reliably. Those optimizations are provided by the USB 3.0 driver stack that is included in Windows 8. The client driver cannot access the URB context; the context is used internally by the bus driver. 

Regardless of the USB protocol version of the host controller, the underlying USB driver stack, the target operating system, the client driver must always call <b>USBD_UrbAllocate</b> to allocate an <a href="buses.urb">URB</a> structure.  <b>USBD_UrbAllocate</b> replaces earlier allocation mechanisms, such as  <a href="kernel.exallocatepoolwithtag">ExAllocatePoolWithTag</a>, or allocating them on the stack. 

The client driver must <i>not</i> use <b>USBD_UrbAllocate</b>, 

For more information about replacement routines, see <a href="buses.how_to_add_xrb_support_for_client_drivers">Allocating and Building URBs</a>.

You must call <a href="buses.usbd_urbfree">USBD_UrbFree</a> to release the URB allocated by <b>USBD_UrbAllocate</b>. 

The following code example shows how to allocate, submit, and release a URB. The example submits the URB synchronously.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usbd_urbfree">USBD_UrbFree</a>
</dt>
<dt>
<a href="buses.how_to_add_xrb_support_for_client_drivers">Allocating and Building URBs</a>
</dt>
<dt>
<a href="buses.communicating_with_a_usb_device">Sending Requests to a USB Device</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_UrbAllocate routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
