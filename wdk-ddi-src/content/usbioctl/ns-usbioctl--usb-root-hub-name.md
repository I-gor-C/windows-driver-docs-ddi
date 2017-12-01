---
UID: NS.usbioctl._USB_ROOT_HUB_NAME
title: USB_ROOT_HUB_NAME
author: windows-driver-content
description: The USB_ROOT_HUB_NAME structure stores the root hub's symbolic device name.
old-location: buses\usb_root_hub_name.htm
old-project: usbref
ms.assetid: bd9697ce-bd05-4169-9b0f-13877307c0d7
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_ROOT_HUB_NAME, USB_ROOT_HUB_NAME, *PUSB_ROOT_HUB_NAME
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
req.alt-api: USB_ROOT_HUB_NAME
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

# USB_ROOT_HUB_NAME structure



## -description
<p>The <b>USB_ROOT_HUB_NAME</b> structure stores the root hub's symbolic device name.</p>


## -syntax

````
typedef struct _USB_ROOT_HUB_NAME {
  ULONG ActualLength;
  WCHAR RootHubName[1];
} USB_ROOT_HUB_NAME, *PUSB_ROOT_HUB_NAME;
````


## -struct-fields
<dl>

### -field <b>ActualLength</b>

<dd>
<p>Size of the entire data structure in bytes.</p>
</dd>

### -field <b>RootHubName</b>

<dd>
<p>Specifies the Unicode string containing the root hub's symbolic device name.</p>
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
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl-internal-usb-get-hub-name.md">IOCTL_INTERNAL_USB_GET_HUB_NAME</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_ROOT_HUB_NAME structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
