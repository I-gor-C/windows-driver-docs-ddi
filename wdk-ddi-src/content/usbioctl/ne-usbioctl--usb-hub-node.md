---
UID: NE.usbioctl._USB_HUB_NODE
title: USB_HUB_NODE
author: windows-driver-content
description: The USB_HUB_NODE enumerator indicates whether a device is a hub or a composite device.
old-location: buses\usb_hub_node.htm
old-project: usbref
ms.assetid: fdd69121-2b3c-4394-b67e-c29f43daf113
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_USB_STRING, USBFN_USB_STRING, *PUSBFN_USB_STRING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_HUB_NODE
req.alt-loc: usbioctl.h
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

# USB_HUB_NODE enumeration



## -description
<p>The <b>USB_HUB_NODE</b> enumerator indicates whether a device is a hub or a composite device.</p>


## -syntax

````
typedef enum _USB_HUB_NODE { 
  UsbHub       = 0,
  UsbMIParent  = 1
} USB_HUB_NODE;
````


## -enum-fields
<dl>

### -field <a id="UsbHub"></a><a id="usbhub"></a><a id="USBHUB"></a><b>UsbHub</b>

<dd>
<p>Indicates that the device is a hub.</p>
</dd>

### -field <a id="UsbMIParent"></a><a id="usbmiparent"></a><a id="USBMIPARENT"></a><b>UsbMIParent</b>

<dd>
<p>Indicates that the device is a composite device with multiple interfaces.</p>
</dd>
</dl>

## -remarks
<p>Composite devices are devices that have multiple interfaces. Windows loads the USB generic parent driver for composite devices, instead of the hub driver, but the generic parent driver performs many of the functions of the hub driver. It creates a child PDO for each interface, as though the interface were a separate device.</p>

<p>Composite devices are devices that have multiple interfaces. Windows loads the USB generic parent driver for composite devices, instead of the hub driver, but the generic parent driver performs many of the functions of the hub driver. It creates a child PDO for each interface, as though the interface were a separate device.</p>

<p>Composite devices are devices that have multiple interfaces. Windows loads the USB generic parent driver for composite devices, instead of the hub driver, but the generic parent driver performs many of the functions of the hub driver. It creates a child PDO for each interface, as though the interface were a separate device.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540110">USB_NODE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539322">USB Constants and Enumerations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_HUB_NODE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
