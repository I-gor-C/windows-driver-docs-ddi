---
UID: NE.d3d12umddi.D3D12DDICAPS_TYPE
title: D3D12DDICAPS_TYPE
author: windows-driver-content
description: Specifies a capability type.
old-location: display\d3d12ddicaps_type.htm
old-project: display
ms.assetid: C74697BF-A191-4371-9F23-7F655EBC53B3
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
req.alt-api: D3D12DDICAPS_TYPE
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

# D3D12DDICAPS_TYPE enumeration



## -description
<p>Specifies a capability type. </p>


## -syntax

````
typedef enum D3D12DDICAPS_TYPE { 
  D3D12DDICAPS_TYPE_TEXTURE_LAYOUT                         = 1000,
  D3D12DDICAPS_TYPE_SWIZZLE_PATTERN                        = 1001,
  D3D12DDICAPS_TYPE_MEMORY_ARCHITECTURE                    = 1002,
  D3D12DDICAPS_TYPE_TEXTURE_LAYOUT_SETS                    = 1003,
  D3D12DDICAPS_TYPE_SHADER                                 = 1004,
  D3D12DDICAPS_TYPE_ARCHITECTURE_INFO                      = 1005,
  D3D12DDICAPS_TYPE_D3D12_OPTIONS                          = 1006,
  D3D12DDICAPS_TYPE_3DPIPELINESUPPORT                      = 1007,
  D3D12DDICAPS_TYPE_JPEG_OPTIONS                           = 1008,
  D3D12DDICAPS_TYPE_GPUVA_CAPS                             = 1009,
  D3D12DDICAPS_TYPE_TEXTURE_LAYOUT1                        = 1010,
  D3D12DDICAPS_TYPE_0011_SHADER_MODELS                     = 1012,
  D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_SUPPORT        = 1057,
  D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_DRM_SUPPORT    = 1058,
  D3D12DDICAPS_TYPE_0022_CPU_PAGE_TABLE_FALSE_POSITIVES    = 1059,
  D3D12DDICAPS_TYPE_0022_TEXTURE_LAYOUT                    = 1060,
  D3D12DDICAPS_TYPE_0022_SWIZZLE_PATTERN                   = 1061,
  D3D12DDICAPS_TYPE_0023_UMD_BASED_COMMAND_QUEUE_PRIORITY  = 1062
} D3D12DDICAPS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDICAPS_TYPE_TEXTURE_LAYOUT"></a><a id="d3d12ddicaps_type_texture_layout"></a><b>D3D12DDICAPS_TYPE_TEXTURE_LAYOUT</b>

<dd>
<p>Texture layout.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_SWIZZLE_PATTERN"></a><a id="d3d12ddicaps_type_swizzle_pattern"></a><b>D3D12DDICAPS_TYPE_SWIZZLE_PATTERN</b>

<dd>
<p>Swizzle pattern.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_MEMORY_ARCHITECTURE"></a><a id="d3d12ddicaps_type_memory_architecture"></a><b>D3D12DDICAPS_TYPE_MEMORY_ARCHITECTURE</b>

<dd>
<p>Memory architecture.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_TEXTURE_LAYOUT_SETS"></a><a id="d3d12ddicaps_type_texture_layout_sets"></a><b>D3D12DDICAPS_TYPE_TEXTURE_LAYOUT_SETS</b>

<dd>
<p>Texture layout sets.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_SHADER"></a><a id="d3d12ddicaps_type_shader"></a><b>D3D12DDICAPS_TYPE_SHADER</b>

<dd>
<p>Shader.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_ARCHITECTURE_INFO"></a><a id="d3d12ddicaps_type_architecture_info"></a><b>D3D12DDICAPS_TYPE_ARCHITECTURE_INFO</b>

<dd>
<p>Architecture information.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_D3D12_OPTIONS"></a><a id="d3d12ddicaps_type_d3d12_options"></a><b>D3D12DDICAPS_TYPE_D3D12_OPTIONS</b>

<dd>
<p>Options for D3D12.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_3DPIPELINESUPPORT"></a><a id="d3d12ddicaps_type_3dpipelinesupport"></a><b>D3D12DDICAPS_TYPE_3DPIPELINESUPPORT</b>

<dd>
<p>Support for 3D pipeline.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_JPEG_OPTIONS"></a><a id="d3d12ddicaps_type_jpeg_options"></a><b>D3D12DDICAPS_TYPE_JPEG_OPTIONS</b>

<dd>
<p>JPEG options.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_GPUVA_CAPS"></a><a id="d3d12ddicaps_type_gpuva_caps"></a><b>D3D12DDICAPS_TYPE_GPUVA_CAPS</b>

<dd>
<p>GPU video acceleration capabilities.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_TEXTURE_LAYOUT1"></a><a id="d3d12ddicaps_type_texture_layout1"></a><b>D3D12DDICAPS_TYPE_TEXTURE_LAYOUT1</b>

<dd>
<p>Texture layout.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0011_SHADER_MODELS"></a><a id="d3d12ddicaps_type_0011_shader_models"></a><b>D3D12DDICAPS_TYPE_0011_SHADER_MODELS</b>

<dd>
<p>Shader models.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_SUPPORT"></a><a id="d3d12ddicaps_type_0020_content_protection_support"></a><b>D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_SUPPORT</b>

<dd>
<p>Content protection support.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_DRM_SUPPORT"></a><a id="d3d12ddicaps_type_0020_content_protection_drm_support"></a><b>D3D12DDICAPS_TYPE_0020_CONTENT_PROTECTION_DRM_SUPPORT</b>

<dd>
<p>Content protection digital rights management (DRM) support.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0022_CPU_PAGE_TABLE_FALSE_POSITIVES"></a><a id="d3d12ddicaps_type_0022_cpu_page_table_false_positives"></a><b>D3D12DDICAPS_TYPE_0022_CPU_PAGE_TABLE_FALSE_POSITIVES</b>

<dd>
<p>CPU page table false positives.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0022_TEXTURE_LAYOUT"></a><a id="d3d12ddicaps_type_0022_texture_layout"></a><b>D3D12DDICAPS_TYPE_0022_TEXTURE_LAYOUT</b>

<dd>
<p>Texture layout.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0022_SWIZZLE_PATTERN"></a><a id="d3d12ddicaps_type_0022_swizzle_pattern"></a><b>D3D12DDICAPS_TYPE_0022_SWIZZLE_PATTERN</b>

<dd>
<p>Swizzle pattern.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_0023_UMD_BASED_COMMAND_QUEUE_PRIORITY"></a><a id="d3d12ddicaps_type_0023_umd_based_command_queue_priority"></a><b>D3D12DDICAPS_TYPE_0023_UMD_BASED_COMMAND_QUEUE_PRIORITY</b>

<dd>
<p>UMD-based command queue priority. </p>
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