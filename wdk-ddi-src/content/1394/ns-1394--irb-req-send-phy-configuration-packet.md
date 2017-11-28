---
UID: NS.1394._IRB_REQ_SEND_PHY_CONFIGURATION_PACKET
title: IRB_REQ_SEND_PHY_CONFIGURATION_PACKET
author: windows-driver-content
description: This structure contains the fields necessary to carry out a SendPhyConfigurationPacket request.
old-location: ieee\irb_req_send_phy_configuration_packet.htm
old-project: IEEE
ms.assetid: FCB87010-EA7D-495F-B58A-6E0322F9C846
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_SEND_PHY_CONFIGURATION_PACKET, IRB_REQ_SEND_PHY_CONFIGURATION_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_SEND_PHY_CONFIGURATION_PACKET
req.alt-loc: 1394.h
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
---

# IRB_REQ_SEND_PHY_CONFIGURATION_PACKET structure



## -description
<p>This structure contains the fields necessary to carry out a SendPhyConfigurationPacket request.</p>


## -syntax

````
typedef struct _IRB_REQ_SEND_PHY_CONFIGURATION_PACKET {
  PHY_CONFIGURATION_PACKET PhyConfigurationPacket;
} IRB_REQ_SEND_PHY_CONFIGURATION_PACKET;
````


## -struct-fields
<dl>

### -field <b>PhyConfigurationPacket</b>

<dd>
<p>Points to the PHY_CONFIGURATION_PACKET structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>