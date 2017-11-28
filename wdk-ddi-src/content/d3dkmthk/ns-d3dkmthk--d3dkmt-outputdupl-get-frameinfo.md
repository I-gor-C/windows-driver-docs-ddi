---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPL_GET_FRAMEINFO
title: D3DKMT_OUTPUTDUPL_GET_FRAMEINFO
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_outputdupl_get_frameinfo.htm
old-project: display
ms.assetid: e358f8b6-623b-4dd0-82d7-5b46f31b26c7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_OUTPUTDUPL_GET_FRAMEINFO, D3DKMT_OUTPUTDUPL_GET_FRAMEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OUTPUTDUPL_GET_FRAMEINFO
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
req.iface: 
---

# D3DKMT_OUTPUTDUPL_GET_FRAMEINFO structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPL_GET_FRAMEINFO {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DKMT_OUTPUTDUPL_FRAMEINFO    FrameInfo;
} D3DKMT_OUTPUTDUPL_GET_FRAMEINFO;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd></dd>

### -field <b>VidPnSourceId</b>

<dd></dd>

### -field <b>FrameInfo</b>

<dd></dd>
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