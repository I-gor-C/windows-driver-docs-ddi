---
UID: NS:d3d10umddi.D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK
title: D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK
author: windows-driver-content
description: D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK is used with VideoDecoderSubmitBuffers1 to describe the decoder buffer sub sample mapping block size.
old-location: display\d3dwddm2_0ddi_video_decoder_sub_sample_mapping_block.htm
old-project: display
ms.assetid: FDB38644-AC61-401A-97E2-7CB0ED1C33D4
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK, D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK structure [Display Devices], d3d10umddi/D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK, display.d3dwddm2_0ddi_video_decoder_sub_sample_mapping_block
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	D3d10umddi.h
api_name:
-	D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK
product: Windows
targetos: Windows
req.typenames: D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK
---

# D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK structure
<b>D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK</b> is used with  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecodersubmitbuffers1.md">VideoDecoderSubmitBuffers1</a> to describe the decoder buffer sub sample mapping block size.

## Syntax
````
typedef struct D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK {
  UINT ClearSize;
  UINT EncryptedSize;
} D3DWDDM2_0DDI_VIDEO_DECODER_SUB_SAMPLE_MAPPING_BLOCK;
````

## Members


`ClearSize`

The number of clear (non-encrypted) bytes at the start of the block.

`EncryptedSize`

The number of encrypted bytes following the clear bytes.

## Remarks
Values in the sub sample mapping blocks are relative to the start of the decode buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm2_0ddi_videodecodersubmitbuffers1.md">VideoDecoderSubmitBuffers1</a>