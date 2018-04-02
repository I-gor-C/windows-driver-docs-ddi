---
UID: NE:ucxendpoint._ENDPOINT_RESET_FLAGS
title: "_ENDPOINT_RESET_FLAGS"
author: windows-driver-content
description: Defines parameters for a request to reset an endpoint.
old-location: buses\endpoint_reset_flags.htm
old-project: usbref
ms.assetid: 3775836D-DC1E-47B4-8186-2AC329825FCE
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: ENDPOINT_RESET_FLAGS, ENDPOINT_RESET_FLAGS enumeration [Buses], FlagEndpointResetPreserveTransferState, _ENDPOINT_RESET_FLAGS, buses.endpoint_reset_flags, ucxendpoint/ENDPOINT_RESET_FLAGS, ucxendpoint/FlagEndpointResetPreserveTransferState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
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
req.irql: DISPATCH_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucxendpoint.h
api_name:
-	ENDPOINT_RESET_FLAGS
product:
- Windows
targetos: Windows
req.typenames: ENDPOINT_RESET_FLAGS
req.product: Windows 10 or later.
---

# _ENDPOINT_RESET_FLAGS Enumeration
Defines parameters for a request to reset an endpoint.

## Syntax
```
typedef enum _ENDPOINT_RESET_FLAGS {
  FlagEndpointResetPreserveTransferState
} ENDPOINT_RESET_FLAGS;
```

## Constants

<table>
            
                <tr>
                    <td>FlagEndpointResetPreserveTransferState</td>
                    <td>The transfer state must be preserved after the endpoint reset operation is complete.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxendpoint.h (include Ucxclass.h, Ucxendpoint.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188021">ENDPOINT_RESET</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt187828">EVT_UCX_ENDPOINT_RESET</a>