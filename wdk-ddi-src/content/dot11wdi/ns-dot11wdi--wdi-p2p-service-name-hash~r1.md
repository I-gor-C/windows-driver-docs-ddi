---
UID: NS.dot11wdi._WDI_P2P_SERVICE_NAME_HASH~r1
title: WDI_P2P_SERVICE_NAME_HASH
author: windows-driver-content
description: The WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name.
old-location: netvista\wdi_p2p_service_name_hash.htm
old-project: netvista
ms.assetid: B03C779A-ED25-48D7-BB5E-EB95ED1B2D00
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_P2P_SERVICE_NAME_HASH,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_P2P_SERVICE_NAME_HASH
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# WDI_P2P_SERVICE_NAME_HASH structure



## -description
<p>The 
  WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name.</p>


## -syntax

````
typedef struct _WDI_P2P_SERVICE_NAME_HASH {
  UINT8 Hash[6];
} WDI_P2P_SERVICE_NAME_HASH, *PWDI_P2P_SERVICE_NAME_HASH;
````


## -struct-fields
<dl>

### -field <b>Hash</b>

<dd>
<p>Hash of a WFDS Service Name.</p>
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