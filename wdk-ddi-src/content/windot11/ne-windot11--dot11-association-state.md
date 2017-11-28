---
UID: NE.windot11._DOT11_ASSOCIATION_STATE
title: DOT11_ASSOCIATION_STATE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_association_state.htm
old-project: netvista
ms.assetid: 90d2457f-4246-464b-8de6-f8fda056eb7b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PRINTER_EVENT_ATTRIBUTES_INFO, PRINTER_EVENT_ATTRIBUTES_INFO, *PPRINTER_EVENT_ATTRIBUTES_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_ASSOCIATION_STATE
req.alt-loc: windot11.h
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_ASSOCIATION_STATE enumeration



## -description

## -syntax

````
typedef enum _DOT11_ASSOCIATION_STATE { 
  dot11_assoc_state_zero            = 0,
  dot11_assoc_state_unauth_unassoc  = 1,
  dot11_assoc_state_auth_unassoc    = 2,
  dot11_assoc_state_auth_assoc      = 3
} DOT11_ASSOCIATION_STATE, *PDOT11_ASSOCIATION_STATE;
````


## -enum-fields
<dl>

### -field <a id="dot11_assoc_state_zero"></a><a id="DOT11_ASSOC_STATE_ZERO"></a><b>dot11_assoc_state_zero</b>

<dd>
<p>The association state is undefined.</p>
</dd>

### -field <a id="dot11_assoc_state_unauth_unassoc"></a><a id="DOT11_ASSOC_STATE_UNAUTH_UNASSOC"></a><b>dot11_assoc_state_unauth_unassoc</b>

<dd>
<p>The 802.11 station is unauthenticated with the peer and is not associated.</p>
</dd>

### -field <a id="dot11_assoc_state_auth_unassoc"></a><a id="DOT11_ASSOC_STATE_AUTH_UNASSOC"></a><b>dot11_assoc_state_auth_unassoc</b>

<dd>
<p>The 802.11 station is authenticated with the peer but is not associated.</p>
</dd>

### -field <a id="dot11_assoc_state_auth_assoc"></a><a id="DOT11_ASSOC_STATE_AUTH_ASSOC"></a><b>dot11_assoc_state_auth_assoc</b>

<dd>
<p>The 802.11 station is authenticated and associated with the peer.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>