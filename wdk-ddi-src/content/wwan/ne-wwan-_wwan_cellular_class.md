---
UID: NE:wwan._WWAN_CELLULAR_CLASS
title: "_WWAN_CELLULAR_CLASS"
author: windows-driver-content
description: The WWAN_CELLULAR_CLASS enumeration lists the different classes of cellular technology that are supported by the MB device.
old-location: netvista\wwan_cellular_class.htm
old-project: netvista
ms.assetid: c49f40b8-feb4-4dfd-9a2b-c800f3b5343a
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_CELLULAR_CLASS, PWWAN_CELLULAR_CLASS, PWWAN_CELLULAR_CLASS enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_CELLULAR_CLASS, WWAN_CELLULAR_CLASS enumeration [Network Drivers Starting with Windows Vista], WwanCellularClassCdma, WwanCellularClassGsm, WwanCellularClassMax, WwanCellularClassUnknown, WwanRef_cbffbef4-6a05-4042-abf0-7495fadf869d.xml, _WWAN_CELLULAR_CLASS, netvista.wwan_cellular_class, wwan/PWWAN_CELLULAR_CLASS, wwan/WWAN_CELLULAR_CLASS, wwan/WwanCellularClassCdma, wwan/WwanCellularClassGsm, wwan/WwanCellularClassMax, wwan/WwanCellularClassUnknown"
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
-	WWAN_CELLULAR_CLASS
product: Windows
targetos: Windows
req.typenames: WWAN_CELLULAR_CLASS, *PWWAN_CELLULAR_CLASS
req.product: Windows 10 or later.
---

# _WWAN_CELLULAR_CLASS Enumeration
The WWAN_CELLULAR_CLASS enumeration lists the different classes of cellular technology that are
  supported by the MB device.

## Syntax
```
typedef enum _WWAN_CELLULAR_CLASS {
  WwanCellularClassUnknown  ,
  WwanCellularClassGsm      ,
  WwanCellularClassCdma     ,
  WwanCellularClassMax
} *PWWAN_CELLULAR_CLASS, WWAN_CELLULAR_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>WwanCellularClassUnknown</td>
                    <td>The device uses an unknown cellular technology.</td>
                </tr>
            
                <tr>
                    <td>WwanCellularClassGsm</td>
                    <td>The device uses GSM-based technology.</td>
                </tr>
            
                <tr>
                    <td>WwanCellularClassCdma</td>
                    <td>The device uses CDMA-based technology.</td>
                </tr>
            
                <tr>
                    <td>WwanCellularClassMax</td>
                    <td>The total number of supported cellular classes.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571204">WWAN_DEVICE_CAPS</a>