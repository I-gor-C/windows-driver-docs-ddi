---
UID: NE.usbioctl._USB_CONNECTION_STATUS~r1
title: USB_CONNECTION_STATUS
author: windows-driver-content
description: The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port.
old-location: buses\usb_connection_status.htm
old-project: usbref
ms.assetid: 9006f74f-4033-4f07-816c-380d6d8b3a2d
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
req.alt-api: USB_CONNECTION_STATUS
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

# USB_CONNECTION_STATUS enumeration



## -description
<p>The <b>USB_CONNECTION_STATUS</b> enumerator indicates the status of the connection to a device on a USB hub port.</p>


## -syntax

````
typedef enum _USB_CONNECTION_STATUS { 
  NoDeviceConnected         = 0,
  DeviceConnected           = 1,
  DeviceFailedEnumeration   = 2,
  DeviceGeneralFailure      = 3,
  DeviceCausedOvercurrent   = 4,
  DeviceNotEnoughPower      = 5,
  DeviceNotEnoughBandwidth  = 6,
  DeviceHubNestedTooDeeply  = 7,
  DeviceInLegacyHub         = 8,
  DeviceEnumerating         = 9,
  DeviceReset               = 10
} USB_CONNECTION_STATUS, *PUSB_CONNECTION_STATUS;
````


## -enum-fields
<dl>

### -field NoDeviceConnected

<dd>
<p>Indicates that there is no device connected to the port.</p>
</dd>

### -field DeviceConnected

<dd>
<p>Indicates that a device was successfully connected to the port.</p>
</dd>

### -field DeviceFailedEnumeration

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but the enumeration of the device failed.</p>
</dd>

### -field DeviceGeneralFailure

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but the connection failed for unspecified reasons.</p>
</dd>

### -field DeviceCausedOvercurrent

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but the attempt failed because of an overcurrent condition.</p>
</dd>

### -field DeviceNotEnoughPower

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but there was not enough power to drive the device, and the connection failed.</p>
</dd>

### -field DeviceNotEnoughBandwidth

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but there was not enough bandwidth available for the device to function properly, and the connection failed.</p>
</dd>

### -field DeviceHubNestedTooDeeply

<dd>
<p>Indicates that an attempt was made to connect a device to the port, but the nesting of USB hubs was too deep, so the connection failed. </p>
</dd>

### -field DeviceInLegacyHub

<dd>
<p>Indicates that an attempt was made to connect a device to the port of an unsupported legacy hub, and the connection failed.</p>
</dd>

### -field DeviceEnumerating

<dd>
<p>Indicates that a device connected to the port is currently being enumerated.  </p>
<p><b>Note</b>  This constant is supported in Windows Vista and later operating systems.</p>
</dd>

### -field DeviceReset

<dd>
<p>Indicates that device connected to the port is currently being reset.  </p>
<p><b>Note</b>  This constant is supported in Windows Vista and later operating systems.</p>
</dd>
</dl>

## -remarks
<p>The USB bus driver reports connection status in a <a href="..\usbioctl\ns-usbioctl--usb-node-connection-information-ex.md">USB_NODE_CONNECTION_INFORMATION_EX</a> structure in response to an <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-connection-information-ex.md">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a> request.</p>

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
<a href="..\usbioctl\ns-usbioctl--usb-node-connection-information-ex.md">USB_NODE_CONNECTION_INFORMATION_EX</a>
</dt>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-connection-information-ex.md">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a>
</dt>
<dt>
<a href="buses.usb_enumerations">USB Constants and Enumerations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_CONNECTION_STATUS enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
