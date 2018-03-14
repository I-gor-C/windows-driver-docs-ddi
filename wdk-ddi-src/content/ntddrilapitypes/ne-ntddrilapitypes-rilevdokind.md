---
UID: NE:ntddrilapitypes.RILEVDOKIND
title: RILEVDOKIND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilevdokind.htm
old-project: netvista
ms.assetid: 9887342b-85bd-4161-b9de-06ceb56014e5
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILEVDOKIND, RILEVDOKIND enumeration [Network Drivers Starting with Windows Vista], RIL_EVDOKIND_MAX, RIL_EVDOKIND_REVA, RIL_EVDOKIND_REVB, netvista.rilevdokind, ntddrilapitypes/RILEVDOKIND, ntddrilapitypes/RIL_EVDOKIND_MAX, ntddrilapitypes/RIL_EVDOKIND_REVA, ntddrilapitypes/RIL_EVDOKIND_REVB
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
-	RILEVDOKIND
product: Windows
targetos: Windows
req.typenames: RILEVDOKIND
---

# RILEVDOKIND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEVDOKIND { 
  RIL_EVDOKIND_REVA,
  RIL_EVDOKIND_REVB,
  RIL_EVDOKIND_MAX
} RILEVDOKIND;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_EVDOKIND_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EVDOKIND_REV0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EVDOKIND_REVA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EVDOKIND_REVB</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |