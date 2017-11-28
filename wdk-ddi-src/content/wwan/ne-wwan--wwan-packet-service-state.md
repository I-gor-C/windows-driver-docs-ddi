---
UID: NE.wwan._WWAN_PACKET_SERVICE_STATE
title: WWAN_PACKET_SERVICE_STATE
author: windows-driver-content
description: The WWAN_PACKET_SERVICE_STATE enumeration lists the different packet service attachment states that are supported by the MB device.
old-location: netvista\wwan_packet_service_state.htm
old-project: netvista
ms.assetid: 542a8a3b-7704-434c-ad81-0cf8e1f70015
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PACKET_SERVICE_STATE
req.alt-loc: wwan.h
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

# WWAN_PACKET_SERVICE_STATE enumeration



## -description
<p>The WWAN_PACKET_SERVICE_STATE enumeration lists the different packet service attachment states that
  are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_PACKET_SERVICE_STATE { 
  WwanPacketServiceStateUnknown    = 0,
  WwanPacketServiceStateAttaching,
  WwanPacketServiceStateAttached,
  WwanPacketServiceStateDetaching,
  WwanPacketServiceStateDetached
} WWAN_PACKET_SERVICE_STATE, *PWWAN_PACKET_SERVICE_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanPacketServiceStateUnknown"></a><a id="wwanpacketservicestateunknown"></a><a id="WWANPACKETSERVICESTATEUNKNOWN"></a><b>WwanPacketServiceStateUnknown</b>

<dd>
<p>Packet service state is unknown. The miniport driver should specify this state on a failure to set
     the MB packet service state.</p>
</dd>

### -field <a id="WwanPacketServiceStateAttaching"></a><a id="wwanpacketservicestateattaching"></a><a id="WWANPACKETSERVICESTATEATTACHING"></a><b>WwanPacketServiceStateAttaching</b>

<dd>
<p>Packet service attach action is in progress.</p>
</dd>

### -field <a id="WwanPacketServiceStateAttached"></a><a id="wwanpacketservicestateattached"></a><a id="WWANPACKETSERVICESTATEATTACHED"></a><b>WwanPacketServiceStateAttached</b>

<dd>
<p>Packet service is attached.</p>
</dd>

### -field <a id="WwanPacketServiceStateDetaching"></a><a id="wwanpacketservicestatedetaching"></a><a id="WWANPACKETSERVICESTATEDETACHING"></a><b>WwanPacketServiceStateDetaching</b>

<dd>
<p>Packet service detach action is in progress.</p>
</dd>

### -field <a id="WwanPacketServiceStateDetached"></a><a id="wwanpacketservicestatedetached"></a><a id="WWANPACKETSERVICESTATEDETACHED"></a><b>WwanPacketServiceStateDetached</b>

<dd>
<p>Packet service is detached.</p>
</dd>
</dl>

## -remarks
<p>The packet service attach or detach state is typically reflected in the device's user interface.</p>

<p>The packet service attach or detach state is typically reflected in the device's user interface.</p>

<p>The packet service attach or detach state is typically reflected in the device's user interface.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571210">WWAN_PACKET_SERVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PACKET_SERVICE_STATE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
