---
UID: NE:wditypes._WDI_QOS_PROTOCOL
title: "_WDI_QOS_PROTOCOL"
author: windows-driver-content
description: The WDI_QOS_PROTOCOL enumeration defines Wi-Fi QOS protocols.
old-location: netvista\wdi_qos_protocol.htm
old-project: netvista
ms.assetid: 39466BF7-0517-4113-9C94-26D8691CCCC1
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: WDI_QOS_PROTOCOL, WDI_QOS_PROTOCOL enumeration [Device and Driver Installation], WDI_QOS_PROTOCOL_11E, WDI_QOS_PROTOCOL_NONE, WDI_QOS_PROTOCOL_WMM, _WDI_QOS_PROTOCOL, netvista.wdi_qos_protocol, netvista.wifi_qos_protocol, wditypes/WDI_QOS_PROTOCOL, wditypes/WDI_QOS_PROTOCOL_11E, wditypes/WDI_QOS_PROTOCOL_NONE, wditypes/WDI_QOS_PROTOCOL_WMM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wditypes.hpp
api_name:
-	WDI_QOS_PROTOCOL
product:
- Windows
targetos: Windows
req.typenames: WDI_QOS_PROTOCOL
req.product: Windows 10 or later.
---

# _WDI_QOS_PROTOCOL Enumeration
The WDI_QOS_PROTOCOL enumeration defines Wi-Fi QOS protocols.

## Syntax
```
typedef enum _WDI_QOS_PROTOCOL {
  WDI_QOS_PROTOCOL_NONE  ,
  WDI_QOS_PROTOCOL_WMM   ,
  WDI_QOS_PROTOCOL_11E   ,
  WDI_QOS_PROTOCOL_MAX
} WDI_QOS_PROTOCOL;
```

## Constants

<table>
            
                <tr>
                    <td>WDI_QOS_PROTOCOL_NONE</td>
                    <td>None</td>
                </tr>
            
                <tr>
                    <td>WDI_QOS_PROTOCOL_WMM</td>
                    <td>Wi-Fi Multimedia (WMM, formerly known as Wireless Multimedia Extensions)</td>
                </tr>
            
                <tr>
                    <td>WDI_QOS_PROTOCOL_11E</td>
                    <td>802.11E</td>
                </tr>
            
                <tr>
                    <td>WDI_QOS_PROTOCOL_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | wditypes.hpp |