---
UID: NS:d3dkmddi._DXGK_CREATECONTEXTFLAGS
title: "_DXGK_CREATECONTEXTFLAGS"
author: windows-driver-content
description: The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.
old-location: display\dxgk_createcontextflags.htm
old-project: display
ms.assetid: f7cadf78-c908-4034-889d-b5c7d0ffdaad
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: DXGK_CREATECONTEXTFLAGS structure [Display Devices], display.dxgk_createcontextflags, DXGK_CREATECONTEXTFLAGS, _DXGK_CREATECONTEXTFLAGS, d3dkmddi/DXGK_CREATECONTEXTFLAGS, DmStructs_19418464-77f9-407f-8b04-c6a35561069b.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	d3dkmddi.h
apiname:
-	DXGK_CREATECONTEXTFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_CREATECONTEXTFLAGS
---

# _DXGK_CREATECONTEXTFLAGS structure
The DXGK_CREATECONTEXTFLAGS structure identifies how to create contexts.

## Syntax
````
typedef struct _DXGK_CREATECONTEXTFLAGS {
  union {
    struct {
      UINT SystemContext  :1;
      UINT GdiContext  :1;
      UINT VirtualAddressing  :1;
      UINT SystemProtectedContext  :1;
      UINT Reserved  :28;
    };
    UINT Value;
  };
} DXGK_CREATECONTEXTFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_createcontext.md">DxgkDdiCreateContext</a>



<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_createcontext.md">DXGKARG_CREATECONTEXT</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CREATECONTEXTFLAGS structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>