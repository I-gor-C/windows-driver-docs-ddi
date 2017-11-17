---
UID: NS.d3dkmthk._D3DKMT_DISPLAYMODELIST
title: D3DKMT_DISPLAYMODELIST
author: windows-driver-content
description: Describes a list of display modes.
old-location: display\d3dkmt_displaymodelist.htm
ms.assetid: 2eb99f42-3639-4327-a880-47e18d1da71d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_DISPLAYMODELIST
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_DISPLAYMODELIST, D3DKMT_DISPLAYMODELIST
req.iface: 
---

# D3DKMT_DISPLAYMODELIST structure



## -description
<p>Describes a list of display modes.</p>


## -syntax

````
typedef struct _D3DKMT_DISPLAYMODELIST {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           ModeCount;
  D3DKMT_DISPLAYMODE             pModeList[];
} D3DKMT_DISPLAYMODELIST;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology that the display modes apply to.</p>
</dd>

### -field <b>ModeCount</b>

<dd>
<p>[in/out] The number of display modes in the array that <b>pModeList</b> specifies.</p>
</dd>

### -field <b>pModeList</b>

<dd>
<p>[out] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff547942">D3DKMT_DISPLAYMODE</a> structures that represent the list of display modes.</p>
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
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>