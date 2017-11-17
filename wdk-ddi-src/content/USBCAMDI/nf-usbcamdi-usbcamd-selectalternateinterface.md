---
UID: NF.usbcamdi.USBCAMD_SelectAlternateInterface
title: USBCAMD_SelectAlternateInterface
author: windows-driver-content
description: The USBCAMD_SelectAlternateInterface function selects an alternate setting within the USB video streaming interface.
old-location: stream\usbcamd_selectalternateinterface.htm
ms.assetid: b9a31719-2674-4d3f-8792-b099640faa07
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_SelectAlternateInterface
req.alt-loc: usbcamd2.lib,usbcamd2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbcamd2.lib
req.dll: 
req.irql: 
ms.keywords: USBCAMD_SelectAlternateInterface
req.iface: 
req.product: Windows 10 or later.
---

# USBCAMD_SelectAlternateInterface function



## -description
<p>The <b>USBCAMD_SelectAlternateInterface</b> function selects an alternate setting within the USB video streaming interface.</p>


## -syntax

````
NTSTATUS USBCAMD_SelectAlternateInterface(
  _In_    PVOID                       DeviceContext,
  _Inout_ PUSBD_INTERFACE_INFORMATION RequestInterface
);
````


## -parameters
<dl>

### -param <i>DeviceContext</i> [in]

<dd>
<p>Pointer to a device-specific context.</p>
</dd>

### -param <i>RequestInterface</i> [in, out]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539068">USBD_INTERFACE_INFORMATION</a> structure initialized with the proper values for a SELECT_INTERFACE URB request. This interface structure corresponds to a single isochronous interface on the device.</p>
</dd>
</dl>

## -returns
<p><b>USBCAMD_SelectAlternateInterface </b>returns the status of the SELECT_INTERFACE USB bus driver request. Other possible error codes include:</p><dl>
<dt><b>STATUS_DEVICE_DATA_ERROR</b></dt>
</dl><p>USBCAMD failed to cancel outstanding bulk/interrupt IRPs.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There are insufficient resources to allocate the USB request block</p>

<p> </p>

## -remarks
<p>On successful completion, the structure pointed to by the <i>RequestInterface</i> argument is filled in with the information from the SELECT_INTERFACE USB bus driver request.</p>

<p>This function is typically called by a camera minidriver in response to a request to allocate or free bandwidth. This function should not be called when any video streams in the minidriver are open and/or actively streaming data.</p>

<p>On successful completion, the structure pointed to by the <i>RequestInterface</i> argument is filled in with the information from the SELECT_INTERFACE USB bus driver request.</p>

<p>This function is typically called by a camera minidriver in response to a request to allocate or free bandwidth. This function should not be called when any video streams in the minidriver are open and/or actively streaming data.</p>

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
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamd2.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539068">USBD_INTERFACE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_SelectAlternateInterface function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
