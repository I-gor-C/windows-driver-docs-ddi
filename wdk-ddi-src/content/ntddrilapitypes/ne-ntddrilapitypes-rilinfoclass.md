---
UID: NE:ntddrilapitypes.RILINFOCLASS
title: RILINFOCLASS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilinfoclass.htm
old-project: netvista
ms.assetid: 2e4bd8bd-ce7e-4eb4-ac0d-68fb8890eb26
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILINFOCLASS, RILINFOCLASS enumeration [Network Drivers Starting with Windows Vista], RIL_INFOCLASS_ALL, RIL_INFOCLASS_DATA, RIL_INFOCLASS_DATACIRCUITASYNC, RIL_INFOCLASS_DATACIRCUITSYNC, RIL_INFOCLASS_FAX, RIL_INFOCLASS_PACKETACCESS, RIL_INFOCLASS_PADACCESS, RIL_INFOCLASS_SMS, RIL_INFOCLASS_VOICE, netvista.rilinfoclass, ntddrilapitypes/RILINFOCLASS, ntddrilapitypes/RIL_INFOCLASS_ALL, ntddrilapitypes/RIL_INFOCLASS_DATA, ntddrilapitypes/RIL_INFOCLASS_DATACIRCUITASYNC, ntddrilapitypes/RIL_INFOCLASS_DATACIRCUITSYNC, ntddrilapitypes/RIL_INFOCLASS_FAX, ntddrilapitypes/RIL_INFOCLASS_PACKETACCESS, ntddrilapitypes/RIL_INFOCLASS_PADACCESS, ntddrilapitypes/RIL_INFOCLASS_SMS, ntddrilapitypes/RIL_INFOCLASS_VOICE
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
-	RILINFOCLASS
product: Windows
targetos: Windows
req.typenames: RILINFOCLASS
---

# RILINFOCLASS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILINFOCLASS { 
  RIL_INFOCLASS_VOICE,
  RIL_INFOCLASS_DATA,
  RIL_INFOCLASS_FAX,
  RIL_INFOCLASS_SMS,
  RIL_INFOCLASS_DATACIRCUITSYNC,
  RIL_INFOCLASS_DATACIRCUITASYNC,
  RIL_INFOCLASS_PACKETACCESS,
  RIL_INFOCLASS_PADACCESS,
  RIL_INFOCLASS_ALL
} RILINFOCLASS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_INFOCLASS_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_DATACIRCUITASYNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_DATACIRCUITSYNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_FAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_PACKETACCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_PADACCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_SMS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_INFOCLASS_VOICE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |