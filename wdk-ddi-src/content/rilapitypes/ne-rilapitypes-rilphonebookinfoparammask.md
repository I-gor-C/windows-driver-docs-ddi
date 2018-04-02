---
UID: NE:rilapitypes.RILPHONEBOOKINFOPARAMMASK
title: RILPHONEBOOKINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookinfoparammask.htm
old-project: netvista
ms.assetid: 1aab5008-eb27-4f48-9d87-74959f932883
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILPHONEBOOKINFOPARAMMASK, RILPHONEBOOKINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_PBI_ADDRESSLENGTH, RIL_PARAM_PBI_ALL, RIL_PARAM_PBI_MAXAASTEXTLENGTH, RIL_PARAM_PBI_MAXANR, RIL_PARAM_PBI_MAXANRLENGTH, RIL_PARAM_PBI_MAXEMAILLENGTH, RIL_PARAM_PBI_MAXEMAILS, RIL_PARAM_PBI_MAXGASLENGTH, RIL_PARAM_PBI_MAXGROUPS, RIL_PARAM_PBI_MAXSNELENGTH, RIL_PARAM_PBI_TEXTLENGTH, RIL_PARAM_PBI_TOTAL, RIL_PARAM_PBI_TOTALAAS, RIL_PARAM_PBI_TOTALGAS, RIL_PARAM_PBI_USEDAAS, RIL_PARAM_PBI_USEDGAS, netvista.rilphonebookinfoparammask, ntddrilapitypes/RILPHONEBOOKINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_PBI_ADDRESSLENGTH, ntddrilapitypes/RIL_PARAM_PBI_ALL, ntddrilapitypes/RIL_PARAM_PBI_MAXAASTEXTLENGTH, ntddrilapitypes/RIL_PARAM_PBI_MAXANR, ntddrilapitypes/RIL_PARAM_PBI_MAXANRLENGTH, ntddrilapitypes/RIL_PARAM_PBI_MAXEMAILLENGTH, ntddrilapitypes/RIL_PARAM_PBI_MAXEMAILS, ntddrilapitypes/RIL_PARAM_PBI_MAXGASLENGTH, ntddrilapitypes/RIL_PARAM_PBI_MAXGROUPS, ntddrilapitypes/RIL_PARAM_PBI_MAXSNELENGTH, ntddrilapitypes/RIL_PARAM_PBI_TEXTLENGTH, ntddrilapitypes/RIL_PARAM_PBI_TOTAL, ntddrilapitypes/RIL_PARAM_PBI_TOTALAAS, ntddrilapitypes/RIL_PARAM_PBI_TOTALGAS, ntddrilapitypes/RIL_PARAM_PBI_USEDAAS, ntddrilapitypes/RIL_PARAM_PBI_USEDGAS
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
-	RILPHONEBOOKINFOPARAMMASK
product:
- Windows
targetos: Windows
req.typenames: RILPHONEBOOKINFOPARAMMASK
req.product: Windows 10 or later.
---

# RILPHONEBOOKINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILPHONEBOOKINFOPARAMMASK {
  RIL_PARAM_PBI_USED              ,
  RIL_PARAM_PBI_TOTAL             ,
  RIL_PARAM_PBI_ADDRESSLENGTH     ,
  RIL_PARAM_PBI_TEXTLENGTH        ,
  RIL_PARAM_PBI_MAXANR            ,
  RIL_PARAM_PBI_MAXANRLENGTH      ,
  RIL_PARAM_PBI_MAXAASTEXTLENGTH  ,
  RIL_PARAM_PBI_USEDAAS           ,
  RIL_PARAM_PBI_TOTALAAS          ,
  RIL_PARAM_PBI_MAXEMAILS         ,
  RIL_PARAM_PBI_MAXEMAILLENGTH    ,
  RIL_PARAM_PBI_MAXGROUPS         ,
  RIL_PARAM_PBI_MAXGASLENGTH      ,
  RIL_PARAM_PBI_USEDGAS           ,
  RIL_PARAM_PBI_TOTALGAS          ,
  RIL_PARAM_PBI_MAXSNELENGTH      ,
  RIL_PARAM_PBI_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_PBI_USED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_TOTAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_ADDRESSLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_TEXTLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXANR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXANRLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXAASTEXTLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_USEDAAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_TOTALAAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXEMAILS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXEMAILLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXGROUPS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXGASLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_USEDGAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_TOTALGAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_MAXSNELENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PBI_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |