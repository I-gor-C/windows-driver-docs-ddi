---
UID: NE:ntddrilapitypes.RILOPERATORINFOSTATUS
title: RILOPERATORINFOSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatorinfostatus.htm
old-project: netvista
ms.assetid: 372d84da-600f-44db-ac76-b59ceac7321d
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILOPERATORINFOSTATUS, RILOPERATORINFOSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_OPSTATUS_AVAILABLE, RIL_OPSTATUS_CURRENT, RIL_OPSTATUS_FORBIDDEN, RIL_OPSTATUS_MAX, netvista.riloperatorinfostatus, ntddrilapitypes/RILOPERATORINFOSTATUS, ntddrilapitypes/RIL_OPSTATUS_AVAILABLE, ntddrilapitypes/RIL_OPSTATUS_CURRENT, ntddrilapitypes/RIL_OPSTATUS_FORBIDDEN, ntddrilapitypes/RIL_OPSTATUS_MAX
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
-	RILOPERATORINFOSTATUS
product: Windows
targetos: Windows
req.typenames: RILOPERATORINFOSTATUS
---

# RILOPERATORINFOSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILOPERATORINFOSTATUS { 
  RIL_OPSTATUS_AVAILABLE,
  RIL_OPSTATUS_CURRENT,
  RIL_OPSTATUS_FORBIDDEN,
  RIL_OPSTATUS_MAX
} RILOPERATORINFOSTATUS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_OPSTATUS_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSTATUS_AVAILABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSTATUS_CURRENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSTATUS_FORBIDDEN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSTATUS_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |