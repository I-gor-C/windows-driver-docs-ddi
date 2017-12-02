---
UID: NC.wlanihv.DOT11EXTIHV_CREATE_DISCOVERY_PROFILES
title: DOT11EXTIHV_CREATE_DISCOVERY_PROFILES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11extihvcreatediscoveryprofiles.htm
old-project: netvista
ms.assetid: e741bfa7-eb97-4f94-beb4-545d7bedcea8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wlanihv.h
req.include-header: Wlanihv.h, Winclient.h, L2cmn.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Dot11ExtIhvCreateDiscoveryProfiles
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

# DOT11EXTIHV_CREATE_DISCOVERY_PROFILES callback



## -description

## -prototype

````
DOT11EXTIHV_CREATE_DISCOVERY_PROFILES Dot11ExtIhvCreateDiscoveryProfiles;

DWORD APIENTRY Dot11ExtIhvCreateDiscoveryProfiles(
  _In_opt_ HANDLE                               hIhvExtAdapter,
  _In_     BOOL                                 bInsecure,
  _In_opt_ PDOT11EXT_IHV_PROFILE_PARAMS         pIhvProfileParams,
  _In_opt_ PDOT11_BSS_LIST                      pConnectableBssid,
  _Out_    PDOT11EXT_IHV_DISCOVERY_PROFILE_LIST pIhvDiscoveryProfileList,
  _Out_    PDWORD                               pdwReasonCode
)
{ ... }
````


## -parameters
<dl>

### -param hIhvExtAdapter [in, optional]

<dd>
<p>The handle used by the IHV Extensions DLL to reference the wireless LAN (WLAN) adapter. This
     handle value was specified through a previous call to the 
     <a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a> IHV
     Handler function.</p>
</dd>

### -param bInsecure [in]

<dd>
<p>A Boolean value that specifies the security status of the discovery profiles. If set to <b>TRUE</b>, the
     IHV Extensions DLL can only return secure profiles, such as profiles which involve user
     authentication.</p>
</dd>

### -param pIhvProfileParams [in, optional]

<dd>
<p>A pointer to a 
     <a href="..\wlanihvtypes\ns-wlanihvtypes--dot11ext-ihv-profile-params.md">
     DOT11EXT_IHV_PROFILE_PARAMS</a> structure. This structure defines the attributes of the basic service
     set (BSS) network to which the profile extensions will be applied.</p>
</dd>

### -param pConnectableBssid [in, optional]

<dd>
<p>A pointer to a 
     <a href="..\wlclient\ns-wlclient--dot11-bss-list.md">DOT11_BSS_LIST</a> structure, which contains one
     or more 802.11 Beacon or Probe Response frames received from a BSS network. This list is derived from
     the results of the last scan operation performed by the WLAN adapter. For more information about the
     scan operation, see 
     <a href="netvista.native_802_11_scan_operations">Native 802.11 Scan Operations</a>.
     </p>
<div class="alert"><b>Note</b>  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic
     service set (BSS) networks.</div>
<div> </div>
</dd>

### -param pIhvDiscoveryProfileList [out]

<dd>
<p>A pointer to a 
     <a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-discovery-profile-list.md">
     DOT11EXT_IHV_DISCOVERY_PROFILE_LIST</a> structure that specifies a list of IHV discovery
     profiles.</p>
</dd>

### -param pdwReasonCode [out]

<dd>
<p>A pointer to a DWORD value, which provides additional information for the return value of the 
     <i>Dot11ExtIhvCreateDiscoveryProfiles</i> function. The IHV Extensions DLL must set *
     <i>pdwReasonCode</i> to an L2_REASON_CODE_xxxx value, which are defined in 
     L2cmn.h.</p>
</dd>
</dl>

## -returns
<p>If the call succeeds, the function returns ERROR_SUCCESS. Otherwise, it returns an error code
     defined in 
     Winerror.h.</p>

## -remarks
<p>After the WLAN adapter completes a scan operation, the operating system might call 
    <i>Dot11ExtIhvCreateDiscoveryProfiles</i> to create temporary profile fragments that could be used to
    connect to a BSS network for which a network profile has not been created by the user.</p>

<p>When 
    <i>Dot11ExtIhvCreateDiscoveryProfiles</i> is called, the IHV Extensions DLL must follow these
    guidelines.</p>

<p>If the IHV Extensions DLL can return profile fragments that can be used to connect to the BSS
      network, the 
      <i>Dot11ExtIhvCreateDiscoveryProfiles</i> function must return ERROR_SUCCESS. Otherwise, the function
      must return an appropriate error code from the ERROR_xxxx values defined in 
      Winerror.h.</p>

<p>The IHV Extensions DLL provides more information regarding the return result of the 
      <i>Dot11ExtIhvCreateDiscoveryProfiles</i> function. The DLL must set *
      <i>pdwReasonCode</i> to one of the following:</p>

<p>L2_REASON_CODE_SUCCESS, if profile fragments can be returned for the list of BSS networks.</p>

<p>An appropriate L2_REASON_CODE_xxxx error value, if the profile fragments cannot be returned for
        the list of BSS networks.</p>

<p>An IHV-defined value in the range from L2_REASON_CODE_IHV_BASE to (L2_REASON_CODE_IHV_BASE+
        L2_REASON_CODE_GROUP_SIZE-1), regardless of whether profile fragments are returned.</p>

<p>For more information about creating discovery profiles, see 
    <a href="netvista.creating_network_profile_extensions">Creating Network Profile
    Extensions</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<dt>Wlanihv.h (include Wlanihv.h, Winclient.h, or L2cmn.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wlclient\ns-wlclient--dot11-bss-list.md">DOT11_BSS_LIST</a>
</dt>
<dt>
<a href="..\wlanihv\ns-wlanihv--dot11ext-ihv-discovery-profile-list.md">
   DOT11EXT_IHV_DISCOVERY_PROFILE_LIST</a>
</dt>
<dt>
<a href="..\wlanihvtypes\ns-wlanihvtypes--dot11ext-ihv-profile-params.md">DOT11EXT_IHV_PROFILE_PARAMS</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-allocate-buffer.md">Dot11ExtAllocateBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-free-buffer.md">Dot11ExtFreeBuffer</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-init-adapter.md">Dot11ExtIhvInitAdapter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11EXTIHV_CREATE_DISCOVERY_PROFILES callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
