---
UID: NS.windot11.DOT11_EXTSTA_ATTRIBUTES
title: DOT11_EXTSTA_ATTRIBUTES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_extsta_attributes.htm
old-project: netvista
ms.assetid: 319017a7-f398-46f7-ab03-1dcb057c1332
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_EXTSTA_ATTRIBUTES,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_EXTSTA_ATTRIBUTES
req.alt-loc: Windot11.h
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

# DOT11_EXTSTA_ATTRIBUTES structure



## -description

## -syntax

````
typedef struct DOT11_EXTSTA_ATTRIBUTES {
  NDIS_OBJECT_HEADER              Header;
  ULONG                           uScanSSIDListSize;
  ULONG                           uDesiredBSSIDListSize;
  ULONG                           uDesiredSSIDListSize;
  ULONG                           uExcludedMacAddressListSize;
  ULONG                           uPrivacyExemptionListSize;
  ULONG                           uKeyMappingTableSize;
  ULONG                           uDefaultKeyTableSize;
  ULONG                           uWEPKeyValueMaxLength;
  ULONG                           uPMKIDCacheSize;
  ULONG                           uMaxNumPerSTADefaultKeyTables;
  BOOLEAN                         bStrictlyOrderedServiceClassImplemented;
  UCHAR                           ucSupportedQoSProtocolFlags;
  BOOLEAN                         bSafeModeImplemented;
  ULONG                           uNumSupportedCountryOrRegionStrings;
  PDOT11_COUNTRY_OR_REGION_STRING pSupportedCountryOrRegionStrings;
  ULONG                           uInfraNumSupportedUcastAlgoPairs;
  PDOT11_AUTH_CIPHER_PAIR         pInfraSupportedUcastAlgoPairs;
  ULONG                           uInfraNumSupportedMcastAlgoPairs;
  PDOT11_AUTH_CIPHER_PAIR         pInfraSupportedMcastAlgoPairs;
  ULONG                           uAdhocNumSupportedUcastAlgoPairs;
  PDOT11_AUTH_CIPHER_PAIR         pAdhocSupportedUcastAlgoPairs;
  ULONG                           uAdhocNumSupportedMcastAlgoPairs;
  PDOT11_AUTH_CIPHER_PAIR         pAdhocSupportedMcastAlgoPairs;
  BOOLEAN                         bAutoPowerSaveMode;
  ULONG                           uMaxNetworkOffloadListSize;
  BOOLEAN                         bMFPCapable;
  ULONG                           uInfraNumSupportedMcastMgmtAlgoPairs;
  PDOT11_AUTH_CIPHER_PAIR         pInfraSupportedMcastMgmtAlgoPairs;
} DOT11_EXTSTA_ATTRIBUTES, *PDOT11_EXTSTA_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>DOT11_EXTSTA_ATTRIBUTES</b> structure. This member is formatted as
     an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values.</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b>

<dd>
<p>This member must be set to <b>NDIS_OBJECT_TYPE_DEFAULT</b>.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b>

<dd>
<p>This member must be set to one of the following values according to the operating system that
       the driver is intended to run on:
       </p>
<p></p>
<dl>

### -field <a id="DOT11_EXTSTA_ATTRIBUTES_REVISION_1"></a><a id="dot11_extsta_attributes_revision_1"></a>DOT11_EXTSTA_ATTRIBUTES_REVISION_1

<dd>
<p>Windows Vista</p>
</dd>

### -field <a id="DOT11_EXTSTA_ATTRIBUTES_REVISION_2"></a><a id="dot11_extsta_attributes_revision_2"></a>DOT11_EXTSTA_ATTRIBUTES_REVISION_2

<dd>
<p>Windows Vista with Service Pack 1 (SP1) or later versions of the Windows operating
         systems</p>
</dd>

### -field <a id="DOT11_EXTSTA_ATTRIBUTES_REVISION_3"></a><a id="dot11_extsta_attributes_revision_3"></a>DOT11_EXTSTA_ATTRIBUTES_REVISION_3

<dd>
<p>Windows 8 or later versions of the Windows operating
         systems</p>
</dd>
</dl>
<p>These values determine how the operating system interprets the 
       <b>bSafeModeImplemented</b> member.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       <b>sizeof</b>(<b>DOT11_EXTSTA_ATTRIBUTES</b>).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uScanSSIDListSize</b>

<dd>
<p>The maximum number of service set identifiers (SSIDs) supported by the 802.11 station for scan
     operations. The 802.11 station must support an SSID list of at least four entries.
     </p>
<p>The SSID list that the 802.11 station uses for scanning is specified when 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a> is
     set.</p>
</dd>

### -field <b>uDesiredBSSIDListSize</b>

<dd>
<p>The maximum number of entries in the desired list of basic service set identifiers (BSSIDs)
     supported by the 802.11 station. The 802.11 station must support a BSSID list with at least one entry.
     </p>
<p>For more information about the desired BSSID list, see 
     <a href="netvista.oid_dot11_desired_bssid_list">
     OID_DOT11_DESIRED_BSSID_LIST</a>.</p>
</dd>

### -field <b>uDesiredSSIDListSize</b>

<dd>
<p>The maximum number of entries in the desired SSID list supported by the 802.11 station. The 802.11
     station must support a desired SSID list with at least one entry.
     </p>
<p>For more information about the desired SSID list, see 
     <a href="netvista.oid_dot11_desired_ssid_list">
     OID_DOT11_DESIRED_SSID_LIST</a>.</p>
</dd>

### -field <b>uExcludedMacAddressListSize</b>

<dd>
<p>The maximum number of entries in the excluded MAC address list supported by the 802.11 station.
     The 802.11 station must support an excluded MAC address list with at least four entries.
     </p>
<p>For more information about the desired excluded MAC address list, see 
     <a href="netvista.oid_dot11_excluded_mac_address_list">
     OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST</a>.</p>
</dd>

### -field <b>uPrivacyExemptionListSize</b>

<dd>
<p>The maximum number of entries in the privacy exemption list supported by the 802.11 station. The
     802.11 station must support a privacy exemption list with at least one entry.
     </p>
<p>For more information about the privacy exemption list, see 
     <a href="netvista.oid_dot11_privacy_exemption_list">
     OID_DOT11_PRIVACY_EXEMPTION_LIST</a>.</p>
</dd>

### -field <b>uKeyMappingTableSize</b>

<dd>
<p>The maximum number of cipher key-mapping keys supported by the 802.11 station. It is recommended
     that the 802.11 station support at least 32 key-mapping keys.
     </p>
<p>For more information about key mapping keys, see 
     <a href="netvista.oid_dot11_cipher_key_mapping_key">
     OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>.</p>
</dd>

### -field <b>uDefaultKeyTableSize</b>

<dd>
<p>The maximum number of cipher keys the 802.11 station supports for the default key and per-station
     default key tables.
     </p>
<p>For standard 802.11 cipher algorithms, the 802.11 station must support a table size of at least four
     cipher keys. For cipher algorithms developed by the independent hardware vendor (IHV), the table size
     can be four or greater.</p>
</dd>

### -field <b>uWEPKeyValueMaxLength</b>

<dd>
<p>The maximum length, in bytes, of a WEP cipher key supported by the 802.11 station.
     </p>
<p>The following table lists the minimum and maximum key lengths, in bytes, for the various WEP cipher
     values defined through 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547672">DOT11_CIPHER_ALGORITHM</a>.</p>
<table>
<tr>
<th>WEP cipher</th>
<th>Minimum key length</th>
<th>Maximum key length</th>
</tr>
<tr>
<td>
<p><b>DOT11_CIPHER_ALGO_WEP40</b></p>
</td>
<td>
<p>5</p>
</td>
<td>
<p>5</p>
</td>
</tr>
<tr>
<td>
<p><b>DOT11_CIPHER_ALGO_WEP104</b></p>
</td>
<td>
<p>13</p>
</td>
<td>
<p>13</p>
</td>
</tr>
<tr>
<td>
<p><b>DOT11_CIPHER_ALGO_WEP</b></p>
</td>
<td>
<p>13</p>
</td>
<td>
<p>Any length supported by the 802.11 station</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>uPMKIDCacheSize</b>

<dd>
<p>The maximum number of entries in the pairwise master key identifier (PMKID) cache supported by the
     802.11 station. 
     </p>
<p>If the 802.11 station does not support a PMKID cache, the miniport driver must set this member to
     zero. Otherwise, the 802.11 station must support a PMKID cache size of at least three entries.</p>
<p>For more information about the PMKID cache, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569400">OID_DOT11_PMKID_LIST</a>.</p>
</dd>

### -field <b>uMaxNumPerSTADefaultKeyTables</b>

<dd>
<p>The maximum number of per-station default cipher key tables supported by the 802.11 station. It is
     recommended that the 802.11 station support at least 32 per-station default cipher key tables.
     </p>
<p>For more information about per-station default cipher key tables, see 
     <a href="NULL">Per-Station Default Keys</a>.</p>
</dd>

### -field <b>bStrictlyOrderedServiceClassImplemented</b>

<dd>
<p>A Boolean value that, if set to <b>TRUE</b>, specifies that the 802.11 station supports the IEEE 802.11
     StrictlyOrdered service class for media access control (MAC) service data unit (MSDU) packet delivery.
     </p>
<p>For more information about the StrictlyOrdered service class, refer to Clause 5.1.3 of the IEEE
     802.11-2012 standard.</p>
</dd>

### -field <b>ucSupportedQoSProtocolFlags</b>

<dd>
<p>A set of flags that specify the quality of service (QoS) protocols that the NIC implements. This
     member is either zero or a bitwise OR combination of the following flags:
     </p>
<p></p>
<dl>

### -field <a id="DOT11_QOS_PROTOCOL_FLAG_WMM"></a><a id="dot11_qos_protocol_flag_wmm"></a>DOT11_QOS_PROTOCOL_FLAG_WMM

<dd>
<p>The NIC implements the 802.11 WMM QoS protocol.</p>
</dd>

### -field <a id="DOT11_QOS_PROTOCOL_FLAG_11E"></a><a id="dot11_qos_protocol_flag_11e"></a>DOT11_QOS_PROTOCOL_FLAG_11E

<dd>
<p>The NIC implements the 802.11e QoS protocol.</p>
</dd>
</dl>
</dd>

### -field <b>bSafeModeImplemented</b>

<dd>
<p>The safe mode support capability of the NIC/miniport driver combination. The operating system
     interprets this member differently depending on the value of 
     <b>Header.Revision</b>:
     </p>
<p></p>
<dl>

### -field <a id="Revision___DOT11_EXTSTA_ATTRIBUTES_REVISION_1"></a><a id="revision___dot11_extsta_attributes_revision_1"></a><a id="REVISION___DOT11_EXTSTA_ATTRIBUTES_REVISION_1"></a>Revision = DOT11_EXTSTA_ATTRIBUTES_REVISION_1

<dd>
<p>The operating system interprets the 
       <b>bSafeModeImplemented</b> member as a Boolean value. If this value is <b>TRUE</b>, the NIC implements the
       802.11 safe mode of operation. Otherwise, the value is <b>FALSE</b>.</p>
</dd>

### -field <a id="Revision___DOT11_EXTSTA_ATTRIBUTES_REVISION_2_or_higher"></a><a id="revision___dot11_extsta_attributes_revision_2_or_higher"></a><a id="REVISION___DOT11_EXTSTA_ATTRIBUTES_REVISION_2_OR_HIGHER"></a>Revision = DOT11_EXTSTA_ATTRIBUTES_REVISION_2 or higher

<dd>
<p>The operating system interprets the 
       <b>bSafeModeImplemented</b> member as a bit field with the following possible bit values set:
       </p>
<ul>
<li>
<p>If the bit field is set to <b>DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_OID_SUPPORTED</b> with no other bits set,
         the miniport driver implements the 802.11 safe mode of operation.</p>
</li>
<li>
<p>If the bit field is set to <b>DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_CERTIFIED</b>, the NIC/miniport
         combination has received a validation certificate from the National Institute of Standards and
         Technology (NIST) under Federal Information Processing Standards (FIPS) Publication 140-2, 
         <i>Security Requirements for Cryptographic Modules</i>.</p>
</li>
</ul>
</dd>
</dl>
<p>This member is used in conjunction with 
     <a href="netvista.oid_dot11_safe_mode_enabled">
     OID_DOT11_SAFE_MODE_ENABLED</a>.</p>
</dd>

### -field <b>uNumSupportedCountryOrRegionStrings</b>

<dd>
<p>The number of country or region strings supported by the 802.11 station. If the 802.11 station
     supports multiple regulatory domains as specified by the IEEE 802.11d-2001 standard, each country or
     region string identifies a regulatory domain supported by the 802.11 station.
     </p>
<p>If the 802.11 station does not support the IEEE 802.11d-2001 standard, the miniport driver must set 
     <b>uNumSupportedCountryOrRegionStrings</b> to zero.</p>
</dd>

### -field <b>pSupportedCountryOrRegionStrings</b>

<dd>
<p>A pointer to an array of 802.11d country or region strings that are supported by the 802.11
     station. Each entry in the array is formatted as a 
     <a href="netvista.dot11_country_or_region_string">
     DOT11_COUNTRY_OR_REGION_STRING</a> structure.</p>
</dd>

### -field <b>uInfraNumSupportedUcastAlgoPairs</b>

<dd>
<p>The number of authentication and cipher algorithms supported by the 802.11 station for sending and
     receiving unicast packets when configured for operation in an infrastructure basic service set (BSS)
     network. The 
     <b>uInfraNumSupportedUcastAlgoPairs</b> member must be the number of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547659">DOT11_AUTH_CIPHER_PAIR</a> structures in
     the array referenced by the 
     <b>pInfraSupportedUcastAlgoPairs</b> member.</p>
</dd>

### -field <b>pInfraSupportedUcastAlgoPairs</b>

<dd>
<p>A pointer to an array of authentication and cipher algorithms supported by the 802.11 station for
     sending and receiving unicast packets in an infrastructure BSS network. Each entry in the array is
     formatted as a 
     <a href="..\wlantypes\ns-wlantypes-dot11-auth-cipher-pair.md">
     DOT11_AUTH_CIPHER_PAIR</a> structure.</p>
</dd>

### -field <b>uInfraNumSupportedMcastAlgoPairs</b>

<dd>
<p>The number of authentication and cipher algorithms supported by the 802.11 station for sending and
     receiving multicast and broadcast packets when configured for operation in an infrastructure basic
     service set (BSS) network. The 
     <b>uInfraNumSupportedMcastAlgoPairs</b> member must be the number of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547659">DOT11_AUTH_CIPHER_PAIR</a> structures in
     the array referenced by the 
     <b>pInfraSupportedMcastAlgoPairs</b> member.</p>
</dd>

### -field <b>pInfraSupportedMcastAlgoPairs</b>

<dd>
<p>A pointer to an array of authentication and cipher algorithms supported by the 802.11 station for
     sending and receiving multicast and broadcast packets in an infrastructure BSS network. Each entry in
     the array is formatted as a 
     <a href="..\wlantypes\ns-wlantypes-dot11-auth-cipher-pair.md">
     DOT11_AUTH_CIPHER_PAIR</a> structure.</p>
</dd>

### -field <b>uAdhocNumSupportedUcastAlgoPairs</b>

<dd>
<p>The number of authentication and cipher algorithms supported by the 802.11 station for sending and
     receiving unicast packets when configured for operation in an independent BSS (IBSS) network. The 
     <b>uAdhocNumSupportedUcastAlgoPairs</b> member must be the number of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547659">DOT11_AUTH_CIPHER_PAIR</a> structures in
     the array referenced by the 
     <b>pAdhocSupportedUcastAlgoPairs</b> member.</p>
</dd>

### -field <b>pAdhocSupportedUcastAlgoPairs</b>

<dd>
<p>A pointer to an array of authentication and cipher algorithms supported by the 802.11 station for
     sending and receiving unicast packets in an IBSS network. Each entry in the array is formatted as a 
     <a href="..\wlantypes\ns-wlantypes-dot11-auth-cipher-pair.md">
     DOT11_AUTH_CIPHER_PAIR</a> structure.</p>
</dd>

### -field <b>uAdhocNumSupportedMcastAlgoPairs</b>

<dd>
<p>The number of authentication and cipher algorithms supported by the 802.11 station for sending and
     receiving multicast and broadcast packets when configured for operation in an IBSS network. The 
     <b>uAdhocNumSupportedMcastAlgoPairs</b> member must be the number of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff547659">DOT11_AUTH_CIPHER_PAIR</a> structures in
     the array referenced by the 
     <b>pAdhocSupportedMcastAlgoPairs</b> member.</p>
</dd>

### -field <b>pAdhocSupportedMcastAlgoPairs</b>

<dd>
<p>A pointer to an array of authentication and cipher algorithms supported by the 802.11 station for
     sending and receiving multicast and broadcast packets in an IBSS network. Each entry in the array is
     formatted as a 
     <a href="..\wlantypes\ns-wlantypes-dot11-auth-cipher-pair.md">
     DOT11_AUTH_CIPHER_PAIR</a> structure.</p>
</dd>

### -field <b>bAutoPowerSaveMode</b>

<dd>
<p>The support capability of the NIC/miniport driver combination to autonomously manage power well, including detection and negotiation of proper Wi-Fi Power Save Mode (PSM) between the device and the Wi-Fi Access Point. NDIS 6.30 compliant Wi-Fi miniport drivers should set this member to TRUE.</p>
</dd>

### -field <b>uMaxNetworkOffloadListSize</b>

<dd>
<p>The maximum number of networks a miniport driver can offload, if it has the ability to support the Network List Offload capability.</p>
</dd>

### -field <b>bMFPCapable</b>

<dd>
<p>The support capability of the NIC/miniport driver to combination to support management frame protection between the device and the Wi-Fi Access Point  as specified in the 802.11w-2009 specification. Set to TRUE if supported. Otherwise, this member should be set to FALSE. </p>
</dd>

### -field <b>uInfraNumSupportedMcastMgmtAlgoPairs</b>

<dd>
<p>The length of the array of authentication and cipher algorithm pairs pointed to in <b>pInfraSupportedMcastMgmtAlgoPairs</b>.</p>
</dd>

### -field <b>pInfraSupportedMcastMgmtAlgoPairs</b>

<dd>
<p>A pointer to an array of authentication and cipher algorithm pair which the device supports for MFP in Infra mode. The recommended cipher for Windows 8 is BIP with WPA or WPA2 authentication. Each entry in the array is
     formatted as a 
     <a href="..\wlantypes\ns-wlantypes-dot11-auth-cipher-pair.md">
     DOT11_AUTH_CIPHER_PAIR</a> structure.</p>
</dd>
</dl>

## -remarks
<p>The 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-native-802-11-attributes.md">
    NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES</a> structure contains a member (<b>pExtSTAAttributes</b>) that specifies the address of a DOT11_EXTSTA_ATTRIBUTES structure. When the
    miniport driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>,
    the driver sets the 
    <i>MiniportAttributes</i> parameter to the address of a driver-allocated block of memory which contains an
    NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES structure along with the DOT11_EXTSTA_ATTRIBUTES
    structure.</p>

<p>Management Frame Protection Required (MFPR) enforcement on Windows 8 is not supported. Hence miniport drivers should never set this bit in the RSN capabilities of RSN IE during an association request. For policy,  the access point may advertise MFPR which will allow MFP-capable STA to associate. Access points not supporting MFP capability will fail association. If MFPR is set by an access point and STA is not MFP capable, Windows 8 will treat the network as mismatched in capability and not send an association request to the miniport.</p>

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
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547659">DOT11_AUTH_CIPHER_PAIR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547672">DOT11_CIPHER_ALGORITHM</a>
</dt>
<dt>
<a href="netvista.dot11_country_or_region_string">
   DOT11_COUNTRY_OR_REGION_STRING</a>
</dt>
<dt>
<a href="netvista.extensible_station_operation_mode">Extensible Station Operation
   Mode</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-native-802-11-attributes.md">
   NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="netvista.oid_dot11_cipher_key_mapping_key">
   OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569141">OID_DOT11_DESIRED_BSSID_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569145">OID_DOT11_DESIRED_SSID_LIST</a>
</dt>
<dt>
<a href="netvista.oid_dot11_excluded_mac_address_list">
   OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569400">OID_DOT11_PMKID_LIST</a>
</dt>
<dt>
<a href="netvista.oid_dot11_privacy_exemption_list">
   OID_DOT11_PRIVACY_EXEMPTION_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569412">OID_DOT11_SAFE_MODE_ENABLED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a>
</dt>
<dt>
<a href="NULL">Per-Station Default Keys</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_EXTSTA_ATTRIBUTES structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
