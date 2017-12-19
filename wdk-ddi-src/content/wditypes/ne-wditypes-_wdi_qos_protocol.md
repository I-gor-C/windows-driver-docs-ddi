---
UID: NE.wditypes._WDI_QOS_PROTOCOL
title: _WDI_QOS_PROTOCOL
author: windows-driver-content
description: The WDI_QOS_PROTOCOL enumeration defines Wi-Fi QOS protocols.
old-location: netvista\wdi_qos_protocol.htm
old-project: NetVista
ms.assetid: 39466BF7-0517-4113-9C94-26D8691CCCC1
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WDI_QOS_PROTOCOL, WDI_QOS_PROTOCOL
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
req.alt-api: WDI_QOS_PROTOCOL
req.alt-loc: wditypes.hpp
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
req.product: Windows 10 or later.
---

# _WDI_QOS_PROTOCOL enumeration



## -description
The WDI_QOS_PROTOCOL enumeration defines Wi-Fi QOS protocols.



## -syntax

````
typedef enum _WDI_QOS_PROTOCOL { 
  WDI_QOS_PROTOCOL_NONE  = 0x00,
  WDI_QOS_PROTOCOL_WMM   = 0x01,
  WDI_QOS_PROTOCOL_11E   = 0x02
} WDI_QOS_PROTOCOL;
````


## -enum-fields

### -field WDI_QOS_PROTOCOL_NONE

None


### -field WDI_QOS_PROTOCOL_WMM

Wi-Fi Multimedia (WMM, formerly known as Wireless Multimedia Extensions)


### -field WDI_QOS_PROTOCOL_11E

802.11E


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>