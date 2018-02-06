---
UID: NE:rilapitypes.RILIMSSIPREASON
title: RILIMSSIPREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssipreason_2.htm
old-project: netvista
ms.assetid: 45cee356-e05e-4f3a-bccf-4d95a64587d4
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE, rilapitypes/RIL_IMSSIPREASON_MAX, netvista.rilimssipreason_2, RIL_IMSSIPREASON_MAX, RILIMSSIPREASON, RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE, rilapitypes/RILIMSSIPREASON, RILIMSSIPREASON enumeration [Network Drivers Starting with Windows Vista]
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
-	RILIMSSIPREASON
product: Windows
targetos: Windows
req.typenames: RILIMSSIPREASON
req.product: Windows 10 or later.
---

# RILIMSSIPREASON Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSSIPREASON { 
  RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE,
  RIL_IMSSIPREASON_MAX
} RILIMSSIPREASON;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_IMSSIPREASON_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMSSIPREASON_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |