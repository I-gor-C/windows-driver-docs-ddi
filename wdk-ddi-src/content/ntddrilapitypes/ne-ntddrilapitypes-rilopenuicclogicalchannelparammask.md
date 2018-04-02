---
UID: NE:ntddrilapitypes.RILOPENUICCLOGICALCHANNELPARAMMASK
title: RILOPENUICCLOGICALCHANNELPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilopenuicclogicalchannelparammask.htm
old-project: netvista
ms.assetid: 28512a46-506b-40c2-a14d-165823bf94fb
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILOPENUICCLOGICALCHANNELPARAMMASK, RILOPENUICCLOGICALCHANNELPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_OULC_ALL, RIL_PARAM_OULC_SELECTRESPLENGTH, RIL_PARAM_OULC_SELECTRESPONSE, netvista.rilopenuicclogicalchannelparammask, ntddrilapitypes/RILOPENUICCLOGICALCHANNELPARAMMASK, ntddrilapitypes/RIL_PARAM_OULC_ALL, ntddrilapitypes/RIL_PARAM_OULC_SELECTRESPLENGTH, ntddrilapitypes/RIL_PARAM_OULC_SELECTRESPONSE
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
-	RILOPENUICCLOGICALCHANNELPARAMMASK
product:
- Windows
targetos: Windows
req.typenames: RILOPENUICCLOGICALCHANNELPARAMMASK
---

# RILOPENUICCLOGICALCHANNELPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILOPENUICCLOGICALCHANNELPARAMMASK {
  RIL_PARAM_OULC_CHANNELID         ,
  RIL_PARAM_OULC_SELECTRESPLENGTH  ,
  RIL_PARAM_OULC_SELECTRESPONSE    ,
  RIL_PARAM_OULC_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_OULC_CHANNELID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_OULC_SELECTRESPLENGTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_OULC_SELECTRESPONSE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_OULC_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |