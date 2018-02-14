---
UID: NE:rilapitypes.RILGETPREFERENCEDOPERATORLISTFORMAT
title: RILGETPREFERENCEDOPERATORLISTFORMAT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgetpreferencedoperatorlistformat_2.htm
old-project: netvista
ms.assetid: 1193174e-9247-4854-94d8-7404b2b15e5c
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_OPFORMAT_NUM, rilapitypes/RILGETPREFERENCEDOPERATORLISTFORMAT, rilapitypes/RIL_OPFORMAT_MAX, netvista.rilgetpreferencedoperatorlistformat_2, RIL_OPFORMAT_SHORT, RILGETPREFERENCEDOPERATORLISTFORMAT, RILGETPREFERENCEDOPERATORLISTFORMAT enumeration [Network Drivers Starting with Windows Vista], RIL_OPFORMAT_NUM, RIL_OPFORMAT_MAX, rilapitypes/RIL_OPFORMAT_SHORT
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
-	RILGETPREFERENCEDOPERATORLISTFORMAT
product: Windows
targetos: Windows
req.typenames: RILGETPREFERENCEDOPERATORLISTFORMAT
req.product: Windows 10 or later.
---

# RILGETPREFERENCEDOPERATORLISTFORMAT Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILGETPREFERENCEDOPERATORLISTFORMAT { 
  RIL_OPFORMAT_SHORT,
  RIL_OPFORMAT_NUM,
  RIL_OPFORMAT_MAX
} RILGETPREFERENCEDOPERATORLISTFORMAT;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_OPFORMAT_LONG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPFORMAT_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPFORMAT_NUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPFORMAT_SHORT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |