---
UID: NS.wlanihv._DOT11EXT_IHV_CONNECTIVITY_PROFILE
title: DOT11EXT_IHV_CONNECTIVITY_PROFILE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_connectivity_profile.htm
old-project: netvista
ms.assetid: 56ef9b59-5dbb-4720-bae1-7af6d9dbc110
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11EXT_IHV_CONNECTIVITY_PROFILE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_IHV_CONNECTIVITY_PROFILE
req.alt-loc: wlanihv.h
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

# DOT11EXT_IHV_CONNECTIVITY_PROFILE structure



## -description

## -syntax

````
typedef struct _DOT11EXT_IHV_CONNECTIVITY_PROFILE {
  LPWSTR pszXmlFragmentIhvConnectivity;
} DOT11EXT_IHV_CONNECTIVITY_PROFILE, *PDOT11EXT_IHV_CONNECTIVITY_PROFILE;
````


## -struct-fields
<dl>

### -field <b>pszXmlFragmentIhvConnectivity</b>

<dd>
<p>A pointer to the string that defines the IHV connectivity profile.</p>
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
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>