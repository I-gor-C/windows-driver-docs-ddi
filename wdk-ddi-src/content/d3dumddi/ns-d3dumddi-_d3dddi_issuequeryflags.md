---
UID: NS:d3dumddi._D3DDDI_ISSUEQUERYFLAGS
title: "_D3DDDI_ISSUEQUERYFLAGS"
author: windows-driver-content
description: The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue.
old-location: display\d3dddi_issuequeryflags.htm
old-project: display
ms.assetid: 68360c2e-4b03-40a3-a313-bdb9ef26a298
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: d3dumddi/D3DDDI_ISSUEQUERYFLAGS, D3DDDI_ISSUEQUERYFLAGS structure [Display Devices], display.d3dddi_issuequeryflags, _D3DDDI_ISSUEQUERYFLAGS, D3DDDI_ISSUEQUERYFLAGS, D3D_other_Structs_794dd0b0-f24c-4e9e-befe-d79dd4efbaef.xml
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
-	D3DDDI_ISSUEQUERYFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_ISSUEQUERYFLAGS
---

# _D3DDDI_ISSUEQUERYFLAGS structure
The D3DDDI_ISSUEQUERYFLAGS structure identifies the state of a query issue.

## Syntax
````
typedef struct _D3DDDI_ISSUEQUERYFLAGS {
  union {
    struct {
      UINT Begin  :1;
      UINT End  :1;
      UINT Reserved  :30;
    };
    UINT   Value;
  };
} D3DDDI_ISSUEQUERYFLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_issuequery.md">D3DDDIARG_ISSUEQUERY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_ISSUEQUERYFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>