---
UID: NS:d3dukmdt._D3DDDICB_DESTROYALLOCATION2FLAGS
title: "_D3DDDICB_DESTROYALLOCATION2FLAGS"
author: windows-driver-content
description: The D3DDDICB_DESTROYALLOCATION2FLAGS structure is used with the D3DKMT_DESTROYALLOCATION2 structure to describe parameters for releasing allocations with D3DKMTDestroyAllocation2.D3DDDICB_DESTROYALLOCATION2FLAGS structure is used with the D3DKMT_DESTROYALLOCATION2 structure to describe parameters for releasing allocations with D3DKMTDestroyAllocation2.
old-location: display\d3dddicb_destroyallocation2flags.htm
old-project: display
ms.assetid: 50D4BFB7-B5AC-4202-B426-F152B06C9F46
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3DDDICB_DESTROYALLOCATION2FLAGS, D3DDDICB_DESTROYALLOCATION2FLAGS structure [Display Devices], _D3DDDICB_DESTROYALLOCATION2FLAGS, d3dukmdt/D3DDDICB_DESTROYALLOCATION2FLAGS, display.d3dddicb_destroyallocation2flags
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dukmdt.h
api_name:
-	D3DDDICB_DESTROYALLOCATION2FLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDICB_DESTROYALLOCATION2FLAGS
---

# _D3DDDICB_DESTROYALLOCATION2FLAGS structure
The <b>D3DDDICB_DESTROYALLOCATION2FLAGS</b> structure is used with the <a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_destroyallocation2.md">D3DKMT_DESTROYALLOCATION2</a> structure to describe parameters for releasing allocations with <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtdestroyallocation2.md">D3DKMTDestroyAllocation2</a>.

## Syntax
````
typedef struct _D3DDDICB_DESTROYALLOCATION2FLAGS {
  union {
    struct {
      UINT AssumeNotInUse  :1;
      UINT SynchronousDestroy  :1;
      UINT Reserved  :29;
      UINT SystemUseOnly  :1;
    };
    UINT Value;
  };
} D3DDDICB_DESTROYALLOCATION2FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtdestroyallocation2.md">D3DKMTDestroyAllocation2</a>



<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_destroyallocation2.md">D3DKMT_DESTROYALLOCATION2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_DESTROYALLOCATION2FLAGS structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>