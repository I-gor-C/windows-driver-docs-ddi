---
UID: NE:rilapitypes.RILINFOCLASS
title: RILINFOCLASS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilinfoclass_2.htm
old-project: netvista
ms.assetid: 19927cd1-8afa-4006-a882-d5222c690724
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: netvista.rilinfoclass_2, RIL_INFOCLASS_VOICE, rilapitypes/RIL_INFOCLASS_ALL, rilapitypes/RIL_INFOCLASS_PADACCESS, rilapitypes/RIL_INFOCLASS_DATACIRCUITSYNC, rilapitypes/RIL_INFOCLASS_DATA, rilapitypes/RIL_INFOCLASS_DATACIRCUITASYNC, RIL_INFOCLASS_FAX, RILINFOCLASS enumeration [Network Drivers Starting with Windows Vista], RIL_INFOCLASS_SMS, RIL_INFOCLASS_DATACIRCUITSYNC, rilapitypes/RIL_INFOCLASS_FAX, rilapitypes/RIL_INFOCLASS_VOICE, rilapitypes/RIL_INFOCLASS_PACKETACCESS, RIL_INFOCLASS_DATACIRCUITASYNC, rilapitypes/RILINFOCLASS, RILINFOCLASS, RIL_INFOCLASS_PACKETACCESS, RIL_INFOCLASS_ALL, RIL_INFOCLASS_PADACCESS, RIL_INFOCLASS_DATA, rilapitypes/RIL_INFOCLASS_SMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILINFOCLASS
product: Windows
targetos: Windows
req.typenames: RILINFOCLASS
req.product: Windows 10 or later.
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
| **Header** | rilapitypes.h |