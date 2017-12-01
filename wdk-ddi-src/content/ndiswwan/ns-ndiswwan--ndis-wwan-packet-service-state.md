---
UID: NS.ndiswwan._NDIS_WWAN_PACKET_SERVICE_STATE
title: NDIS_WWAN_PACKET_SERVICE_STATE
author: windows-driver-content
description: The NDIS_WWAN_PACKET_SERVICE_STATE structure represents the packet service attachment state of the MB device.
old-location: netvista\ndis_wwan_packet_service_state.htm
old-project: netvista
ms.assetid: 63dbd674-32b3-4843-8349-706c3c0380e5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_PACKET_SERVICE_STATE, NDIS_WWAN_PACKET_SERVICE_STATE, *PNDIS_WWAN_PACKET_SERVICE_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_PACKET_SERVICE_STATE
req.alt-loc: ndiswwan.h
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

# NDIS_WWAN_PACKET_SERVICE_STATE structure



## -description
<p>The NDIS_WWAN_PACKET_SERVICE_STATE structure represents the packet service attachment state of the MB
  device.</p>


## -syntax

````
typedef struct _NDIS_WWAN_PACKET_SERVICE_STATE {
  NDIS_OBJECT_HEADER  Header;
  WWAN_STATUS         uStatus;
  WWAN_PACKET_SERVICE PacketService;
} NDIS_WWAN_PACKET_SERVICE_STATE, *PNDIS_WWAN_PACKET_SERVICE_STATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_PACKET_SERVICE_STATE
     structure. The MB Service sets the header with the values that are shown in the following table when it
     sends the data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_PACKET_SERVICE_STATE_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_PACKET_SERVICE_STATE)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>A miniport driver must set this to WWAN_STATUS_SUCCESS for unsolicited events
     (NDIS_STATUS_INDICATION::RequestId = 0).
     </p>
<p>WWAN_STATUS_SUCCESS is also set for successful execution of 
     <i>set</i> and 
     <i>query</i> requests.</p>
<p>WWAN_STATUS_SUCCESS should be returned by the miniport driver, if the requested state and the current
     state are same for a 
     <i>set</i> request.</p>
<p>The following table shows the other possible error status codes.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PIN_REQUIRED</p>
</td>
<td>
<p>Device requires PIN value input.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>Unable to get or set packet service state.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_INITIALIZED</p>
</td>
<td>
<p>The operation failed because the device is in the process of initializing. Retry the operation
        after the ready-state of the device changes to 
        <b>WwanReadyStateInitialized</b>.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>The operation failed because the SIM card was not inserted fully into the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>The operation failed because a bad SIM card was detected.</p>
</td>
</tr>
</table>
<p> </p>
<p>Miniport drivers can return the error codes (in addition to the above listed) shown in the following
     table in the event that a packet-attach 
     <i>set</i> request fails.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>Packet-attach or packet-detach has failed. More information is set at 
        <b>uNwError</b> member of WWAN_PACKET_SERVICE structure. For other WWAN_STATUS_XXX errors, 
        <b>uNwError</b> should be set to zero.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SERVICE_NOT_ACTIVATED</p>
</td>
<td>
<p>The device does not allow setting packet service state because of service activation failure or
        expired subscription.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PROVIDER_NOT_VISIBLE</p>
</td>
<td>
<p>Provider is not visible for packet service operations.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_REGISTERED</p>
</td>
<td>
<p>The device is not in registered state to perform a packet-attach operation.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>SET packet service is not supported by this CDMA-based device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_RADIO_POWER_OFF</p>
</td>
<td>
<p>Unable to packet-attach because the radio is turned off.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>A SIM card is not inserted.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>A bad SIM card is detected.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PacketService</b>

<dd>
<p>A formatted 
     <a href="..\wwan\ns-wwan--wwan-packet-service.md">WWAN_PACKET_SERVICE</a> object that
     represents the packet service attachment state of the MB device.</p>
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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-packet-service.md">WWAN_PACKET_SERVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_PACKET_SERVICE_STATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
