---
UID: NE:rilapitypes.RILMSGCDMAMSGDISPLAYMODE
title: RILMSGCDMAMSGDISPLAYMODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgdisplaymode_2.htm
old-project: netvista
ms.assetid: 6ec37cf6-0d07-445b-9a5b-8d560069c612
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILMSGCDMAMSGDISPLAYMODE enumeration [Network Drivers Starting with Windows Vista], RIL_MSGDISPLAYMODE_MOBILEDEFAULT, RIL_MSGDISPLAYMODE_USERDEFAULT, RIL_MSGDISPLAYMODE_MAX, netvista.rilmsgcdmamsgdisplaymode_2, rilapitypes/RILMSGCDMAMSGDISPLAYMODE, rilapitypes/RIL_MSGDISPLAYMODE_MAX, RILMSGCDMAMSGDISPLAYMODE, rilapitypes/RIL_MSGDISPLAYMODE_USERDEFAULT, rilapitypes/RIL_MSGDISPLAYMODE_MOBILEDEFAULT
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
-	RILMSGCDMAMSGDISPLAYMODE
product: Windows
targetos: Windows
req.typenames: RILMSGCDMAMSGDISPLAYMODE
req.product: Windows 10 or later.
---

# RILMSGCDMAMSGDISPLAYMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMAMSGDISPLAYMODE { 
  RIL_MSGDISPLAYMODE_MOBILEDEFAULT,
  RIL_MSGDISPLAYMODE_USERDEFAULT,
  RIL_MSGDISPLAYMODE_MAX
} RILMSGCDMAMSGDISPLAYMODE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGDISPLAYMODE_IMMEDIATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDISPLAYMODE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDISPLAYMODE_MOBILEDEFAULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGDISPLAYMODE_USERDEFAULT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |