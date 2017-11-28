---
UID: NE.ntddndis._NDIS_MEDIUM
title: NDIS_MEDIUM
author: windows-driver-content
description: The NDIS_MEDIUM enumeration type identifies the medium types that NDIS drivers support.
old-location: netvista\ndis_medium.htm
old-project: netvista
ms.assetid: 3e4aa7fb-0dd4-4c45-ab5e-21342e9fb4d8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
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
req.alt-api: NDIS_MEDIUM
req.alt-loc: ntddndis.h
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
req.iface: 
---

# NDIS_MEDIUM enumeration



## -description
<p>The <b>NDIS_MEDIUM</b> enumeration type identifies the medium types that NDIS drivers support.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="NdisMedium802_3"></a><a id="ndismedium802_3"></a><a id="NDISMEDIUM802_3"></a><b>NdisMedium802_3</b>

<dd>
<p>Specifies an Ethernet (802.3) network.</p>
</dd>

### -field <a id="NdisMedium802_5"></a><a id="ndismedium802_5"></a><a id="NDISMEDIUM802_5"></a><b>NdisMedium802_5</b>

<dd>
<p>Specifies a Token Ring (802.5) network.</p>
<div class="alert"><b>Note</b>   Not supported in Windows 8 or later.</div>
<div> </div>
</dd>

### -field <a id="NdisMediumFddi"></a><a id="ndismediumfddi"></a><a id="NDISMEDIUMFDDI"></a><b>NdisMediumFddi</b>

<dd>
<p>Specifies a Fiber Distributed Data Interface (FDDI) network.</p>
<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div>
</dd>

### -field <a id="NdisMediumWan"></a><a id="ndismediumwan"></a><a id="NDISMEDIUMWAN"></a><b>NdisMediumWan</b>

<dd>
<p>Specifies a wide area network. This type covers various forms of point-to-point and WAN NICs, as
     well as variant address/header formats that must be negotiated between the protocol driver and the
     underlying driver after the binding is established.</p>
</dd>

### -field <a id="NdisMediumLocalTalk"></a><a id="ndismediumlocaltalk"></a><a id="NDISMEDIUMLOCALTALK"></a><b>NdisMediumLocalTalk</b>

<dd>
<p>Specifies a LocalTalk network.</p>
</dd>

### -field <a id="NdisMediumDix"></a><a id="ndismediumdix"></a><a id="NDISMEDIUMDIX"></a><b>NdisMediumDix</b>

<dd>
<p>Specifies an Ethernet network for which the drivers use the DIX Ethernet header format.</p>
</dd>

### -field <a id="NdisMediumArcnetRaw"></a><a id="ndismediumarcnetraw"></a><a id="NDISMEDIUMARCNETRAW"></a><b>NdisMediumArcnetRaw</b>

<dd>
<p>Specifies an ARCNET network.</p>
<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div>
</dd>

### -field <a id="NdisMediumArcnet878_2"></a><a id="ndismediumarcnet878_2"></a><a id="NDISMEDIUMARCNET878_2"></a><b>NdisMediumArcnet878_2</b>

<dd>
<p>Specifies an ARCNET (878.2) network.</p>
<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div>
</dd>

### -field <a id="NdisMediumAtm"></a><a id="ndismediumatm"></a><a id="NDISMEDIUMATM"></a><b>NdisMediumAtm</b>

<dd>
<p>Specifies an ATM network. Connection-oriented client protocol drivers can bind themselves to an
     underlying miniport driver that returns this value. Otherwise, legacy protocol drivers bind themselves
     to the system-supplied LanE intermediate driver, which reports its medium type as either of 
     <b>NdisMedium802_3</b> or 
     <b>NdisMedium802_5</b>, depending on how the LanE driver is configured by the network
     administrator.</p>
</dd>

### -field <a id="NdisMediumWirelessWan"></a><a id="ndismediumwirelesswan"></a><a id="NDISMEDIUMWIRELESSWAN"></a><b>NdisMediumWirelessWan</b>

<dd>
<p>Specifies a wireless network. NDIS 5.X miniport drivers that support wireless LAN (WLAN) or
     wireless WAN (WWAN) packets declare their medium as 
     <b>NdisMedium802_3</b> and emulate Ethernet to higher-level NDIS drivers.
     </p>
<p>
<div class="alert"><b>Note</b>  Starting with Windows 7, this media type is supported and can
      be used for Mobile Broadband.</div>
<div> </div>
</p>
</dd>

### -field <a id="NdisMediumIrda"></a><a id="ndismediumirda"></a><a id="NDISMEDIUMIRDA"></a><b>NdisMediumIrda</b>

<dd>
<p>Specifies an infrared (IrDA) network.</p>
</dd>

### -field <a id="NdisMediumBpc"></a><a id="ndismediumbpc"></a><a id="NDISMEDIUMBPC"></a><b>NdisMediumBpc</b>

<dd>
<p>Specifies a broadcast PC network.</p>
</dd>

### -field <a id="NdisMediumCoWan"></a><a id="ndismediumcowan"></a><a id="NDISMEDIUMCOWAN"></a><b>NdisMediumCoWan</b>

<dd>
<p>Specifies a wide area network in a connection-oriented environment.</p>
</dd>

### -field <a id="NdisMedium1394"></a><a id="ndismedium1394"></a><a id="NDISMEDIUM1394"></a><b>NdisMedium1394</b>

<dd>
<p>Specifies an IEEE 1394 (fire wire) network. </p>
<div class="alert"><b>Note</b>   Not supported in Windows Vista/Windows Server 2008 or later.</div>
<div> </div>
</dd>

### -field <a id="NdisMediumInfiniBand"></a><a id="ndismediuminfiniband"></a><a id="NDISMEDIUMINFINIBAND"></a><b>NdisMediumInfiniBand</b>

<dd>
<p>Specifies an InfiniBand network.</p>
</dd>

### -field <a id="NdisMediumTunnel"></a><a id="ndismediumtunnel"></a><a id="NDISMEDIUMTUNNEL"></a><b>NdisMediumTunnel</b>

<dd>
<p>Specifies a tunnel network.</p>
</dd>

### -field <a id="NdisMediumNative802_11"></a><a id="ndismediumnative802_11"></a><a id="NDISMEDIUMNATIVE802_11"></a><b>NdisMediumNative802_11</b>

<dd>
<p>Specifies a native IEEE 802.11 network.</p>
</dd>

### -field <a id="NdisMediumLoopback"></a><a id="ndismediumloopback"></a><a id="NDISMEDIUMLOOPBACK"></a><b>NdisMediumLoopback</b>

<dd>
<p>Specifies an NDIS loopback network.</p>
</dd>

### -field <a id="NdisMediumIP"></a><a id="ndismediumip"></a><a id="NDISMEDIUMIP"></a><b>NdisMediumIP</b>

<dd>
<p>Specifies a generic medium that is capable of sending and receiving raw IP packets.</p>
</dd>

### -field <a id="NdisMediumMax"></a><a id="ndismediummax"></a><a id="NDISMEDIUMMAX"></a><b>NdisMediumMax</b>

<dd>
<p>A maximum value for testing purposes.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 5.1, and NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ntddndis.h)</dt>
</dl>
</td>
</tr>
</table>