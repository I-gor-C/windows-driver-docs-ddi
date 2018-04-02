---
UID: NE:rilapitypes.RILMSGACKSTATUS
title: RILMSGACKSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgackstatus.htm
old-project: netvista
ms.assetid: 551193d0-596c-40bf-9a31-f8b6eb330e25
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILMSGACKSTATUS, RILMSGACKSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_MSGACKSTATUS_ERROR, RIL_MSGACKSTATUS_FAIL_MEM_FULL, RIL_MSGACKSTATUS_MAX, netvista.rilmsgackstatus, ntddrilapitypes/RILMSGACKSTATUS, ntddrilapitypes/RIL_MSGACKSTATUS_ERROR, ntddrilapitypes/RIL_MSGACKSTATUS_FAIL_MEM_FULL, ntddrilapitypes/RIL_MSGACKSTATUS_MAX
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
-	RILMSGACKSTATUS
product: Windows
targetos: Windows
req.typenames: RILMSGACKSTATUS
req.product: Windows 10 or later.
---

# RILMSGACKSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILMSGACKSTATUS {
  RIL_MSGACKSTATUS_STORED         ,
  RIL_MSGACKSTATUS_FAIL_MEM_FULL  ,
  RIL_MSGACKSTATUS_ERROR          ,
  RIL_MSGACKSTATUS_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGACKSTATUS_STORED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGACKSTATUS_FAIL_MEM_FULL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGACKSTATUS_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGACKSTATUS_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |