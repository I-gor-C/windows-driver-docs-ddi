---
UID: NS.windot11.DOT11_STATISTICS
title: DOT11_STATISTICS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_statistics.htm
old-project: netvista
ms.assetid: 714ad442-596b-4e67-82ce-a50e1808a3af
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_STATISTICS, DOT11_STATISTICS, *PDOT11_STATISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_STATISTICS
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

# DOT11_STATISTICS structure



## -description

## -syntax

````
typedef struct DOT11_STATISTICS {
  NDIS_OBJECT_HEADER         Header;
  ULONGLONG                  ullFourWayHandshakeFailures;
  ULONGLONG                  ullTKIPCounterMeasuresInvoked;
  ULONGLONG                  ullReserved;
  DOT11_MAC_FRAME_STATISTICS MacUcastCounters;
  DOT11_MAC_FRAME_STATISTICS MacMcastCounters;
  DOT11_PHY_FRAME_STATISTICS PhyCounters[1];
} DOT11_STATISTICS, *PDOT11_STATISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_STATISTICS structure. This member is formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a>Type

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a>Revision

<dd>
<p>This member must be set to DOT11_STATISTICS_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a>Size

<dd>
<p>This member must be set to 
       sizeof(DOT11_STATISTICS).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>ullFourWayHandshakeFailures</b>

<dd>
<p>The number of four-way handshake failures that the 802.11 station encountered during Wi-Fi
     Protected Access (WPA) or Robust Security Network Association (RSNA) authentication.
     </p>
<p>If the 802.11 station is not performing the WPA or RSNA authentication, it should set this member to
     DOT11_STATISTICS_UNKNOWN.</p>
</dd>

### -field <b>ullTKIPCounterMeasuresInvoked</b>

<dd>
<p>The number of times that the 802.11 station invoked countermeasures following a message integrity
     code (MIC) failure.
     </p>
<p>If the 802.11 station is not performing TKIP countermeasures, it should set this member to
     DOT11_STATISTICS_UNKNOWN.</p>
</dd>

### -field <b>ullReserved</b>

<dd>
<p>This member is reserved for use by the operating system. The miniport driver must not write to
     this member.</p>
</dd>

### -field <b>MacUcastCounters</b>

<dd>
<p>The MAC layer counters based on unicast packets sent or received by the 802.11 station. The data
     structure for this member is the 
     <a href="..\windot11\ns-windot11-dot11-mac-frame-statistics.md">
     DOT11_MAC_FRAME_STATISTICS</a> structure.
     </p>
<div class="alert"><b>Note</b>  <p class="note"> Counters for received unicast packets must only be incremented for those packets with a
     destination MAC address in the 802.11 MAC header that matches the 802.11 station's MAC
     address.</p>
</div>
<div> </div>
</dd>

### -field <b>MacMcastCounters</b>

<dd>
<p>The MAC layer counters based on multicast or broadcast packets sent or received by the 802.11
     station. The data structure for this member is the 
     <a href="..\windot11\ns-windot11-dot11-mac-frame-statistics.md">
     DOT11_MAC_FRAME_STATISTICS</a> structure.
     </p>
<div class="alert"><b>Note</b>  <p class="note"> Counters for received multicast or broadcast packets must only be incremented for those
     packets with a destination MAC address in the 802.11 MAC header that matches an entry in the multicast
     address list of the 802.11 station. For more information about the multicast address list, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569388">OID_DOT11_MULTICAST_LIST</a>.</p>
</div>
<div> </div>
</dd>

### -field <b>PhyCounters</b>

<dd>
<p>An array of PHY layer counters. Each entry in this array is formatted as a 
     <a href="..\windot11\ns-windot11-dot11-phy-frame-statistics.md">
     DOT11_PHY_FRAME_STATISTICS</a> structure.
     </p>
<p>The miniport driver must maintain an entry within the 
     <b>PhyCounters</b> array for each supported PHY. If the 802.11 station supports multiple PHYs of the same
     type, the miniport driver must create separate entries for each.</p>
<p>Entries within the 
     <b>PhyCounters</b> array must be in the same order as the list of supported PHYs that the driver returns
     when queried by 
     <a href="netvista.oid_dot11_supported_phy_types">
     OID_DOT11_SUPPORTED_PHY_TYPES</a>.</p>
</dd>
</dl>

## -remarks
<p>The miniport driver must unconditionally set all of the counters in the DOT11_STATISTICS structure to
    zero, including MAC-layer and PHY-layer counters, when one of the following occurs:</p>

<p>The driver's 
      <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function is
      called.</p>

<p>The driver's 
      <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function is
      called with an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569409">OID_DOT11_RESET_REQUEST</a>,
      regardless of the type of reset operation specified in the set request.</p>

<p>For more information about the statistics gathered by a Native 802.11 miniport driver, see 
    <a href="NULL">Native 802.11 Statistics</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569420">OID_DOT11_STATISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_STATISTICS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
