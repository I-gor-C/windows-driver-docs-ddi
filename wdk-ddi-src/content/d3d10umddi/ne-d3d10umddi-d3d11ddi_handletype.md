---
UID: NE:d3d10umddi.D3D11DDI_HANDLETYPE
title: D3D11DDI_HANDLETYPE
author: windows-driver-content
description: Contains values that identify handle types.
old-location: display\d3d11ddi_handletype.htm
old-project: display
ms.assetid: 9ac032fe-b870-49aa-8602-3c7aa997ef9a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D10DDI_HT_BLENDSTATE, D3D10DDI_HT_DEPTHSTENCILSTATE, D3D10DDI_HT_DEPTHSTENCILVIEW, D3D10DDI_HT_ELEMENTLAYOUT, D3D10DDI_HT_QUERY, D3D10DDI_HT_RASTERIZERSTATE, D3D10DDI_HT_RENDERTARGETVIEW, D3D10DDI_HT_RESOURCE, D3D10DDI_HT_SAMPLERSTATE, D3D10DDI_HT_SHADER, D3D10DDI_HT_SHADERRESOURCEVIEW, D3D11DDI_HANDLETYPE, D3D11DDI_HANDLETYPE enumeration [Display Devices], D3D11DDI_HT_COMMANDLIST, D3D11DDI_HT_UNORDEREDACCESSVIEW, D3D11_1DDI_HT_DECODE, D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW, D3D11_1DDI_HT_VIDEOPROCESSOR, D3D11_1DDI_HT_VIDEOPROCESSORENUM, D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW, D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW, D3D12DDI_HT_COMMAND_ALLOCATOR, D3D12DDI_HT_COMMAND_LIST, D3D12DDI_HT_COMMAND_QUEUE, D3D12DDI_HT_DESCRIPTOR_HEAP, D3D12DDI_HT_FENCE, D3D12DDI_HT_HEAP, D3D12DDI_HT_PIPELINE_STATE, D3D12DDI_HT_UNORDERED_ACCESS_VIEW_COUNTER, UMDisplayDriver_Dx11param_Structs_b979aef9-205a-4af9-b68e-9064499faca5.xml, d3d10umddi/ D3D12DDI_HT_COMMAND_ALLOCATOR, d3d10umddi/ D3D12DDI_HT_COMMAND_LIST, d3d10umddi/ D3D12DDI_HT_COMMAND_QUEUE, d3d10umddi/ D3D12DDI_HT_DESCRIPTOR_HEAP, d3d10umddi/ D3D12DDI_HT_FENCE, d3d10umddi/ D3D12DDI_HT_HEAP, d3d10umddi/ D3D12DDI_HT_PIPELINE_STATE, d3d10umddi/ D3D12DDI_HT_UNORDERED_ACCESS_VIEW_COUNTER, d3d10umddi/D3D10DDI_HT_BLENDSTATE, d3d10umddi/D3D10DDI_HT_DEPTHSTENCILSTATE, d3d10umddi/D3D10DDI_HT_DEPTHSTENCILVIEW, d3d10umddi/D3D10DDI_HT_ELEMENTLAYOUT, d3d10umddi/D3D10DDI_HT_QUERY, d3d10umddi/D3D10DDI_HT_RASTERIZERSTATE, d3d10umddi/D3D10DDI_HT_RENDERTARGETVIEW, d3d10umddi/D3D10DDI_HT_RESOURCE, d3d10umddi/D3D10DDI_HT_SAMPLERSTATE, d3d10umddi/D3D10DDI_HT_SHADER, d3d10umddi/D3D10DDI_HT_SHADERRESOURCEVIEW, d3d10umddi/D3D11DDI_HANDLETYPE, d3d10umddi/D3D11DDI_HT_COMMANDLIST, d3d10umddi/D3D11DDI_HT_UNORDEREDACCESSVIEW, d3d10umddi/D3D11_1DDI_HT_DECODE, d3d10umddi/D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW, d3d10umddi/D3D11_1DDI_HT_VIDEOPROCESSOR, d3d10umddi/D3D11_1DDI_HT_VIDEOPROCESSORENUM, d3d10umddi/D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW, d3d10umddi/D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW, display.d3d11ddi_handletype
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDI_HANDLETYPE is supported beginning with the Windows 7 operating system.
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
-	d3d10umddi.h
api_name:
-	D3D11DDI_HANDLETYPE
product:
- Windows
targetos: Windows
req.typenames: D3D11DDI_HANDLETYPE
---

# D3D11DDI_HANDLETYPE Enumeration
Contains values that identify handle types.

## Syntax
```
typedef enum D3D11DDI_HANDLETYPE {
  D3D10DDI_HT_RESOURCE                    ,
  D3D10DDI_HT_SHADERRESOURCEVIEW          ,
  D3D10DDI_HT_RENDERTARGETVIEW            ,
  D3D10DDI_HT_DEPTHSTENCILVIEW            ,
  D3D10DDI_HT_SHADER                      ,
  D3D10DDI_HT_ELEMENTLAYOUT               ,
  D3D10DDI_HT_BLENDSTATE                  ,
  D3D10DDI_HT_DEPTHSTENCILSTATE           ,
  D3D10DDI_HT_RASTERIZERSTATE             ,
  D3D10DDI_HT_SAMPLERSTATE                ,
  D3D10DDI_HT_QUERY                       ,
  D3D11DDI_HT_COMMANDLIST                 ,
  D3D11DDI_HT_UNORDEREDACCESSVIEW         ,
  D3D11_1DDI_HT_DECODE                    ,
  D3D11_1DDI_HT_VIDEOPROCESSORENUM        ,
  D3D11_1DDI_HT_VIDEOPROCESSOR            ,
  D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW    ,
  D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW   ,
  D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW  ,
  D3DWDDM2_2DDI_HT_CACHESESSION
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D10DDI_HT_RESOURCE</td>
                    <td>A resource handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_SHADERRESOURCEVIEW</td>
                    <td>A shader-resource-view handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_RENDERTARGETVIEW</td>
                    <td>A render-target-view handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_DEPTHSTENCILVIEW</td>
                    <td>A depth-stencil-view handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_SHADER</td>
                    <td>A shader handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_ELEMENTLAYOUT</td>
                    <td>A value that identifies an element-layout handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_BLENDSTATE</td>
                    <td>A blend-state handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_DEPTHSTENCILSTATE</td>
                    <td>A depth-stencil-state handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_RASTERIZERSTATE</td>
                    <td>A rasterizer-state handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_SAMPLERSTATE</td>
                    <td>A sampler-state handle.</td>
                </tr>
            
                <tr>
                    <td>D3D10DDI_HT_QUERY</td>
                    <td>A query handle.</td>
                </tr>
            
                <tr>
                    <td>D3D11DDI_HT_COMMANDLIST</td>
                    <td>A command-list handle.</td>
                </tr>
            
                <tr>
                    <td>D3D11DDI_HT_UNORDEREDACCESSVIEW</td>
                    <td>An unordered-access-view handle.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_DECODE</td>
                    <td>A video decoder handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_VIDEOPROCESSORENUM</td>
                    <td>A video processor enumeration handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_VIDEOPROCESSOR</td>
                    <td>A video processor handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_VIDEODECODEROUTPUTVIEW</td>
                    <td>A video decoder output-view handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_VIDEOPROCESSORINPUTVIEW</td>
                    <td>A video processor input-view handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_HT_VIDEOPROCESSOROUTPUTVIEW</td>
                    <td>A video processor output-view handle.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_2DDI_HT_CACHESESSION</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3D11DDI_HANDLETYPE is supported beginning with the Windows 7 operating system. D3D11DDI_HANDLETYPE is supported beginning with the Windows 7 operating system. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |