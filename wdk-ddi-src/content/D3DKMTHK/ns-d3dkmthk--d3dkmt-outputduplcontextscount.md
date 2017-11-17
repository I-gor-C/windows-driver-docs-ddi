---
UID: NS.d3dkmthk._D3DKMT_OUTPUTDUPLCONTEXTSCOUNT
title: D3DKMT_OUTPUTDUPLCONTEXTSCOUNT
author: windows-driver-content
description: Specifies the number of current Desktop Duplication API (DDA) clients that are attached to a given video present network (VidPN).
old-location: display\d3dkmt_outputduplcontextscount.htm
ms.assetid: db63b984-73da-4b66-8a5e-06704dd7c031
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
req.alt-api: D3DKMT_OUTPUTDUPLCONTEXTSCOUNT
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
ms.keywords: D3DKMT_OUTPUTDUPLCONTEXTSCOUNT, D3DKMT_OUTPUTDUPLCONTEXTSCOUNT
req.iface: 
---

# D3DKMT_OUTPUTDUPLCONTEXTSCOUNT structure



## -description
<p>Specifies the number of current <a href="direct3ddxgi.desktop_dup_api">Desktop Duplication API</a> (DDA) clients that are attached to a given video present network (VidPN).</p>


## -syntax

````
typedef struct _D3DKMT_OUTPUTDUPLCONTEXTSCOUNT {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           OutputDuplicationCount;
} D3DKMT_OUTPUTDUPLCONTEXTSCOUNT;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>The ID of the video present network (VidPN).</p>
</dd>

### -field <b>OutputDuplicationCount</b>

<dd>
<p>The number of current DDA clients that are attached to the VidPN specified by the <b>VidPnSourceId</b> member.</p>
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