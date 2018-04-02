---
UID: NS:windot11._DOT11_WFD_DEVICE_ENTRY
title: "_DOT11_WFD_DEVICE_ENTRY"
author: windows-driver-content
description: The DOT11_WFD_DEVICE_ENTRY structure contains information about a discovered Wi-Fi Direct (WFD) device, a discovered WFD Group Owner (GO), or or a discovered infrastructure access point.
old-location: netvista\_dot11_wfd_device_entry.htm
old-project: netvista
ms.assetid: 548A40F7-1C02-4BF0-8F78-EB8C3C97CEB4
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*PDOT11_WFD_DEVICE_ENTRY, DOT11_WFD_DEVICE_ENTRY, DOT11_WFD_DEVICE_ENTRY structure [Network Drivers Starting with Windows Vista], PDOT11_WFD_DEVICE_ENTRY, PDOT11_WFD_DEVICE_ENTRY structure pointer [Network Drivers Starting with Windows Vista], _DOT11_WFD_DEVICE_ENTRY, netvista._dot11_wfd_device_entry, windot11/ DOT11_WFD_DEVICE_ENTRY, windot11/PDOT11_WFD_DEVICE_ENTRY"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Windot11.h
api_name:
-	DOT11_WFD_DEVICE_ENTRY
product:
- Windows
targetos: Windows
req.typenames: DOT11_WFD_DEVICE_ENTRY, *PDOT11_WFD_DEVICE_ENTRY
req.product: Windows 10 or later.
---

# _DOT11_WFD_DEVICE_ENTRY structure
<div class="alert"><b>Important</b>  The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560689">Native 802.11 Wireless LAN</a> interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see <a href="https://msdn.microsoft.com/6EF92E34-7BC9-465E-B05D-2BCB29165A18">WLAN Universal Windows driver model</a>.</div><div> </div>The <b>DOT11_WFD_DEVICE_ENTRY</b> structure contains information about a discovered Wi-Fi Direct (WFD) device, a discovered WFD Group Owner (GO), or or a discovered infrastructure access point. This structure is returned from both an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451796">OID_DOT11_WFD_ENUM_DEVICE_LIST</a> and a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451704">NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE</a> notification.

## Syntax
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

## Members


`uPhyId`

The identifer of the PHY the miniport used to detect the device. This identifier is in the index range of the list of supported PHYs returned from an <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-dot11-supported-phy-types">OID_DOT11_SUPPORTED_PHY_TYPES</a> query request. This identifer cannot be <b>DOT_PHY_ID_ANY</b>.

`PhySpecificInfo`

The attributes of the PHY identified by <b>uPhyId</b>.

`dot11BSSID`

The MAC address of the device that sent the beacon or probe response packet during a discovery.

`dot11BSSType`

The BSS network type. This member is set to <b>dot11_BSS_type_infrastructure</b> for all discovered WFD devices and WFD GOs.

`TransmitterAddress`

The MAC address for the transmitter of the device that sent the beacon or probe response packet during a discovery.

`lRSSI`

The recieved signal strength indicator value of the discovered device. The units for this value are in decibels referenced to 1 milliwatt (dBm).

`uLinkQuality`

Link quality value ranging from 0 to 100. A value of 100 indicates highest link quality.

`usBeaconPeriod`

The value received from the beacon interval field of the most recent beacon or probe response packet.

`ullTimestamp`

The value received from the timestamp field of the most recent beacon or probe response packet.

`ullBeaconHostTimestamp`

The timestamp, determined by a value returned from <a href="..\ndis\nf-ndis-ndisgetcurrentsystemtime.md">NdisGetCurrentSystemTime</a>, recording the time when the beacon packet was received.

`ullProbeResponseHostTimestamp`

The timestamp, determined by a value returned from <a href="..\ndis\nf-ndis-ndisgetcurrentsystemtime.md">NdisGetCurrentSystemTime</a>, recording the time when the probe response packet was received.

`usCapabilityInformation`

The value received from the capability field of the most recent beacon or probe response packet.

`uBeaconIEsOffset`

The offset, in bytes, from the beginning of this structure  of the list of information elements (IEs) from the last beacon packet received from this device. If no beacon packet was received, this value should be 0.

`uBeaconIEsLength`

The length, in bytes, of the IEs at <b>uBeaconIEsOffset</b>. This is an exact length value and contains no padding for alignment. If no beacon packet was received, this value should be 0.

`uProbeResponseIEsOffset`

The offset, in bytes, from the beginning of this structure  of the list of information elements (IEs) from the last probe response packet received from this device. If no beacon packet was received, this value should be 0.

`uProbeResponseIEsLength`

The length, in bytes, of the IEs at <b>uProbeResponseIEsOffset</b>. This is an exact length value and contains no padding for alignment. If no probe response packet was received, this value should be 0.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows 8 Versions:\_Supported in Windows 8 |
| **Header** | windot11.h (include Windot11.h) |

## See Also

<a href="..\wlantypes\ne-wlantypes-_dot11_bss_type.md">DOT11_BSS_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451704">NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451796">OID_DOT11_WFD_ENUM_DEVICE_LIST</a>



<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-dot11-supported-phy-types">OID_DOT11_SUPPORTED_PHY_TYPES</a>



<a href="..\windot11\ns-windot11-_dot11_mac_address.md">DOT11_MAC_ADDRESS</a>



<a href="..\windot11\ns-windot11-dot11_bss_entry_phy_specific_info.md">DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO</a>



<a href="..\ndis\nf-ndis-ndisgetcurrentsystemtime.md">NdisGetCurrentSystemTime</a>