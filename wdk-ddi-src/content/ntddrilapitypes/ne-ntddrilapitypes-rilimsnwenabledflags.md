---
UID: NE:ntddrilapitypes.RILIMSNWENABLEDFLAGS
title: RILIMSNWENABLEDFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsnwenabledflags.htm
old-project: netvista
ms.assetid: ae13790a-2442-4a8e-88cb-2cb6c8e02da6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILIMSNWENABLEDFLAGS, RILIMSNWENABLEDFLAGS enumeration [Network Drivers Starting with Windows Vista], RIL_IMS_NW_ENABLED_FLAG_ALL, RIL_IMS_NW_ENABLED_FLAG_EAB, RIL_IMS_NW_ENABLED_FLAG_PROVISION, RIL_IMS_NW_ENABLED_FLAG_VIDEO, RIL_IMS_NW_ENABLED_FLAG_VOICE, netvista.rilimsnwenabledflags, ntddrilapitypes/RILIMSNWENABLEDFLAGS, ntddrilapitypes/RIL_IMS_NW_ENABLED_FLAG_ALL, ntddrilapitypes/RIL_IMS_NW_ENABLED_FLAG_EAB, ntddrilapitypes/RIL_IMS_NW_ENABLED_FLAG_PROVISION, ntddrilapitypes/RIL_IMS_NW_ENABLED_FLAG_VIDEO, ntddrilapitypes/RIL_IMS_NW_ENABLED_FLAG_VOICE
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILIMSNWENABLEDFLAGS
product: Windows
targetos: Windows
req.typenames: RILIMSNWENABLEDFLAGS
---

# RILIMSNWENABLEDFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSNWENABLEDFLAGS { 
  RIL_IMS_NW_ENABLED_FLAG_PROVISION,
  RIL_IMS_NW_ENABLED_FLAG_VOICE,
  RIL_IMS_NW_ENABLED_FLAG_VIDEO,
  RIL_IMS_NW_ENABLED_FLAG_EAB,
  RIL_IMS_NW_ENABLED_FLAG_ALL
} RILIMSNWENABLEDFLAGS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_EAB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_PROVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_VIDEO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMS_NW_ENABLED_FLAG_VOICE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |