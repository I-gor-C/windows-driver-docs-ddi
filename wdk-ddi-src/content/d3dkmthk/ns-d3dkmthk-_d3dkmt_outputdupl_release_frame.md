---
UID: NS:d3dkmthk._D3DKMT_OUTPUTDUPL_RELEASE_FRAME
title: "_D3DKMT_OUTPUTDUPL_RELEASE_FRAME"
author: windows-driver-content
description: Defines the duplicated desktop image that is to be released in a call to the D3DKMTOutputDuplReleaseFrame function.
old-location: display\d3dkmt_outputdupl_release_frame.htm
old-project: display
ms.assetid: 98d31b6b-c31a-4509-a89f-f09932468313
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_OUTPUTDUPL_RELEASE_FRAME, D3DKMT_OUTPUTDUPL_RELEASE_FRAME structure [Display Devices], _D3DKMT_OUTPUTDUPL_RELEASE_FRAME, d3dkmthk/D3DKMT_OUTPUTDUPL_RELEASE_FRAME, display.d3dkmt_outputdupl_release_frame
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3dkmthk.h
api_name:
-	D3DKMT_OUTPUTDUPL_RELEASE_FRAME
product: Windows
targetos: Windows
req.typenames: D3DKMT_OUTPUTDUPL_RELEASE_FRAME
---

# _D3DKMT_OUTPUTDUPL_RELEASE_FRAME structure
Defines the duplicated desktop image that is to be released in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439438">D3DKMTOutputDuplReleaseFrame</a> function.

## Syntax
```
typedef struct _D3DKMT_OUTPUTDUPL_RELEASE_FRAME {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           NextKeyMutexIdx;
} D3DKMT_OUTPUTDUPL_RELEASE_FRAME;
```

## Members


`hAdapter`

[in] A handle of type <b>D3DKMT_HANDLE</b> that represents a kernel-mode handle to the graphics adapter that contains the duplicated desktop image.

`VidPnSourceId`

[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology.

`NextKeyMutexIdx`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439438">D3DKMTOutputDuplReleaseFrame</a>