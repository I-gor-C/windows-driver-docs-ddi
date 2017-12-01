---
UID: NS.wwan._WWAN_PROVIDER
title: WWAN_PROVIDER
author: windows-driver-content
description: The WWAN_PROVIDER structure represents details about a network provider.
old-location: netvista\wwan_provider.htm
old-project: netvista
ms.assetid: 2bca3123-3ac4-44fe-8d47-051314ef3cb7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_PROVIDER, WWAN_PROVIDER, *PWWAN_PROVIDER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PROVIDER
req.alt-loc: wwan.h
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

# WWAN_PROVIDER structure



## -description
<p>The WWAN_PROVIDER structure represents details about a network provider.</p>


## -syntax

````
typedef struct _WWAN_PROVIDER {
  WCHAR ProviderId[WWAN_PROVIDERID_LEN];
  ULONG ProviderState;
  WCHAR ProviderName[WWAN_PROVIDERNAME_LEN];
  ULONG WwanDataClass;
} WWAN_PROVIDER, *PWWAN_PROVIDER;
````


## -struct-fields
<dl>

### -field <b>ProviderId</b>

<dd>
<p>A NULL-terminated numeric (0-9) string that represents the network provider identity.
     </p>
<p>For GSM-based networks, this string is a concatenation of a three-digit Mobile Country Code (MCC) and
     a two or three-digit Mobile Network Code (MNC). GSM-based carriers may have more than one MNC, and hence
     more than one 
     <b>ProviderId</b> .</p>
<p>For CDMA-based networks, this string is a five-digit System ID (SID). Generally a CDMA-based carrier
     has more than one SID. Typically, the carrier has one SID for each market, which is usually divided
     geographically within a nation by regulations, such as Metropolitan Statistical Areas (MSA) in the
     United States of America. Miniport drivers of CDMA-based devices must specify
     WWAN_CDMA_DEFAULT_PROVIDER_ID if this information is not available.</p>
</dd>

### -field <b>ProviderState</b>

<dd>
<p>A value that represents the various states that the network provider's entry can be tagged with.
     The following table shows the possible values that miniport drivers should specify (one or more values
     can be specified).
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_HOME</p>
</td>
<td>
<p>The network provider is the home operator.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_FORBIDDEN</p>
</td>
<td>
<p>The network provider is on the forbidden list.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_PREFERRED</p>
</td>
<td>
<p>The network provider is on the preferred list.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_VISIBLE</p>
</td>
<td>
<p>The network provider is visible.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_REGISTERED</p>
</td>
<td>
<p>The network provider is currently registered by the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_UNKNOWN</p>
</td>
<td>
<p>The network provider state is unknown.</p>
</td>
</tr>
</table>
<p> </p>
<p>Some values in the previous table apply only to specific object identifiers (OIDs). The following
     table shows the associations between those values and related OIDs.</p>
<table>
<tr>
<th>Value</th>
<th>OID</th>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_HOME</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569826">OID_WWAN_HOME_PROVIDER</a>
</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_FORBIDDEN</p>
<p>WWAN_PROVIDER_STATE_PREFERRED</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a>
</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_PROVIDER_STATE_VISIBLE</p>
<p>WWAN_PROVIDER_STATE_REGISTERED</p>
<p>WWAN_PROVIDER_STATE_HOME</p>
<p>WWAN_PROVIDER_STATE_PREFERRED</p>
<p>WWAN_PROVIDER_STATE_FORBIDDEN</p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569843">OID_WWAN_VISIBLE_PROVIDERS</a>
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ProviderName</b>

<dd>
<p>A NULL-terminated string that represents the network provider's name. This member is limited to,
     at most, WWAN_PROVIDERNAME_LEN characters.
     </p>
<p>For GSM-based networks, if the Preferred Presentation of Country Initials and Mobile Network Name
     (PPCI&amp;N) is longer than WWAN_PROVIDERNAME_LEN characters, the miniport driver should abbreviate the
     network name.</p>
<p>This member is ignored when the MB Service sets the preferred provider list.</p>
<p>Miniport drivers should specify a <b>NULL</b> string for devices that do not have this
     information.</p>
</dd>

### -field <b>WwanDataClass</b>

<dd>
<p>A bitmap that represents the data-class(es) that the device supports. For a detailed list of
     values, see the 
     <b>WwanDataClass</b> member of 
     <a href="..\wwan\ns-wwan--wwan-device-caps.md">WWAN_DEVICE_CAPS</a>.
     </p>
<p>This member can be ignored when queried for OID_WWAN_HOME_PROVIDER.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-home-provider.md">NDIS_WWAN_HOME_PROVIDER</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-preferred-providers.md">NDIS_WWAN_PREFERRED_PROVIDERS</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-visible-providers.md">NDIS_WWAN_VISIBLE_PROVIDERS</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-device-caps.md">WWAN_DEVICE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PROVIDER structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
