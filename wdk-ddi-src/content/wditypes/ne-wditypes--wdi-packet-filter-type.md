---
UID: NE.wditypes._WDI_PACKET_FILTER_TYPE
title: WDI_PACKET_FILTER_TYPE
author: windows-driver-content
description: The WDI_PACKET_FILTER_TYPE enumeration defines the packet filter types.
old-location: netvista\wdi_packet_filter_type.htm
old-project: netvista
ms.assetid: 252CE7F6-2DA7-45F8-97F0-85B51A0181C2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_PACKET_FILTER_TYPE
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
req.iface: 
req.product: Windows 10 or later.
---

# WDI_PACKET_FILTER_TYPE enumeration



## -description
<p>The WDI_PACKET_FILTER_TYPE enumeration defines the packet filter types.</p>


## -syntax

````
typedef enum _WDI_PACKET_FILTER_TYPE { 
  WDI_PACKET_FILTER_NONE                       = 0x00000000,
  WDI_PACKET_FILTER_DIRECTED                   = 0x00000001,
  WDI_PACKET_FILTER_MULTICAST                  = 0x00000002,
  WDI_PACKET_FILTER_ALL_MULTICAST              = 0x00000004,
  WDI_PACKET_FILTER_BROADCAST                  = 0x00000008,
  WDI_PACKET_FILTER_PROMISCUOUS                = 0x00000020,
  WDI_PACKET_FILTER_802_11_RAW_DATA            = 0x00010000,
  WDI_PACKET_FILTER_802_11_DIRECTED_MGMT       = 0x00020000,
  WDI_PACKET_FILTER_802_11_BROADCAST_MGMT      = 0x00040000,
  WDI_PACKET_FILTER_802_11_MULTICAST_MGMT      = 0x00080000,
  WDI_PACKET_FILTER_802_11_ALL_MULTICAST_MGMT  = 0x00100000,
  WDI_PACKET_FILTER_802_11_PROMISCUOUS_MGMT    = 0x00200000,
  WDI_PACKET_FILTER_802_11_RAW_MGMT            = 0x00400000,
  WDI_PACKET_FILTER_802_11_DIRECTED_CTRL       = 0x00800000,
  WDI_PACKET_FILTER_802_11_BROADCAST_CTRL      = 0x01000000,
  WDI_PACKET_FILTER_802_11_PROMISCUOUS_CTRL    = 0x02000000,
  WDI_PACKET_FILTER_ALL                        = WDI_PACKET_FILTER_802_11_PROMISCUOUS_CTRL 
                    | WDI_PACKET_FILTER_802_11_BROADCAST_CTRL
                    | WDI_PACKET_FILTER_802_11_DIRECTED_CTRL
                    | WDI_PACKET_FILTER_802_11_RAW_MGMT
                    | WDI_PACKET_FILTER_802_11_PROMISCUOUS_MGMT
                    | WDI_PACKET_FILTER_802_11_ALL_MULTICAST_MGMT
                    | WDI_PACKET_FILTER_802_11_MULTICAST_MGMT
                    | WDI_PACKET_FILTER_802_11_BROADCAST_MGMT
                    | WDI_PACKET_FILTER_802_11_DIRECTED_MGMT
                    | WDI_PACKET_FILTER_802_11_RAW_DATA
                    | WDI_PACKET_FILTER_PROMISCUOUS
                    | WDI_PACKET_FILTER_BROADCAST
                    | WDI_PACKET_FILTER_ALL_MULTICAST
                    | WDI_PACKET_FILTER_MULTICAST
                    | WDI_PACKET_FILTER_DIRECTED
} WDI_PACKET_FILTER_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WDI_PACKET_FILTER_NONE"></a><a id="wdi_packet_filter_none"></a><b>WDI_PACKET_FILTER_NONE</b>

<dd>
<p>None.</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_DIRECTED"></a><a id="wdi_packet_filter_directed"></a><b>WDI_PACKET_FILTER_DIRECTED</b>

<dd>
<p>Directed packets. Directed packets contain a destination address equal to the station address of the NIC.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_MULTICAST"></a><a id="wdi_packet_filter_multicast"></a><b>WDI_PACKET_FILTER_MULTICAST</b>

<dd>
<p>Multicast address packets sent to addresses in the multicast address list. 

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_ALL_MULTICAST"></a><a id="wdi_packet_filter_all_multicast"></a><b>WDI_PACKET_FILTER_ALL_MULTICAST</b>

<dd>
<p>All multicast address packets, not just the ones enumerated in the multicast address list.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_BROADCAST"></a><a id="wdi_packet_filter_broadcast"></a><b>WDI_PACKET_FILTER_BROADCAST</b>

<dd>
<p>Broadcast packets.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_PROMISCUOUS"></a><a id="wdi_packet_filter_promiscuous"></a><b>WDI_PACKET_FILTER_PROMISCUOUS</b>

<dd>
<p>Specifies all packets regardless of whether VLAN filtering is enabled or not and whether the VLAN identifier matches or not.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_RAW_DATA"></a><a id="wdi_packet_filter_802_11_raw_data"></a><b>WDI_PACKET_FILTER_802_11_RAW_DATA</b>

<dd>
<p>An 802.11 media access control (MAC) protocol data unit (MPDU) frame, which contains all of the data in the format received by the 802.11 station. When this filter is set, the driver must indicate every unmodified MPDU fragment before it indicates the MAC service data unit (MSDU) packet reassembled from the MPDU fragments. 

</p>
<p>If an MPDU fragment is encrypted, it must not decrypt the fragment before it is indicated. However, the miniport driver must decrypt each MPDU fragment before reassembling and indicating the MSDU packet.

</p>
<p>If enabled, this filter type only affects other standard packet filters, such as WDI_PACKET_FILTER_DIRECTED or WDI_PACKET_FILTER_BROADCAST.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_DIRECTED_MGMT"></a><a id="wdi_packet_filter_802_11_directed_mgmt"></a><b>WDI_PACKET_FILTER_802_11_DIRECTED_MGMT</b>

<dd>
<p>Directed 802.11 management packets. Directed packets contain a destination address equal to the station address of the NIC.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_BROADCAST_MGMT"></a><a id="wdi_packet_filter_802_11_broadcast_mgmt"></a><b>WDI_PACKET_FILTER_802_11_BROADCAST_MGMT</b>

<dd>
<p>Broadcast 802.11 management packets received by the 802.11 station.</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_MULTICAST_MGMT"></a><a id="wdi_packet_filter_802_11_multicast_mgmt"></a><b>WDI_PACKET_FILTER_802_11_MULTICAST_MGMT</b>

<dd>
<p>Multicast 802.11 management packets sent to addresses in the multicast address list.</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_ALL_MULTICAST_MGMT"></a><a id="wdi_packet_filter_802_11_all_multicast_mgmt"></a><b>WDI_PACKET_FILTER_802_11_ALL_MULTICAST_MGMT</b>

<dd>
<p>All multicast 802.11 management packets received by the 802.11 station, regardless of whether the destination address in the 802.11 MAC header is in the multicast address list.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_PROMISCUOUS_MGMT"></a><a id="wdi_packet_filter_802_11_promiscuous_mgmt"></a><b>WDI_PACKET_FILTER_802_11_PROMISCUOUS_MGMT</b>

<dd>
<p>All 802.11 management packets received by the 802.11 station.</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_RAW_MGMT"></a><a id="wdi_packet_filter_802_11_raw_mgmt"></a><b>WDI_PACKET_FILTER_802_11_RAW_MGMT</b>

<dd>
<p>An 802.11 MPDU management frame, which contains all of the data in the format received by the 802.11 station. When this filter is set, the driver must indicate every unmodified MPDU fragment before it indicates the MAC management protocol data unit (MMPDU) packet reassembled from the MPDU fragments. 

</p>
<p>If enabled, this filter type only affects other 802.11 management packet filters, such as WDI_PACKET_FILTER_802_11_DIRECTED_MGMT or WDI_PACKET_FILTER_802_11_MULTICAST_MGMT.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_DIRECTED_CTRL"></a><a id="wdi_packet_filter_802_11_directed_ctrl"></a><b>WDI_PACKET_FILTER_802_11_DIRECTED_CTRL</b>

<dd>
<p>Directed 802.11 control packets. Directed packets contain a destination address equal to the station address of the NIC.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_BROADCAST_CTRL"></a><a id="wdi_packet_filter_802_11_broadcast_ctrl"></a><b>WDI_PACKET_FILTER_802_11_BROADCAST_CTRL</b>

<dd>
<p>Broadcast 802.11 control packets received by the 802.11 station.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_802_11_PROMISCUOUS_CTRL"></a><a id="wdi_packet_filter_802_11_promiscuous_ctrl"></a><b>WDI_PACKET_FILTER_802_11_PROMISCUOUS_CTRL</b>

<dd>
<p>All 802.11 control packets received by the 802.11 station.

</p>
</dd>

### -field <a id="WDI_PACKET_FILTER_ALL"></a><a id="wdi_packet_filter_all"></a><b>WDI_PACKET_FILTER_ALL</b>

<dd>
<p>All packet types.</p>
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