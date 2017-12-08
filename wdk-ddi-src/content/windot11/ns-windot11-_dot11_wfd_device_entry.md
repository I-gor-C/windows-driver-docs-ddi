---
UID: NS.WINDOT11._DOT11_WFD_DEVICE_ENTRY
title: _DOT11_WFD_DEVICE_ENTRY
author: windows-driver-content
description: The DOT11_WFD_DEVICE_ENTRY structure contains information about a discovered Wi-Fi Direct (WFD) device, a discovered WFD Group Owner (GO), or or a discovered infrastructure access point.
old-location: netvista\_dot11_wfd_device_entry.htm
old-project: netvista
ms.assetid: 548A40F7-1C02-4BF0-8F78-EB8C3C97CEB4
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DOT11_WFD_DEVICE_ENTRY, *PDOT11_WFD_DEVICE_ENTRY, DOT11_WFD_DEVICE_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_WFD_DEVICE_ENTRY
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
req.product: Windows 10 or later.
---

# _DOT11_WFD_DEVICE_ENTRY structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_DEVICE_ENTRY {
  ULONG                             uPhyId;
  DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO PhySpecificInfo;
  DOT11_MAC_ADDRESS                 dot11BSSID;
  DOT11_BSS_TYPE                    dot11BSSType;
  DOT11_MAC_ADDRESS                 TransmitterAddress;
  LONG                              lRSSI;
  ULONG                             uLinkQuality;
  USHORT                            usBeaconPeriod;
  ULONGLONG                         ullTimestamp;
  ULONGLONG                         ullBeaconHostTimestamp;
  ULONGLONG                         ullProbeResponseHostTimestamp;
  USHORT                            usCapabilityInformation;
  ULONG                             uBeaconIEsOffset;
  ULONG                             uBeaconIEsLength;
  ULONG                             uProbeResponseIEsOffset;
  ULONG                             uProbeResponseIEsLength;
}  DOT11_WFD_DEVICE_ENTRY, *PDOT11_WFD_DEVICE_ENTRY;
````


## -struct-fields

### -field uPhyId

The identifer of the PHY the miniport used to detect the device. This identifier is in the index range of the list of supported PHYs returned from an <a href="https://msdn.microsoft.com/library/windows/hardware/ff569426">OID_DOT11_SUPPORTED_PHY_TYPES</a> query request. This identifer cannot be <b>DOT_PHY_ID_ANY</b>.

### -field PhySpecificInfo

The attributes of the PHY identified by <b>uPhyId</b>.

### -field dot11BSSID

The MAC address of the device that sent the beacon or probe response packet during a discovery.

### -field dot11BSSType

The BSS network type. This member is set to <b>dot11_BSS_type_infrastructure</b> for all discovered WFD devices and WFD GOs.

### -field TransmitterAddress

The MAC address for the transmitter of the device that sent the beacon or probe response packet during a discovery.

### -field lRSSI

The recieved signal strength indicator value of the discovered device. The units for this value are in decibels referenced to 1 milliwatt (dBm).

### -field uLinkQuality

Link quality value ranging from 0 to 100. A value of 100 indicates highest link quality.

### -field usBeaconPeriod

The value received from the beacon interval field of the most recent beacon or probe response packet.

### -field ullTimestamp

The value received from the timestamp field of the most recent beacon or probe response packet.

### -field ullBeaconHostTimestamp

The timestamp, determined by a value returned from <a href="netvista.ndisgetcurrentsystemtime">NdisGetCurrentSystemTime</a>, recording the time when the beacon packet was received.

### -field ullProbeResponseHostTimestamp

The timestamp, determined by a value returned from <a href="netvista.ndisgetcurrentsystemtime">NdisGetCurrentSystemTime</a>, recording the time when the probe response packet was received.

### -field usCapabilityInformation

The value received from the capability field of the most recent beacon or probe response packet.

### -field uBeaconIEsOffset

The offset, in bytes, from the beginning of this structure  of the list of information elements (IEs) from the last beacon packet received from this device. If no beacon packet was received, this value should be 0.

### -field uBeaconIEsLength

The length, in bytes, of the IEs at <b>uBeaconIEsOffset</b>. This is an exact length value and contains no padding for alignment. If no beacon packet was received, this value should be 0.

### -field uProbeResponseIEsOffset

The offset, in bytes, from the beginning of this structure  of the list of information elements (IEs) from the last probe response packet received from this device. If no beacon packet was received, this value should be 0.

### -field uProbeResponseIEsLength

The length, in bytes, of the IEs at <b>uProbeResponseIEsOffset</b>. This is an exact length value and contains no padding for alignment. If no probe response packet was received, this value should be 0.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Versions: Supported in Windows 8
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.dot11_bss_type">DOT11_BSS_TYPE</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11-dot11_bss_entry_phy_specific_info.md">DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO</a>
</dt>
<dt>
<a href="netvista.dot11_mac_address">DOT11_MAC_ADDRESS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451704">NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE</a>
</dt>
<dt>
<a href="netvista.ndisgetcurrentsystemtime">NdisGetCurrentSystemTime</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569426">OID_DOT11_SUPPORTED_PHY_TYPES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451796">OID_DOT11_WFD_ENUM_DEVICE_LIST</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20 DOT11_WFD_DEVICE_ENTRY structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>