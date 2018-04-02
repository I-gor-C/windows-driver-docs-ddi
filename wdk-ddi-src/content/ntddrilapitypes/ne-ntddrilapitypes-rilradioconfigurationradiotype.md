---
UID: NE:ntddrilapitypes.RILRADIOCONFIGURATIONRADIOTYPE
title: RILRADIOCONFIGURATIONRADIOTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradioconfigurationradiotype.htm
old-project: netvista
ms.assetid: f4efebb4-0258-44f6-bdf0-ff61d3b13792
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILRADIOCONFIGURATIONRADIOTYPE, RILRADIOCONFIGURATIONRADIOTYPE enumeration [Network Drivers Starting with Windows Vista], RIL_RADIOTYPE_1XCSFB, RIL_RADIOTYPE_DUALACTIVE, RIL_RADIOTYPE_DUALSTANDBY, RIL_RADIOTYPE_MAX, RIL_RADIOTYPE_MULTIMODE, RIL_RADIOTYPE_SGLTE, RIL_RADIOTYPE_SGLTE_DUALACTIVE, RIL_RADIOTYPE_SINGLE, RIL_RADIOTYPE_SRLTE, RIL_RADIOTYPE_SVLTE, RIL_RADIOTYPE_SVLTE_DUALACTIVE, netvista.rilradioconfigurationradiotype, ntddrilapitypes/RILRADIOCONFIGURATIONRADIOTYPE, ntddrilapitypes/RIL_RADIOTYPE_1XCSFB, ntddrilapitypes/RIL_RADIOTYPE_DUALACTIVE, ntddrilapitypes/RIL_RADIOTYPE_DUALSTANDBY, ntddrilapitypes/RIL_RADIOTYPE_MAX, ntddrilapitypes/RIL_RADIOTYPE_MULTIMODE, ntddrilapitypes/RIL_RADIOTYPE_SGLTE, ntddrilapitypes/RIL_RADIOTYPE_SGLTE_DUALACTIVE, ntddrilapitypes/RIL_RADIOTYPE_SINGLE, ntddrilapitypes/RIL_RADIOTYPE_SRLTE, ntddrilapitypes/RIL_RADIOTYPE_SVLTE, ntddrilapitypes/RIL_RADIOTYPE_SVLTE_DUALACTIVE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
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
-	RILRADIOCONFIGURATIONRADIOTYPE
product: Windows
targetos: Windows
req.typenames: RILRADIOCONFIGURATIONRADIOTYPE
---

# RILRADIOCONFIGURATIONRADIOTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILRADIOCONFIGURATIONRADIOTYPE {
  RIL_RADIOTYPE_NONE              ,
  RIL_RADIOTYPE_SINGLE            ,
  RIL_RADIOTYPE_MULTIMODE         ,
  RIL_RADIOTYPE_1XCSFB            ,
  RIL_RADIOTYPE_SVLTE             ,
  RIL_RADIOTYPE_DUALSTANDBY       ,
  RIL_RADIOTYPE_DUALACTIVE        ,
  RIL_RADIOTYPE_SGLTE             ,
  RIL_RADIOTYPE_SVLTE_DUALACTIVE  ,
  RIL_RADIOTYPE_SGLTE_DUALACTIVE  ,
  RIL_RADIOTYPE_SRLTE             ,
  RIL_RADIOTYPE_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_RADIOTYPE_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SINGLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_MULTIMODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_1XCSFB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SVLTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_DUALSTANDBY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_DUALACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SGLTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SVLTE_DUALACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SGLTE_DUALACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_SRLTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOTYPE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |