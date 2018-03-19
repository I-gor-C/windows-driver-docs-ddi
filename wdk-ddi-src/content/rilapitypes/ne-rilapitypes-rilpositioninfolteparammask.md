---
UID: NE:rilapitypes.RILPOSITIONINFOLTEPARAMMASK
title: RILPOSITIONINFOLTEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfolteparammask_2.htm
old-project: netvista
ms.assetid: 9c71420f-8b85-4f31-9a08-7f363be75cc0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILPOSITIONINFOLTEPARAMMASK, RILPOSITIONINFOLTEPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_POSITION_LTE_ALL, RIL_PARAM_POSITION_LTE_CELLID, RIL_PARAM_POSITION_LTE_EARFCN, RIL_PARAM_POSITION_LTE_MNC, RIL_PARAM_POSITION_LTE_PHYSCELLID, RIL_PARAM_POSITION_LTE_RSRP, RIL_PARAM_POSITION_LTE_RSRQ, RIL_PARAM_POSITION_LTE_TA, RIL_PARAM_POSITION_LTE_TAC, netvista.rilpositioninfolteparammask_2, rilapitypes/RILPOSITIONINFOLTEPARAMMASK, rilapitypes/RIL_PARAM_POSITION_LTE_ALL, rilapitypes/RIL_PARAM_POSITION_LTE_CELLID, rilapitypes/RIL_PARAM_POSITION_LTE_EARFCN, rilapitypes/RIL_PARAM_POSITION_LTE_MNC, rilapitypes/RIL_PARAM_POSITION_LTE_PHYSCELLID, rilapitypes/RIL_PARAM_POSITION_LTE_RSRP, rilapitypes/RIL_PARAM_POSITION_LTE_RSRQ, rilapitypes/RIL_PARAM_POSITION_LTE_TA, rilapitypes/RIL_PARAM_POSITION_LTE_TAC
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
-	RILPOSITIONINFOLTEPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILPOSITIONINFOLTEPARAMMASK
req.product: Windows 10 or later.
---

# RILPOSITIONINFOLTEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPOSITIONINFOLTEPARAMMASK { 
  RIL_PARAM_POSITION_LTE_MNC,
  RIL_PARAM_POSITION_LTE_CELLID,
  RIL_PARAM_POSITION_LTE_EARFCN,
  RIL_PARAM_POSITION_LTE_PHYSCELLID,
  RIL_PARAM_POSITION_LTE_TAC,
  RIL_PARAM_POSITION_LTE_RSRP,
  RIL_PARAM_POSITION_LTE_RSRQ,
  RIL_PARAM_POSITION_LTE_TA,
  RIL_PARAM_POSITION_LTE_ALL
} RILPOSITIONINFOLTEPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_MCC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_MNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_CELLID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_EARFCN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_PHYSCELLID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_TAC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_RSRP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_RSRQ</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_TA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_LTE_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |