---
UID: NE:rilapitypes.RILUICCSLOTINFOPARAMMASK
title: RILUICCSLOTINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccslotinfoparammask.htm
old-project: netvista
ms.assetid: f99fc76e-a569-4a7e-9f8d-3f604ccfa6a3
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILUICCSLOTINFOPARAMMASK, RILUICCSLOTINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_SLOTINFO_ALL, RIL_PARAM_SLOTINFO_SLOTSTATE, netvista.riluiccslotinfoparammask, ntddrilapitypes/RILUICCSLOTINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_SLOTINFO_ALL, ntddrilapitypes/RIL_PARAM_SLOTINFO_SLOTSTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: Rilapitypes.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILUICCSLOTINFOPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILUICCSLOTINFOPARAMMASK
req.product: Windows 10 or later.
---

# RILUICCSLOTINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILUICCSLOTINFOPARAMMASK {
  RIL_PARAM_SLOTINFO_NUMSLOTS   ,
  RIL_PARAM_SLOTINFO_SLOTSTATE  ,
  RIL_PARAM_SLOTINFO_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_SLOTINFO_NUMSLOTS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SLOTINFO_SLOTSTATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SLOTINFO_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |