---
UID: NS:d3dukmdt._D3DDDI_RESOURCEFLAGS
title: "_D3DDDI_RESOURCEFLAGS"
author: windows-driver-content
description: The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's CreateResource function.
old-location: display\d3dddi_resourceflags.htm
old-project: display
ms.assetid: a466a158-dacf-42cc-b2ad-8af5b2c6c7d5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_RESOURCEFLAGS, D3DDDI_RESOURCEFLAGS structure [Display Devices], D3D_other_Structs_f00f4222-1c56-4b96-abe4-bf05088b7aa4.xml, _D3DDDI_RESOURCEFLAGS, d3dukmdt/D3DDDI_RESOURCEFLAGS, display.d3dddi_resourceflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	d3dukmdt.h
api_name:
-	D3DDDI_RESOURCEFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_RESOURCEFLAGS
---

# _D3DDDI_RESOURCEFLAGS structure
The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's <a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a> function.

## Syntax
```
typedef struct _D3DDDI_RESOURCEFLAGS {
  union {
    struct {
      UINT  : 1 RenderTarget;
      UINT  : 1 ZBuffer;
      UINT  : 1 Dynamic;
      UINT  : 1 HintStatic;
      UINT  : 1 AutogenMipmap;
      UINT  : 1 DMap;
      UINT  : 1 WriteOnly;
      UINT  : 1 NotLockable;
      UINT  : 1 Points;
      UINT  : 1 RtPatches;
      UINT  : 1 NPatches;
      UINT  : 1 SharedResource;
      UINT  : 1 DiscardRenderTarget;
      UINT  : 1 Video;
      UINT  : 1 CaptureBuffer;
      UINT  : 1 Primary;
      UINT  : 1 Texture;
      UINT  : 1 CubeMap;
      UINT  : 1 Volume;
      UINT  : 1 VertexBuffer;
      UINT  : 1 IndexBuffer;
      UINT  : 1 DecodeRenderTarget;
      UINT  : 1 DecodeCompressedBuffer;
      UINT  : 1 VideoProcessRenderTarget;
      UINT  : 1 CpuOptimized;
      UINT  : 1 MightDrawFromLocked;
      UINT  : 1 Overlay;
      UINT  : 1 MatchGdiPrimary;
      UINT  : 1 InterlacedRefresh;
      UINT  : 1 TextApi;
      UINT  : 1 RestrictedContent;
      UINT  : 1 RestrictSharedAccess;
    };
    UINT Value;
  };
} D3DDDI_RESOURCEFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/5b74c989-1a62-4415-a19a-dd0ba2fcff83">CreateResource</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542963">D3DDDIARG_CREATERESOURCE</a>