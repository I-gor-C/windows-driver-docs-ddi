---
UID: NS.wlanihvtypes._DOT11EXT_IHV_PROFILE_PARAMS
title: DOT11EXT_IHV_PROFILE_PARAMS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_profile_params.htm
old-project: netvista
ms.assetid: 9bf4b27c-3cf0-45a0-9e56-b01ad1ba6b19
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11EXT_IHV_PROFILE_PARAMS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wlanihvtypes.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_IHV_PROFILE_PARAMS
req.alt-loc: wlanihvtypes.h
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

# DOT11EXT_IHV_PROFILE_PARAMS structure



## -description

## -syntax

````
typedef struct _DOT11EXT_IHV_PROFILE_PARAMS {
  PDOT11EXT_IHV_SSID_LIST    pSsidList;
  DOT11_BSS_TYPE             BssType;
  PDOT11_MSSECURITY_SETTINGS pMSSecuritySettings;
} DOT11EXT_IHV_PROFILE_PARAMS, *PDOT11EXT_IHV_PROFILE_PARAMS;
````


## -struct-fields
<dl>

### -field pSsidList

<dd>
<p>A pointer to the list of service set identifiers (SSIDs) of the basic service set (BSS) network.
     The 
     <b>pSsidList</b> member is formatted as a pointer to a 
     <a href="..\wlanihvtypes\ns-wlanihvtypes--dot11ext-ihv-ssid-list.md">
     DOT11EXT_IHV_SSID_LIST</a> structure.</p>
</dd>

### -field BssType

<dd>
<p>The type of the BSS network. The 
     <b>BssType</b> member contains a value defined for the 
     <a href="..\wlantypes\ne-wlantypes--dot11-bss-type.md">DOT11_BSS_TYPE</a> enumeration.</p>
</dd>

### -field pMSSecuritySettings

<dd>
<p>A pointer to a 
     <a href="..\wlanihvtypes\ns-wlanihvtypes--dot11-mssecurity-settings.md">
     DOT11_MSSECURITY_SETTINGS</a> structure that defines Microsoft security settings in the Microsoft
     802.1X implementation.</p>
</dd>
</dl>

## -remarks
<p>The operating system passes a pointer to a DOT11EXT_IHV_PROFILE_PARAMS structure as a parameter to any
    IHV handler function that processes the IHV-defined fragments of connectivity and security profiles. For
    more information, see 
    <a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
    Functions</a>.</p>

<p>Although the IHV handler function cannot access the entire network profile, the function can access
    the general attributes of the profile through the DOT11EXT_IHV_PROFILE_PARAMS structure.</p>

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
<dt>Wlanihvtypes.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlantypes\ne-wlantypes--dot11-bss-type.md">DOT11_BSS_TYPE</a>
</dt>
<dt>
<a href="..\wlanihvtypes\ns-wlanihvtypes--dot11-mssecurity-settings.md">DOT11_MSSECURITY_SETTINGS</a>
</dt>
<dt>
<a href="..\wlanihvtypes\ns-wlanihvtypes--dot11ext-ihv-ssid-list.md">DOT11EXT_IHV_SSID_LIST</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-create-discovery-profiles.md">
   Dot11ExtIhvCreateDiscoveryProfiles</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-capability-match.md">
   Dot11ExtIhvPerformCapabilityMatch</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-perform-pre-associate.md">
   Dot11ExtIhvPerformPreAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-validate-profile.md">Dot11ExtIhvValidateProfile</a>
</dt>
<dt>
<a href="netvista.idot11extuiproperty_dot11extuipropertygetdisplayinfo">
   IDot11ExtUIProperty::Dot11ExtUIPropertyGetDisplayInfo</a>
</dt>
<dt>
<a href="netvista.idot11extuiproperty_dot11extuipropertysetdisplayinfo">
   IDot11ExtUIProperty::Dot11ExtUIPropertySetDisplayInfo</a>
</dt>
<dt>
<a href="netvista.native_802_11_ihv_handler_functions">Native 802.11 IHV Handler
   Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXT_IHV_PROFILE_PARAMS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
