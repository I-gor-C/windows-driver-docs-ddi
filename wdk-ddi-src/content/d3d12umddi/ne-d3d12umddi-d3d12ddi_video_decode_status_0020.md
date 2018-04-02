---
UID: NE:d3d12umddi.D3D12DDI_VIDEO_DECODE_STATUS_0020
title: D3D12DDI_VIDEO_DECODE_STATUS_0020
author: windows-driver-content
description: Contains status values for video decode.
old-location: display\d3d12ddi_video_decode_status.htm
old-project: display
ms.assetid: E7A3944D-142E-450C-B9EE-9190BF264C60
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_VIDEO_DECODE_STATUS_0020, D3D12DDI_VIDEO_DECODE_STATUS_0020 enumeration [Display Devices], D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE, D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE_SKIP_DISPLAY, D3D12DDI_VIDEO_DECODE_STATUS_0020_OK, D3D12DDI_VIDEO_DECODE_STATUS_0020_RATE_EXCEEDED, D3D12DDI_VIDEO_DECODE_STATUS_0020_RESTART, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE_SKIP_DISPLAY, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020_OK, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020_RATE_EXCEEDED, d3d12umddi/D3D12DDI_VIDEO_DECODE_STATUS_0020_RESTART, display.d3d12ddi_video_decode_status
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
-	D3D12DDI_VIDEO_DECODE_STATUS_0020
product:
- Windows
targetos: Windows
req.typenames: D3D12DDI_VIDEO_DECODE_STATUS_0020
---

# D3D12DDI_VIDEO_DECODE_STATUS_0020 Enumeration
Contains status values for video decode.

## Syntax
```
typedef enum D3D12DDI_VIDEO_DECODE_STATUS_0020 {
  D3D12DDI_VIDEO_DECODE_STATUS_0020_OK                     ,
  D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE               ,
  D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE_SKIP_DISPLAY  ,
  D3D12DDI_VIDEO_DECODE_STATUS_0020_RESTART                ,
  D3D12DDI_VIDEO_DECODE_STATUS_0020_RATE_EXCEEDED
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_VIDEO_DECODE_STATUS_0020_OK</td>
                    <td>Operation succeeded.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE</td>
                    <td>There was a minor problem in the data format, but the host decoder should continue processing.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_DECODE_STATUS_0020_CONTINUE_SKIP_DISPLAY</td>
                    <td>There was a significant problem in the data format. The host decoder should continue processing, but should skip display.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_DECODE_STATUS_0020_RESTART</td>
                    <td>There was a severe problem in the data format. The host decoder should restart the entire decoding process, starting at a sequence or random-access entry point.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_VIDEO_DECODE_STATUS_0020_RATE_EXCEEDED</td>
                    <td>The bit rate or frame rate supplied to decode stream creation was insufficient for this frame.  When this status is reported, the <b>BitRate</b> member of the <a href="https://msdn.microsoft.com/F58AB9E1-4061-46B8-8137-319DF30D9CA7">D3D12DDI_QUERY_DATA_VIDEO_DECODE_STATISTICS</a> structure reports a value that can be used to recreate the decode stream at the same frame rate and succeed decoding the failed frames.  Subsequent frames may still fail if those frames exceed the new value.  The reported bit rate is calculated with the frame rate with which the stream was created.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/F58AB9E1-4061-46B8-8137-319DF30D9CA7">D3D12DDI_QUERY_DATA_VIDEO_DECODE_STATISTICS</a>