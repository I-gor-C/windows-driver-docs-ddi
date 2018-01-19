---
UID : NE:ntddndis._NDIS_PM_WOL_PACKET
title : _NDIS_PM_WOL_PACKET
author : windows-driver-content
description : The NDIS_PM_WOL_PACKET enumeration identifies the type of a wake-on-LAN (WOL) packet.
old-location : netvista\ndis_pm_wol_packet.htm
old-project : netvista
ms.assetid : 154a9d3d-4bb9-4c63-a820-816b254c69c2
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_PM_WOL_PACKET, *PNDIS_PM_WOL_PACKET, NDIS_PM_WOL_PACKET
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddndis.h
req.include-header : Ntddndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.20 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_PM_WOL_PACKET
req.alt-loc : ntddndis.h
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
req.typenames : "*PNDIS_PM_WOL_PACKET, NDIS_PM_WOL_PACKET"
---

# _NDIS_PM_WOL_PACKET Enumeration
The <b>NDIS_PM_WOL_PACKET</b> enumeration identifies the type of a wake-on-LAN (WOL) packet.

## Syntax
````
typedef enum _NDIS_PM_WOL_PACKET { 
  NdisPMWoLPacketUnspecified,
  NdisPMWoLPacketBitmapPattern,
  NdisPMWoLPacketMagicPacket,
  NdisPMWoLPacketIPv4TcpSyn,
  NdisPMWoLPacketIPv6TcpSyn,
  NdisPMWoLPacketEapolRequestIdMessage,
  NdisPMWoLPacketMaximum
} NDIS_PM_WOL_PACKET, *PNDIS_PM_WOL_PACKET;
````

## Constants

<table>

<tr>
<td>NdisPMWoLPacketBitmapPattern</td>
<td>Specifies a bitmap pattern. This packet type is specified in the 
     <b>WoLBitMapPattern</b> member of the 
     <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a> structure.</td>
</tr>

<tr>
<td>NdisPMWoLPacketEapolRequestIdMessage</td>
<td>Specifies an EAPOL request message packet. This packet type is specified in the 
     <b>EapolRequestIdMessageParameters</b> member of the <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a> structure.</td>
</tr>

<tr>
<td>NdisPMWoLPacketIPv4TcpSyn</td>
<td>An IPv4 TCP SYN wake-on-LAN packet pattern. This packet pattern is specified in the 
     <b>IPv4TcpSynParameters</b> member of the <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a> structure.</td>
</tr>

<tr>
<td>NdisPMWoLPacketIPv6TcpSyn</td>
<td>An IPv6 TCP SYN wake-on-LAN packet pattern. This packet pattern is specified in the 
     <b>IPv6TcpSynParameters</b> member of the <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a> structure.</td>
</tr>

<tr>
<td>NdisPMWoLPacketMagicPacket</td>
<td>WOL packets based on WOL magic packet. The media access control (MAC) address in the 
     <a href="netvista.wol_methods_in_windows_7">magic packet</a> is the current MAC
     address of the network adapter.</td>
</tr>

<tr>
<td>NdisPMWoLPacketMaximum</td>
<td>The maximum value for this enumeration. This value might change in future versions of NDIS header
     files and binaries.</td>
</tr>

<tr>
<td>NdisPMWoLPacketUnspecified</td>
<td>The WOL packet type is not specified.</td>
</tr>
</table>

## Remarks

The <b>NDIS_PM_WOL_PACKET</b> enumeration is used in the 
    <b>WoLPacketType</b> member of the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ntddndis.h) |

## See Also

<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_pm_wol_pattern.md">NDIS_PM_WOL_PATTERN</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_WOL_PACKET enumeration%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>