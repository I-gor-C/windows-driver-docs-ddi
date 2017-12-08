---
UID: NS.windot11._DOT11_MAC_ADDRESS
title: DOT11_MAC_ADDRESS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_mac_address.htm
old-project: netvista
ms.assetid: 6b2b17fd-3695-4598-8d9a-be28e1bc5b53
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_MAC_ADDRESS, DOT11_MAC_ADDRESS, *PDOT11_MAC_ADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_MAC_ADDRESS
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

# DOT11_MAC_ADDRESS structure



## -description

## -syntax

````
typedef struct _DOT11_MAC_ADDRESS {
  UCHAR ucDot11MacAddress[6];
} DOT11_MAC_ADDRESS, *PDOT11_MAC_ADDRESS;
````


## -struct-fields
<dl>

### -field ucDot11MacAddress

<dd>
<p>The MAC address in unicast, multicast, or broadcast format.</p>
</dd>
</dl>

## -remarks
<p>A unicast MAC address uniquely identifies a station on a WLAN. A MAC address is defined as a unicast
    address if the following is true:</p>

<p>A multicast MAC address uniquely identifies a group of stations on a WLAN. A MAC address is defined as
    a multicast address if the following is true:</p>

<p>A broadcast MAC address identifies all stations on a WLAN. The broadcast MAC address is
    0xFFFFFFFFFFFF.</p>

<p>The PDOT11_MAC_ADDRESS type is defined as a pointer to the DOT11_MAC_ADDRESS type as follows:</p>

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

## -see-also
<dl>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11extihv-stop-post-associate.md">
   Dot11ExtIhvStopPostAssociate</a>
</dt>
<dt>
<a href="..\wlanihv\nc-wlanihv-dot11ext-post-associate-completion.md">
   Dot11ExtPostAssociateCompletion</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-association-completion-parameters.md">
   DOT11_ASSOCIATION_COMPLETION_PARAMETERS</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-bss-entry.md">DOT11_BSS_ENTRY</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-disassociation-parameters.md">
   DOT11_DISASSOCIATION_PARAMETERS</a>
</dt>
<dt>
<a href="..\wlclient\ns-wlclient--dot11-port-state.md">DOT11_PORT_STATE</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-roaming-completion-parameters.md">
   DOT11_ROAMING_COMPLETION_PARAMETERS</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11--dot11-scan-request-v2.md">DOT11_SCAN_REQUEST_V2</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_association_start">
   NDIS_STATUS_DOT11_ASSOCIATION_START</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_connection_start">
   NDIS_STATUS_DOT11_CONNECTION_START</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_disassociation">
   NDIS_STATUS_DOT11_DISASSOCIATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567344">NDIS_STATUS_DOT11_LINK_QUALITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567360">NDIS_STATUS_DOT11_ROAMING_START</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_tkipmic_failure">
   NDIS_STATUS_DOT11_TKIPMIC_FAILURE</a>
</dt>
<dt>
<a href="netvista.oid_dot11_cipher_key_mapping_key">
   OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569125">OID_DOT11_CURRENT_ADDRESS</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-cipher-default-key-value.md">
   DOT11_CIPHER_DEFAULT_KEY_VALUE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569141">OID_DOT11_DESIRED_BSSID_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569359">OID_DOT11_ENUM_ASSOCIATION_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569360">OID_DOT11_ENUM_BSS_LIST</a>
</dt>
<dt>
<a href="netvista.oid_dot11_excluded_mac_address_list">
   OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569400">OID_DOT11_PMKID_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569409">OID_DOT11_RESET_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569413">OID_DOT11_SCAN_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569419">OID_DOT11_STATION_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_MAC_ADDRESS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
