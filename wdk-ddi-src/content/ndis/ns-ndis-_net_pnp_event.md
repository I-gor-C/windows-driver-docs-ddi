---
UID : NS:ndis._NET_PNP_EVENT
title : _NET_PNP_EVENT
author : windows-driver-content
description : The NET_PNP_EVENT structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a power management event.
old-location : netvista\net_pnp_event.htm
old-project : netvista
ms.assetid : b68fb279-c1d4-4f0b-8b04-b17a01a65560
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : _NET_PNP_EVENT, PNET_PNP_EVENT structure pointer [Network Drivers Starting with Windows Vista], ndis/PNET_PNP_EVENT, *PNET_PNP_EVENT, PNET_PNP_EVENT, NET_PNP_EVENT, ndis/NET_PNP_EVENT, NET_PNP_EVENT structure [Network Drivers Starting with Windows Vista], protocol_structures_ref_0d2da286-4352-4097-901d-d3eba45d31c2.xml, netvista.net_pnp_event
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 5.1, and NDIS 6.0 and later. For more information about the NDIS 5.1 version of this structure, see    NET_PNP_EVENT (NDIS 5.1).
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
req.irql : See Remarks section
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PNET_PNP_EVENT, NET_PNP_EVENT"
---

# _NET_PNP_EVENT structure
The <b>NET_PNP_EVENT</b> structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a
  power management event.

## Syntax
````
typedef struct _NET_PNP_EVENT {
  NET_PNP_EVENT_CODE NetEvent;
  PVOID              Buffer;
  ULONG              BufferLength;
  ULONG_PTR          NdisReserved[4];
  ULONG_PTR          TransportReserved[4];
  ULONG_PTR          TdiReserved[4];
  ULONG_PTR          TdiClientReserved[4];
} NET_PNP_EVENT, *PNET_PNP_EVENT;
````

## Members


`Buffer`

The address of a buffer that contains information that is specific to the event indicated in the 
     <b>NetEvent</b> member. For each type of event, the buffer contains the following information:

`BufferLength`

The number of bytes of event-specific information at 
     <b>Buffer</b>.

`NdisReserved`

An area reserved for used by NDIS.

`NetEvent`

An event code that describes the event as one of the following:

`TdiClientReserved`

An area reserved for used by a TDI client.

`TdiReserved`

An area reserved for used by TDI.

`TransportReserved`

An area reserved for used by the transport driver.

## Remarks
In NDIS 6.0 and later versions, when the operating system issues a system PnP event or a power
    management event to a target device object that represents a miniport adapter, NDIS translates the event
    into a 
    <mshelp:link keywords="netvista.net_pnp_event_notification" tabindex="0"><b>
    NET_PNP_EVENT_NOTIFICATION</b></mshelp:link> structure. The 
    <b>NetPnPEvent</b> member of the <b>NET_PNP_EVENT_NOTIFICATION</b> structure is a <b>NET_PNP_EVENT</b> structure.

NDIS passes a pointer to the <b>NET_PNP_EVENT</b> structure to each protocol driver that is bound to the
    miniport adapter by calling the protocol driver's 
    <a href="..\ndis\nc-ndis-protocol_net_pnp_event.md">ProtocolNetPnPEvent</a> function. The
    protocol driver should save this pointer, because the pointer is an input parameter to the 
    <a href="..\ndis\nf-ndis-ndiscompletenetpnpevent.md">NdisCompleteNetPnPEvent</a> function,
    which the driver calls to complete the call to 
    <i>ProtocolNetPnPEvent</i> asynchronously.

NDIS passes a pointer to the <b>NET_PNP_EVENT</b> structure to each filter driver that is bound to the
    miniport adapter by calling the filter driver's 
    <a href="..\ndis\nc-ndis-filter_net_pnp_event.md">FilterNetPnPEvent</a> function. The
    filter driver does not have to save this pointer because the driver must complete the call to 
    <i>FilterNetPnPEvent</i> synchronously.

Starting with NDIS 6.30, the  protocol or filter driver must follow these guidelines when NDIS calls the <a href="..\ndis\nc-ndis-protocol_net_pnp_event.md">ProtocolNetPnPEvent</a> or <a href="..\ndis\nc-ndis-filter_net_pnp_event.md">FilterNetPnPEvent</a> functions:
<ul>
<li>
If the <b>NetEvent</b> member of the <b>NET_PNP_EVENT</b> structure is set to <b>NetEventSetPower</b>, the driver must stop generating new I/O requests. Also, the driver must not wait for the completion of any pending I/O requests.

After the protocol or filter driver  returns from <a href="..\ndis\nc-ndis-protocol_net_pnp_event.md">ProtocolNetPnPEvent</a> or <a href="..\ndis\nc-ndis-filter_net_pnp_event.md">FilterNetPnPEvent</a>, NDIS will not pause and restart these drivers during power-state transitions if the following conditions are true:

<ul>
<li>
The underlying miniport driver sets the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag in the <a href="..\ndis\ns-ndis-_ndis_miniport_adapter_registration_attributes.md">NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure. The driver passes a pointer to this structure in its call to the <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a> function.


</li>
<li>
All filter drivers that are attached to the miniport driver support NDIS 6.30 or later versions of NDIS.

</li>
<li>
All protocol drivers that are bound to the miniport driver support NDIS 6.30 or later versions of NDIS.

</li>
</ul>
</li>
<li>
If the <b>NetEvent</b> member of the <b>NET_PNP_EVENT</b> structure is set to <b>NetEventSetPower</b> or <b>NetEventQueryPower</b>, the driver must not wait for the completion of any pending I/O requests.

</li>
</ul>The 
    <b>NetEvent</b> member in the <b>NET_PNP_EVENT</b> structure identifies the type of Plug and Play or power
    management event. The 
    <b>Buffer</b> contains information that is specific to the type of event.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\nc-ndis-filter_net_pnp_event.md">FilterNetPnPEvent</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_switch_parameters.md">NDIS_SWITCH_PARAMETERS</a>

<a href="..\ndis\nc-ndis-protocol_bind_adapter_ex.md">ProtocolBindAdapterEx</a>

<mshelp:link keywords="netvista.ndis_protocol_pause_parameters" tabindex="0"><b>
   NDIS_PROTOCOL_PAUSE_PARAMETERS</b></mshelp:link>

<a href="https://msdn.microsoft.com/AF646860-01AB-4F4B-84F8-B570054B10FC">Querying the Hyper-V Extensible Switch Configuration</a>

<a href="..\ndis\nf-ndis-ndiscompletenetpnpevent.md">NdisCompleteNetPnPEvent</a>

<mshelp:link keywords="netvista.ndisiminitializedeviceinstanceex" tabindex="0"><b>
   NdisIMInitializeDeviceInstanceEx</b></mshelp:link>

<a href="..\ndis\ns-ndis-_net_pnp_event_notification.md">NET_PNP_EVENT_NOTIFICATION</a>

<mshelp:link keywords="netvista.ndis_protocol_restart_parameters" tabindex="0"><b>
   NDIS_PROTOCOL_RESTART_PARAMETERS</b></mshelp:link>

<a href="..\ndis\ns-ndis-_ndis_bind_failed_notification.md">NDIS_BIND_FAILED_NOTIFICATION</a>

<a href="..\ndis\ns-ndis-_ndis_restart_attributes.md">NDIS_RESTART_ATTRIBUTES</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_port.md">NDIS_PORT</a>

<a href="..\ndis\nc-ndis-protocol_net_pnp_event.md">ProtocolNetPnPEvent</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_PNP_EVENT structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>