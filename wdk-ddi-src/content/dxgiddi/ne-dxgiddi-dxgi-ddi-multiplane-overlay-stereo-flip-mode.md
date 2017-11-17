---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
title: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
author: windows-driver-content
description: Identifies the overlay plane's stereo flip mode. Only the DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE value is supported.
old-location: display\dxgi_ddi_multiplane_overlay_stereo_flip_mode.htm
ms.assetid: f44317c5-661c-42f6-847b-b325e4c1321a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE
req.alt-loc: Dxgiddi.h
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
ms.keywords: DxApiGetVersion
req.iface: 
---

# DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE enumeration



## -description
<p>Identifies the overlay plane's stereo flip mode. Only the <b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</b> value is supported.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE { 
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE    = 0,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0  = 1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1  = 2
} DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_MODE;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE"></a><a id="dxgi_ddi_multiplane_overlay_stereo_flip_none"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_NONE</b>

<dd>
<p>The overplay plane data is not presented in stereo mode.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0"></a><a id="dxgi_ddi_multiplane_overlay_stereo_flip_frame0"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME0</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1"></a><a id="dxgi_ddi_multiplane_overlay_stereo_flip_frame1"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FLIP_FRAME1</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>