---
UID: NS:d3dkmddi._DXGK_DESTROYALLOCATIONFLAGS
title: "_DXGK_DESTROYALLOCATIONFLAGS"
author: windows-driver-content
description: The DXGK_DESTROYALLOCATIONFLAGS structure identifies how to release allocations.
old-location: display\dxgk_destroyallocationflags.htm
old-project: display
ms.assetid: 8f848d68-cef4-45a2-bdda-1bc8c9df6272
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DmStructs_acc32f8d-3d16-493e-be05-e739bc635bd0.xml, d3dkmddi/DXGK_DESTROYALLOCATIONFLAGS, DXGK_DESTROYALLOCATIONFLAGS, _DXGK_DESTROYALLOCATIONFLAGS, DXGK_DESTROYALLOCATIONFLAGS structure [Display Devices], display.dxgk_destroyallocationflags
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
-	DXGK_DESTROYALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_DESTROYALLOCATIONFLAGS
---

# _DXGK_DESTROYALLOCATIONFLAGS structure
The DXGK_DESTROYALLOCATIONFLAGS structure identifies how to release allocations.

## Syntax
````
typedef struct _DXGK_DESTROYALLOCATIONFLAGS {
  union {
    struct {
      UINT DestroyResource  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_DESTROYALLOCATIONFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_destroyallocation.md">DXGKARG_DESTROYALLOCATION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_DESTROYALLOCATIONFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>