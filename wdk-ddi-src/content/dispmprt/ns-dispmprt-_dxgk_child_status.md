---
UID: NS:dispmprt._DXGK_CHILD_STATUS
title: "_DXGK_CHILD_STATUS"
author: windows-driver-content
description: The DXGK_CHILD_STATUS structure contains members that indicate the status of a child device of the display adapter.
old-location: display\dxgk_child_status.htm
old-project: display
ms.assetid: e2aba049-b51f-49b9-b0bb-c98c318dea86
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_CHILD_STATUS, DXGK_CHILD_STATUS, DXGK_CHILD_STATUS structure [Display Devices], DmStructs_9a370d5a-9ca8-4c4f-a5cf-3361847d65e7.xml, PDXGK_CHILD_STATUS, PDXGK_CHILD_STATUS structure pointer [Display Devices], _DXGK_CHILD_STATUS, display.dxgk_child_status, dispmprt/DXGK_CHILD_STATUS, dispmprt/PDXGK_CHILD_STATUS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
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
-	dispmprt.h
api_name:
-	DXGK_CHILD_STATUS
product:
- Windows
targetos: Windows
req.typenames: DXGK_CHILD_STATUS, *PDXGK_CHILD_STATUS
---

# _DXGK_CHILD_STATUS structure
The DXGK_CHILD_STATUS structure contains members that indicate the status of a child device of the display adapter.

## Syntax
```
typedef struct _DXGK_CHILD_STATUS {
  DXGK_CHILD_STATUS_TYPE Type;
  ULONG                  ChildUid;
  union {
    struct {
      BOOLEAN Connected;
    } HotPlug;
    struct {
      UCHAR Angle;
    } Rotation;
    struct {
      BOOLEAN                         Connected;
      D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY MiracastMonitorType;
    } Miracast;
  };
} *PDXGK_CHILD_STATUS, DXGK_CHILD_STATUS;
```

## Members


`Type`

A member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561015">DXGK_CHILD_STATUS_TYPE</a> enumeration that indicates the type of status being requested.

`ChildUid`

An integer, created previously by the display miniport driver, that identifies the child device for which status is being requested.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546605">D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561015">DXGK_CHILD_STATUS_TYPE</a>



<a href="https://msdn.microsoft.com/780a8867-bba1-4b1b-a941-b55bfe087b7b">DxgkCbIndicateChildStatus</a>



<a href="https://msdn.microsoft.com/eb1a0df0-6239-4d82-8477-7dd015f80b6e">DxgkDdiQueryChildRelations</a>



<a href="https://msdn.microsoft.com/478e0c52-4324-4062-8e1e-381808b0f481">DxgkDdiQueryChildStatus</a>