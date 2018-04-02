---
UID: NE:nfccx._NFC_CX_HOST_ACTION
title: "_NFC_CX_HOST_ACTION"
author: windows-driver-content
description: The NFC_CX_HOST_ACTION enumeration specifies host actions.
old-location: nfpdrivers\nfc_cx_host_action.htm
old-project: nfpdrivers
ms.assetid: CE485A6F-8480-4535-9145-A8CBF78C804D
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PNFC_CX_HOST_ACTION, HostActionRestart, HostActionStart, HostActionStop, HostActionUnload, NFC_CX_HOST_ACTION, NFC_CX_HOST_ACTION enumeration [Near-Field Proximity Drivers], _NFC_CX_HOST_ACTION, nfccx/HostActionRestart, nfccx/HostActionStart, nfccx/HostActionStop, nfccx/HostActionUnload, nfccx/NFC_CX_HOST_ACTION, nfpdrivers.nfc_cx_host_action"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
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
req.irql: Requires same
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	nfccx.h
api_name:
-	NFC_CX_HOST_ACTION
product:
- Windows
targetos: Windows
req.typenames: NFC_CX_HOST_ACTION, *PNFC_CX_HOST_ACTION
---

# _NFC_CX_HOST_ACTION Enumeration
The NFC_CX_HOST_ACTION enumeration specifies host actions.

## Syntax
```
typedef enum _NFC_CX_HOST_ACTION {
  HostActionStart    ,
  HostActionStop     ,
  HostActionRestart  ,
  HostActionUnload
} NFC_CX_HOST_ACTION, *PNFC_CX_HOST_ACTION;
```

## Constants

<table>
            
                <tr>
                    <td>HostActionStart</td>
                    <td>Specifies full initialization.</td>
                </tr>
            
                <tr>
                    <td>HostActionStop</td>
                    <td>Specifies de-initialization.</td>
                </tr>
            
                <tr>
                    <td>HostActionRestart</td>
                    <td>Specifies a full driver restart.</td>
                </tr>
            
                <tr>
                    <td>HostActionUnload</td>
                    <td>Specifies to unload the driver.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | nfccx.h |

## See Also

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>



<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>