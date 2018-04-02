---
UID: NE:dispmprt._DXGK_CHILD_STATUS_TYPE
title: "_DXGK_CHILD_STATUS_TYPE"
author: windows-driver-content
description: The DXGK_CHILD_STATUS_TYPE enumeration indicates the type of status being requested or reported for a child device of the display adapter.
old-location: display\dxgk_child_status_type.htm
old-project: display
ms.assetid: 5fa4b7e2-8215-49d8-9d70-b45c972b39b4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_CHILD_STATUS_TYPE, DXGK_CHILD_STATUS_TYPE, DXGK_CHILD_STATUS_TYPE enumeration [Display Devices], DmEnums_684c935e-6fd5-4743-a196-d6674b8f2e56.xml, PDXGK_CHILD_STATUS_TYPE, PDXGK_CHILD_STATUS_TYPE enumeration pointer [Display Devices], StatusConnection, StatusMiracast, StatusRotation, StatusUninitialized, _DXGK_CHILD_STATUS_TYPE, display.dxgk_child_status_type, dispmprt/DXGK_CHILD_STATUS_TYPE, dispmprt/PDXGK_CHILD_STATUS_TYPE, dispmprt/StatusConnection, dispmprt/StatusMiracast, dispmprt/StatusRotation, dispmprt/StatusUninitialized"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
-	DXGK_CHILD_STATUS_TYPE
product: Windows
targetos: Windows
req.typenames: DXGK_CHILD_STATUS_TYPE, *PDXGK_CHILD_STATUS_TYPE
---

# _DXGK_CHILD_STATUS_TYPE Enumeration
The DXGK_CHILD_STATUS_TYPE enumeration indicates the type of status being requested or reported for a child device of the display adapter.

## Syntax
```
typedef enum _DXGK_CHILD_STATUS_TYPE {
  StatusUninitialized       ,
  StatusConnection          ,
  StatusRotation            ,
  StatusMiracastConnection
} DXGK_CHILD_STATUS_TYPE, *PDXGK_CHILD_STATUS_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>StatusUninitialized</td>
                    <td>Indicates that a variable of type DXGK_CHILD_STATUS_TYPE has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>StatusConnection</td>
                    <td>Indicates that the request or report pertains to whether the child device has a monitor (or other display device) connected to it.</td>
                </tr>
            
                <tr>
                    <td>StatusRotation</td>
                    <td>Indicates that the request or report pertains to the rotation angle of the monitor (or other display device) that is connected to the child device.</td>
                </tr>
            
                <tr>
                    <td>StatusMiracastConnection</td>
                    <td></td>
                </tr>
</table>

## Remarks

The <b>Type</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561010">DXGK_CHILD_STATUS</a> structure is a member of the <b>DXGK_CHILD_STATUS_TYPE</b> enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/780a8867-bba1-4b1b-a941-b55bfe087b7b">DxgkCbIndicateChildStatus</a>



<a href="https://msdn.microsoft.com/478e0c52-4324-4062-8e1e-381808b0f481">DxgkDdiQueryChildStatus</a>