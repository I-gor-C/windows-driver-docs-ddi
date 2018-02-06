---
UID: NE:rilapitypes.RILSYSTEMSELECTIONPREFSMODE
title: RILSYSTEMSELECTIONPREFSMODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsystemselectionprefsmode_2.htm
old-project: netvista
ms.assetid: 10aa6bfb-5ada-42f6-8f89-d8d4066d196b
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILSYSTEMSELECTIONPREFSMODE, RIL_OPSELMODE_MAX, netvista.rilsystemselectionprefsmode_2, rilapitypes/RILSYSTEMSELECTIONPREFSMODE, rilapitypes/RIL_OPSELMODE_MANUAL, RILSYSTEMSELECTIONPREFSMODE enumeration [Network Drivers Starting with Windows Vista], RIL_OPSELMODE_MANUAL, rilapitypes/RIL_OPSELMODE_MAX
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
-	RILSYSTEMSELECTIONPREFSMODE
product: Windows
targetos: Windows
req.typenames: RILSYSTEMSELECTIONPREFSMODE
req.product: Windows 10 or later.
---

# RILSYSTEMSELECTIONPREFSMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSYSTEMSELECTIONPREFSMODE { 
  RIL_OPSELMODE_MANUAL,
  RIL_OPSELMODE_MAX
} RILSYSTEMSELECTIONPREFSMODE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_OPSELMODE_AUTOMATIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSELMODE_MANUAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSELMODE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |