---
UID: NS.DOT11WDI._WDI_P2P_SERVICE_NAME_HASH
title: _WDI_P2P_SERVICE_NAME_HASH
author: windows-driver-content
description: The WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name.
old-location: netvista\wdi_p2p_service_name_hash.htm
old-project: NetVista
ms.assetid: B03C779A-ED25-48D7-BB5E-EB95ED1B2D00
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WDI_P2P_SERVICE_NAME_HASH, PWDI_P2P_SERVICE_NAME_HASH, WDI_P2P_SERVICE_NAME_HASH, *PWDI_P2P_SERVICE_NAME_HASH
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
---

# _WDI_P2P_SERVICE_NAME_HASH structure



## -description
The 
  WDI_P2P_SERVICE_NAME_HASH structure defines a hash of a WFDS Service Name.



## -syntax

````
typedef struct _WDI_P2P_SERVICE_NAME_HASH {
  UINT8 Hash[6];
} WDI_P2P_SERVICE_NAME_HASH, *PWDI_P2P_SERVICE_NAME_HASH;
````


## -struct-fields

### -field Hash

Hash of a WFDS Service Name.


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
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>