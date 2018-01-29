---
UID : NS:ntddndis._NDIS_PM_CAPABILITIES
title : _NDIS_PM_CAPABILITIES
author : windows-driver-content
description : The NDIS_PM_CAPABILITIES structure specifies power management capabilities of a network adapter.
old-location : netvista\ndis_pm_capabilities.htm
old-project : netvista
ms.assetid : 713c8ecc-e0a5-480a-9c53-e331aeaeb38e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*PNDIS_PM_CAPABILITIES, PNDIS_PM_CAPABILITIES structure pointer [Network Drivers Starting with Windows Vista], _NDIS_PM_CAPABILITIES, NDIS_PM_CAPABILITIES, miniport_power_management_ref_e70356b9-5c5a-4b38-b413-553a772da8b6.xml, ntddndis/PNDIS_PM_CAPABILITIES, ntddndis/NDIS_PM_CAPABILITIES, NDIS_PM_CAPABILITIES structure [Network Drivers Starting with Windows Vista], PNDIS_PM_CAPABILITIES, netvista.ndis_pm_capabilities"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ntddndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.20 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDIS_PM_CAPABILITIES, *PNDIS_PM_CAPABILITIES
---

# _NDIS_PM_CAPABILITIES structure
The <b>NDIS_PM_CAPABILITIES</b> structure specifies power management capabilities of a network adapter.

## Syntax
````
typedef struct _NDIS_PM_CAPABILITIES {
  NDIS_OBJECT_HEADER      Header;
  ULONG                   Flags;
  ULONG                   SupportedWoLPacketPatterns;
  ULONG                   NumTotalWoLPatterns;
  ULONG                   MaxWoLPatternSize;
  ULONG                   MaxWoLPatternOffset;
  ULONG                   MaxWoLPacketSaveBuffer;
  ULONG                   SupportedProtocolOffloads;
  ULONG                   NumArpOffloadIPv4Addresses;
  ULONG                   NumNSOffloadIPv6Addresses;
  NDIS_DEVICE_POWER_STATE MinMagicPacketWakeUp;
  NDIS_DEVICE_POWER_STATE MinPatternWakeUp;
  NDIS_DEVICE_POWER_STATE MinLinkChangeWakeUp;
#if (NDIS_SUPPORT_NDIS630)
  ULONG                   SupportedWakeUpEvents;
  ULONG                   MediaSpecificWakeUpEvents;
#endif 
} NDIS_PM_CAPABILITIES, *PNDIS_PM_CAPABILITIES;
````

## Members


`Flags`

A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. For NDIS 6.20, this member is reserved for NDIS.

Starting with NDIS 6.30, the following flags are defined:

`Header`

The type, revision, and size of the <b>NDIS_PM_CAPABILITIES</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.

The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_PM_CAPABILITIES</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value:

`MaxWoLPacketSaveBuffer`

A ULONG value that contains the number of bytes of a WOL packet that a miniport driver can save to
     a buffer and indicate up the driver stack. This value must be less than or equal to the size, in bytes, of the maximum transmission unit (MTU)  for the network media. The driver reports the MTU size through OID query requests of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569598">OID_GEN_MAXIMUM_FRAME_SIZE</a>.
<div class="alert"><b>Note</b>  This member is ignored in NDIS 6.20 and earlier versions of NDIS. Starting with NDIS 6.30, this member must contain a nonzero value if the NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED flag is set in the <b>Flags</b> member.</div><div> </div>

`MaxWoLPatternOffset`

A ULONG value that contains the number of bytes in a packet that can be examined, starting at
     the beginning of the MAC header.

`MaxWoLPatternSize`

A ULONG value that contains the maximum number of bytes that can be compared with a
     pattern.

`MediaSpecificWakeUpEvents`

A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. These flags specify the media-specific wake-up events that a network adapter supports. 
     

Starting with NDIS 6.30, the following flags are defined:

`MinLinkChangeWakeUp`

Starting with NDIS 6.20, this member specifies the lowest device power state from which a network adapter can signal a wake-up event when the link
     state changes from media disconnected to media connected. 

Starting with NDIS 6.30, this member specifies the lowest device power state from which a network adapter can signal    wake-up events. These events are specified in the  <b>SupportedWakeUpEvents</b> member.

The power state is specified as one of the
     following <a href="..\ntddndis\ne-ntddndis-_ndis_device_power_state.md">NDIS_DEVICE_POWER_STATE</a> values:

`MinMagicPacketWakeUp`

Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of
     a magic packet. A 
     <i>magic packet</i> contains within its payload a string of six bytes with a value of 0xFF, followed
     immediately by 16 contiguous copies of the receiving network adapter's MAC address.
     
<div class="alert"><b>Note</b>  Device power states are specified by a value of D<i>x</i>, where D0 is the highest device power state and D3 is the lowest device power state.</div><div> </div>The device power state is specified as one of the following <a href="..\ntddndis\ne-ntddndis-_ndis_device_power_state.md">NDIS_DEVICE_POWER_STATE</a> values:

`MinPatternWakeUp`

Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of
     a network frame that contains a pattern that is specified by the protocol driver. The power state is
     specified as one of the following <a href="..\ntddndis\ne-ntddndis-_ndis_device_power_state.md">NDIS_DEVICE_POWER_STATE</a> values:

`NumArpOffloadIPv4Addresses`

A <b>ULONG</b> value that contains the number of IPv4 addresses that the adapter supports for ARP
     offload.

`NumNSOffloadIPv6Addresses`

A <b>ULONG</b> value that contains the number of IPv6 NS offload requests that the adapter supports. This should be at least 2.
<div class="alert"><b>Note</b>  Despite its name, the <b>NumNSOffloadIPv6Addresses</b> contains the number of supported requests, not addresses.</div><div> </div>

`NumTotalWoLPatterns`

A <b>ULONG</b> value that contains the total number of WOL patterns that a network adapter supports. This is the sum of "number of
      supported WOL protocol patterns" and "number of supported WOL bitmap patterns."

For example, if  your driver supports 8 flexible bitmap patterns, IPv4 TCP SYN (via preset filter), and magic packet, then you would report 9 in NumTotalWoLPatterns. (8 bitmaps + 1 IPv4 TCP SYN = 9)
<div class="alert"><b>Note</b>  The total number of WOL patterns does not include the magic packet wake-up
      pattern.</div><div> </div>For more information about WOL
     protocol patterns, see 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>.

`SupportedProtocolOffloads`

A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags that specify the protocol offload features that
     a network adapter supports. Miniport drivers use these flags to report the low power protocol offload capabilities
     of a network adapter.

`SupportedWakeUpEvents`

A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. These flags specify the   media-independent wake-up events that a network adapter supports. 
     These events are not specific to media type.

Starting with NDIS 6.30, the following flags are defined:

`SupportedWoLPacketPatterns`

A ULONG value that contains a bitwise OR of flags that specify the wake-on-LAN (WOL) patterns that
     a network adapter supports. Miniport drivers use these flags to advertise packet based WOL patterns that a network adapter
     supports. 
     

For more information about this member, see the Remarks section. For more information about WOL
     patterns, see 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>.

## Remarks
The <b>NDIS_PM_CAPABILITIES</b> structure is used in the 
    <b>PowerManagementCapabilitiesEx</b> member of the 
    <mshelp:link keywords="netvista.ndis_miniport_adapter_general_attributes" tabindex="0"><b>
    NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b></mshelp:link> and 
    <a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a> structures and in
    the 
    <mshelp:link keywords="netvista.ndis_status_pm_capabilities_change" tabindex="0"><b>
    NDIS_STATUS_PM_CAPABILITIES_CHANGE</b></mshelp:link> status indication.

During miniport initialization, the miniport driver initializes an <b>NDIS_PM_CAPABILITIES</b> structure with
    the power management capabilities of the network adapter hardware. The miniport driver then sets the 
    <b>PowerManagementCapabilitiesEx</b> member of the NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure to
    point to the initialized <b>NDIS_PM_CAPABILITIES</b> structure.

An overlying driver should not try to enable capabilities that a network adapter does not support. To
    allow an overlying driver to determine what capabilities a network adapter provides, NDIS provides the
    capabilities in the 
    <b>PowerManagementCapabilitiesEx</b> member of the NDIS_BIND_PARAMETERS structure.
<div class="alert"><b>Note</b>  NDIS 6.20 drivers must use the 
    <b>PowerManagementCapabilitiesEx</b> member instead of the 
    <b>PowerManagementCapabilities</b> member.</div><div> </div>The 
    <b>SupportedProtocolOffloads</b> member contains flags that specify the protocol offload features that a
    network adapter supports. The network adapter handles these protocols in a low power state. For example, if the network adapter hardware can
    handle IPv4 ARP packets for the driver stack while it is in a low power state, the miniport driver sets
    the NDIS_PM_PROTOCOL_OFFLOAD_ARP_SUPPORTED bit in 
    <b>SupportedProtocolOffloads</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ntddndis.h) |

## See Also

<a href="..\ndis\ns-ndis-_ndis_bind_parameters.md">NDIS_BIND_PARAMETERS</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439808">NDIS_STATUS_PM_WAKE_REASON</a>

<a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">NdisMIndicateReceiveNetBufferLists</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>

<mshelp:link keywords="netvista.ndis_status_pm_capabilities_change" tabindex="0"><b>
   NDIS_STATUS_PM_CAPABILITIES_CHANGE</b></mshelp:link>

<a href="..\ndis\nf-ndis-ndismindicatestatusex.md">NdisMIndicateStatusEx</a>

<mshelp:link keywords="netvista.ndis_miniport_adapter_general_attributes" tabindex="0"><b>
   NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</b></mshelp:link>

<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_CAPABILITIES structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>