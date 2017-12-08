---
UID: NS.wlanihv._DOT11EXT_IHV_DISCOVERY_PROFILE
title: DOT11EXT_IHV_DISCOVERY_PROFILE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_discovery_profile.htm
old-project: netvista
ms.assetid: 9044d045-a997-4660-815d-07dad0ac832e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11EXT_IHV_DISCOVERY_PROFILE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_IHV_DISCOVERY_PROFILE
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

# DOT11EXT_IHV_DISCOVERY_PROFILE structure



## -description

## -syntax

````
typedef struct _DOT11EXT_IHV_DISCOVERY_PROFILE {
  DOT11EXT_IHV_CONNECTIVITY_PROFILE IhvConnectivityProfile;
  DOT11EXT_IHV_SECURITY_PROFILE     IhvSecurityProfile;
} DOT11EXT_IHV_DISCOVERY_PROFILE, *PDOT11EXT_IHV_DISCOVERY_PROFILE;
````


## -struct-fields
<dl>

### -field IhvConnectivityProfile

<dd>
<p>The IHV connectivity profile specified by a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-connectivity-profile.md">
     DOT11EXT_IHV_CONNECTIVITY_PROFILE</a> structure.</p>
</dd>

### -field IhvSecurityProfile

<dd>
<p>The IHV security profile specified by a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-security-profile.md">
     DOT11EXT_IHV_SECURITY_PROFILE</a> structure.</p>
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

## -see-also
<dl>
<dt>
<a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-connectivity-profile.md">
   DOT11EXT_IHV_CONNECTIVITY_PROFILE</a>
</dt>
<dt>
<a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-security-profile.md">DOT11EXT_IHV_SECURITY_PROFILE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_IHV_DISCOVERY_PROFILE structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
