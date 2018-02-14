---
UID: NE:rilapitypes.RILMSGDCSTYPE
title: RILMSGDCSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgdcstype_2.htm
old-project: netvista
ms.assetid: 5eabc972-f372-4d70-ab38-8830f7907a7a
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_DCSTYPE_MSGCLASS, RIL_DCSTYPE_MAX, rilapitypes/RIL_DCSTYPE_MSGCLASS, RIL_DCSTYPE_LANGUAGE, rilapitypes/RILMSGDCSTYPE, RIL_DCSTYPE_MSGWAIT, RILMSGDCSTYPE enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_DCSTYPE_MSGWAIT, rilapitypes/RIL_DCSTYPE_LANGUAGE, rilapitypes/RIL_DCSTYPE_MAX, netvista.rilmsgdcstype_2, RILMSGDCSTYPE
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
-	RILMSGDCSTYPE
product: Windows
targetos: Windows
req.typenames: RILMSGDCSTYPE
req.product: Windows 10 or later.
---

# RILMSGDCSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSTYPE { 
  RIL_DCSTYPE_MSGWAIT,
  RIL_DCSTYPE_MSGCLASS,
  RIL_DCSTYPE_LANGUAGE,
  RIL_DCSTYPE_MAX
} RILMSGDCSTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DCSTYPE_GENERAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSTYPE_LANGUAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSTYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSTYPE_MSGCLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DCSTYPE_MSGWAIT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |