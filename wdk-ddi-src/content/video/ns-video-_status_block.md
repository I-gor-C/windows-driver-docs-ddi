---
UID: NS:video._STATUS_BLOCK
title: "_STATUS_BLOCK"
author: windows-driver-content
description: The STATUS_BLOCK structure is a substructure within the VIDEO_REQUEST_PACKET structure. A miniport driver's HwVidStartIO function must set the status block of each VRP that it gets.
old-location: display\status_block.htm
old-project: display
ms.assetid: 8e3126df-d081-4545-a5db-8637ee27f15b
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTATUS_BLOCK, PSTATUS_BLOCK, PSTATUS_BLOCK structure pointer [Display Devices], STATUS_BLOCK, STATUS_BLOCK structure [Display Devices], Video_Structs_90f8dc6a-a666-4976-bc71-edf43b31b6e4.xml, _STATUS_BLOCK, display.status_block, video/PSTATUS_BLOCK, video/STATUS_BLOCK"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	video.h
api_name:
-	STATUS_BLOCK
product:
- Windows
targetos: Windows
req.typenames: STATUS_BLOCK, *PSTATUS_BLOCK
req.product: Windows 10 or later.
---

# _STATUS_BLOCK structure
The STATUS_BLOCK structure is a substructure within the VIDEO_REQUEST_PACKET structure. A miniport driver's <a href="https://msdn.microsoft.com/82951291-cf3e-486b-ad0e-f347fefe0370">HwVidStartIO</a> function must set the status block of each <a href="https://msdn.microsoft.com/a1de1905-09f3-4689-ace9-06690a1f930a">VRP</a> that it gets.

## Syntax
```
typedef struct _STATUS_BLOCK {
  union {
    PVOID     Pointer;
    VP_STATUS Status;
  };
  ULONG_PTR Information;
} *PSTATUS_BLOCK, STATUS_BLOCK;
```

## Members


`Information`

Supplies additional information about the completed operation. The meaning of the value varies according to VRP. Generally, this member is used to return the minimum size required for the input buffer if the VRP passes data in the <b>InputBuffer</b>. Alternatively, it contains the number of bytes of data transferred if the requested operation returns data in the VRP <b>OutputBuffer</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | video.h (include Video.h) |

## See Also

<a href="https://msdn.microsoft.com/82951291-cf3e-486b-ad0e-f347fefe0370">HwVidStartIO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570547">VIDEO_REQUEST_PACKET</a>