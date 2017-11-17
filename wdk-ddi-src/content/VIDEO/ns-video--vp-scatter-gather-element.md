---
UID: NS.video._VP_SCATTER_GATHER_ELEMENT
title: VP_SCATTER_GATHER_ELEMENT
author: windows-driver-content
description: The VP_SCATTER_GATHER_ELEMENT structure is used to store information about a single scatter/gather element.
old-location: display\vp_scatter_gather_element.htm
ms.assetid: 7b0ca123-8847-4dc3-b0f5-9788104381ec
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VP_SCATTER_GATHER_ELEMENT
req.alt-loc: video.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
ms.keywords: VP_SCATTER_GATHER_ELEMENT, VP_SCATTER_GATHER_ELEMENT, *PVP_SCATTER_GATHER_ELEMENT
req.iface: 
req.product: Windows 10 or later.
---

# VP_SCATTER_GATHER_ELEMENT structure



## -description
<p>The VP_SCATTER_GATHER_ELEMENT structure is used to store information about a single scatter/gather element.</p>


## -syntax

````
typedef struct _VP_SCATTER_GATHER_ELEMENT {
  PHYSICAL_ADDRESS Address;
  ULONG            Length;
  ULONG_PTR        Reserved;
} VP_SCATTER_GATHER_ELEMENT, *PVP_SCATTER_GATHER_ELEMENT;
````


## -struct-fields
<dl>

### -field <b>Address</b>

<dd>
<p>Specifies the logical address of one scatter/gather element.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Specifies the length, in bytes, of the scatter/gather element.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>This structure is available in Windows XP and later.</p>

<p>A VP_SCATTER_GATHER_ELEMENT structure is one element of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570572">VP_SCATTER_GATHER_LIST</a> structure's array member.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570572">VP_SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VP_SCATTER_GATHER_ELEMENT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
