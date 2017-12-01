---
UID: NS.ucxroothub._PARENT_HUB_FLAGS
title: PARENT_HUB_FLAGS
author: windows-driver-content
description: This structure is used by the HUB_INFO_FROM_PARENT structure to get hub information from the parent.
old-location: buses\_parent_hub_flags.htm
old-project: usbref
ms.assetid: 9107CC24-48FF-4A2C-AA27-1E9E316B7944
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PARENT_HUB_FLAGS, PARENT_HUB_FLAGS, *PPARENT_HUB_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARENT_HUB_FLAGS
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PARENT_HUB_FLAGS structure



## -description
<p>This structure is used by the <a href="buses._hub_info_from_parent">HUB_INFO_FROM_PARENT</a> structure to get hub information from the parent.</p>


## -syntax

````
typedef union _PARENT_HUB_FLAGS {
  ULONG  AsUlong32;
  struct {
    ULONG DisableLpmForAllDownstreamDevices  :1;
    ULONG HubIsHighSpeedCapable  :1;
  };
} PARENT_HUB_FLAGS;
````


## -struct-fields
<dl>

### -field <b>AsUlong32</b>

<dd>
<p>The size of structure represented as a LONG (32-bit) value.</p>
</dd>

### -field <b>DisableLpmForAllDownstreamDevices</b>

<dd>
<p>Indicates that all devices behind the hub must be disabled.</p>
</dd>

### -field <b>HubIsHighSpeedCapable</b>

<dd>
<p>Indicates that the hub is high-speed capable.</p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._hub_info_from_parent">HUB_INFO_FROM_PARENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20PARENT_HUB_FLAGS union%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
