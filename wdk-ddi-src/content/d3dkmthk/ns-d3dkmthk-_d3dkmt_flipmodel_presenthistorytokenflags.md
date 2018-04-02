---
UID: NS:d3dkmthk._D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS
title: "_D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS"
author: windows-driver-content
description: The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure identifies attributes of a flip present-history operation.
old-location: display\d3dkmt_flipmodel_presenthistorytokenflags.htm
old-project: display
ms.assetid: 61901e06-fefd-4481-9f19-60ead55bbe36
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS, D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure [Display Devices], OpenGL_Structs_1ffd61bb-ba0b-4ee5-95af-d8c7e38c0b15.xml, _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS, d3dkmthk/D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS, display.d3dkmt_flipmodel_presenthistorytokenflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 7.
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
-	d3dkmthk.h
api_name:
-	D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS
---

# _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure
The D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS structure identifies attributes of a flip present-history operation.

## Syntax
```
typedef struct _D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS {
  union {
    struct {
      UINT  : 1                                    Video;
      UINT  : 1                                    RestrictedContent;
      UINT  : 1                                    ClipToView;
      UINT  : 1                                    StereoPreferRight;
      UINT  : 1                                    TemporaryMono;
      UINT  : 1                                    FlipRestart;
      UINT  : 1                                    HDRMetaDataChanged;
      UINT  : 2                                    AlphaMode;
      UINT  : 1                                    SignalLimitOnTokenCompletion;
      UINT  : 3                                    YCbCrFlags;
      UINT  : 1                                    IndependentFlip;
      D3DKMT_FLIPMODEL_INDEPENDENT_FLIP_STAGE  : 2 IndependentFlipStage;
      UINT  : 2                                    IndependentFlipReleaseCount;
      UINT  : 1                                    IndependentFlipForceNotifyDwm;
      UINT  : 1                                    UseCustomDuration;
      UINT  : 1                                    IndependentFlipRequestDwmConfirm;
      UINT  : 1                                    IndependentFlipCandidate;
      UINT  : 1                                    IndependentFlipCheckNeeded;
      UINT  : 1                                    IndependentFlipTrueImmediate;
      UINT  : 1                                    IndependentFlipRequestDwmExit;
      UINT  : 1                                    CompSurfaceNotifiedEarly;
      UINT  : 6                                    Reserved;
      UINT  : 29                                   Reserved;
    };
    UINT Value;
  };
} D3DKMT_FLIPMODEL_PRESENTHISTORYTOKENFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 7. Supported starting with Windows 7. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>