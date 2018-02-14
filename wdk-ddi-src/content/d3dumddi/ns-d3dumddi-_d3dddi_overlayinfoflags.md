---
UID: NS:d3dumddi._D3DDDI_OVERLAYINFOFLAGS
title: "_D3DDDI_OVERLAYINFOFLAGS"
author: windows-driver-content
description: The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform.
old-location: display\d3dddi_overlayinfoflags.htm
old-project: display
ms.assetid: ebf31c28-857b-4885-a910-16da5a011ce1
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3D_other_Structs_3c20db45-e3b5-4e0e-96a6-d2171dbf309a.xml, D3DDDI_OVERLAYINFOFLAGS structure [Display Devices], display.d3dddi_overlayinfoflags, _D3DDDI_OVERLAYINFOFLAGS, d3dumddi/D3DDDI_OVERLAYINFOFLAGS, D3DDDI_OVERLAYINFOFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dumddi.h
apiname:
-	D3DDDI_OVERLAYINFOFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_OVERLAYINFOFLAGS
---

# _D3DDDI_OVERLAYINFOFLAGS structure
The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform.

## Syntax
````
typedef struct _D3DDDI_OVERLAYINFOFLAGS {
  union {
    struct {
      UINT DstColorKey  :1;
      UINT DstColorKeyRange  :1;
      UINT SrcColorKey  :1;
      UINT SrcColorKeyRange  :1;
      UINT Bob  :1;
      UINT Interleaved  :1;
      UINT MirrorLeftRight  :1;
      UINT MirrorUpDown  :1;
      UINT Deinterlace  :1;
      UINT LimitedRGB  :1;
      UINT YCbCrBT709  :1;
      UINT YCbCrxvYCC  :1;
      UINT Reserved  :20;
    };
    UINT   Value;
  };
} D3DDDI_OVERLAYINFOFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_overlayinfo.md">D3DDDI_OVERLAYINFO</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_OVERLAYINFOFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>