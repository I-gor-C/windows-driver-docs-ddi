---
UID: NE:ntddrilapitypes.RILLOCATIONINFOPARAMMASK
title: RILLOCATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rillocationinfoparammask.htm
old-project: netvista
ms.assetid: 3d681026-7ccb-4dcb-bed1-505c13089177
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILLOCATIONINFOPARAMMASK, RIL_PARAM_LU_ALL, ntddrilapitypes/RILLOCATIONINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_LU_HUICCAPP, RIL_PARAM_LU_LAC, RIL_PARAM_LU_HUICCAPP, ntddrilapitypes/RIL_PARAM_LU_CELLID, RILLOCATIONINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_LU_TAC, netvista.rillocationinfoparammask, ntddrilapitypes/RIL_PARAM_LU_LAC, RIL_PARAM_LU_CELLID, ntddrilapitypes/RIL_PARAM_LU_TAC, ntddrilapitypes/RIL_PARAM_LU_ALL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
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
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILLOCATIONINFOPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILLOCATIONINFOPARAMMASK
---

# RILLOCATIONINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILLOCATIONINFOPARAMMASK { 
  RIL_PARAM_LU_HUICCAPP,
  RIL_PARAM_LU_LAC,
  RIL_PARAM_LU_TAC,
  RIL_PARAM_LU_CELLID,
  RIL_PARAM_LU_ALL
} RILLOCATIONINFOPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_LU_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_LU_CELLID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_LU_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_LU_HUICCAPP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_LU_LAC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_LU_TAC</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |