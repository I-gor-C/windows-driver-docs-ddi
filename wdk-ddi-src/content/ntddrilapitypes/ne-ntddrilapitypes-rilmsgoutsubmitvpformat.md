---
UID: NE:ntddrilapitypes.RILMSGOUTSUBMITVPFORMAT
title: RILMSGOUTSUBMITVPFORMAT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgoutsubmitvpformat.htm
old-project: netvista
ms.assetid: c0a2646c-aa0a-4946-999f-a78d1c488752
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: netvista.rilmsgoutsubmitvpformat, ntddrilapitypes/RIL_MSGVP_MAX, RILMSGOUTSUBMITVPFORMAT enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_MSGVP_RELATIVE, ntddrilapitypes/RIL_MSGVP_ABSOLUTE, ntddrilapitypes/RIL_MSGVP_ENHANCED, RIL_MSGVP_ABSOLUTE, ntddrilapitypes/RILMSGOUTSUBMITVPFORMAT, RILMSGOUTSUBMITVPFORMAT, RIL_MSGVP_ENHANCED, RIL_MSGVP_RELATIVE, RIL_MSGVP_MAX
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
-	RILMSGOUTSUBMITVPFORMAT
product: Windows
targetos: Windows
req.typenames: RILMSGOUTSUBMITVPFORMAT
---

# RILMSGOUTSUBMITVPFORMAT Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGOUTSUBMITVPFORMAT { 
  RIL_MSGVP_RELATIVE,
  RIL_MSGVP_ENHANCED,
  RIL_MSGVP_ABSOLUTE,
  RIL_MSGVP_MAX
} RILMSGOUTSUBMITVPFORMAT;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGVP_ABSOLUTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGVP_ENHANCED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGVP_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGVP_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGVP_RELATIVE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |