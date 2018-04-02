---
UID: NE:ntddndis._NDIS_PM_WOL_PACKET
title: "_NDIS_PM_WOL_PACKET"
author: windows-driver-content
description: The NDIS_PM_WOL_PACKET enumeration identifies the type of a wake-on-LAN (WOL) packet.
old-location: netvista\ndis_pm_wol_packet.htm
old-project: netvista
ms.assetid: 154a9d3d-4bb9-4c63-a820-816b254c69c2
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_PM_WOL_PACKET, NDIS_PM_WOL_PACKET, NDIS_PM_WOL_PACKET enumeration [Network Drivers Starting with Windows Vista], NdisPMWoLPacketBitmapPattern, NdisPMWoLPacketEapolRequestIdMessage, NdisPMWoLPacketIPv4TcpSyn, NdisPMWoLPacketIPv6TcpSyn, NdisPMWoLPacketMagicPacket, NdisPMWoLPacketMaximum, NdisPMWoLPacketUnspecified, PNDIS_PM_WOL_PACKET, PNDIS_PM_WOL_PACKET enumeration pointer [Network Drivers Starting with Windows Vista], _NDIS_PM_WOL_PACKET, miniport_power_management_ref_4788c1ee-7ed8-49f2-950b-7a820223bc32.xml, netvista.ndis_pm_wol_packet, ntddndis/NDIS_PM_WOL_PACKET, ntddndis/NdisPMWoLPacketBitmapPattern, ntddndis/NdisPMWoLPacketEapolRequestIdMessage, ntddndis/NdisPMWoLPacketIPv4TcpSyn, ntddndis/NdisPMWoLPacketIPv6TcpSyn, ntddndis/NdisPMWoLPacketMagicPacket, ntddndis/NdisPMWoLPacketMaximum, ntddndis/NdisPMWoLPacketUnspecified, ntddndis/PNDIS_PM_WOL_PACKET"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddndis.h
api_name:
-	NDIS_PM_WOL_PACKET
product:
- Windows
targetos: Windows
req.typenames: NDIS_PM_WOL_PACKET, *PNDIS_PM_WOL_PACKET
---

# _NDIS_PM_WOL_PACKET Enumeration
The <b>NDIS_PM_WOL_PACKET</b> enumeration identifies the type of a wake-on-LAN (WOL) packet.

## Syntax
```
typedef enum _NDIS_PM_WOL_PACKET {
  NdisPMWoLPacketUnspecified            ,
  NdisPMWoLPacketBitmapPattern          ,
  NdisPMWoLPacketMagicPacket            ,
  NdisPMWoLPacketIPv4TcpSyn             ,
  NdisPMWoLPacketIPv6TcpSyn             ,
  NdisPMWoLPacketEapolRequestIdMessage  ,
  NdisPMWoLPacketMaximum
} *PNDIS_PM_WOL_PACKET, NDIS_PM_WOL_PACKET;
```

## Constants

<table>
            
                <tr>
                    <td>NdisPMWoLPacketUnspecified</td>
                    <td>The WOL packet type is not specified.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketBitmapPattern</td>
                    <td>Specifies a bitmap pattern. This packet type is specified in the 
     <b>WoLBitMapPattern</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a> structure.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketMagicPacket</td>
                    <td>WOL packets based on WOL magic packet. The media access control (MAC) address in the 
     <a href="https://technet.microsoft.com/en-us/windows/hh147630.aspx">magic packet</a> is the current MAC
     address of the network adapter.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketIPv4TcpSyn</td>
                    <td>An IPv4 TCP SYN wake-on-LAN packet pattern. This packet pattern is specified in the 
     <b>IPv4TcpSynParameters</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a> structure.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketIPv6TcpSyn</td>
                    <td>An IPv6 TCP SYN wake-on-LAN packet pattern. This packet pattern is specified in the 
     <b>IPv6TcpSynParameters</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a> structure.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketEapolRequestIdMessage</td>
                    <td>Specifies an EAPOL request message packet. This packet type is specified in the 
     <b>EapolRequestIdMessageParameters</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a> structure.</td>
                </tr>
            
                <tr>
                    <td>NdisPMWoLPacketMaximum</td>
                    <td>The maximum value for this enumeration. This value might change in future versions of NDIS header
     files and binaries.</td>
                </tr>
</table>

## Remarks

The <b>NDIS_PM_WOL_PACKET</b> enumeration is used in the 
    <b>WoLPacketType</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a> structure.

<div class="alert"><b>Note</b>  The <b>NDIS_PM_WOL_PACKET</b> enumeration type specifies packet based wake-on-LAN (WOL)
    patterns. Wake-on-LAN that is based on NETBIOS over TCP is obsolete and, if necessary, it can be set with
    the pattern bitmap method.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later. Supported in NDIS 6.20 and later. |
| **Header** | ntddndis.h (include Ntddndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566768">NDIS_PM_WOL_PATTERN</a>