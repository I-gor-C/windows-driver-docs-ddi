---
UID: NE.d3d12umddi.D3D12DDI_TABLE_TYPE
title: D3D12DDI_TABLE_TYPE
author: windows-driver-content
description: Command list and queue types to allow drivers to point to different implementations for video.
old-location: display\d3d12ddi_table_type.htm
old-project: display
ms.assetid: 93562C36-7ADE-4CC6-B33D-D6E955E3D42C
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
req.alt-api: D3D12DDI_TABLE_TYPE
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

# D3D12DDI_TABLE_TYPE enumeration



## -description
<p>Command list and queue types to allow drivers to point to different implementations for video.</p>


## -syntax

````
typedef enum D3D12DDI_TABLE_TYPE { 
  D3D12DDI_TABLE_TYPE_DEVICE_CORE                               = 0,
  D3D12DDI_TABLE_TYPE_COMMAND_LIST_3D                           = 1,
  D3D12DDI_TABLE_TYPE_COMMAND_QUEUE_3D                          = 2,
  D3D12DDI_TABLE_TYPE_DXGI                                      = 3,
  D3D12DDI_TABLE_TYPE_0020_DEVICE_VIDEO                         = 4,
  D3D12DDI_TABLE_TYPE_0020_DEVICE_CORE_VIDEO                    = 7,
  D3D12DDI_TABLE_TYPE_0020_EXTENDED_FEATURES                    = 8,
  D3D12DDI_TABLE_TYPE_0020_PASS_EXPERIMENT                      = 9,
  D3D12DDI_TABLE_TYPE_0021_SHADERCACHE_CALLBACKS                = 10,
  D3D12DDI_TABLE_TYPE_0022_COMMAND_QUEUE_VIDEO_DECODE           = 11,
  D3D12DDI_TABLE_TYPE_0022_COMMAND_LIST_VIDEO_DECODE            = 12,
  D3D12DDI_TABLE_TYPE_0022_COMMAND_QUEUE_VIDEO_PROCESS          = 13,
  D3D12DDI_TABLE_TYPE_0022_COMMAND_LIST_VIDEO_PROCESS           = 14,
  D3D12DDI_TABLE_TYPE_0030_DEVICE_CONTENT_PROTECTION_RESOURCES  = 15,
  D3D12DDI_TABLE_TYPE_0030_CONTENT_PROTECTION_CALLBACKS         = 16,
  D3D12DDI_TABLE_TYPE_0030_DEVICE_CONTENT_PROTECTION_STREAMING  = 17
} D3D12DDI_TABLE_TYPE;
````


## -enum-fields
<dl>

### -field D3D12DDI_TABLE_TYPE_DEVICE_CORE

<dd>
<p>Device core.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_COMMAND_LIST_3D

<dd>
<p>List 3D.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_COMMAND_QUEUE_3D

<dd>
<p>Queue 3D.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_DXGI

<dd>
<p>DXGI.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0020_DEVICE_VIDEO

<dd>
<p>Device video.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0020_DEVICE_CORE_VIDEO

<dd>
<p>Queue video.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0020_EXTENDED_FEATURES

<dd>
<p>Extended features.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0020_PASS_EXPERIMENT

<dd>
<p>Pass experiment.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0021_SHADERCACHE_CALLBACKS

<dd>
<p>Shader cache callbacks.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0022_COMMAND_QUEUE_VIDEO_DECODE

<dd>
<p>Queue video decode.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0022_COMMAND_LIST_VIDEO_DECODE

<dd>
<p>List video decode.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0022_COMMAND_QUEUE_VIDEO_PROCESS

<dd>
<p>Queue video process.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0022_COMMAND_LIST_VIDEO_PROCESS

<dd>
<p>List video process.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0030_DEVICE_CONTENT_PROTECTION_RESOURCES

<dd>
<p>Device content protection resources.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0030_CONTENT_PROTECTION_CALLBACKS

<dd>
<p>Content protection callbacks.</p>
</dd>

### -field D3D12DDI_TABLE_TYPE_0030_DEVICE_CONTENT_PROTECTION_STREAMING

<dd>
<p>Device content protection streaming.</p>
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