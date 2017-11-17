---
UID: NS.wwan._WWAN_REGISTRATION_STATE
title: WWAN_REGISTRATION_STATE
author: windows-driver-content
description: The WWAN_REGISTRATION_STATE structure represents the registration state of the MB device.
old-location: netvista\wwan_registration_state.htm
ms.assetid: 72a41403-9e22-4212-955a-16e243f7af1d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_REGISTRATION_STATE
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
ms.keywords: WWAN_REGISTRATION_STATE, WWAN_REGISTRATION_STATE, *PWWAN_REGISTRATION_STATE
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_REGISTRATION_STATE structure



## -description
<p>The WWAN_REGISTRATION_STATE structure represents the registration state of the MB device.</p>


## -syntax

````
typedef struct _WWAN_REGISTRATION_STATE {
  ULONG               uNwError;
  WWAN_REGISTER_STATE RegisterState;
  WWAN_REGISTER_MODE  RegisterMode;
  WCHAR               ProviderId[WWAN_PROVIDERID_LEN];
  WCHAR               ProviderName[WWAN_PROVIDERNAME_LEN];
  WCHAR               RoamingText[WWAN_ROAMTEXT_LEN];
  DWORD               WwanRegFlags;
  WWAN_CELLULAR_CLASS CurrentCellularClass;
} WWAN_REGISTRATION_STATE, *PWWAN_REGISTRATION_STATE;
````


## -struct-fields
<dl>

### -field <b>uNwError</b>

<dd>
<p>A network specific error, in the event of a registration failure. For more information about this
     member, see the following 
     "Remarks" section.</p>
</dd>

### -field <b>RegisterState</b>

<dd>
<p>The registration state of the device. For a list of defined values, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571230">WWAN_REGISTER_STATE</a>.
     </p>
<p>The 
     <b>WwanRegisterStatePartner</b> value indicates the device is roaming on a preferred partner network
     provider, whereas 
     <b>WwanRegisterStateRoaming</b> value indicates the device is just roaming. If the partner
     characterization of the roaming state is not available, the miniport driver should report 
     <b>WwanRegisterStateRoaming</b>.</p>
</dd>

### -field <b>RegisterMode</b>

<dd>
<p>The registration mode of the device. For a list of defined values, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571229">WWAN_REGISTER_MODE</a>.</p>
</dd>

### -field <b>ProviderId</b>

<dd>
<p>A NULL-terminated numeric (0-9) string that represents the network provider identity.
     </p>
<p>For GSM-based networks, this string is a concatenation of a three-digit Mobile Country Code (MCC) and
     a two or three-digit Mobile Network Code (MNC). GSM-based carriers may have more than one MNC, and hence
     more than one 
     <b>ProviderId</b> .</p>
<p>For CDMA-based networks, this string is a five-digit System ID (SID). Generally, a CDMA-based carrier
     has more than one SID. Typically, a carrier has one SID for each market, which is usually divided
     geographically within a nation by regulations, such as Metropolitan Statistical Areas (MSA) in the
     United States of America. Miniport drivers of CDMA-based devices must specify
     WWAN_CDMA_DEFAULT_PROVIDER_ID if this information is not available.</p>
<p>When processing a 
     <i>query</i> request, and the registration state is in automatic register mode, this member contains the
     provider ID that the device is currently associated with (if applicable). When the registration state is
     in manual register mode, this member contains the provider ID that the device is requested to register
     with (even if the provider is unavailable).</p>
<p>When processing a 
     <i>set</i> request and the registration state is in manual mode, this contains the provider ID selected
     by the MB Service for the device to register with. When the registration state is in automatic register
     mode, this parameter is ignored.</p>
<p>CDMA 1xRTT providers must be set to WWAN_CDMA_DEFAULT_PROVIDER_ID if the provider ID is not
     available.</p>
</dd>

### -field <b>ProviderName</b>

<dd>
<p>A NULL-terminated string that represents the network provider's name. This member is limited to,
     at most, WWAN_PROVIDERNAME_LEN characters.
     </p>
<p>For GSM-based networks, if the Preferred Presentation of Country Initials and Mobile Network Name
     (PPCI&amp;N) is longer than twenty characters, the miniport driver should abbreviate the network
     name.</p>
<p>This member is ignored when the MB Service sets the preferred provider list.</p>
<p>Miniport drivers should specify a <b>NULL</b> string for devices that do not have this
     information.</p>
</dd>

### -field <b>RoamingText</b>

<dd>
<p>A NULL-terminated string to inform the user that the device is roaming. This member is limited to
     at most WWAN_ROAMTEXT_LEN characters.
     </p>
<p>This text should provide additional information to the user when the registration state is either 
     <b>WwanRegisterStatePartner</b> or 
     <b>WwanRegisterStateRoaming</b>. This member is optional.</p>
</dd>

### -field <b>WwanRegFlags</b>

<dd>
<p>Registration flags.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_REG_FLAGS_NONE</p>
</td>
<td>
<p>No registration flags.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_REG_FLAGS_NO_MANUAL_REG</p>
</td>
<td>
<p>No manual attach.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_REG_FLAGS_PS_AUTO_ATTACH</p>
</td>
<td>
<p>Iindicates that the MB device manages its own packet context. The MB Service will not send a packet detach to the miniport driver, but may send a packet attach.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CurrentCellularClass</b>

<dd>
<p>The current cellular class of the registered network. For networks that only support a single cellular class this member should be set to that cellular class. For multi-mode capable networks the miniport driver sends  NDIS_STATUS_WWAN_REGISTER_STATE notifications to the MB service when the network changes its cellular class.</p>
</dd>
</dl>

## -remarks
<p><i>Query</i> and 
    <i>set</i> OID requests as well as unsolicited status events use the 
    <b>uNwError</b> member. If there is no network specific error or the network specific error is not known,
    miniport drivers should set this member to zero. The 
    "Status Indication Structure" section in 
    <a href="NULL">MB Operational Semantics</a> shows the
    registration cause code failure values that are defined in the 
    <i>3GPP TS 24.008 Specification</i>.</p>

<p>The following points provide guidelines on returning network specific error in different
    scenarios:</p>

<p>If network registration fails because of network specific error, miniport drivers should return the
      network specific error in response to 
      <i>query</i> requests. In this case, miniport drivers should set the 
      <b>uStatus</b> member of the NDIS_WWAN_REGISTRATION_STATE structure to WWAN_STATUS_SUCCESS and set the 
      <b>uNwError</b> member to the network specific error code.</p>

<p>If a 
      <i>set</i> request fails, miniport drivers should return the network specific error code. In this case,
      miniport drivers should set the 
      <b>uStatus</b> member of the NDIS_WWAN_REGISTRATION_STATE structure to WWAN_STATUS_FAILURE and set the 
      <b>uNwError</b> member to the network specific error code.</p>

<p>Whenever the device registration state changes because the network de-registers the device (for
      example, the network de-registered the device because the device's subscription expired) then
      unsolicited status events should include the network specific error. In this case, the miniport driver
      should set the 
      <b>uStatus</b> member of the NDIS_WWAN_REGISTRATION_STATE structure to WWAN_STATUS_SUCCESS and set the 
      <b>uNwError</b> member to the network specific error code.</p>

<p>To return a network specific error when processing OID_WWAN_REGISTER_STATE requests, miniport drivers
    should set the 
    <b>uStatus</b> member of the NDIS_WWAN_REGISTRATION_STATE structure to WWAN_STATUS_FAILURE and set the 
    <b>uNwError</b> member to the network specific error code.</p>

<p>Miniport drivers can provide additional error codes as defined by the GSM standards specification of
    packet-attach error codes returned by the network. For example, miniport drivers can communicate the 3GPP
    specification TS 24.008 packet-attach error codes, such as error code 12 (Location area not allowed), to
    the MB Service through the 
    <b>uNwError</b> member.</p>

<p>Miniport drivers must report the cause code at the earliest possible instance. For example, if the MB
    device encounters one of these codes when attempting to register the device on with a network provider,
    the miniport driver should report it at that time.</p>

<p>Miniport drivers connected to a multi-mode network should indicate the cellular class change through a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567857">NDIS_STATUS_WWAN_REGISTER_STATE</a> notification.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of Windows.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571230">WWAN_REGISTER_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571229">WWAN_REGISTER_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567917">NDIS_WWAN_REGISTRATION_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_REGISTRATION_STATE structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
