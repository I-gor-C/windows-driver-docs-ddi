---
UID: NS.dispmprt._LINKED_DEVICE
title: LINKED_DEVICE
author: windows-driver-content
description: The LINKED_DEVICE structure holds information that describes a linked display adapter configuration.
old-location: display\linked_device.htm
old-project: display
ms.assetid: 65289123-46b8-4a4b-985a-8087f4afd250
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: LINKED_DEVICE, LINKED_DEVICE, *PLINKED_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LINKED_DEVICE
req.alt-loc: dispmprt.h
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
---

# LINKED_DEVICE structure



## -description
<p>The LINKED_DEVICE structure holds information that describes a linked display adapter configuration.</p>


## -syntax

````
typedef struct _LINKED_DEVICE {
  ULONG   ChainUid;
  ULONG   NumberOfLinksInChain;
  BOOLEAN LeadLink;
} LINKED_DEVICE, *PLINKED_DEVICE;
````


## -struct-fields
<dl>

### -field <b>ChainUid</b>

<dd>
<p>A unique identifier for this chain of display adapters.</p>
</dd>

### -field <b>NumberOfLinksInChain</b>

<dd>
<p>The expected number of linked adapters that the operating system should enumerate.</p>
</dd>

### -field <b>LeadLink</b>

<dd>
<p>A value that indicates the leading link in the chain of linked adapters. The value is <b>TRUE</b> only for the adapter that will be allowed to enumerate child adapters. Otherwise, the value is <b>FALSE</b>.</p>
</dd>
</dl>

## -remarks
<p>Prior to a call to <a href="display.dxgkddilinkdevice">DxgkDdiLinkDevice</a>, the display miniport driver should fill the LINKED_DEVICE structure with information about the linked adapter configuration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddilinkdevice">DxgkDdiLinkDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20LINKED_DEVICE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
