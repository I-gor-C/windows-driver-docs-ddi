---
UID: NF.usbdlib.UsbBuildGetStatusRequest
title: UsbBuildGetStatusRequest
author: windows-driver-content
description: The UsbBuildGetStatusRequest macro formats an URB to obtain status from a device, interface, endpoint, or other device-defined target on a USB device.
old-location: buses\usbbuildgetstatusrequest.htm
old-project: usbref
ms.assetid: 7a5fcb4f-fc9a-4ebb-93ef-b83461557b22
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UsbBuildGetStatusRequest
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
req.alt-api: UsbBuildGetStatusRequest
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

# UsbBuildGetStatusRequest function



## -description
<p>
   The <b>UsbBuildGetStatusRequest</b> macro formats an <a href="..\usb\ns-usb--urb.md">URB</a> to obtain status from a device, interface, endpoint, or other device-defined target on a USB device.</p>


## -syntax

````
void UsbBuildGetStatusRequest(
  _Inout_         Urb,
  _In_     USHORT Op,
  _In_     USHORT Index,
  _In_opt_ PVOID  TransferBuffer,
  _In_opt_ PMDL   TransferBufferMDL,
  _In_     PURB   Link
);
````


## -parameters
<dl>

### -param <i>Urb</i> [in, out]

<dd>
<p>Pointer to an <a href="..\usb\ns-usb--urb.md">URB</a> to be formatted as an status request.</p>
</dd>

### -param <i>Op</i> [in]

<dd>
<p>Specifies one of the following values:</p>
<p></p>
<dl>

### -param <a id="URB_FUNCTION_GET_STATUS_FROM_DEVICE"></a><a id="urb_function_get_status_from_device"></a>URB_FUNCTION_GET_STATUS_FROM_DEVICE

<dd>
<p>Retrieves status from a USB device.</p>
</dd>

### -param <a id="URB_FUNCTION_GET_STATUS_FROM_INTERFACE"></a><a id="urb_function_get_status_from_interface"></a>URB_FUNCTION_GET_STATUS_FROM_INTERFACE

<dd>
<p>Retrieves status from an interface on a USB device.</p>
</dd>

### -param <a id="URB_FUNCTION_GET_STATUS_FROM_ENDPOINT"></a><a id="urb_function_get_status_from_endpoint"></a>URB_FUNCTION_GET_STATUS_FROM_ENDPOINT

<dd>
<p>Retrieves status from an endpoint for an interface on a USB device.</p>
</dd>

### -param <a id="URB_FUNCTION_GET_STATUS_FROM_OTHER"></a><a id="urb_function_get_status_from_other"></a>URB_FUNCTION_GET_STATUS_FROM_OTHER

<dd>
<p>Retrieves status from a device-defined target on a USB device.</p>
</dd>
</dl>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the device-defined index, returned by a successful configuration request, if the request is for an endpoint or interface. Otherwise, <i>Index</i> must be zero.</p>
</dd>

### -param <i>TransferBuffer</i> [in, optional]

<dd>
<p>Pointer to a resident buffer to receive the status data or is <b>NULL</b> if an MDL is supplied in <i>TransferBufferMDL</i>.</p>
</dd>

### -param <i>TransferBufferMDL</i> [in, optional]

<dd>
<p>Pointer to an MDL that describes a resident buffer to receive the status data or is <b>NULL</b> if a buffer is supplied in <i>TransferBuffer</i>.</p>
</dd>

### -param <i>Link</i> [in]

<dd>
<p>Reserved. Must be set to <b>NULL</b>. </p>
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
<a href="..\usb\ns-usb--urb.md">URB</a>
</dt>
<dt>
<a href="buses._urb_control_get_status_request">_URB_CONTROL_GET_STATUS_REQUEST</a>
</dt>
<dt><a href="usb_reference.htm#client">USB device driver programming reference</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UsbBuildGetStatusRequest routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
