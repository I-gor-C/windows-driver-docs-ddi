---
UID: NS:dxgiddi.DXGI_DDI_PRESENT_FLAGS
title: DXGI_DDI_PRESENT_FLAGS
author: windows-driver-content
description: Identifies how to perform a present operation.
old-location: display\dxgi_ddi_present_flags.htm
old-project: display
ms.assetid: 87f3b66a-0fcb-4325-ae23-7f89d6b389e6
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGI_DDI_PRESENT_FLAGS, dxgiddi/DXGI_DDI_PRESENT_FLAGS, DXGI_DDI_PRESENT_FLAGS structure [Display Devices], display.dxgi_ddi_present_flags, UMDisplayDriver_Dx10param_Structs_75234d4d-acce-4f1f-804c-f7128d885c2f.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
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
-	dxgiddi.h
apiname:
-	DXGI_DDI_PRESENT_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGI_DDI_PRESENT_FLAGS
---

# DXGI_DDI_PRESENT_FLAGS structure
Identifies how to perform a present operation.

## Syntax
````
typedef struct DXGI_DDI_PRESENT_FLAGS {
  union {
    struct {
      UINT Blt  :1;
      UINT Flip  :1;
      UINT PreferRight  :1;
      UINT TemporaryMono  :1;
      UINT Reserved  :28;
    };
    UINT   Value;
  };
} DXGI_DDI_PRESENT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dxgiddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff569179">PresentDXGI</a>

<a href="..\dxgiddi\ns-dxgiddi-dxgi_ddi_arg_present.md">DXGI_DDI_ARG_PRESENT</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_PRESENT_FLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>