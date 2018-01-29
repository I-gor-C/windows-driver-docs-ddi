---
UID : NE:d3d12umddi.D3D12DDI_HANDLETYPE
title : D3D12DDI_HANDLETYPE
author : windows-driver-content
description : Contains driver handle types.
old-location : display\d3d12ddi_handletype.htm
old-project : display
ms.assetid : 807CC73E-C5A5-4D49-AFAF-32A51D832F82
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDI_HT_0030_CRYPTOSESSIONPOLICY, D3D12DDI_HT_PIPELINE_STATE, d3d12umddi/D3D12DDI_HT_FENCE, d3d12umddi/D3D12DDI_HT_0032_VIDEO_DECODER_HEAP, D3D12DDI_HT_COMMAND_QUEUE, D3D12DDI_HT_0020_VIDEO_DECODE_STREAM, d3d12umddi/D3D12DDI_HT_PIPELINE_STATE, D3D12DDI_HT_0010_PIPELINE_LIBRARY, D3D12DDI_HT_PASS, d3d12umddi/D3D12DDI_HT_0020_VIDEO_DECODE_STREAM, d3d12umddi/D3D12DDI_HT_DESCRIPTOR_HEAP, D3D12DDI_HT_COMMAND_SIGNATURE, d3d12umddi/D3D12DDI_HT_COMMAND_ALLOCATOR, d3d12umddi/D3D12DDI_HANDLETYPE, d3d12umddi/D3D12DDI_HT_0030_CRYPTOSESSION, d3d12umddi/D3D12DDI_HT_COMMAND_SIGNATURE, D3D12DDI_HT_0030_PROTECTEDRESOURCESESSION, D3D12DDI_HT_0020_VIDEO_DECODER, D3D12DDI_HT_0030_CRYPTOSESSION, d3d12umddi/D3D12DDI_HT_QUERY_HEAP, d3d12umddi/D3D12DDI_HT_COMMAND_LIST, D3D12DDI_HT_0012_RESOURCE, D3D12DDI_HANDLETYPE, d3d12umddi/D3D12DDI_HT_0020_VIDEO_PROCESSOR, display.d3d12ddi_handletype, d3d12umddi/D3D12DDI_HT_0020_VIDEO_PROCESS_STREAM, D3D12DDI_HT_COMMAND_LIST, d3d12umddi/D3D12DDI_HT_0010_PIPELINE_LIBRARY, d3d12umddi/D3D12DDI_HT_0020_VIDEO_DECODER, D3D12DDI_HT_0032_VIDEO_DECODER_HEAP, d3d12umddi/D3D12DDI_HT_0030_PROTECTEDRESOURCESESSION, D3D12DDI_HT_0020_VIDEO_PROCESS_STREAM, D3D12DDI_HT_HEAP, d3d12umddi/D3D12DDI_HT_0012_RESOURCE, d3d12umddi/D3D12DDI_HT_HEAP, D3D12DDI_HANDLETYPE enumeration [Display Devices], D3D12DDI_HT_DESCRIPTOR_HEAP, d3d12umddi/D3D12DDI_HT_PASS, D3D12DDI_HT_COMMAND_ALLOCATOR, d3d12umddi/D3D12DDI_HT_0030_CRYPTOSESSIONPOLICY, D3D12DDI_HT_0020_VIDEO_PROCESSOR, d3d12umddi/D3D12DDI_HT_COMMAND_QUEUE, D3D12DDI_HT_QUERY_HEAP, D3D12DDI_HT_FENCE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D12DDI_HANDLETYPE
---

# D3D12DDI_HANDLETYPE Enumeration
Contains driver handle types.

## Syntax
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

## Constants

<table>

<tr>
<td>D3D12DDI_HT_0010_PIPELINE_LIBRARY</td>
<td>A pipeline library handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0012_RESOURCE</td>
<td>A resource handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0020_VIDEO_DECODER</td>
<td>A video decoder handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0020_VIDEO_PROCESSOR</td>
<td>A video processor handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0030_CRYPTOSESSION</td>
<td>A crypto session handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0030_CRYPTOSESSIONPOLICY</td>
<td>A crypto session policy handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0030_PROTECTEDRESOURCESESSION</td>
<td>A protected resource session handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_0032_VIDEO_DECODER_HEAP</td>
<td>A video decoder heap handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_COMMAND_ALLOCATOR</td>
<td>A command allocator handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_COMMAND_LIST</td>
<td>A command list handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_COMMAND_QUEUE</td>
<td>A command queue handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_COMMAND_SIGNATURE</td>
<td>A command signature handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_DESCRIPTOR_HEAP</td>
<td>A descriptor heap handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_FENCE</td>
<td>A fence handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_HEAP</td>
<td>A heap handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_PASS</td>
<td>A pass handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_PIPELINE_STATE</td>
<td>A pipeline state handle type.</td>
</tr>

<tr>
<td>D3D12DDI_HT_QUERY_HEAP</td>
<td>A query heap handle type.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |