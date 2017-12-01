---
UID: NS.udecxusbdevice._UDECX_USB_DEVICE_PLUG_IN_OPTIONS
title: UDECX_USB_DEVICE_PLUG_IN_OPTIONS
author: windows-driver-content
description: Contains the port numbers to which a virtual USB device is connected. Initialize this structure by calling the UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT method.
old-location: buses\udecx_usb_device_plug_in_options.htm
old-project: usbref
ms.assetid: D09A124A-82F6-4B0A-B60F-E60EB54B0EC1
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UDECX_USB_DEVICE_PLUG_IN_OPTIONS, UDECX_USB_DEVICE_PLUG_IN_OPTIONS, *PUDECX_USB_DEVICE_PLUG_IN_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_DEVICE_PLUG_IN_OPTIONS
req.alt-loc: UdecxUsbDevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure



## -description
<p>Contains the port numbers to which a virtual USB device is connected. Initialize this structure by calling the <a href="buses.udecx_usb_device_plug_in_options_init">UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT</a> method.</p>


## -syntax

````
typedef struct _UDECX_USB_DEVICE_PLUG_IN_OPTIONS {
  ULONG Size;
  ULONG Usb20PortNumber;
  ULONG Usb30PortNumber;
} UDECX_USB_DEVICE_PLUG_IN_OPTIONS, * PUDECX_USB_DEVICE_PLUG_IN_OPTIONS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>Usb20PortNumber</b>

<dd>
<p>The USB 2.0 port number.</p>
</dd>

### -field <b>Usb30PortNumber</b>

<dd>
<p>The USB 2.0 port number.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="buses.udecxusbdeviceplugin">UdecxUsbDevicePlugIn</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
