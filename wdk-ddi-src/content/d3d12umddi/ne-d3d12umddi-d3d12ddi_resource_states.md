---
UID: NE:d3d12umddi.D3D12DDI_RESOURCE_STATES
title: D3D12DDI_RESOURCE_STATES
author: windows-driver-content
description: Contains resource states.
old-location: display\d3d12ddi_resource_states.htm
old-project: display
ms.assetid: E5DB8AF3-A6ED-4CD7-9723-78ACD57F1723
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_RESOURCE_STATES, D3D12DDI_RESOURCE_STATES enumeration [Display Devices], D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ, D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE, D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ, D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE, D3D12DDI_RESOURCE_STATE_COMMON, D3D12DDI_RESOURCE_STATE_COPY_DEST, D3D12DDI_RESOURCE_STATE_COPY_SOURCE, D3D12DDI_RESOURCE_STATE_DEPTH_READ, D3D12DDI_RESOURCE_STATE_DEPTH_WRITE, D3D12DDI_RESOURCE_STATE_INDEX_BUFFER, D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT, D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE, D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE, D3D12DDI_RESOURCE_STATE_RENDER_TARGET, D3D12DDI_RESOURCE_STATE_RESOLVE_DEST, D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE, D3D12DDI_RESOURCE_STATE_STREAM_OUT, D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS, D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER, d3d12umddi/D3D12DDI_RESOURCE_STATES, d3d12umddi/D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ, d3d12umddi/D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE, d3d12umddi/D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ, d3d12umddi/D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE, d3d12umddi/D3D12DDI_RESOURCE_STATE_COMMON, d3d12umddi/D3D12DDI_RESOURCE_STATE_COPY_DEST, d3d12umddi/D3D12DDI_RESOURCE_STATE_COPY_SOURCE, d3d12umddi/D3D12DDI_RESOURCE_STATE_DEPTH_READ, d3d12umddi/D3D12DDI_RESOURCE_STATE_DEPTH_WRITE, d3d12umddi/D3D12DDI_RESOURCE_STATE_INDEX_BUFFER, d3d12umddi/D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT, d3d12umddi/D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE, d3d12umddi/D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE, d3d12umddi/D3D12DDI_RESOURCE_STATE_RENDER_TARGET, d3d12umddi/D3D12DDI_RESOURCE_STATE_RESOLVE_DEST, d3d12umddi/D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE, d3d12umddi/D3D12DDI_RESOURCE_STATE_STREAM_OUT, d3d12umddi/D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS, d3d12umddi/D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER, display.d3d12ddi_resource_states
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d12umddi.h
api_name:
-	D3D12DDI_RESOURCE_STATES
product:
- Windows
targetos: Windows
req.typenames: D3D12DDI_RESOURCE_STATES
---

# D3D12DDI_RESOURCE_STATES Enumeration
Contains resource states.

## Syntax
```
typedef enum D3D12DDI_RESOURCE_STATES {
  D3D12DDI_RESOURCE_STATE_COMMON                      ,
  D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER  ,
  D3D12DDI_RESOURCE_STATE_INDEX_BUFFER                ,
  D3D12DDI_RESOURCE_STATE_RENDER_TARGET               ,
  D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS            ,
  D3D12DDI_RESOURCE_STATE_DEPTH_WRITE                 ,
  D3D12DDI_RESOURCE_STATE_DEPTH_READ                  ,
  D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE   ,
  D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE       ,
  D3D12DDI_RESOURCE_STATE_STREAM_OUT                  ,
  D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT           ,
  D3D12DDI_RESOURCE_STATE_COPY_DEST                   ,
  D3D12DDI_RESOURCE_STATE_COPY_SOURCE                 ,
  D3D12DDI_RESOURCE_STATE_RESOLVE_DEST                ,
  D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE              ,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ      ,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE     ,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ     ,
  D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_COMMON</td>
                    <td>Common.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_VERTEX_AND_CONSTANT_BUFFER</td>
                    <td>Vertex and constant buffer.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_INDEX_BUFFER</td>
                    <td>Index buffer.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_RENDER_TARGET</td>
                    <td>Render target.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_UNORDERED_ACCESS</td>
                    <td>Unordered access.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_DEPTH_WRITE</td>
                    <td>Depth write.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_DEPTH_READ</td>
                    <td>Depth read.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_NON_PIXEL_SHADER_RESOURCE</td>
                    <td>Non-pixel shader resource.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_PIXEL_SHADER_RESOURCE</td>
                    <td>Pixel shader retsource.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_STREAM_OUT</td>
                    <td>Stream out.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_INDIRECT_ARGUMENT</td>
                    <td>Indirect argument.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_COPY_DEST</td>
                    <td>Copy destination.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_COPY_SOURCE</td>
                    <td>Copy source.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_RESOLVE_DEST</td>
                    <td>Resolve destination.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_RESOLVE_SOURCE</td>
                    <td>Resolve source.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_READ</td>
                    <td>Video decode read.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_0020_VIDEO_DECODE_WRITE</td>
                    <td>Video decode write.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_READ</td>
                    <td>Video process read.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_RESOURCE_STATE_0020_VIDEO_PROCESS_WRITE</td>
                    <td>Video process write.</td>
                </tr>
</table>

## Remarks

Resource barriers allow transitioning between hardware specific states for a corresponding operation and to synchronize read after write.  

Resource barriers are an existing concept in D3D12 that is extended to support video decode by adding new usage flags.
The write state is used for the decode target.  The write state is also used when decode conversion is enabled for the non-converted reference.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |