---
UID: NE:wwan._WWAN_REGISTER_MODE
title: "_WWAN_REGISTER_MODE"
author: windows-driver-content
description: The WWAN_REGISTER_MODE enumeration lists the different network selection modes which defines the way the device should select a network while registering.
old-location: netvista\wwan_register_mode.htm
old-project: netvista
ms.assetid: 608d041c-1034-49cf-b8da-cb3f7769ac55
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PWWAN_REGISTER_MODE, PWWAN_REGISTER_MODE, PWWAN_REGISTER_MODE enumeration pointer [Network Drivers Starting with Windows Vista], WWAN_REGISTER_MODE, WWAN_REGISTER_MODE enumeration [Network Drivers Starting with Windows Vista], WwanRef_eac9611f-2097-43fc-96ea-ade56e77b7e7.xml, WwanRegisterModeAutomatic, WwanRegisterModeManual, WwanRegisterModeMax, WwanRegisterModeUnknown, _WWAN_REGISTER_MODE, netvista.wwan_register_mode, wwan/PWWAN_REGISTER_MODE, wwan/WWAN_REGISTER_MODE, wwan/WwanRegisterModeAutomatic, wwan/WwanRegisterModeManual, wwan/WwanRegisterModeMax, wwan/WwanRegisterModeUnknown"
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
-	WWAN_REGISTER_MODE
product: Windows
targetos: Windows
req.typenames: WWAN_REGISTER_MODE, *PWWAN_REGISTER_MODE
req.product: Windows 10 or later.
---

# _WWAN_REGISTER_MODE Enumeration
The WWAN_REGISTER_MODE enumeration lists the different network selection modes which defines the way
  the device should select a network while registering.

## Syntax
```
typedef enum _WWAN_REGISTER_MODE {
  WwanRegisterModeUnknown    ,
  WwanRegisterModeAutomatic  ,
  WwanRegisterModeManual     ,
  WwanRegisterModeMax
} *PWWAN_REGISTER_MODE, WWAN_REGISTER_MODE;
```

## Constants

<table>
            
                <tr>
                    <td>WwanRegisterModeUnknown</td>
                    <td>It is not specified how the device registers with network providers.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterModeAutomatic</td>
                    <td>Device automatically selects a network on which it should register.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterModeManual</td>
                    <td>Device registers to a pre-selected (manually selected) network.</td>
                </tr>
            
                <tr>
                    <td>WwanRegisterModeMax</td>
                    <td>The total number of supported registration modes.</td>
                </tr>
</table>

## Remarks

<b>WwanRegisterModeAutomatic</b> and 
    <b>WwanRegisterModeManual</b> are the only acceptable values. Miniport drivers can return 
    <b>WwanRegisterModeManual</b> in cases where it is not able to get this value from device.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff571231">WWAN_REGISTRATION_STATE</a>