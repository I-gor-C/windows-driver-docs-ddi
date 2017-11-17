---
UID: NE.udecxusbdevice._UDECX_USB_DEVICE_SPEED
title: UDECX_USB_DEVICE_SPEED
author: windows-driver-content
description: Defines values for USB device speeds.
old-location: buses\udecx_usb_device_speed.htm
ms.assetid: 337C9FFE-F97A-4F0F-9567-D1FF532FE165
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: udecxusbdevice.h
req.include-header: Udecx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UDECX_USB_DEVICE_SPEED
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: UdecxUrbSetBytesCompleted
req.iface: 
req.product: Windows 10 or later.
---

# UDECX_USB_DEVICE_SPEED enumeration



## -description
<p>Defines values for USB device speeds. </p>


## -syntax

````
typedef enum _UDECX_USB_DEVICE_SPEED { 
  UdecxUsbLowSpeed    = 0,
  UdecxUsbFullSpeed   = ,
  UdecxUsbHighSpeed   = ,
  UdecxUsbSuperSpeed  = 
} UDECX_USB_DEVICE_SPEED;
````


## -enum-fields
<dl>

### -field <a id="UdecxUsbLowSpeed"></a><a id="udecxusblowspeed"></a><a id="UDECXUSBLOWSPEED"></a><b>UdecxUsbLowSpeed</b>

<dd>
<p>Indicates a low-speed USB 1.1-compliant device.</p>
</dd>

### -field <a id="UdecxUsbFullSpeed"></a><a id="udecxusbfullspeed"></a><a id="UDECXUSBFULLSPEED"></a><b>UdecxUsbFullSpeed</b>

<dd>
<p>Indicates a full-speed USB 1.1-compliant device.</p>
</dd>

### -field <a id="UdecxUsbHighSpeed"></a><a id="udecxusbhighspeed"></a><a id="UDECXUSBHIGHSPEED"></a><b>UdecxUsbHighSpeed</b>

<dd>
<p>Indicates a high-speed USB 2.0-compliant device. </p>
</dd>

### -field <a id="UdecxUsbSuperSpeed"></a><a id="udecxusbsuperspeed"></a><a id="UDECXUSBSUPERSPEED"></a><b>UdecxUsbSuperSpeed</b>

<dd>
<p>Indicates a SuperSpeed USB 3.0-compliant device. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt627971">UdecxUsbDeviceInitSetSpeed</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UDECX_USB_DEVICE_SPEED enumeration%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
