---
UID: NS:d3dukmdt._D3DDDI_RESOURCEFLAGS2
title: "_D3DDDI_RESOURCEFLAGS2"
author: windows-driver-content
description: Identifies the type of resource to create in a call to the driver's CreateResource2 function.
old-location: display\d3dddi_resourceflags2.htm
old-project: display
ms.assetid: 2edf2104-ad17-4c84-b991-57e64565029f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3DDDI_RESOURCEFLAGS2 structure [Display Devices], d3dukmdt/D3DDDI_RESOURCEFLAGS2, D3DDDI_RESOURCEFLAGS2, _D3DDDI_RESOURCEFLAGS2, display.d3dddi_resourceflags2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h, D3dkmddi.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	D3dukmdt.h
apiname:
-	D3DDDI_RESOURCEFLAGS2
product: Windows
targetos: Windows
req.typenames: D3DDDI_RESOURCEFLAGS2
---

# _D3DDDI_RESOURCEFLAGS2 structure
Identifies the type of resource to create in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource2.md">CreateResource2</a> function.

## Syntax
````
typedef struct _D3DDDI_RESOURCEFLAGS2 {
  union {
    struct {
      UINT VideoEncoder  :1;
      UINT UserMemory  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3))
      UINT CrossAdapter  :1;
      UINT Reserved  :29;
#else 
      UINT Reserved  :30;
#endif 
    };
    UINT   Value;
  };
} D3DDDI_RESOURCEFLAGS2;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dukmdt.h (include D3dukmdt.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_formatop.md">FORMATOP</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createresource2.md">CreateResource2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_RESOURCEFLAGS2 structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>