---
UID: NF.udecxusbdevice.UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
title: UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
author: windows-driver-content
description: Initializes a UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure.
old-location: buses\udecx_usb_device_plug_in_options_init.htm
old-project: usbref
ms.assetid: 3188E2EE-E011-476D-9DDC-1DF61ECF9413
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT
req.alt-loc: Udecxstub.lib,Udecxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function



## -description
<p>Initializes a <a href="buses.udecx_usb_device_plug_in_options">UDECX_USB_DEVICE_PLUG_IN_OPTIONS</a> structure.</p>


## -syntax

````
FORCEINLINE void UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT(
  _Out_ PUDECX_USB_DEVICE_PLUG_IN_OPTIONS Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [out]

<dd>
<p>A pointer to a <a href="buses.udecx_usb_device_plug_in_options">UDECX_USB_DEVICE_PLUG_IN_OPTIONS</a> structure to initialize.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The method initializes <b>Usb20PortNumber</b> and <b>Usb30PortNumber</b>  to 0. This indicates a request for  automatic port number selection.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UdecxUsbDevice.h (include Udecx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Udecxstub.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.udecxusbdeviceplugin">UdecxUsbDevicePlugIn</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
