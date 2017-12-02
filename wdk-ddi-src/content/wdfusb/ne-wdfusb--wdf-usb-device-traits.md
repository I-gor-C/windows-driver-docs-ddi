---
UID: NE.wdfusb._WDF_USB_DEVICE_TRAITS
title: WDF_USB_DEVICE_TRAITS
author: windows-driver-content
description: The WDF_USB_DEVICE_TRAITS enumeration identifies USB device traits.
old-location: wdf\wdf_usb_device_traits.htm
old-project: wdf
ms.assetid: 5ba625f5-5bc0-4e2b-a7a9-5014746086c8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_TIMER_CONFIG, WDF_TIMER_CONFIG, *PWDF_TIMER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_DEVICE_TRAITS
req.alt-loc: wdfusb.h
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

# WDF_USB_DEVICE_TRAITS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_DEVICE_TRAITS</b> enumeration identifies USB device traits.</p>


## -syntax

````
typedef enum _WDF_USB_DEVICE_TRAITS { 
  WDF_USB_DEVICE_TRAIT_SELF_POWERED         = 0x00000001,
  WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE  = 0x00000002,
  WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED        = 0x00000004
} WDF_USB_DEVICE_TRAITS;
````


## -enum-fields
<dl>

### -field WDF_USB_DEVICE_TRAIT_SELF_POWERED

<dd>
<p>The device is self-powered.</p>
</dd>

### -field WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE

<dd>
<p>The device has a remote wakeup capability.</p>
</dd>

### -field WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED

<dd>
<p>The device is operating at high speed or SuperSpeed.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_USB_DEVICE_TRAITS</b> enumeration is used in the <a href="..\wdfusb\ns-wdfusb--wdf-usb-device-information.md">WDF_USB_DEVICE_INFORMATION</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-device-information.md">WDF_USB_DEVICE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_DEVICE_TRAITS enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
