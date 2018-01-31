---
UID : NE:d3d12umddi.D3D12DDICAPS_TYPE_VIDEO_0020
title : D3D12DDICAPS_TYPE_VIDEO_0020
author : windows-driver-content
description : Contains capability types for video.
old-location : display\d3d12ddicaps_type_video_0020.htm
old-project : display
ms.assetid : 3B95996D-EB7C-4DCF-B00C-BA5AFEFD4110
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT, D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES, D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT, D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES, D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS, D3D12DDICAPS_TYPE_VIDEO_0020 enumeration [Display Devices], d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO, display.d3d12ddicaps_type_video_0020, D3D12DDICAPS_TYPE_VIDEO_0020, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS, D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES, D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT, D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES, d3d12umddi/D3D12DDICAPS_TYPE_VIDEO_0020
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
req.typenames : D3D12DDICAPS_TYPE_VIDEO_0020
---

# D3D12DDICAPS_TYPE_VIDEO_0020 Enumeration
Contains capability types for video.

## Syntax
````
typedef enum _D3D12DDICAPS_TYPE_VIDEO_0020 { 
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT                       = 0,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES                      = 1,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS                       = 2,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT            = 3,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES  = 4,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT                      = 5,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS            = 6,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO               = 7
} D3D12DDICAPS_TYPE_VIDEO_0020;
````

## Constants

<table>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES</td>
<td>Retrieve the list of bitstream encryption schemes supported by the adapter.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT</td>
<td>Check whether a colorspace conversion, format conversion, and scale are supported.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS</td>
<td>Retrieves the supported decode formats.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES</td>
<td>Retrieve the list of decode profiles supported by the adapter.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT</td>
<td>Check if a decode profile, bitstream encryption, resolution, and format are supported</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS</td>
<td>The maximum number of streams that can be enabled at the same time.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO</td>
<td>Retrieves the number of past and future frames required for a given deinterlace mode, filters, frame rate conversion, and features.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT</td>
<td>Retrieves the video processor capabilities.</td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_CONTENT_PROTECTION_SYSTEM_COUNT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_CONTENT_PROTECTION_SYSTEM_SUPPORT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_CRYPTO_SESSION_SUPPORT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_CRYPTO_SESSION_TRANSFORM_SUPPORT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_DECODE_FORMAT_COUNT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_DECODE_PROFILE_COUNT</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_DECODER_HEAP_SIZE</td>
<td></td>
</tr>

<tr>
<td>D3D12DDICAPS_TYPE_VIDEO_0032_PROCESSOR_SIZE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |