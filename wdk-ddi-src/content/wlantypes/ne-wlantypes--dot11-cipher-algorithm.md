---
UID: NE.wlantypes._DOT11_CIPHER_ALGORITHM
title: DOT11_CIPHER_ALGORITHM
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_cipher_algorithm.htm
old-project: netvista
ms.assetid: 5fc1af01-7dd5-43dd-aefe-99dec0b5aa6a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11EXT_IHV_SSID_LIST,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wlantypes.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_CIPHER_ALGORITHM
req.alt-loc: wlantypes.h
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

# DOT11_CIPHER_ALGORITHM enumeration



## -description

## -syntax

````
typedef enum _DOT11_CIPHER_ALGORITHM { 
  DOT11_CIPHER_ALGO_NONE           = 0x00,
  DOT11_CIPHER_ALGO_WEP40          = 0x01,
  DOT11_CIPHER_ALGO_TKIP           = 0x02,
  DOT11_CIPHER_ALGO_CCMP           = 0x04,
  DOT11_CIPHER_ALGO_WEP104         = 0x05,
  DOT11_CIPHER_ALGO_BIP            = 0x06,
  DOT11_CIPHER_ALGO_WPA_USE_GROUP  = 0x100,
  DOT11_CIPHER_ALGO_RSN_USE_GROUP  = 0x100,
  DOT11_CIPHER_ALGO_WEP            = 0x101,
  DOT11_CIPHER_ALGO_IHV_START      = 0x80000000,
  DOT11_CIPHER_ALGO_IHV_END        = 0xffffffff
} DOT11_CIPHER_ALGORITHM, *PDOT11_CIPHER_ALGORITHM;
````


## -enum-fields
<dl>

### -field <a id="DOT11_CIPHER_ALGO_NONE"></a><a id="dot11_cipher_algo_none"></a><b>DOT11_CIPHER_ALGO_NONE</b>

<dd>
<p>Specifies that no cipher algorithm is enabled or supported.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_WEP40"></a><a id="dot11_cipher_algo_wep40"></a><b>DOT11_CIPHER_ALGO_WEP40</b>

<dd>
<p>Specifies a Wired Equivalent Privacy (WEP) algorithm, which is the RC4-based algorithm that is
     specified in the IEEE 802.11-2012 standard. This enumerator specifies the WEP cipher algorithm with a
     40-bit cipher key.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_TKIP"></a><a id="dot11_cipher_algo_tkip"></a><b>DOT11_CIPHER_ALGO_TKIP</b>

<dd>
<p>Specifies a Temporal Key Integrity Protocol (TKIP) algorithm, which is the RC4-based cipher suite
     that is based on the algorithms that are defined in the WPA specification and IEEE 802.11i-2004
     standard. This cipher also uses the Michael Message Integrity Code (MIC) algorithm for forgery
     protection.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_CCMP"></a><a id="dot11_cipher_algo_ccmp"></a><b>DOT11_CIPHER_ALGO_CCMP</b>

<dd>
<p>Specifies an AES-CCMP algorithm, as specified in the IEEE 802.11i-2004 standard and RFC 3610.
     Advanced Encryption Standard (AES) is the encryption algorithm defined in FIPS PUB 197.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_WEP104"></a><a id="dot11_cipher_algo_wep104"></a><b>DOT11_CIPHER_ALGO_WEP104</b>

<dd>
<p>Specifies a WEP cipher algorithm with a 104-bit cipher key.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_BIP"></a><a id="dot11_cipher_algo_bip"></a><b>DOT11_CIPHER_ALGO_BIP</b>

<dd>
<p>Specifies a BIP cipher algorithm.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_WPA_USE_GROUP"></a><a id="dot11_cipher_algo_wpa_use_group"></a><b>DOT11_CIPHER_ALGO_WPA_USE_GROUP</b>

<dd>
<p>Specifies a Wifi Protected Access (WPA) Use Group Key cipher suite.</p>
<p>For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE
      802.11i-2004 standard.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_RSN_USE_GROUP"></a><a id="dot11_cipher_algo_rsn_use_group"></a><b>DOT11_CIPHER_ALGO_RSN_USE_GROUP</b>

<dd>
<p>Specifies a Robust Security Network (RSN) Use Group Key cipher suite.</p>
<p>For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE
      802.11i-2004 standard.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_WEP"></a><a id="dot11_cipher_algo_wep"></a><b>DOT11_CIPHER_ALGO_WEP</b>

<dd>
<p>Specifies a WEP cipher algorithm with a cipher key of any length.
     </p>
<p>A miniport driver that operates in Extensible Station (ExtSTA) mode specifies the maximum WEP cipher
     key length through a query of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569366">OID_DOT11_EXTSTA_CAPABILITY</a>.</p>
<div class="alert"><b>Note</b>  The operating system will only enable this cipher algorithm if authentication
     algorithms of 
     <b>DOT11_AUTH_ALGO_80211_OPEN</b> or 
     <b>DOT11_AUTH_ALGO_80211_SHARED_KEY</b> have been enabled. For more information about these
     authentication algorithms, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547655">DOT11_AUTH_ALGORITHM</a>.</div>
<div> </div>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_IHV_START"></a><a id="dot11_cipher_algo_ihv_start"></a><b>DOT11_CIPHER_ALGO_IHV_START</b>

<dd>
<p>Specifies the start of the range that is used to define proprietary cipher algorithms that are
     developed by an independent hardware vendor (IHV).
     </p>
<p>The 
     <b>DOT11_CIPHER_ALGO_IHV_START</b> enumerator is valid only when the miniport driver is operating in
     ExtSTA mode.</p>
</dd>

### -field <a id="DOT11_CIPHER_ALGO_IHV_END"></a><a id="dot11_cipher_algo_ihv_end"></a><b>DOT11_CIPHER_ALGO_IHV_END</b>

<dd>
<p>Specifies the end of the range that is used to define proprietary authentication algorithms that
     are developed by an IHV.
     </p>
<p>The 
     <b>DOT11_CIPHER_ALGO_IHV_END</b> enumerator is valid only when the miniport driver is operating in ExtSTA
     mode.</p>
</dd>
</dl>

## -remarks
<p>An IHV can assign a value for its proprietary cipher algorithms from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>. The IHV must assign a unique number in this range to each of its
    proprietary cipher algorithms.</p>

<p>If the IHV develops its own support for an cipher algorithm supported by the operating system, the IHV
    must also assign a unique number from this range. For example, if the IHV develops its own version of
    TKIP, it must assign a value for this version from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>.</p>

<p>A miniport driver must enable or select cipher algorithms based on the following preference order
    (listed from highest to lowest):</p><dl>
<dd>
<p><b>DOT11_CIPHER_ALGO_CCMP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_NONE</b></p>
</dd>
</dl><p><b>DOT11_CIPHER_ALGO_CCMP</b></p>

<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>

<p><b>DOT11_CIPHER_ALGO_NONE</b></p>

<p>If the miniport driver supports IHV-defined cipher algorithms, the miniport driver can determine the
    preference order for these algorithms with respect to the 802.11 standard cipher algorithms.</p>

<p>Starting with Windows 7, an 802.11 miniport driver can report any combination of supported
    authentication and cipher algorithm pairs in the 
    <a href="..\windot11\ns-windot11-dot11-auth-cipher-pair-list.md">
    DOT11_AUTH_CIPHER_PAIR_LIST</a> structure. However, if the operating system starts Soft AP, it enables
    only the 
    <b>DOT11_AUTH_ALGO_RSNA_PSK</b> authentication algorithm and the 
    <b>DOT11_CIPHER_ALGO_CCMP</b> cipher algorithm. To support Soft AP, the miniport driver must support this
    authentication/cipher pair.</p>

<p>If WPS is enabled on a NIC that is operating in Extensible AP mode, the miniport driver must allow
    peer stations to associate with the Extensible AP by using 
    <a href="NULL">Open System Authentication</a> or 
    <a href="https://msdn.microsoft.com/41dd280b-e54c-4233-8051-45e7b1284d1d">Wired Equivalent Privacy (WEP)</a> algorithms, regardless of
    the enabled authorization and cipher algorithms. For more information about WPS and Extensible AP, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569436">OID_DOT11_WPS_ENABLED</a>.</p>

<p>An IHV can assign a value for its proprietary cipher algorithms from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>. The IHV must assign a unique number in this range to each of its
    proprietary cipher algorithms.</p>

<p>If the IHV develops its own support for an cipher algorithm supported by the operating system, the IHV
    must also assign a unique number from this range. For example, if the IHV develops its own version of
    TKIP, it must assign a value for this version from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>.</p>

<p>A miniport driver must enable or select cipher algorithms based on the following preference order
    (listed from highest to lowest):</p><dl>
<dd>
<p><b>DOT11_CIPHER_ALGO_CCMP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_NONE</b></p>
</dd>
</dl><p><b>DOT11_CIPHER_ALGO_CCMP</b></p>

<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>

<p><b>DOT11_CIPHER_ALGO_NONE</b></p>

<p>If the miniport driver supports IHV-defined cipher algorithms, the miniport driver can determine the
    preference order for these algorithms with respect to the 802.11 standard cipher algorithms.</p>

<p>Starting with Windows 7, an 802.11 miniport driver can report any combination of supported
    authentication and cipher algorithm pairs in the 
    <a href="..\windot11\ns-windot11-dot11-auth-cipher-pair-list.md">
    DOT11_AUTH_CIPHER_PAIR_LIST</a> structure. However, if the operating system starts Soft AP, it enables
    only the 
    <b>DOT11_AUTH_ALGO_RSNA_PSK</b> authentication algorithm and the 
    <b>DOT11_CIPHER_ALGO_CCMP</b> cipher algorithm. To support Soft AP, the miniport driver must support this
    authentication/cipher pair.</p>

<p>If WPS is enabled on a NIC that is operating in Extensible AP mode, the miniport driver must allow
    peer stations to associate with the Extensible AP by using 
    <a href="NULL">Open System Authentication</a> or 
    <a href="https://msdn.microsoft.com/41dd280b-e54c-4233-8051-45e7b1284d1d">Wired Equivalent Privacy (WEP)</a> algorithms, regardless of
    the enabled authorization and cipher algorithms. For more information about WPS and Extensible AP, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569436">OID_DOT11_WPS_ENABLED</a>.</p>

<p>An IHV can assign a value for its proprietary cipher algorithms from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>. The IHV must assign a unique number in this range to each of its
    proprietary cipher algorithms.</p>

<p>If the IHV develops its own support for an cipher algorithm supported by the operating system, the IHV
    must also assign a unique number from this range. For example, if the IHV develops its own version of
    TKIP, it must assign a value for this version from 
    <b>DOT11_CIPHER_ALGO_IHV_START</b> through 
    <b>DOT11_CIPHER_ALGO_IHV_END</b>.</p>

<p>A miniport driver must enable or select cipher algorithms based on the following preference order
    (listed from highest to lowest):</p><dl>
<dd>
<p><b>DOT11_CIPHER_ALGO_CCMP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>
</dd>
<dd>
<p><b>DOT11_CIPHER_ALGO_NONE</b></p>
</dd>
</dl><p><b>DOT11_CIPHER_ALGO_CCMP</b></p>

<p><b>DOT11_CIPHER_ALGO_TKIP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>

<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>

<p><b>DOT11_CIPHER_ALGO_NONE</b></p>

<p>If the miniport driver supports IHV-defined cipher algorithms, the miniport driver can determine the
    preference order for these algorithms with respect to the 802.11 standard cipher algorithms.</p>

<p>Starting with Windows 7, an 802.11 miniport driver can report any combination of supported
    authentication and cipher algorithm pairs in the 
    <a href="..\windot11\ns-windot11-dot11-auth-cipher-pair-list.md">
    DOT11_AUTH_CIPHER_PAIR_LIST</a> structure. However, if the operating system starts Soft AP, it enables
    only the 
    <b>DOT11_AUTH_ALGO_RSNA_PSK</b> authentication algorithm and the 
    <b>DOT11_CIPHER_ALGO_CCMP</b> cipher algorithm. To support Soft AP, the miniport driver must support this
    authentication/cipher pair.</p>

<p>If WPS is enabled on a NIC that is operating in Extensible AP mode, the miniport driver must allow
    peer stations to associate with the Extensible AP by using 
    <a href="NULL">Open System Authentication</a> or 
    <a href="https://msdn.microsoft.com/41dd280b-e54c-4233-8051-45e7b1284d1d">Wired Equivalent Privacy (WEP)</a> algorithms, regardless of
    the enabled authorization and cipher algorithms. For more information about WPS and Extensible AP, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569436">OID_DOT11_WPS_ENABLED</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlantypes.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\windot11\ns-windot11-dot11-association-completion-parameters.md">
   DOT11_ASSOCIATION_COMPLETION_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547662">DOT11_AUTH_CIPHER_PAIR_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547673">DOT11_CIPHER_ALGORITHM_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569119">OID_DOT11_CIPHER_DEFAULT_KEY</a>
</dt>
<dt>
<a href="netvista.oid_dot11_cipher_key_mapping_key">
   OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569135">OID_DOT11_CURRENT_PHY_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_CIPHER_ALGORITHM enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
