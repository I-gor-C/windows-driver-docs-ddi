---
UID: NE:rilapitypes.RILMSGDCSPARAMMASK
title: RILMSGDCSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsparammask.htm
old-project: netvista
ms.assetid: 2cd5afcd-1d69-475f-95ea-165a405d8ee8
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILMSGDCSPARAMMASK, RILMSGDCSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_MDCS_ALL, RIL_PARAM_MDCS_ALPHABET, RIL_PARAM_MDCS_FLAGS, RIL_PARAM_MDCS_INDICATION, RIL_PARAM_MDCS_LANGUAGE, RIL_PARAM_MDCS_MSGCLASS, netvista.rilmsgdcsparammask, ntddrilapitypes/RILMSGDCSPARAMMASK, ntddrilapitypes/RIL_PARAM_MDCS_ALL, ntddrilapitypes/RIL_PARAM_MDCS_ALPHABET, ntddrilapitypes/RIL_PARAM_MDCS_FLAGS, ntddrilapitypes/RIL_PARAM_MDCS_INDICATION, ntddrilapitypes/RIL_PARAM_MDCS_LANGUAGE, ntddrilapitypes/RIL_PARAM_MDCS_MSGCLASS
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
-	RILMSGDCSPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILMSGDCSPARAMMASK
req.product: Windows 10 or later.
---

# RILMSGDCSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILMSGDCSPARAMMASK {
  RIL_PARAM_MDCS_TYPE        ,
  RIL_PARAM_MDCS_FLAGS       ,
  RIL_PARAM_MDCS_MSGCLASS    ,
  RIL_PARAM_MDCS_ALPHABET    ,
  RIL_PARAM_MDCS_INDICATION  ,
  RIL_PARAM_MDCS_LANGUAGE    ,
  RIL_PARAM_MDCS_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_MDCS_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_MSGCLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_ALPHABET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_INDICATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_LANGUAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_MDCS_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |