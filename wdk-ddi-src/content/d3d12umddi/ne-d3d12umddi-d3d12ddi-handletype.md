---
UID: NE.d3d12umddi.D3D12DDI_HANDLETYPE
title: D3D12DDI_HANDLETYPE
author: windows-driver-content
description: Contains driver handle types.
old-location: display\d3d12ddi_handletype.htm
old-project: display
ms.assetid: 807CC73E-C5A5-4D49-AFAF-32A51D832F82
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_HANDLETYPE
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_HANDLETYPE enumeration



## -description
<p>Contains driver handle types.</p>


## -syntax

````
typedef enum D3D12DDI_HANDLETYPE { 
  D3D12DDI_HT_COMMAND_QUEUE                  = 19,
  D3D12DDI_HT_COMMAND_ALLOCATOR              = 20,
  D3D12DDI_HT_PIPELINE_STATE                 = 21,
  D3D12DDI_HT_COMMAND_LIST                   = 22,
  D3D12DDI_HT_FENCE                          = 23,
  D3D12DDI_HT_DESCRIPTOR_HEAP                = 24,
  D3D12DDI_HT_HEAP                           = 25,
  D3D12DDI_HT_QUERY_HEAP                     = 27,
  D3D12DDI_HT_COMMAND_SIGNATURE              = 28,
  D3D12DDI_HT_0010_PIPELINE_LIBRARY          = 29,
  D3D12DDI_HT_0020_VIDEO_DECODER             = 30,
  D3D12DDI_HT_0020_VIDEO_DECODE_STREAM       = 31,
  D3D12DDI_HT_0020_VIDEO_PROCESSOR           = 32,
  D3D12DDI_HT_0020_VIDEO_PROCESS_STREAM      = 33,
  D3D12DDI_HT_0012_RESOURCE                  = 34,
  D3D12DDI_HT_PASS                           = 35,
  D3D12DDI_HT_0030_CRYPTOSESSION             = 36,
  D3D12DDI_HT_0030_CRYPTOSESSIONPOLICY       = 37,
  D3D12DDI_HT_0030_PROTECTEDRESOURCESESSION  = 37,
  D3D12DDI_HT_0032_VIDEO_DECODER_HEAP        = 39
} D3D12DDI_HANDLETYPE;
````


## -enum-fields
<dl>

### -field D3D12DDI_HT_COMMAND_QUEUE

<dd>
<p>A command queue handle type.</p>
</dd>

### -field D3D12DDI_HT_COMMAND_ALLOCATOR

<dd>
<p>A command allocator handle type.</p>
</dd>

### -field D3D12DDI_HT_PIPELINE_STATE

<dd>
<p>A pipeline state handle type.</p>
</dd>

### -field D3D12DDI_HT_COMMAND_LIST

<dd>
<p>A command list handle type.</p>
</dd>

### -field D3D12DDI_HT_FENCE

<dd>
<p>A fence handle type.</p>
</dd>

### -field D3D12DDI_HT_DESCRIPTOR_HEAP

<dd>
<p>A descriptor heap handle type.</p>
</dd>

### -field D3D12DDI_HT_HEAP

<dd>
<p>A heap handle type.</p>
</dd>

### -field D3D12DDI_HT_QUERY_HEAP

<dd>
<p>A query heap handle type.</p>
</dd>

### -field D3D12DDI_HT_COMMAND_SIGNATURE

<dd>
<p>A command signature handle type.</p>
</dd>

### -field D3D12DDI_HT_0010_PIPELINE_LIBRARY

<dd>
<p>A pipeline library handle type.</p>
</dd>

### -field D3D12DDI_HT_0020_VIDEO_DECODER

<dd>
<p>A video decoder handle type.</p>
</dd>

### -field D3D12DDI_HT_0020_VIDEO_DECODE_STREAM

<dd>
<p>A video decode stream handle type.</p>
</dd>

### -field D3D12DDI_HT_0020_VIDEO_PROCESSOR

<dd>
<p>A video processor handle type.</p>
</dd>

### -field D3D12DDI_HT_0020_VIDEO_PROCESS_STREAM

<dd>
<p>A video process stream handle type.</p>
</dd>

### -field D3D12DDI_HT_0012_RESOURCE

<dd>
<p>A resource handle type.</p>
</dd>

### -field D3D12DDI_HT_PASS

<dd>
<p>A pass handle type.</p>
</dd>

### -field D3D12DDI_HT_0030_CRYPTOSESSION

<dd>
<p>A crypto session handle type.</p>
</dd>

### -field D3D12DDI_HT_0030_CRYPTOSESSIONPOLICY

<dd>
<p>A crypto session policy handle type.</p>
</dd>

### -field D3D12DDI_HT_0030_PROTECTEDRESOURCESESSION

<dd>
<p>A protected resource session handle type.</p>
</dd>

### -field D3D12DDI_HT_0032_VIDEO_DECODER_HEAP

<dd>
<p>A video decoder heap handle type.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>