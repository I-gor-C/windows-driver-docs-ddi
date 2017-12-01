---
UID: NS.windot11.DOT11_CIPHER_DEFAULT_KEY_VALUE
title: DOT11_CIPHER_DEFAULT_KEY_VALUE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_cipher_default_key_value.htm
old-project: netvista
ms.assetid: 7362b20a-6ec4-4b22-8981-3a4b647a3cfa
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DOT11_CIPHER_DEFAULT_KEY_VALUE, DOT11_CIPHER_DEFAULT_KEY_VALUE, *PDOT11_CIPHER_DEFAULT_KEY_VALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8 and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_CIPHER_DEFAULT_KEY_VALUE
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

# DOT11_CIPHER_DEFAULT_KEY_VALUE structure



## -description

## -syntax

````
typedef struct DOT11_CIPHER_DEFAULT_KEY_VALUE {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  uKeyIndex;
  DOT11_CIPHER_ALGORITHM AlgorithmId;
  DOT11_MAC_ADDRESS      MacAddr;
  BOOLEAN                bDelete;
  BOOLEAN                bStatic;
  USHORT                 usKeyLength;
  UCHAR                  ucKey[1];
} DOT11_CIPHER_DEFAULT_KEY_VALUE, *PDOT11_CIPHER_DEFAULT_KEY_VALUE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_CIPHER_DEFAULT_KEY_VALUE structure. This member is
     formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <i>Header</i> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b>

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b>

<dd>
<p>This member must be set to DOT11_CIPHER_DEFAULT_KEY_VALUE_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       <code>sizeof(DOT11_CIPHER_DEFAULT_KEY_VALUE)</code>.</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uKeyIndex</b>

<dd>
<p>The index of the key in the 802.11 station's default key array. 
     </p>
<p>For standard 802.11 cipher algorithms, 
     <b>uKeyIndex</b> must be from 0 through 3. For a cipher algorithm developed by an IHV, 
     <b>uKeyIndex</b> can be any value within the range defined by the IHV.</p>
<p>For BIP <b>uKeyIndex</b> must be 4 or 5.</p>
<p>The IEEE 802.11-2012 standard defines default key index values from 1 through 4. The value 
     <i>x</i> specified by this member maps to the 802.11 default key index 
     (<i>x</i> + 1).</p>
</dd>

### -field <b>AlgorithmId</b>

<dd>
<p>The value of the cipher algorithm that uses this key. For more information about values for cipher
     algorithms, see 
     <a href="..\wlantypes\ne-wlantypes--dot11-cipher-algorithm.md">DOT11_CIPHER_ALGORITHM</a>.
     </p>
<p>For BIP, this should be set to DOT11_CIPHER_ALGO_BIP to pre-set the initial IGTK packet number.</p>
<p>The miniport driver must ignore this member if 
     <b>bDelete</b> is <b>TRUE</b>.</p>
</dd>

### -field <b>MacAddr</b>

<dd>
<p>The media access control (MAC) address, which identifies the default key table to add or remove
     the key.
     </p>
<p>If the 
     <b>dot11DesiredBSSType</b> management information base (MIB) object is set to 
     <b>dot11_BSS_type_infrastructure</b>, the 802.11 station adds or removes the key from the default key
     table regardless of the value of the 
     <b>MacAddr</b> member. If the key is dynamically obtained from the access point (AP) the station is
     associated with, the 
     <b>MacAddr</b> member will contain the AP's MAC address. Otherwise, 
     <b>MacAddr</b> will have a value of 0x000000000000.</p>
<p>If the 
     <b>dot11DesiredBSSType</b> management information base (MIB) object is set to 
     <b>dot11_BSS_type_independent</b>, the 802.11 station must add or remove the key in the following
     way:</p>
<ul>
<li>
<p>If the value of this member is 0x000000000000, the 802.11 station adds or removes the key from the
       default key table. When the NIC is in the Extensible Access Point (ExtAP) OP mode, this value is
       zero.</p>
</li>
<li>
<p>If the value of this member is a valid unicast MAC address, the 802.11 station adds or removes the
       key from the per-station default key table for the peer station in an independent BSS (IBSS) network
       with a MAC address equal to the value of 
       <b>MacAddr</b> .</p>
<p>If a per-station default key table does not exist for the value of 
       <b>MacAddr</b>, the 802.11 station must use any unused per-station default key table.</p>
</li>
</ul>
<p>For more information about the 
     <b>dot11DesiredBSSType</b> MIB object, see 
     <a href="netvista.oid_dot11_desired_bss_type">
     OID_DOT11_DESIRED_BSS_TYPE</a>.</p>
</dd>

### -field <b>bDelete</b>

<dd>
<p>A Boolean value that specifies whether the miniport driver should delete the default key.
     </p>
<p>If set to <b>TRUE</b>, the miniport driver must delete the default key referenced by 
     <b>uKeyIndex</b>. If set to <b>FALSE</b>, the miniport driver must add or update the default key referenced by 
     <b>uKeyIndex</b> .</p>
</dd>

### -field <b>bStatic</b>

<dd>
<p>A Boolean value that specifies whether the miniport driver should delete the default key following
     a connection or roaming operation.
     </p>
<p>If set to <b>FALSE</b>, the miniport driver must delete the default key referenced by 
     <b>uKeyIndex</b> whenever the 802.11 station:</p>
<ul>
<li>
<p>Disconnects from the basic service set (BSS) network.</p>
</li>
<li>
<p>Roams to a new BSS network.</p>
</li>
<li>
<p>Reconnects to the same BSS network.</p>
</li>
</ul>
<p>If set to <b>TRUE</b>, the default key referenced by 
     <b>uKeyIndex</b> must not be deleted unless it is:</p>
<ul>
<li>
<p>Explicitly deleted through a set request of 
       <a href="netvista.oid_dot11_cipher_default_key">
       OID_DOT11_CIPHER_DEFAULT_KEY</a>.</p>
</li>
<li>
<p>Implicitly deleted through a method request of 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569409">OID_DOT11_RESET_REQUEST</a>.</p>
</li>
</ul>
</dd>

### -field <b>usKeyLength</b>

<dd>
<p>The length, in bytes, of the key material in the 
     <b>ucKey</b> array.</p>
</dd>

### -field <b>ucKey</b>

<dd>
<p>The key material. 
     </p>
<p>If 
     <b>AlgorithmId</b> is set to 
     <b>DOT11_CIPHER_ALGO_TKIP</b>, the 
     <b>ucKey</b> array defines the key material through the 
     <a href="..\windot11\ns-windot11-dot11-key-algo-tkip-mic.md">
     DOT11_KEY_ALGO_TKIP_MIC</a> structure.</p>
<p>If 
     <b>AlgorithmId</b> is set to 
     <b>DOT11_CIPHER_ALGO_CCMP</b>, the 
     <b>ucKey</b> array defines the key material through the
     <a href="..\windot11\ns-windot11-dot11-key-algo-ccmp.md">
     DOT11_KEY_ALGO_CCMP</a> structure.</p>
<p>If 
     <b>AlgorithmId</b> is set to 
     <b>DOT11_CIPHER_ALGO_BIP</b>, the 
     <b>ucKey</b> array defines the key material through the
     
     <a href="..\windot11\ns-windot11-dot11-key-algo-bip.md">DOT11_KEY_ALGO_BIP</a> structure.</p>
</dd>
</dl>

## -remarks
<p>If the 
    <b>bDelete</b> member is <b>TRUE</b>, the following members are not valid and must be ignored:</p>

<p><b>bStatic</b></p>

<p><b>usKeyLength</b></p>

<p><b>ucKey</b></p>

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
<a href="..\wlantypes\ne-wlantypes--dot11-cipher-algorithm.md">DOT11_CIPHER_ALGORITHM</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-key-algo-ccmp.md">DOT11_KEY_ALGO_CCMP</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11-key-algo-tkip-mic.md">DOT11_KEY_ALGO_TKIP_MIC</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569119">OID_DOT11_CIPHER_DEFAULT_KEY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569142">OID_DOT11_DESIRED_BSS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569409">OID_DOT11_RESET_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_CIPHER_DEFAULT_KEY_VALUE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
