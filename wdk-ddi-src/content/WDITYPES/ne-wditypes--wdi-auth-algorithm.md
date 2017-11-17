---
UID: NE.wditypes._WDI_AUTH_ALGORITHM
title: WDI_AUTH_ALGORITHM
author: windows-driver-content
description: The WDI_AUTH_ALGORITHM enumeration defines the authentication algorithm values.
old-location: netvista\wdi_auth_algorithm.htm
ms.assetid: B908A174-F977-484E-A086-6C8C9A914D6C
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_AUTH_ALGORITHM
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDI_AUTH_ALGORITHM enumeration



## -description
<p>The WDI_AUTH_ALGORITHM enumeration defines the authentication algorithm values.</p>


## -syntax

````
typedef enum _WDI_AUTH_ALGORITHM { 
  WDI_AUTH_ALGO_80211_OPEN        = 1,
  WDI_AUTH_ALGO_80211_SHARED_KEY  = 2,
  WDI_AUTH_ALGO_WPA               = 3,
  WDI_AUTH_ALGO_WPA_PSK           = 4,
  WDI_AUTH_ALGO_WPA_NONE          = 5,
  WDI_AUTH_ALGO_RSNA              = 6,
  WDI_AUTH_ALGO_RSNA_PSK          = 7,
  WDI_AUTH_ALGO_IHV_START         = 0x80000000,
  WDI_AUTH_ALGO_IHV_END           = 0xffffffff
} WDI_AUTH_ALGORITHM;
````


## -enum-fields
<dl>

### -field <a id="WDI_AUTH_ALGO_80211_OPEN"></a><a id="wdi_auth_algo_80211_open"></a><b>WDI_AUTH_ALGO_80211_OPEN</b>

<dd>
<p>Specifies an IEEE 802.11 Open System authentication algorithm. </p>
</dd>

### -field <a id="WDI_AUTH_ALGO_80211_SHARED_KEY"></a><a id="wdi_auth_algo_80211_shared_key"></a><b>WDI_AUTH_ALGO_80211_SHARED_KEY</b>

<dd>
<p>Specifies an IEEE 802.11 Shared Key authentication algorithm that requires the use of a pre-shared Wired Equivalent Privacy (WEP) key for the 802.11 authentication.</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_WPA"></a><a id="wdi_auth_algo_wpa"></a><b>WDI_AUTH_ALGO_WPA</b>

<dd>
<p>Specifies a Wi-Fi Protected Access (WPA) algorithm. IEEE 802.1X port authorization is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process. </p>
<p>When the WPA algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the WPA information element (IE).</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_WPA_PSK"></a><a id="wdi_auth_algo_wpa_psk"></a><b>WDI_AUTH_ALGO_WPA_PSK</b>

<dd>
<p>Specifies a Wi-Fi Protected Access (WPA) algorithm that uses preshared keys (PSK). IEEE 802.1X port authorization is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator. </p>
<p>When the WPA PSK algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the WPA IE.</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_WPA_NONE"></a><a id="wdi_auth_algo_wpa_none"></a><b>WDI_AUTH_ALGO_WPA_NONE</b>

<dd>
<p>This value is not supported.</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_RSNA"></a><a id="wdi_auth_algo_rsna"></a><b>WDI_AUTH_ALGO_RSNA</b>

<dd>
<p>Specifies an IEEE 802.11i Robust Security Network Association (RSNA) algorithm. IEEE 802.1X port authorization is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process. </p>
<p>When the RSNA algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the Robust Security Network (RSN) IE.</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_RSNA_PSK"></a><a id="wdi_auth_algo_rsna_psk"></a><b>WDI_AUTH_ALGO_RSNA_PSK</b>

<dd>
<p>Specifies an IEEE 802.11i RSNA algorithm that uses PSK. IEEE 802.1X port authorization is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a pre-shared key that is used on both the supplicant and authenticator. </p>
<p>When the RSNA PSK algorithm is enabled, the 802.11 station only associates with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the RSN IE.</p>
</dd>

### -field <a id="WDI_AUTH_ALGO_IHV_START"></a><a id="wdi_auth_algo_ihv_start"></a><b>WDI_AUTH_ALGO_IHV_START</b>

<dd>
<p>Specifies the start of the range that specifies proprietary authentication algorithms that are developed by an IHV. </p>
</dd>

### -field <a id="WDI_AUTH_ALGO_IHV_END"></a><a id="wdi_auth_algo_ihv_end"></a><b>WDI_AUTH_ALGO_IHV_END</b>

<dd>
<p>Specifies the end of the range that specifies proprietary authentication algorithms that are developed by an IHV. </p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>