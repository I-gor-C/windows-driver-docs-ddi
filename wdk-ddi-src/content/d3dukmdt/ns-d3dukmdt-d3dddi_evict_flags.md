---
UID: NS:d3dukmdt.D3DDDI_EVICT_FLAGS
title: D3DDDI_EVICT_FLAGS
author: windows-driver-content
description: D3DDDI_EVICT_FLAGS specifies the eviction behavior.
old-location: display\d3dddi_evict_flags.htm
old-project: display
ms.assetid: 443671F1-98F5-4F9F-900B-37E3E50770CE
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: D3DDDI_EVICT_FLAGS, D3DDDI_EVICT_FLAGS structure [Display Devices], display.d3dddi_evict_flags, d3dukmdt/D3DDDI_EVICT_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	d3dukmdt.h
apiname:
-	D3DDDI_EVICT_FLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_EVICT_FLAGS
---

# D3DDDI_EVICT_FLAGS structure
<b>D3DDDI_EVICT_FLAGS</b> specifies the eviction behavior.

## Syntax
````
typedef struct D3DDDI_EVICT_FLAGS {
  union {
    struct {
      UINT EvictOnlyIfNecessary  :1;
      UINT NotWrittenTo  :1;
      UINT Reserved  :30;
    };
    UINT Value;
  };
} D3DDDI_EVICT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtevict.md">D3DKMTEvict</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_evictcb.md">pfnEvictCb</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_EVICT_FLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>