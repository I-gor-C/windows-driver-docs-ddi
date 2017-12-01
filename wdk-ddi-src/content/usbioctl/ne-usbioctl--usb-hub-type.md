---
UID: NE.usbioctl._USB_HUB_TYPE
title: USB_HUB_TYPE
author: windows-driver-content
description: The USB_HUB_TYPE enumeration defines constants that indicate the type of USB hub. The hub type is retrieved by the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request.
old-location: buses\usb_hub_type.htm
old-project: usbref
ms.assetid: F7516B20-B30F-47BE-BBF3-AB5758D5CF73
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_USB_STRING, USBFN_USB_STRING, *PUSBFN_USB_STRING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_HUB_TYPE
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

# USB_HUB_TYPE enumeration



## -description
<p>The <b>USB_HUB_TYPE</b> enumeration defines constants that indicate the type of USB hub.

The hub type is retrieved by the <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-hub-information-ex.md">IOCTL_USB_GET_HUB_INFORMATION_EX</a> I/O control request.</p>
<p>The request retrieves the hub descriptor associated with the specified hub in the <a href="..\usbioctl\ns-usbioctl--usb-hub-information-ex.md">USB_HUB_INFORMATION_EX</a> structure. The   <b>HubType</b> member contains a <b>USB_HUB_TYPE</b> enumerator that the application can use to evaluate the type of hub descriptor retrieved by the request. </p>


## -syntax

````
typedef enum _USB_HUB_TYPE { 
  UsbRootHub  = 1,
  Usb20Hub    = 2,
  Usb30Hub    = 3
} USB_HUB_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UsbRootHub"></a><a id="usbroothub"></a><a id="USBROOTHUB"></a><b>UsbRootHub</b>

<dd>
<p>Indicates a root hub.</p>
</dd>

### -field <a id="Usb20Hub"></a><a id="usb20hub"></a><a id="USB20HUB"></a><b>Usb20Hub</b>

<dd>
<p>Indicates that the retrieved hub descriptor is defined in USB 2.0 and 1.1 specifications.</p>
</dd>

### -field <a id="Usb30Hub"></a><a id="usb30hub"></a><a id="USB30HUB"></a><b>Usb30Hub</b>

<dd>
<p>Indicates that the retrieved hub descriptor is defined in USB 3.0 specification.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
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
<a href="..\usbioctl\ns-usbioctl--usb-hub-information-ex.md">USB_HUB_INFORMATION_EX</a>
</dt>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-hub-information-ex.md">IOCTL_USB_GET_HUB_INFORMATION_EX</a>
</dt>
<dt>
<a href="buses.usb_enumerations">USB Constants and Enumerations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_HUB_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
