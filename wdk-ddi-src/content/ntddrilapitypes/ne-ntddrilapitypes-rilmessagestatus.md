---
UID: NE:ntddrilapitypes.RILMESSAGESTATUS
title: RILMESSAGESTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessagestatus.htm
old-project: netvista
ms.assetid: 8c111231-f94b-4e52-9887-59d07fe70937
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RILMESSAGESTATUS, RILMESSAGESTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_MSGSTATUS_MAX, RIL_MSGSTATUS_RECREAD, RIL_MSGSTATUS_RECUNREAD, RIL_MSGSTATUS_STOSENT, RIL_MSGSTATUS_STOUNSENT, netvista.rilmessagestatus, ntddrilapitypes/RILMESSAGESTATUS, ntddrilapitypes/RIL_MSGSTATUS_MAX, ntddrilapitypes/RIL_MSGSTATUS_RECREAD, ntddrilapitypes/RIL_MSGSTATUS_RECUNREAD, ntddrilapitypes/RIL_MSGSTATUS_STOSENT, ntddrilapitypes/RIL_MSGSTATUS_STOUNSENT
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
-	RILMESSAGESTATUS
product: Windows
targetos: Windows
req.typenames: RILMESSAGESTATUS
---

# RILMESSAGESTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMESSAGESTATUS { 
  RIL_MSGSTATUS_RECUNREAD,
  RIL_MSGSTATUS_RECREAD,
  RIL_MSGSTATUS_STOUNSENT,
  RIL_MSGSTATUS_STOSENT,
  RIL_MSGSTATUS_MAX
} RILMESSAGESTATUS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGSTATUS_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUS_RECREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUS_RECUNREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUS_STOSENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUS_STOUNSENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUS_UNKNOWN</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |