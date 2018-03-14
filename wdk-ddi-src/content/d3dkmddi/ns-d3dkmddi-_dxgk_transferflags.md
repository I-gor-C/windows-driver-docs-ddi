---
UID: NS:d3dkmddi._DXGK_TRANSFERFLAGS
title: "_DXGK_TRANSFERFLAGS"
author: windows-driver-content
description: The DXGK_TRANSFERFLAGS structure identifies the type of transfer operation to set up in a call to the DxgkDdiBuildPagingBuffer function.
old-location: display\dxgk_transferflags.htm
old-project: display
ms.assetid: b56657ac-98ff-482a-a2af-ffbfb8602248
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_TRANSFERFLAGS, DXGK_TRANSFERFLAGS structure [Display Devices], DmStructs_91973ccf-775f-4e97-bb1a-17cd1343a4f8.xml, _DXGK_TRANSFERFLAGS, d3dkmddi/DXGK_TRANSFERFLAGS, display.dxgk_transferflags
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_TRANSFERFLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_TRANSFERFLAGS
---

# _DXGK_TRANSFERFLAGS structure
The DXGK_TRANSFERFLAGS structure identifies the type of transfer operation to set up in a call to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a> function.

## Syntax
````
typedef struct _DXGK_TRANSFERFLAGS {
  union {
    struct {
      UINT Swizzle  :1;
      UINT Unswizzle  :1;
      UINT AllocationIsIdle  :1;
      UINT TransferStart  :1;
      UINT TransferEnd  :1;
      UINT Reserved  :27;
    };
    UINT Value;
  };
} DXGK_TRANSFERFLAGS;
````

## Members


## Remarks
You can set the transfer-operation type by setting bits in the 32-bit <b>Value</b> member or by setting individual members of the structure in the union that DXGK_TRANSFERFLAGS contains.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_buildpagingbuffer.md">DXGKARG_BUILDPAGINGBUFFER</a>



<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_buildpagingbuffer.md">DxgkDdiBuildPagingBuffer</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_TRANSFERFLAGS structure%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>