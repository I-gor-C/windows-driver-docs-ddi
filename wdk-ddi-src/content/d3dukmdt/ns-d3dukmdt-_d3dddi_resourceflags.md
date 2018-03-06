---
UID: NS:d3dukmdt._D3DDDI_RESOURCEFLAGS
title: "_D3DDDI_RESOURCEFLAGS"
author: windows-driver-content
description: The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's CreateResource function.
old-location: display\d3dddi_resourceflags.htm
old-project: display
ms.assetid: a466a158-dacf-42cc-b2ad-8af5b2c6c7d5
ms.author: windowsdriverdev
ms.date: 2/26/2018
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
product: Windows
targetos: Windows
req.typenames: D3DDDI_RESOURCEFLAGS
---

# _D3DDDI_RESOURCEFLAGS structure
The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource.md">CreateResource</a> function.

## Syntax
````
typedef struct _D3DDDI_RESOURCEFLAGS {
  union {
    struct {
      UINT RenderTarget  :1;
      UINT ZBuffer  :1;
      UINT Dynamic  :1;
      UINT HintStatic  :1;
      UINT AutogenMipmap  :1;
      UINT DMap  :1;
      UINT WriteOnly  :1;
      UINT NotLockable  :1;
      UINT Points  :1;
      UINT RtPatches  :1;
      UINT NPatches  :1;
      UINT SharedResource  :1;
      UINT DiscardRenderTarget  :1;
      UINT Video  :1;
      UINT CaptureBuffer  :1;
      UINT Primary  :1;
      UINT Texture;
      UINT CubeMap  :1;
      UINT Volume  :1;
      UINT VertexBuffer  :1;
      UINT IndexBuffer  :1;
      UINT DecodeRenderTarget  :1;
      UINT DecodeCompressedBuffer  :1;
      UINT VideoProcessRenderTarget  :1;
      UINT CpuOptimized  :1;
      UINT MightDrawFromLocked  :1;
      UINT Overlay  :1;
      UINT MatchGdiPrimary  :1;
      UINT InterlacedRefresh  :1;
      UINT TextApi  :1;
      UINT RestrictedContent  :1;
      UINT RestrictSharedAccess  :1;
    };
    UINT   Value;
  };
} D3DDDI_RESOURCEFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource.md">CreateResource</a>



<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddiarg_createresource.md">D3DDDIARG_CREATERESOURCE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_RESOURCEFLAGS structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>