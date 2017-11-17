---
UID: NS.dispmprt._DXGK_INTEGRATED_DISPLAY_CHILD
title: DXGK_INTEGRATED_DISPLAY_CHILD
author: windows-driver-content
description: Gives information about the connected integrated display.
old-location: display\dxgk_integrated_display_child.htm
ms.assetid: A3E28664-B286-4E4A-85DD-4EAAC7D257F0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_INTEGRATED_DISPLAY_CHILD
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
ms.keywords: DXGK_INTEGRATED_DISPLAY_CHILD, DXGK_INTEGRATED_DISPLAY_CHILD, *PDXGK_INTEGRATED_DISPLAY_CHILD
req.iface: 
---

# DXGK_INTEGRATED_DISPLAY_CHILD structure



## -description
<p>Gives information about the connected integrated display.</p>


## -syntax

````
typedef struct _DXGK_INTEGRATED_DISPLAY_CHILD {
  D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY InterfaceTechnology;
  USHORT                          DescriptorLength;
} DXGK_INTEGRATED_DISPLAY_CHILD, *PDXGK_INTEGRATED_DISPLAY_CHILD;
````


## -struct-fields
<dl>

### -field <b>InterfaceTechnology</b>

<dd>
<p>Provides the type of connection used for the integrated display.  Typically, this would be one of the inherently internal display types:</p>
<ul>
<li>D3DKMDT_VOT_INTERNAL</li>
<li>D3DKMDT_VOT_LVDS</li>
<li>D3DKMDT_VOT_DISPLAYPORT_EMBEDDED</li>
<li>D3DKMDT_VOT_UDI_EMBEDDED</li>
</ul>
<p>However, since it has become common to use external connector types to connect integrated displays in larger form factor systems with a built-in display such as all-in-one systems, the following digital connection types are also allowed:</p>
<ul>
<li>D3DKMDT_VOT_DVI</li>
<li>D3DKMDT_VOT_HDMI</li>
<li>D3DKMDT_VOT_D_JPN</li>
<li>D3DKMDT_VOT_SDI</li>
<li>D3DKMDT_VOT_DISPLAYPORT_EXTERNAL</li>
<li>D3DKMDT_VOT_UDI_EXTERNAL</li>
</ul>
</dd>

### -field <b>DescriptorLength</b>

<dd>
<p>The size in bytes of the descriptor which will be in the Descriptor field of the DXGK_QUERYINTEGRATEDDISPLAYOUT structure.</p>
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
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>