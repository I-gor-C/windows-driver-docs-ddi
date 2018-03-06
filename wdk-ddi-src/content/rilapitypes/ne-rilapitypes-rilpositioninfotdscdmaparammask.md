---
UID: NE:rilapitypes.RILPOSITIONINFOTDSCDMAPARAMMASK
title: RILPOSITIONINFOTDSCDMAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpositioninfotdscdmaparammask_2.htm
old-project: netvista
ms.assetid: c5609649-8e7b-4ec3-8feb-f363536068c6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILPOSITIONINFOTDSCDMAPARAMMASK, RILPOSITIONINFOTDSCDMAPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_POSITION_TDSCDMA_ALL, RIL_PARAM_POSITION_TDSCDMA_CELLID, RIL_PARAM_POSITION_TDSCDMA_CELLPARAM, RIL_PARAM_POSITION_TDSCDMA_LAC, RIL_PARAM_POSITION_TDSCDMA_MNC, RIL_PARAM_POSITION_TDSCDMA_PATHLOSS, RIL_PARAM_POSITION_TDSCDMA_RSCP, RIL_PARAM_POSITION_TDSCDMA_TA, RIL_PARAM_POSITION_TDSCDMA_UARFCN, netvista.rilpositioninfotdscdmaparammask_2, rilapitypes/RILPOSITIONINFOTDSCDMAPARAMMASK, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_ALL, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_CELLID, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_CELLPARAM, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_LAC, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_MNC, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_PATHLOSS, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_RSCP, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_TA, rilapitypes/RIL_PARAM_POSITION_TDSCDMA_UARFCN
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
-	RILPOSITIONINFOTDSCDMAPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILPOSITIONINFOTDSCDMAPARAMMASK
req.product: Windows 10 or later.
---

# RILPOSITIONINFOTDSCDMAPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPOSITIONINFOTDSCDMAPARAMMASK { 
  RIL_PARAM_POSITION_TDSCDMA_MNC,
  RIL_PARAM_POSITION_TDSCDMA_LAC,
  RIL_PARAM_POSITION_TDSCDMA_CELLID,
  RIL_PARAM_POSITION_TDSCDMA_UARFCN,
  RIL_PARAM_POSITION_TDSCDMA_CELLPARAM,
  RIL_PARAM_POSITION_TDSCDMA_TA,
  RIL_PARAM_POSITION_TDSCDMA_RSCP,
  RIL_PARAM_POSITION_TDSCDMA_PATHLOSS,
  RIL_PARAM_POSITION_TDSCDMA_ALL
} RILPOSITIONINFOTDSCDMAPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_CELLID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_CELLPARAM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_LAC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_MCC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_MNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_PATHLOSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_RSCP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_TA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_POSITION_TDSCDMA_UARFCN</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |