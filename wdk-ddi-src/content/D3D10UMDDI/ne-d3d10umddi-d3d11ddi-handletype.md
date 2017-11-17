---
UID: NE.d3d10umddi.D3D11DDI_HANDLETYPE
title: D3D11DDI_HANDLETYPE
author: windows-driver-content
description: Contains values that identify handle types.
old-location: display\d3d11ddi_handletype.htm
ms.assetid: 9ac032fe-b870-49aa-8602-3c7aa997ef9a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDI_HANDLETYPE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDI_HANDLETYPE
req.alt-loc: d3d10umddi.h
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3D11DDI_HANDLETYPE enumeration



## -description
<p>Contains values that identify handle types. </p>


## -syntax

````
typedef enum D3D11DDI_HANDLETYPE { 
  D3D10DDI_HT_RESOURCE                           = 0,
  D3D10DDI_HT_SHADERRESOURCEVIEW                 = 1,
  D3D10DDI_HT_RENDERTARGETVIEW                   = 2,
  D3D10DDI_HT_DEPTHSTENCILVIEW                   = 3,
  D3D10DDI_HT_SHADER                             = 4,
  D3D10DDI_HT_ELEMENTLAYOUT                      = 5,
  D3D10DDI_HT_BLENDSTATE                         = 6,
  D3D10DDI_HT_DEPTHSTENCILSTATE                  = 7,
  D3D10DDI_HT_RASTERIZERSTATE                    = 8,
  D3D10DDI_HT_SAMPLERSTATE                       = 9,
  D3D10DDI_HT_QUERY                              = 10,
  D3D11DDI_HT_COMMANDLIST                        = 11,
  D3D11DDI_HT_UNORDEREDACCESSVIEW                = 12,
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
  D3D11_1DDI_HT_DECODE                           = 13,
  D3D11_1DDI_HT_VIDEOPROCESSORENUM               = 14,
  D3D11_1DDI_HT_VIDEOPROCESSOR                   = 15,
  D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW           = 16,
  D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW          = 17,
  D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW         = 18,
#endif 
#if D3D12DDI_MINOR_HEADER_VERSION >= 2
      D3D12DDI_HT_COMMAND_QUEUE                  = ,
      D3D12DDI_HT_COMMAND_ALLOCATOR              = ,
      D3D12DDI_HT_PIPELINE_STATE                 = ,
      D3D12DDI_HT_COMMAND_LIST                   = ,
      D3D12DDI_HT_FENCE                          = ,
      D3D12DDI_HT_DESCRIPTOR_HEAP                = ,
      D3D12DDI_HT_HEAP                           = ,
      D3D12DDI_HT_UNORDERED_ACCESS_VIEW_COUNTER  = 

#endif } D3D11DDI_HANDLETYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D10DDI_HT_RESOURCE"></a><a id="d3d10ddi_ht_resource"></a><b>D3D10DDI_HT_RESOURCE</b>

<dd>
<p>A resource handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_SHADERRESOURCEVIEW"></a><a id="d3d10ddi_ht_shaderresourceview"></a><b>D3D10DDI_HT_SHADERRESOURCEVIEW</b>

<dd>
<p>
      A shader-resource-view handle. 
     </p>
</dd>

### -field <a id="D3D10DDI_HT_RENDERTARGETVIEW"></a><a id="d3d10ddi_ht_rendertargetview"></a><b>D3D10DDI_HT_RENDERTARGETVIEW</b>

<dd>
<p>A render-target-view handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_DEPTHSTENCILVIEW"></a><a id="d3d10ddi_ht_depthstencilview"></a><b>D3D10DDI_HT_DEPTHSTENCILVIEW</b>

<dd>
<p>A depth-stencil-view handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_SHADER"></a><a id="d3d10ddi_ht_shader"></a><b>D3D10DDI_HT_SHADER</b>

<dd>
<p>A shader handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_ELEMENTLAYOUT"></a><a id="d3d10ddi_ht_elementlayout"></a><b>D3D10DDI_HT_ELEMENTLAYOUT</b>

<dd>
<p>A value that identifies an element-layout handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_BLENDSTATE"></a><a id="d3d10ddi_ht_blendstate"></a><b>D3D10DDI_HT_BLENDSTATE</b>

<dd>
<p>A blend-state handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_DEPTHSTENCILSTATE"></a><a id="d3d10ddi_ht_depthstencilstate"></a><b>D3D10DDI_HT_DEPTHSTENCILSTATE</b>

<dd>
<p>A depth-stencil-state handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_RASTERIZERSTATE"></a><a id="d3d10ddi_ht_rasterizerstate"></a><b>D3D10DDI_HT_RASTERIZERSTATE</b>

<dd>
<p>A rasterizer-state handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_SAMPLERSTATE"></a><a id="d3d10ddi_ht_samplerstate"></a><b>D3D10DDI_HT_SAMPLERSTATE</b>

<dd>
<p>A sampler-state handle. </p>
</dd>

### -field <a id="D3D10DDI_HT_QUERY"></a><a id="d3d10ddi_ht_query"></a><b>D3D10DDI_HT_QUERY</b>

<dd>
<p>A query handle.</p>
</dd>

### -field <a id="D3D11DDI_HT_COMMANDLIST"></a><a id="d3d11ddi_ht_commandlist"></a><b>D3D11DDI_HT_COMMANDLIST</b>

<dd>
<p>A command-list handle. </p>
</dd>

### -field <a id="D3D11DDI_HT_UNORDEREDACCESSVIEW"></a><a id="d3d11ddi_ht_unorderedaccessview"></a><b>D3D11DDI_HT_UNORDEREDACCESSVIEW</b>

<dd>
<p>An unordered-access-view handle. </p>
</dd>

### -field <a id="D3D11_1DDI_HT_DECODE"></a><a id="d3d11_1ddi_ht_decode"></a><b>D3D11_1DDI_HT_DECODE</b>

<dd>
<p>A video decoder handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDI_HT_VIDEOPROCESSORENUM"></a><a id="d3d11_1ddi_ht_videoprocessorenum"></a><b>D3D11_1DDI_HT_VIDEOPROCESSORENUM</b>

<dd>
<p>A video processor enumeration handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDI_HT_VIDEOPROCESSOR"></a><a id="d3d11_1ddi_ht_videoprocessor"></a><b>D3D11_1DDI_HT_VIDEOPROCESSOR</b>

<dd>
<p>A video processor handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW"></a><a id="d3d11_1ddi_ht_videodecoderoutputview"></a><b>D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW</b>

<dd>
<p>A video decoder output-view handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW"></a><a id="d3d11_1ddi_ht_videoprocessorinputview"></a><b>D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW</b>

<dd>
<p>A video processor input-view handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW"></a><a id="d3d11_1ddi_ht_videoprocessoroutputview"></a><b>D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW</b>

<dd>
<p>A video processor output-view handle.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="____D3D12DDI_HT_COMMAND_QUEUE"></a><a id="____d3d12ddi_ht_command_queue"></a><b>    D3D12DDI_HT_COMMAND_QUEUE</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_COMMAND_ALLOCATOR"></a><a id="____d3d12ddi_ht_command_allocator"></a><b>    D3D12DDI_HT_COMMAND_ALLOCATOR</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_PIPELINE_STATE"></a><a id="____d3d12ddi_ht_pipeline_state"></a><b>    D3D12DDI_HT_PIPELINE_STATE</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_COMMAND_LIST"></a><a id="____d3d12ddi_ht_command_list"></a><b>    D3D12DDI_HT_COMMAND_LIST</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_FENCE"></a><a id="____d3d12ddi_ht_fence"></a><b>    D3D12DDI_HT_FENCE</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_DESCRIPTOR_HEAP"></a><a id="____d3d12ddi_ht_descriptor_heap"></a><b>    D3D12DDI_HT_DESCRIPTOR_HEAP</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_HEAP"></a><a id="____d3d12ddi_ht_heap"></a><b>    D3D12DDI_HT_HEAP</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <a id="____D3D12DDI_HT_UNORDERED_ACCESS_VIEW_COUNTER"></a><a id="____d3d12ddi_ht_unordered_access_view_counter"></a><b>    D3D12DDI_HT_UNORDERED_ACCESS_VIEW_COUNTER</b>

<dd>
<p>Supported starting with Windows 10.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D11DDI_HANDLETYPE is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>