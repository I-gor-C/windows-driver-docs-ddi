---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032
title: D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032
author: windows-driver-content
description: Video decode compressed bitstream.
old-location: display\d3d12ddi-video-decode-compressed-bitstream-0032.htm
old-project: display
ms.assetid: 5ef654ff-9a1e-4e97-9087-34ff21e40e1d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032, D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032
req.alt-loc: d3d12umddi.h
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

# D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032 structure



## -description
<p>Video decode compressed bitstream.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032 {
  D3D12DDI_HRESOURCE  hDrvBuffer;
  UINT64              Offset;
  UINT64              Size;
} D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032, D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032;
````


## -struct-fields
<dl>

### -field <b>hDrvBuffer</b>

<dd>
<p>Buffer.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Offset.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Size.</p>
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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>