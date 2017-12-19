---
UID: NS.D3D12UMDDI.D3D12DDIARG_CREATE_VIDEO_DECODER_0032
title: D3D12DDIARG_CREATE_VIDEO_DECODER_0032
author: windows-driver-content
description: Creates a video decoder.
old-location: display\d3d12ddiarg-create-video-decoder-0032.htm
old-project: display
ms.assetid: d4d42334-ae09-4900-828b-86da81b446c1
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3D12DDIARG_CREATE_VIDEO_DECODER_0032, D3D12DDIARG_CREATE_VIDEO_DECODER_0032
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
req.alt-api: D3D12DDIARG_CREATE_VIDEO_DECODER_0032
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
---

# D3D12DDIARG_CREATE_VIDEO_DECODER_0032 structure



## -description
Creates a video decoder.



## -syntax

````
typedef struct _D3D12DDIARG_CREATE_VIDEO_DECODER_0032 {
  UINT                                      NodeMask;
  D3D12DDI_VIDEO_DECODE_CONFIGURATION_0020  Configuration;
} D3D12DDIARG_CREATE_VIDEO_DECODER_0032, D3D12DDIARG_CREATE_VIDEO_DECODER_0032;
````


## -struct-fields

### -field NodeMask

Represents the set of nodes.


### -field Configuration

The video decode configuration.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>