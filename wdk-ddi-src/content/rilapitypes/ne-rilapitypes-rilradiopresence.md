---
UID: NE:rilapitypes.RILRADIOPRESENCE
title: RILRADIOPRESENCE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiopresence_2.htm
old-project: netvista
ms.assetid: 0fd02d1a-e6c4-418d-b890-9b60f4f0c1ce
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RILRADIOPRESENCE, netvista.rilradiopresence_2, rilapitypes/RIL_RADIOPRESENCE_PRESENT, RIL_RADIOPRESENCE_MAX, RILRADIOPRESENCE, RIL_RADIOPRESENCE_PRESENT, rilapitypes/RIL_RADIOPRESENCE_MAX, RILRADIOPRESENCE enumeration [Network Drivers Starting with Windows Vista]
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
-	RILRADIOPRESENCE
product: Windows
targetos: Windows
req.typenames: RILRADIOPRESENCE
req.product: Windows 10 or later.
---

# RILRADIOPRESENCE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILRADIOPRESENCE { 
  RIL_RADIOPRESENCE_PRESENT,
  RIL_RADIOPRESENCE_MAX
} RILRADIOPRESENCE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_RADIOPRESENCE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOPRESENCE_NOTPRESENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_RADIOPRESENCE_PRESENT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |