---
UID: NS.usbioctl._USB_NODE_INFORMATION
title: USB_NODE_INFORMATION
author: windows-driver-content
description: The USB_NODE_INFORMATION structure is used with the IOCTL_USB_GET_NODE_INFORMATION I/O control request to retrieve information about a parent device.
old-location: buses\usb_node_information.htm
old-project: usbref
ms.assetid: 56d30c25-00e7-4edf-af06-64519eb5f755
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_NODE_INFORMATION, USB_NODE_INFORMATION, *PUSB_NODE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_NODE_INFORMATION
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USB_NODE_INFORMATION structure



## -description
<p>The <b>USB_NODE_INFORMATION</b> structure is used with the <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-information.md">IOCTL_USB_GET_NODE_INFORMATION</a> I/O control request to retrieve information about a parent device.</p>


## -syntax

````
typedef struct _USB_NODE_INFORMATION {
  USB_HUB_NODE NodeType;
  union {
    USB_HUB_INFORMATION       HubInformation;
    USB_MI_PARENT_INFORMATION MiParentInformation;
  } u;
} USB_NODE_INFORMATION, *PUSB_NODE_INFORMATION;
````


## -struct-fields
<dl>

### -field NodeType

<dd>
<p>A <a href="..\usbioctl\ne-usbioctl--usb-hub-node.md">USB_HUB_NODE</a> enumerator that indicates whether the parent device is a hub or a non-hub composite device.</p>
</dd>

### -field u

<dd>
<p>The members of the <b>u</b> union are as follows:</p>
<dl>

### -field HubInformation

<dd>
<p>A <a href="..\usbioctl\ns-usbioctl--usb-hub-information.md">USB_HUB_INFORMATION</a> structure that contains information about a parent hub device.</p>
</dd>

### -field MiParentInformation

<dd>
<p>A <a href="..\usbioctl\ns-usbioctl--usb-mi-parent-information.md">USB_MI_PARENT_INFORMATION</a> structure that contains information about a parent non-hub, composite device.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A parent device can be either a hub or a composite device. The USB stack treats the interfaces of a composite device as though they were children of the composite device. The <b>USB_NODE_INFORMATION</b> structure can hold information about either kind of parent device (both hubs and composite devices).</p>

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
<a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-information.md">IOCTL_USB_GET_NODE_INFORMATION</a>
</dt>
<dt>
<a href="..\usbioctl\ns-usbioctl--usb-hub-information.md">USB_HUB_INFORMATION</a>
</dt>
<dt>
<a href="..\usbioctl\ns-usbioctl--usb-mi-parent-information.md">USB_MI_PARENT_INFORMATION</a>
</dt>
<dt>
<a href="..\usbioctl\ne-usbioctl--usb-hub-node.md">USB_HUB_NODE</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_NODE_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
