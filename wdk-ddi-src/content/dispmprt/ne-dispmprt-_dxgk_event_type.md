---
UID: NE:dispmprt._DXGK_EVENT_TYPE
title: "_DXGK_EVENT_TYPE"
author: windows-driver-content
description: The DXGK_EVENT_TYPE enumeration indicates the event type in a call to the display miniport driver's DxgkDdiNotifyAcpiEvent function.
old-location: display\dxgk_event_type.htm
old-project: display
ms.assetid: df28ae8f-01f7-42c5-99df-2a3fc7401173
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_EVENT_TYPE, DXGK_EVENT_TYPE, DXGK_EVENT_TYPE enumeration [Display Devices], DmEnums_94bee105-be3f-4268-982e-be8581bb9bc0.xml, DxgkAcpiEvent, DxgkDockingEvent, DxgkPowerStateEvent, DxgkUndefinedEvent, IN_DXGK_EVENT_TYPE, PDXGK_EVENT_TYPE, PDXGK_EVENT_TYPE enumeration pointer [Display Devices], _DXGK_EVENT_TYPE, display.dxgk_event_type, dispmprt/DXGK_EVENT_TYPE, dispmprt/DxgkAcpiEvent, dispmprt/DxgkDockingEvent, dispmprt/DxgkPowerStateEvent, dispmprt/DxgkUndefinedEvent, dispmprt/PDXGK_EVENT_TYPE"
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
-	DXGK_EVENT_TYPE
product:
- Windows
targetos: Windows
req.typenames: DXGK_EVENT_TYPE, *PDXGK_EVENT_TYPE
---

# _DXGK_EVENT_TYPE Enumeration
The DXGK_EVENT_TYPE enumeration indicates the event type in a call to the display miniport driver's <a href="https://msdn.microsoft.com/fdefde51-0e90-4324-9c14-e8259fc872b3">DxgkDdiNotifyAcpiEvent</a> function.

## Syntax
```
typedef enum _DXGK_EVENT_TYPE {
  DxgkUndefinedEvent    ,
  DxgkAcpiEvent         ,
  DxgkPowerStateEvent   ,
  DxgkDockingEvent      ,
  DxgkChainedAcpiEvent
} *PDXGK_EVENT_TYPE, DXGK_EVENT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>DxgkUndefinedEvent</td>
                    <td>Indicates that a variable of type DXGK_EVENT_TYPE has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>DxgkAcpiEvent</td>
                    <td>Indicates that the event is an ACPI event.</td>
                </tr>
            
                <tr>
                    <td>DxgkPowerStateEvent</td>
                    <td>Indicates that the event is a power state event.</td>
                </tr>
            
                <tr>
                    <td>DxgkDockingEvent</td>
                    <td>Indicates that the event is a docking event.</td>
                </tr>
            
                <tr>
                    <td>DxgkChainedAcpiEvent</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | dispmprt.h (include Dispmprt.h) |

## See Also

<a href="https://msdn.microsoft.com/fdefde51-0e90-4324-9c14-e8259fc872b3">DxgkDdiNotifyAcpiEvent</a>