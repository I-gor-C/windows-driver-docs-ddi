---
UID: NS:d3dkmddi._DXGK_CREATEALLOCATIONFLAGS
title: "_DXGK_CREATEALLOCATIONFLAGS"
author: windows-driver-content
description: The DXGK_CREATEALLOCATIONFLAGS structure identifies how to create allocations.
old-location: display\dxgk_createallocationflags.htm
old-project: display
ms.assetid: 3c6c5515-855a-4016-a327-958959981f0f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.dxgk_createallocationflags, d3dkmddi/DXGK_CREATEALLOCATIONFLAGS, DmStructs_320b15bf-5664-4fb9-9126-2c063ef75467.xml, _DXGK_CREATEALLOCATIONFLAGS, DXGK_CREATEALLOCATIONFLAGS, DXGK_CREATEALLOCATIONFLAGS structure [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
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
-	DXGK_CREATEALLOCATIONFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_CREATEALLOCATIONFLAGS
---

# _DXGK_CREATEALLOCATIONFLAGS structure
The DXGK_CREATEALLOCATIONFLAGS structure identifies how to create allocations.

## Syntax
````
typedef struct _DXGK_CREATEALLOCATIONFLAGS {
  union {
    struct {
      UINT Resource  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_CREATEALLOCATIONFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista. Available starting with Windows Vista. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_createallocation.md">DXGKARG_CREATEALLOCATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CREATEALLOCATIONFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>