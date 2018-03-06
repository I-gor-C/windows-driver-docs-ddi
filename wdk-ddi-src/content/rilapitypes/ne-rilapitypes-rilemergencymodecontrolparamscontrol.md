---
UID: NE:rilapitypes.RILEMERGENCYMODECONTROLPARAMSCONTROL
title: RILEMERGENCYMODECONTROLPARAMSCONTROL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilemergencymodecontrolparamscontrol_2.htm
old-project: netvista
ms.assetid: b169e3a3-141b-4bca-9eaa-ce55f7194e4f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILEMERGENCYMODECONTROLPARAMSCONTROL, RILEMERGENCYMODECONTROLPARAMSCONTROL enumeration [Network Drivers Starting with Windows Vista], RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE, RIL_EMC_MAX, RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE, netvista.rilemergencymodecontrolparamscontrol_2, rilapitypes/RILEMERGENCYMODECONTROLPARAMSCONTROL, rilapitypes/RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE, rilapitypes/RIL_EMC_MAX, rilapitypes/RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILEMERGENCYMODECONTROLPARAMSCONTROL
product: Windows
targetos: Windows
req.typenames: RILEMERGENCYMODECONTROLPARAMSCONTROL
req.product: Windows 10 or later.
---

# RILEMERGENCYMODECONTROLPARAMSCONTROL Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEMERGENCYMODECONTROLPARAMSCONTROL { 
  RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE,
  RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE,
  RIL_EMC_MAX
} RILEMERGENCYMODECONTROLPARAMSCONTROL;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EMC_EXIT_CDMA_ECBM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EMC_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |