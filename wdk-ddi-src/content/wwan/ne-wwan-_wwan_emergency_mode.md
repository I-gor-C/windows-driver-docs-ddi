---
UID: NE:wwan._WWAN_EMERGENCY_MODE
title: "_WWAN_EMERGENCY_MODE"
author: windows-driver-content
description: The WWAN_EMERGENCY_MODE enumeration lists the different types of emergency modes that are supported by the MB device.
old-location: netvista\wwan_emergency_mode.htm
old-project: netvista
ms.assetid: d901e763-5e1c-443d-ba9c-9d1e4413bd47
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_EMERGENCY_MODE, PWWAN_EMERGENCY_MODE, PWWAN_EMERGENCY_MODE enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_EMERGENCY_MODE, WWAN_EMERGENCY_MODE enumeration [Network Drivers Starting with Windows Vista], WwanEmergencyModeMax, WwanEmergencyModeOff, WwanEmergencyModeOn, WwanRef_8b2029ff-7d10-4f36-a4c0-6b41f464b726.xml, _WWAN_EMERGENCY_MODE, netvista.wwan_emergency_mode, wwan/PWWAN_EMERGENCY_MODE, wwan/WWAN_EMERGENCY_MODE, wwan/WwanEmergencyModeMax, wwan/WwanEmergencyModeOff, wwan/WwanEmergencyModeOn"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_EMERGENCY_MODE
product: Windows
targetos: Windows
req.typenames: WWAN_EMERGENCY_MODE, *PWWAN_EMERGENCY_MODE
req.product: Windows 10 or later.
---

# _WWAN_EMERGENCY_MODE Enumeration
The WWAN_EMERGENCY_MODE enumeration lists the different types of emergency modes that are supported
  by the MB device.

## Syntax
```
typedef enum _WWAN_EMERGENCY_MODE {
  WwanEmergencyModeOff  ,
  WwanEmergencyModeOn   ,
  WwanEmergencyModeMax
} WWAN_EMERGENCY_MODE, *PWWAN_EMERGENCY_MODE;
```

## Constants

<table>
            
                <tr>
                    <td>WwanEmergencyModeOff</td>
                    <td>The device is in normal mode.</td>
                </tr>
            
                <tr>
                    <td>WwanEmergencyModeOn</td>
                    <td>The device is in emergency mode. An example of an emergency mode function is a call to 911.</td>
                </tr>
            
                <tr>
                    <td>WwanEmergencyModeMax</td>
                    <td>The total number of supported emergency modes.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571226">WWAN_READY_INFO</a>