---
UID: NE:ucmtypes._UCM_PD_CONN_STATE
title: "_UCM_PD_CONN_STATE"
author: windows-driver-content
description: Defines power delivery (PD) negotiation states of a Type-C port.
old-location: buses\ucm_pd_conn_state.htm
old-project: usbref
ms.assetid: 7D146DDF-58A5-40C2-BF21-AF785DC7DB18
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UCM_PD_CONN_STATE, UCM_PD_CONN_STATE enumeration [Buses], UcmPdConnStateInvalid, UcmPdConnStateNegotiationFailed, UcmPdConnStateNegotiationSucceeded, UcmPdConnStateNotSupported, _UCM_PD_CONN_STATE, buses.ucm_pd_conn_state, ucmtypes/UCM_PD_CONN_STATE, ucmtypes/UcmPdConnStateInvalid, ucmtypes/UcmPdConnStateNegotiationFailed, ucmtypes/UcmPdConnStateNegotiationSucceeded, ucmtypes/UcmPdConnStateNotSupported
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ucmtypes.h
api_name:
-	UCM_PD_CONN_STATE
product:
- Windows
targetos: Windows
req.typenames: UCM_PD_CONN_STATE
req.product: Windows 10 or later.
---

# _UCM_PD_CONN_STATE Enumeration
Defines power delivery (PD) negotiation states of a Type-C port.

## Syntax
```
typedef enum _UCM_PD_CONN_STATE {
  UcmPdConnStateInvalid               ,
  UcmPdConnStateNotSupported          ,
  UcmPdConnStateNegotiationFailed     ,
  UcmPdConnStateNegotiationSucceeded
} UCM_PD_CONN_STATE;
```

## Constants

<table>
            
                <tr>
                    <td>UcmPdConnStateInvalid</td>
                    <td>Indicates the PD negotiation state is invalid.</td>
                </tr>
            
                <tr>
                    <td>UcmPdConnStateNotSupported</td>
                    <td>Indicates a PD connection is not supported.</td>
                </tr>
            
                <tr>
                    <td>UcmPdConnStateNegotiationFailed</td>
                    <td>Indicates the PD negotiation failed.</td>
                </tr>
            
                <tr>
                    <td>UcmPdConnStateNegotiationSucceeded</td>
                    <td>Indicates the PD negotiation succeeded.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187911">UcmConnectorPdConnectionStateChanged</a>