---
UID: NS.ucxcontroller._UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
title: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
author: windows-driver-content
description: Stores the transport characteristics at relevant points in time. This structure is used in the EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function.
old-location: buses\ucx_controller_transport_characteristics.htm
old-project: usbref
ms.assetid: 9F267427-8D70-45D5-A8E6-67A1C6B73CDB
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, *PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS
req.alt-loc: UcxController.h
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

# UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure



## -description
<p>Stores the transport characteristics at relevant points in time. This structure is used in the   <a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-transport-characteristics.md">EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS</a> callback function.</p>


## -syntax

````
typedef struct _UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS {
  ULONG                       TransportCharacteristicsFlags;
  ULONG64                     CurrentRoundtripLatencyInMilliSeconds;
  ULONG64                     MaxPotentialBandwidth;
} UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS, *PUCX_CONTROLLER_TRANSPORT_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field                     TransportCharacteristicsFlags

<dd>
<p>A bitmask that indicates to the client driver the transport characteristics that are available and are returned in this structure. 


</p>
<p>If USB_TRANSPORT_CHARACTERISTICS_LATENCY_AVAILABLE 

is set, <b>CurrentRoundtripLatencyInMilliSeconds</b> contains valid information. Otherwise , it must not be used by the client driver. 


</p>
<p>If USB_TRANSPORT_CHARACTERISTICS_BANDWIDTH_AVAILABLE 

is set, <b>MaxPotentialBandwidth</b> contains valid information. Otherwise, it must not be used by the client driver.  </p>
</dd>

### -field                     CurrentRoundtripLatencyInMilliSeconds

<dd>
<p>Contains the current round-trip delay in milliseconds from the time a non-isochronous transfer is received by the USB driver stack to the time that the transfer is completed.  

For MA-USB, the underlying network could be WiFi, WiGig, Ethernet etc. The delay can vary depending on the underlying network conditions. A client driver should query the latency periodically or whenever it is notified of a change. 
</p>
</dd>

### -field                     MaxPotentialBandwidth

<dd>
<p>Contains the total bandwidth of the host controller’s shared transport. 

For MA-USB, the underlying network transport could be WiFi, WiGig, Ethernet etc. The total available bandwidth can vary depending on several factors such as the negotiation WiFi channel. A client driver should query the total bandwidth periodically or whenever it is notified of a change. 
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UcxController.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-transport-characteristics.md">EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
