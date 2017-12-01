---
UID: NS.bthddi._BASEBAND_CHANNEL_INFO
title: BASEBAND_CHANNEL_INFO
author: windows-driver-content
description: The BASEBAND_CHANNEL_INFO structure describes output information about the baseband channel that is used by a SCO link after a BRB_GET_CHANNEL_INFO BRB completes.
old-location: bltooth\baseband_channel_info.htm
old-project: bltooth
ms.assetid: c9328791-898e-48f2-acfd-30c8a36fcd29
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BASEBAND_CHANNEL_INFO, BASEBAND_CHANNEL_INFO, *PBASEBAND_CHANNEL_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BASEBAND_CHANNEL_INFO
req.alt-loc: bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.iface: IBidiSpl2
---

# BASEBAND_CHANNEL_INFO structure



## -description
<p>The BASEBAND_CHANNEL_INFO structure describes output information about the baseband channel that is
  used by a SCO link after a BRB_GET_CHANNEL_INFO BRB completes.</p>


## -syntax

````
typedef struct _BASEBAND_CHANNEL_INFO {
  UCHAR  Transmission_Interval;
  UCHAR  Retransmission_Window;
  UCHAR  AirMode;
  USHORT Rx_Packet_Length;
  USHORT Tx_Packet_Length;
} BASEBAND_CHANNEL_INFO, *PBASEBAND_CHANNEL_INFO;
````


## -struct-fields
<dl>

### -field <b>Transmission_Interval</b>

<dd>
<p>The elapsed time, in slots, between two consecutive SCO instants. This member will return zero for
     SCO links.</p>
</dd>

### -field <b>Retransmission_Window</b>

<dd>
<p>The length of time, in slots, that an eSCO channel can use to retransmit a request. This member
     will return zero for SCO links.</p>
</dd>

### -field <b>AirMode</b>

<dd>
<p>The air mode data format used by the baseband channel. Possible values include:
     </p>
<p>
<dl>

### -field A-LAW LOG
     


### -field CVSD
     


### -field MU-LAW LOG
     


### -field TRANSPARENT DATA

</dl>
</p>
</dd>

### -field <b>Rx_Packet_Length</b>

<dd>
<p>The size, in bytes, of the eSCO payload in the receive direction. This member will return zero for
     SCO links.</p>
</dd>

### -field <b>Tx_Packet_Length</b>

<dd>
<p>The size, in bytes, of the eSCO payload in the transmit direction. This member will return zero
     for SCO links.</p>
</dd>
</dl>

## -remarks
<p>Profile drivers access the BASEBAND_CHANNEL_INFO structure through the 
    <b>BasebandInfo</b> member of the 
    <a href="bltooth._brb_sco_get_channel_info">
    _BRB_SCO_GET_CHANNEL_INFO</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="bltooth._brb_sco_get_channel_info">_BRB_SCO_GET_CHANNEL_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BASEBAND_CHANNEL_INFO structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
