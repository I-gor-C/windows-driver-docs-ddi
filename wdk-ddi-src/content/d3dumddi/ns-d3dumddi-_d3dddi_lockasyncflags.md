---
UID: NS:d3dumddi._D3DDDI_LOCKASYNCFLAGS
title: "_D3DDDI_LOCKASYNCFLAGS"
author: windows-driver-content
description: The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource.
old-location: display\d3dddi_lockasyncflags.htm
old-project: display
ms.assetid: 0e6dd14c-5192-4c4b-9dcb-716989d24588
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: D3D_other_Structs_765c2b3d-14e2-4eaf-978f-764263aa2a99.xml, _D3DDDI_LOCKASYNCFLAGS, display.d3dddi_lockasyncflags, D3DDDI_LOCKASYNCFLAGS structure [Display Devices], D3DDDI_LOCKASYNCFLAGS, d3dumddi/D3DDDI_LOCKASYNCFLAGS
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
-	D3DDDI_LOCKASYNCFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_LOCKASYNCFLAGS
---

# _D3DDDI_LOCKASYNCFLAGS structure
The D3DDDI_LOCKASYNCFLAGS structure identifies how to lock a resource.

## Syntax
````
typedef struct _D3DDDI_LOCKASYNCFLAGS {
  union {
    struct {
      UINT NoOverwrite  :1;
      UINT Discard  :1;
      UINT RangeValid  :1;
      UINT AreaValid  :1;
      UINT BoxValid  :1;
      UINT NoExistingReferences  :1;
      UINT NotifyOnly  :1;
      UINT Reserved  :25;
    };
    UINT   Value;
  };
} D3DDDI_LOCKASYNCFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_lockasync.md">D3DDDIARG_LOCKASYNC</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_LOCKASYNCFLAGS structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>