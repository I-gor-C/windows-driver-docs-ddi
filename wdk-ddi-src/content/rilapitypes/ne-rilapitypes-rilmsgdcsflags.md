---
UID: NE:rilapitypes.RILMSGDCSFLAGS
title: RILMSGDCSFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcsflags_2.htm
old-project: netvista
ms.assetid: 1bb5a365-1f8f-41d4-a3f5-6a4a7238de03
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILMSGDCSFLAGS, RILMSGDCSFLAGS enumeration [Network Drivers Starting with Windows Vista], RIL_DCSFLAG_ALL, RIL_DCSFLAG_COMPRESSED, RIL_DCSFLAG_DISCARD, RIL_DCSFLAG_INDICATIONACTIVE, netvista.rilmsgdcsflags_2, rilapitypes/RILMSGDCSFLAGS, rilapitypes/RIL_DCSFLAG_ALL, rilapitypes/RIL_DCSFLAG_COMPRESSED, rilapitypes/RIL_DCSFLAG_DISCARD, rilapitypes/RIL_DCSFLAG_INDICATIONACTIVE
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILMSGDCSFLAGS
product: Windows
targetos: Windows
req.typenames: RILMSGDCSFLAGS
req.product: Windows 10 or later.
---

# RILMSGDCSFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSFLAGS { 
  RIL_DCSFLAG_COMPRESSED,
  RIL_DCSFLAG_INDICATIONACTIVE,
  RIL_DCSFLAG_DISCARD,
  RIL_DCSFLAG_ALL
} RILMSGDCSFLAGS;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DCSFLAG_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSFLAG_COMPRESSED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSFLAG_DISCARD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSFLAG_INDICATIONACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSFLAG_NONE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |