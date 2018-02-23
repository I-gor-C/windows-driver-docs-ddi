---
UID: NE:ntddndis._NDIS_MEDIUM
title: "_NDIS_MEDIUM"
author: windows-driver-content
description: The NDIS_MEDIUM enumeration type identifies the medium types that NDIS drivers support.
old-location: netvista\ndis_medium.htm
old-project: netvista
ms.assetid: 3e4aa7fb-0dd4-4c45-ab5e-21342e9fb4d8
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: NdisMediumWan, ntddndis/NDIS_MEDIUM, ntddndis/NdisMediumFddi, NdisMediumInfiniBand, ntddndis/NdisMediumDix, NdisMedium1394, *PNDIS_MEDIUM, ntddndis/NdisMediumBpc, PNDIS_MEDIUM, PNDIS_MEDIUM enumeration pointer [Network Drivers Starting with Windows Vista], NdisMediumBpc, ntddndis/NdisMediumWan, ntddndis/NdisMediumWirelessWan, NdisMediumAtm, ntddndis/NdisMediumArcnet878_2, ntddndis/NdisMediumIrda, ntddndis/NdisMediumNative802_11, NdisMediumCoWan, NdisMediumNative802_11, ntddndis/NdisMediumMax, NdisMedium802_3, ntddndis/NdisMediumAtm, NdisMediumMax, _NDIS_MEDIUM, NdisMediumArcnet878_2, ntddndis/NdisMedium1394, NdisMediumIrda, NdisMediumLoopback, NDIS_MEDIUM, NDIS_MEDIUM enumeration [Network Drivers Starting with Windows Vista], ntddndis/NdisMedium802_5, NdisMediumLocalTalk, ntddndis/PNDIS_MEDIUM, ntddndis/NdisMediumArcnetRaw, ntddndis/NdisMediumInfiniBand, NdisMediumArcnetRaw, ntddndis/NdisMediumCoWan, ntddndis/NdisMediumTunnel, netvista.ndis_medium, NdisMediumFddi, NdisMediumIP, protocol_structures_ref_3b154721-1574-4855-9028-704ce215eb91.xml, ntddndis/NdisMediumLoopback, ntddndis/NdisMediumIP, NdisMediumDix, NdisMediumTunnel, ntddndis/NdisMediumLocalTalk, NdisMedium802_5, NdisMediumWirelessWan, ntddndis/NdisMedium802_3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ntddndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 5.1, and NDIS 6.0 and later.
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddndis.h
apiname:
-	NDIS_MEDIUM
product: Windows
targetos: Windows
req.typenames: NDIS_MEDIUM, *PNDIS_MEDIUM
---

# _NDIS_MEDIUM Enumeration
The <b>NDIS_MEDIUM</b> enumeration type identifies the medium types that NDIS drivers support.

## Syntax
````
typedef enum _NDIS_MEDIUM { 
  NdisMedium802_3,
  NdisMedium802_5,
  NdisMediumFddi,
  NdisMediumWan,
  NdisMediumLocalTalk,
  NdisMediumDix,
  NdisMediumArcnetRaw,
  NdisMediumArcnet878_2,
  NdisMediumAtm,
  NdisMediumWirelessWan,
  NdisMediumIrda,
  NdisMediumBpc,
  NdisMediumCoWan,
  NdisMedium1394,
  NdisMediumInfiniBand,
#if ((NTDDI_VERSION >= NTDDI_VISTA) || NDIS_SUPPORT_NDIS6)
  NdisMediumTunnel,
  NdisMediumNative802_11,
  NdisMediumLoopback,
#if (NTDDI_VERSION >= NTDDI_WIN7)
  NdisMediumIP,
#endif 
#endif 
  NdisMediumMax
} NDIS_MEDIUM, *PNDIS_MEDIUM;
````

## Constants

<table>
            
                <tr>
                    <td>NdisMedium1394</td>
                    <td>Specifies an IEEE 1394 (fire wire) network. 

<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisMedium802_3</td>
                    <td>Specifies an Ethernet (802.3) network.</td>
                </tr>
            
                <tr>
                    <td>NdisMedium802_5</td>
                    <td>Specifies a Token Ring (802.5) network.

<div class="alert"><b>Note</b>   Not supported in Windows 8 or later.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisMediumArcnet878_2</td>
                    <td>Specifies an ARCNET (878.2) network.

<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisMediumArcnetRaw</td>
                    <td>Specifies an ARCNET network.

<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisMediumAtm</td>
                    <td>Specifies an ATM network. Connection-oriented client protocol drivers can bind themselves to an
     underlying miniport driver that returns this value. Otherwise, legacy protocol drivers bind themselves
     to the system-supplied LanE intermediate driver, which reports its medium type as either of 
     <b>NdisMedium802_3</b> or 
     <b>NdisMedium802_5</b>, depending on how the LanE driver is configured by the network
     administrator.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumBpc</td>
                    <td>Specifies a broadcast PC network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumCoWan</td>
                    <td>Specifies a wide area network in a connection-oriented environment.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumDix</td>
                    <td>Specifies an Ethernet network for which the drivers use the DIX Ethernet header format.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumFddi</td>
                    <td>Specifies a Fiber Distributed Data Interface (FDDI) network.

<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div></td>
                </tr>
            
                <tr>
                    <td>NdisMediumInfiniBand</td>
                    <td>Specifies an InfiniBand network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumIP</td>
                    <td>Specifies a generic medium that is capable of sending and receiving raw IP packets.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumIrda</td>
                    <td>Specifies an infrared (IrDA) network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumLocalTalk</td>
                    <td>Specifies a LocalTalk network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumLoopback</td>
                    <td>Specifies an NDIS loopback network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumMax</td>
                    <td>A maximum value for testing purposes.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumNative802_11</td>
                    <td>Specifies a native IEEE 802.11 network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumTunnel</td>
                    <td>Specifies a tunnel network.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumWan</td>
                    <td>Specifies a wide area network. This type covers various forms of point-to-point and WAN NICs, as
     well as variant address/header formats that must be negotiated between the protocol driver and the
     underlying driver after the binding is established.</td>
                </tr>
            
                <tr>
                    <td>NdisMediumWiMAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NdisMediumWirelessWan</td>
                    <td>Specifies a wireless network. NDIS 5.X miniport drivers that support wireless LAN (WLAN) or
     wireless WAN (WWAN) packets declare their medium as 
     <b>NdisMedium802_3</b> and emulate Ethernet to higher-level NDIS drivers.
     


<div class="alert"><b>Note</b>  Starting with Windows 7, this media type is supported and can
      be used for Mobile Broadband.</div>
<div> </div></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 5.1, and NDIS 6.0 and later. Supported in NDIS 5.1, and NDIS 6.0 and later. |
| **Header** | ntddndis.h (include Ntddndis.h) |