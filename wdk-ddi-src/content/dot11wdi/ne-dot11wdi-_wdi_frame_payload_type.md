---
UID: NE:dot11wdi._WDI_FRAME_PAYLOAD_TYPE
title: "_WDI_FRAME_PAYLOAD_TYPE"
author: windows-driver-content
description: The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.
old-location: netvista\wdi_frame_payload_type.htm
old-project: netvista
ms.assetid: 28aef1bd-915a-4f05-a4b0-bec63ddfdfb5
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: WDI_FRAME_PAYLOAD_TYPE, WDI_FRAME_PAYLOAD_TYPE enumeration [Network Drivers Starting with Windows Vista], dot11wdi/WDI_FRAME_MSDU, WDI_FRAME_MSDU_FRAGMENT, _WDI_FRAME_PAYLOAD_TYPE, dot11wdi/WDI_FRAME_MSDU_FRAGMENT, netvista.wifi_frame_payload_type, netvista.wdi_frame_payload_type, WDI_FRAME_MSDU, dot11wdi/WDI_FRAME_PAYLOAD_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	dot11wdi.h
apiname:
-	WDI_FRAME_PAYLOAD_TYPE
product: Windows
targetos: Windows
req.typenames: WDI_FRAME_PAYLOAD_TYPE
---

# _WDI_FRAME_PAYLOAD_TYPE Enumeration
The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.

## Syntax
````
typedef enum _WDI_FRAME_PAYLOAD_TYPE { 
  WDI_FRAME_MSDU           = 0,
  WDI_FRAME_MSDU_FRAGMENT  = 1
} WDI_FRAME_PAYLOAD_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>WDI_FRAME_MSDU</td>
                    <td>MAC service data unit (MSDU).</td>
                </tr>
            
                <tr>
                    <td>WDI_FRAME_MSDU_FRAGMENT</td>
                    <td>MAC service data unit (MSDU) fragment.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | dot11wdi.h |