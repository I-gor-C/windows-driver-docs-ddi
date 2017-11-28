---
UID: NS.d3dumddi._D3DDDIBOX
title: D3DDDIBOX
author: windows-driver-content
description: Describes the bounds of a volume texture.
old-location: display\d3dddibox.htm
old-project: display
ms.assetid: 3CE49C9F-EFFC-4F43-A939-623B28FD5EFB
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIBOX, D3DDDIBOX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIBOX
req.alt-loc: D3dumddi.h
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
---

# D3DDDIBOX structure



## -description
<p>Describes the bounds of a volume texture.</p>


## -syntax

````
typedef struct _D3DDDIBOX {
  UINT Left;
  UINT Top;
  UINT Right;
  UINT Bottom;
  UINT Front;
  UINT Back;
} D3DDDIBOX;
````


## -struct-fields
<dl>

### -field <b>Left</b>

<dd>
<p>[in] The position of the left side of the box on the x-axis.</p>
</dd>

### -field <b>Top</b>

<dd>
<p>[in] The position of the top of the box on the y-axis.</p>
</dd>

### -field <b>Right</b>

<dd>
<p>[in] The position of the right side of the box on the x-axis.</p>
</dd>

### -field <b>Bottom</b>

<dd>
<p>[in] The position of the bottom of the box on the y-axis.</p>
</dd>

### -field <b>Front</b>

<dd>
<p>
      [in] The position of the front of the box on the z-axis.</p>
</dd>

### -field <b>Back</b>

<dd>
<p>[in] The position of the back of the box on the z-axis.</p>
</dd>
</dl>

## -remarks
<p>The height of the volume equals the value in the <b>Bottom</b> member minus the value in the <b>Top</b> member (that is, height = bottom – top). </p>

<p>The width of the volume equals the value in the <b>Right</b> member minus the value in the <b>Left</b> member (that is, width = right – left). </p>

<p>The depth of the volume equals the value in the <b>Back</b> member minus the value in the <b>Front</b> member (that is, depth = back – front). </p>

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
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>