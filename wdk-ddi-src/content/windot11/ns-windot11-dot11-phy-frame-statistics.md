---
UID: NS.windot11.DOT11_PHY_FRAME_STATISTICS
title: DOT11_PHY_FRAME_STATISTICS
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_phy_frame_statistics.htm
ms.assetid: 2adf102b-52aa-40e4-b3de-9189803339bf
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_PHY_FRAME_STATISTICS
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
ms.keywords: DOT11_PHY_FRAME_STATISTICS, DOT11_PHY_FRAME_STATISTICS, *PDOT11_PHY_FRAME_STATISTICS
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_PHY_FRAME_STATISTICS structure



## -description

## -syntax

````
typedef struct DOT11_PHY_FRAME_STATISTICS {
  ULONGLONG ullTransmittedFrameCount;
  ULONGLONG ullMulticastTransmittedFrameCount;
  ULONGLONG ullFailedCount;
  ULONGLONG ullRetryCount;
  ULONGLONG ullMultipleRetryCount;
  ULONGLONG ullMaxTXLifetimeExceededCount;
  ULONGLONG ullTransmittedFragmentCount;
  ULONGLONG ullRTSSuccessCount;
  ULONGLONG ullRTSFailureCount;
  ULONGLONG ullACKFailureCount;
  ULONGLONG ullReceivedFrameCount;
  ULONGLONG ullMulticastReceivedFrameCount;
  ULONGLONG ullPromiscuousReceivedFrameCount;
  ULONGLONG ullMaxRXLifetimeExceededCount;
  ULONGLONG ullFrameDuplicateCount;
  ULONGLONG ullReceivedFragmentCount;
  ULONGLONG ullPromiscuousReceivedFragmentCount;
  ULONGLONG ullFCSErrorCount;
} DOT11_PHY_FRAME_STATISTICS, *PDOT11_PHY_FRAME_STATISTICS;
````


## -struct-fields
<dl>

### -field <b>ullTransmittedFrameCount</b>

<dd>
<p>The number of MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has
     successfully transmitted.</p>
</dd>

### -field <b>ullMulticastTransmittedFrameCount</b>

<dd>
<p>The number of multicast or broadcast MSDU packets and MMPDU frames that the IEEE PHY layer of the
     802.11 station has successfully transmitted.</p>
</dd>

### -field <b>ullFailedCount</b>

<dd>
<p>The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit after
     exceeding the retry limits defined by the 802.11 IEEE 
     <b>dot11ShortRetryLimit</b> or 
     <b>dot11LongRetryLimit</b> MIB counters. For more information about these MIB counters, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569415">OID_DOT11_SHORT_RETRY_LIMIT</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569380">OID_DOT11_LONG_RETRY_LIMIT</a>.</p>
</dd>

### -field <b>ullRetryCount</b>

<dd>
<p>The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after
     one or more attempts.</p>
</dd>

### -field <b>ullMultipleRetryCount</b>

<dd>
<p>The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after
     more than one retransmission attempt. 
     </p>
<p>For MSDU packets, the miniport driver must increment this counter for each packet that was
     transmitted successfully after one or more of its MPDU fragments required retransmission.</p>
</dd>

### -field <b>ullMaxTXLifetimeExceededCount</b>

<dd>
<p>The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit because of
     a timeout as defined by the IEEE 802.11 
     <b>dot11MaxTransmitMSDULifetime</b> MIB object. For more information about this MIB object, see 
     <a href="netvista.oid_dot11_max_transmit_msdu_lifetime">
     OID_DOT11_MAX_TRANSMIT_MSDU_LIFETIME</a>.</p>
</dd>

### -field <b>ullTransmittedFragmentCount</b>

<dd>
<p>The number of MPDU frames that the 802.11 station transmitted and acknowledged through a received
     802.11 ACK frame.</p>
</dd>

### -field <b>ullRTSSuccessCount</b>

<dd>
<p>The number of times that the 802.11 station received a Clear To Send (CTS) frame in response to a
     Request To Send (RTS) frame.</p>
</dd>

### -field <b>ullRTSFailureCount</b>

<dd>
<p>The number of times that the 802.11 station did not receive a CTS frame in response to an RTS
     frame.</p>
</dd>

### -field <b>ullACKFailureCount</b>

<dd>
<p>The number of times that the 802.11 station expected and did not receive an Acknowledgement (ACK)
     frame.</p>
</dd>

### -field <b>ullReceivedFrameCount</b>

<dd>
<p>The total number of MSDU packets and MMPDU frames that the 802.11 station has successfully
     received.
     </p>
<p>For MSDU packets, the miniport driver must increment this counter for each packet whose MPDU
     fragments were received and passed frame check sequence (FCS) verification and replay detection. The
     miniport driver must increment this member regardless of whether the received MSDU packet or MPDU
     fragment fail MAC-layer cipher decryption.</p>
<p>This counter is optional. If the NIC does not support this counter, the miniport driver should set
     this member to DOT11_STATISTICS_UNKNOWN.</p>
</dd>

### -field <b>ullMulticastReceivedFrameCount</b>

<dd>
<p>The number of multicast or broadcast MSDU packets and MMPDU frames that the 802.11 station has
     successfully received.
     </p>
<p>For MSDU packets, the miniport driver must increment this counter for each packet whose MPDU
     fragments were received and passed FCS verification and replay detection. The miniport driver must
     increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer
     cipher decryption.</p>
<p>This counter is optional. If the NIC does not support this counter, the miniport driver should set
     this member to DOT11_STATISTICS_UNKNOWN.</p>
</dd>

### -field <b>ullPromiscuousReceivedFrameCount</b>

<dd>
<p>The number of MSDU packets or MMPDU frames received by the 802.11 station when a promiscuous
     packet filter is enabled. For more information about packet filters, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569575">OID_GEN_CURRENT_PACKET_FILTER</a>.
     </p>
<p>If a promiscuous packet filter is enabled, the miniport driver must only increment this counter for
     received MSDU packets or MMPDU frames that would have been rejected if the filter was not enabled. The
     driver must not increment this counter for:</p>
<ul>
<li>
<p>Unicast MSDU packets or MMPDU frames with a destination MAC address that matches the 802.11
       station's MAC address.</p>
</li>
<li>
<p>Multicast or broadcast MSDU packets or MMPDU frames with a destination MAC address that matches an
       entry in the multicast address list of the 802.11 station. For more information about the multicast
       address list, see 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569388">OID_DOT11_MULTICAST_LIST</a>.</p>
</li>
</ul>
</dd>

### -field <b>ullMaxRXLifetimeExceededCount</b>

<dd>
<p>The number if MSDU packets and MMPDU frames that the 802.11 station discarded because of a timeout
     as defined by the IEEE 802.11 
     <b>dot11MaxReceiveLifetime</b> MIB object. For more information about this MIB object, see 
     <a href="netvista.oid_dot11_max_receive_lifetime">
     OID_DOT11_MAX_RECEIVE_LIFETIME</a>.</p>
</dd>

### -field <b>ullFrameDuplicateCount</b>

<dd>
<p>The number of duplicate MPDU frames that the 802.11 station received. The 802.11 station
     determines duplicate frames through the Sequence Control field of the 802.11 MAC header.</p>
</dd>

### -field <b>ullReceivedFragmentCount</b>

<dd>
<p>The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames.</p>
</dd>

### -field <b>ullPromiscuousReceivedFragmentCount</b>

<dd>
<p>The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames when a
     promiscuous packet filter was enabled. For more information about packet filters, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569575">OID_GEN_CURRENT_PACKET_FILTER</a>.
     </p>
<p>If a promiscuous packet filter is enabled, the miniport driver must only increment this counter for
     received MPDU frames that would have been rejected if the filter was not enabled. The driver must not
     increment this counter for:</p>
<ul>
<li>
<p>Unicast MPDU frames with a destination MAC address that matches the 802.11 station's MAC
       address.</p>
</li>
<li>
<p>Multicast or broadcast MPDU frames with a destination MAC address that matches an entry in the
       multicast address list of the 802.11 station. For more information about the multicast address list,
       see 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff569388">OID_DOT11_MULTICAST_LIST</a>.</p>
</li>
</ul>
</dd>

### -field <b>ullFCSErrorCount</b>

<dd>
<p>The number of MPDU frames that the 802.11 station received with FCS errors.</p>
</dd>
</dl>

## -remarks
<p>The members of this structure are used to record PHY-level statistics for:</p>

<p>802.11 MSDU packets.</p>

<p>802.11 MMPDU frames.</p>

<p>802.11 MPDU frames. MPDU frame counters must include all MPDU fragments sent for an MSDU packet or
      MMPDU frame</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548779">DOT11_STATISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569420">OID_DOT11_STATISTICS</a>
</dt>
<dt>
<a href="NULL">Native 802.11 Statistics</a>
</dt>
<dt>
<a href="netvista.extensible_station_phy_statistics">Extensible Station PHY
   Statistics</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_PHY_FRAME_STATISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
