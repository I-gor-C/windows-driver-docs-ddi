---
UID: NE:wwan._WWAN_SIM_CLASS
title: "_WWAN_SIM_CLASS"
author: windows-driver-content
description: The WWAN_SIM_CLASS enumeration lists the different types of Subscriber Identity Modules (SIMs) that are supported by the MB device.
old-location: netvista\wwan_sim_class.htm
old-project: netvista
ms.assetid: 4d66874b-bb1d-43e5-a4b2-525face7de81
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_SIM_CLASS, PWWAN_SIM_CLASS, PWWAN_SIM_CLASS enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_SIM_CLASS, WWAN_SIM_CLASS enumeration [Network Drivers Starting with Windows Vista], WwanRef_8c5184eb-4ac5-40a7-bb52-875554517f70.xml, WwanSimClassMax, WwanSimClassSimLogical, WwanSimClassSimRemote, WwanSimClassSimRemovable, WwanSimClassUnknown, _WWAN_SIM_CLASS, netvista.wwan_sim_class, wwan/PWWAN_SIM_CLASS, wwan/WWAN_SIM_CLASS, wwan/WwanSimClassMax, wwan/WwanSimClassSimLogical, wwan/WwanSimClassSimRemote, wwan/WwanSimClassSimRemovable, wwan/WwanSimClassUnknown"
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
-	WWAN_SIM_CLASS
product:
- Windows
targetos: Windows
req.typenames: WWAN_SIM_CLASS, *PWWAN_SIM_CLASS
req.product: Windows 10 or later.
---

# _WWAN_SIM_CLASS Enumeration
The WWAN_SIM_CLASS enumeration lists the different types of Subscriber Identity Modules (SIMs) that
  are supported by the MB device.

## Syntax
```
typedef enum _WWAN_SIM_CLASS {
  WwanSimClassUnknown       ,
  WwanSimClassSimLogical    ,
  WwanSimClassSimRemovable  ,
  WwanSimClassSimRemote     ,
  WwanSimClassMax
} *PWWAN_SIM_CLASS, WWAN_SIM_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>WwanSimClassUnknown</td>
                    <td>The device supports an unknown class of SIM.</td>
                </tr>
            
                <tr>
                    <td>WwanSimClassSimLogical</td>
                    <td>The device supports a logical or embedded SIM.</td>
                </tr>
            
                <tr>
                    <td>WwanSimClassSimRemovable</td>
                    <td>The device supports a removable SIM.</td>
                </tr>
            
                <tr>
                    <td>WwanSimClassSimRemote</td>
                    <td>The device supports a remote SIM that is not physically attached to MB device. For example, a
     tethered cellular telephone modem.</td>
                </tr>
            
                <tr>
                    <td>WwanSimClassMax</td>
                    <td>The total number of supported SIM classes.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>