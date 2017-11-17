---
UID: NE.dot11wdi._WDI_FRAME_PAYLOAD_TYPE
title: WDI_FRAME_PAYLOAD_TYPE
author: windows-driver-content
description: The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.
old-location: netvista\wdi_frame_payload_type.htm
ms.assetid: 28aef1bd-915a-4f05-a4b0-bec63ddfdfb5
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_FRAME_PAYLOAD_TYPE
req.alt-loc: dot11wdi.h
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
ms.keywords: SYNTHVOICEPRIORITY_INSTANCE, SYNTHVOICEPRIORITY_INSTANCE, *PSYNTHVOICEPRIORITY_INSTANCE
req.iface: ISynthSinkDMus
---

# WDI_FRAME_PAYLOAD_TYPE enumeration



## -description
<p>The WDI_FRAME_PAYLOAD_TYPE enumeration defines the frame payload type.</p>


## -syntax

````
typedef enum _WDI_FRAME_PAYLOAD_TYPE { 
  WDI_FRAME_MSDU           = 0,
  WDI_FRAME_MSDU_FRAGMENT  = 1
} WDI_FRAME_PAYLOAD_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_FRAME_MSDU"></a><a id="wdi_frame_msdu"></a><b>WDI_FRAME_MSDU</b>

<dd>
<p>MAC service data unit (MSDU).</p>
</dd>

### -field <a id="WDI_FRAME_MSDU_FRAGMENT"></a><a id="wdi_frame_msdu_fragment"></a><b>WDI_FRAME_MSDU_FRAGMENT</b>

<dd>
<p>MAC service data unit (MSDU) fragment.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>