---
UID: NE:wditypes._WDI_POWER_SAVE_LEVEL
title: "_WDI_POWER_SAVE_LEVEL"
author: windows-driver-content
description: The WDI_POWER_SAVE_LEVEL enumeration defines the power save levels.
old-location: netvista\wdi_power_save_level.htm
old-project: netvista
ms.assetid: 3CB311C1-8FAE-44D5-896D-972F5DF1E88A
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: WDI_POWER_SAVE_LEVEL enumeration [Network Drivers Starting with Windows Vista], WDI_POWER_SAVE_LEVEL_FAST_PSP, wditypes/WDI_POWER_SAVE_LEVEL_FAST_PSP, wditypes/WDI_POWER_SAVE_LEVEL, WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE, netvista.wdi_power_save_level, netvista.wifi_power_save_level, wditypes/WDI_POWER_SAVE_LEVEL_MAX_PSP, WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL, wditypes/WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL, WDI_POWER_SAVE_LEVEL_MAX_PSP, wditypes/WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE, _WDI_POWER_SAVE_LEVEL, WDI_POWER_SAVE_LEVEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	wditypes.hpp
apiname:
-	WDI_POWER_SAVE_LEVEL
product: Windows
targetos: Windows
req.typenames: WDI_POWER_SAVE_LEVEL
req.product: Windows 10 or later.
---

# _WDI_POWER_SAVE_LEVEL Enumeration
The WDI_POWER_SAVE_LEVEL enumeration defines the power save levels.

## Syntax
````
typedef enum _WDI_POWER_SAVE_LEVEL { 
  WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE  = 0,
  WDI_POWER_SAVE_LEVEL_FAST_PSP       = 8,
  WDI_POWER_SAVE_LEVEL_MAX_PSP        = 16,
  WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL  = 24
} WDI_POWER_SAVE_LEVEL;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_POWER_SAVE_LEVEL_FAST_PSP</td>
                    <td>Fast PSP.</td>
                </tr>
            
                <tr>
                    <td>WDI_POWER_SAVE_LEVEL_MAX_PSP</td>
                    <td>Maximum PSP.</td>
                </tr>
            
                <tr>
                    <td>WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL</td>
                    <td>Maximum power saving level.</td>
                </tr>
            
                <tr>
                    <td>WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE</td>
                    <td>No power saving.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wditypes.hpp |