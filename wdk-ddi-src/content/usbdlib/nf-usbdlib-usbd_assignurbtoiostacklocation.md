---
UID: NF.usbdlib.USBD_AssignUrbToIoStackLocation
title: USBD_AssignUrbToIoStackLocation function
author: windows-driver-content
description: The USBD_AssignUrbToIoStackLocation routine is called by a client driver to associate an URB with the IRP's next stack location.
old-location: buses\usbd_assignurbtostacklocation.htm
old-project: usbref
ms.assetid: 66A66050-B2BF-47FA-A4E2-BF8816390B16
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: USBD_AssignUrbToIoStackLocation
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
req.alt-api: USBD_AssignUrbToIoStackLocation
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
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# USBD_AssignUrbToIoStackLocation function



## -description
The <b>USBD_AssignUrbToIoStackLocation</b> routine is called by a client driver to associate an <a href="buses.urb">URB</a> with the IRP's next stack location.



## -syntax

````
void USBD_AssignUrbToIoStackLocation(
  _In_ USBD_HANDLE        USBDHandle,
  _In_ PIO_STACK_LOCATION StackLocation,
  _In_ PURB               Urb
);
````


## -parameters

### -param USBDHandle [in]

A USBD handle that is retrieved in a previous call to the <a href="buses.usbd_register">USBD_CreateHandle</a> routine.


### -param StackLocation [in]

Pointer to the IRP's next stack location (<a href="kernel.io_stack_location">IO_STACK_LOCATION</a>). The client driver received a pointer to the stack location in a previous call to <a href="kernel.iogetnextirpstacklocation">IoGetNextIrpStackLocation</a>.


### -param Urb [in]

Pointer to the <a href="buses.urb">URB</a> structure that is allocated by <a href="buses.usbd_urballocate">USBD_UrbAllocate</a>, <a href="buses.usbd_isochurballocate">USBD_IsochUrbAllocate</a>, <a href="buses.usbd_selectconfigurballocateandbuild">USBD_SelectConfigUrbAllocateAndBuild</a>, or 
    <a href="buses.usbd_selectinterfaceurballocateandbuild">USBD_SelectInterfaceUrbAllocateAndBuild</a>.


## -returns
This routine does not return a value.


## -remarks
If the client driver allocated an URB by calling <a href="buses.usbd_urballocate">USBD_UrbAllocate</a>, <a href="buses.usbd_isochurballocate">USBD_IsochUrbAllocate</a>, <a href="buses.usbd_selectconfigurballocateandbuild">USBD_SelectConfigUrbAllocateAndBuild</a>, or 
    <a href="buses.usbd_selectinterfaceurballocateandbuild">USBD_SelectInterfaceUrbAllocateAndBuild</a>, then the driver <i>must</i> call <b>USBD_AssignUrbToIoStackLocation</b> to associate the URB with <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> associated with the IRP. For URBs that are  allocated by those routines, <b>USBD_AssignUrbToIoStackLocation</b> replaces setting   <b>Parameters.Others.Argument1</b> of <b>IO_STACK_LOCATION</b> to the URB. (see <a href="..\usbioctl\ni-usbioctl-ioctl_internal_usb_submit_urb.md">IOCTL_INTERNAL_USB_SUBMIT_URB</a>).  

The client driver must <i>not</i> call <b>USBD_AssignUrbToIoStackLocation</b> for an URB that is allocated by using other mechanisms, such as allocating the URB on the stack. Otherwise, the USB driver stack generates a bugcheck.


The client driver must call <b>USBD_AssignUrbToIoStackLocation</b> before calling <a href="kernel.iocalldriver">IoCallDriver</a> to send  the request. <b>USBD_AssignUrbToIoStackLocation</b> populates the IRP's next stack location with the URB.  The routine also updates the <b>FileObject</b> member of <a href="kernel.io_stack_location">IO_STACK_LOCATION</a>. 

For a code example, see <a href="buses.send_requests_to_the_usb_driver_stack">How to Submit an URB</a>.


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
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usbd_urballocate">USBD_UrbAllocate</a>
</dt>
<dt>
<a href="buses.usbd_isochurballocate">USBD_IsochUrbAllocate</a>
</dt>
<dt>
<a href="buses.usbd_selectconfigurballocateandbuild">USBD_SelectConfigUrbAllocateAndBuild</a>
</dt>
<dt>
<a href="buses.usbd_selectinterfaceurballocateandbuild">USBD_SelectInterfaceUrbAllocateAndBuild</a>
</dt>
<dt>
<a href="buses.send_requests_to_the_usb_driver_stack">How to Submit an URB</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_AssignUrbToIoStackLocation routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

