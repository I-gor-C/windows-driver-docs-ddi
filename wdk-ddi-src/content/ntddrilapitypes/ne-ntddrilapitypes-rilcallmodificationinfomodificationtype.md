---
UID: NE:ntddrilapitypes.RILCALLMODIFICATIONINFOMODIFICATIONTYPE
title: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfomodificationtype.htm
old-project: netvista
ms.assetid: 37b18047-7818-4e57-b25a-3c958106e215
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: ntddrilapitypes/RIL_CALLMODIFICATIONTYPE_BLOCKED, RIL_CALLMODIFICATIONTYPE_MODIFIED, ntddrilapitypes/RIL_CALLMODIFICATIONTYPE_MODIFIED, ntddrilapitypes/RILCALLMODIFICATIONINFOMODIFICATIONTYPE, netvista.rilcallmodificationinfomodificationtype, RIL_CALLMODIFICATIONTYPE_BLOCKED, ntddrilapitypes/RIL_CALLMODIFICATIONTYPE_MAX, RILCALLMODIFICATIONINFOMODIFICATIONTYPE, RIL_CALLMODIFICATIONTYPE_MAX, RILCALLMODIFICATIONINFOMODIFICATIONTYPE enumeration [Network Drivers Starting with Windows Vista]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILCALLMODIFICATIONINFOMODIFICATIONTYPE
product: Windows
targetos: Windows
req.typenames: RILCALLMODIFICATIONINFOMODIFICATIONTYPE
---

# RILCALLMODIFICATIONINFOMODIFICATIONTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMODIFICATIONINFOMODIFICATIONTYPE { 
  RIL_CALLMODIFICATIONTYPE_BLOCKED,
  RIL_CALLMODIFICATIONTYPE_MODIFIED,
  RIL_CALLMODIFICATIONTYPE_MAX
} RILCALLMODIFICATIONINFOMODIFICATIONTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_CALLMODIFICATIONTYPE_BLOCKED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMODIFICATIONTYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMODIFICATIONTYPE_MODIFIED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLMODIFICATIONTYPE_UNKNOWN</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |