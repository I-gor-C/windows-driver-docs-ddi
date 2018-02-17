---
UID: NS:d3dumddi.D3DDDIARG_COPYFLAGS
title: D3DDDIARG_COPYFLAGS
author: windows-driver-content
description: Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.
old-location: display\d3dddiarg_copyflags.htm
old-project: display
ms.assetid: DA114D60-60EE-4D1D-B42C-A84CE54C8B95
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3DDDIARG_COPYFLAGS, D3DDDIARG_COPYFLAGS structure [Display Devices], d3dumddi/D3DDDIARG_COPYFLAGS, display.d3dddiarg_copyflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	D3dumddi.h
apiname:
-	D3DDDIARG_COPYFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDIARG_COPYFLAGS
---

# D3DDDIARG_COPYFLAGS structure
Describes how to handle the existing contents of a resource during a copy or update operation of a region within that resource. Used by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.

## Syntax
````
typedef struct D3DDDIARG_COPYFLAGS {
  union {
    struct {
      UINT NoOverwrite  :1;
      UINT Discard  :1;
      UINT Reserved1  :22;
      UINT BoxValid  :1;
      UINT Reserved2  :7;
    };
    UINT Value;
  };
} D3DDDIARG_COPYFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | d3dumddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-d3dddiarg_updatesubresourceup.md">D3DDDIARG_UPDATESUBRESOURCEUP</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_COPYFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>