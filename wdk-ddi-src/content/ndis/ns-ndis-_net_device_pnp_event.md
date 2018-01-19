---
UID : NS:ndis._NET_DEVICE_PNP_EVENT
title : _NET_DEVICE_PNP_EVENT
author : windows-driver-content
description : The NET_DEVICE_PNP_EVENT structure defines device plug and play (PnP) events for miniport adapters.
old-location : netvista\net_device_pnp_event.htm
old-project : netvista
ms.assetid : 79298332-2d34-4ef3-ad43-5d218e3f6612
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NET_DEVICE_PNP_EVENT, NET_DEVICE_PNP_EVENT, *PNET_DEVICE_PNP_EVENT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NET_DEVICE_PNP_EVENT
req.alt-loc : ndis.h
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
req.typenames : NET_DEVICE_PNP_EVENT, *PNET_DEVICE_PNP_EVENT
---

# _NET_DEVICE_PNP_EVENT structure
The <b>NET_DEVICE_PNP_EVENT</b> structure defines device plug and play (PnP) events for miniport
  adapters.

## Syntax
````
typedef struct _NET_DEVICE_PNP_EVENT {
  NDIS_OBJECT_HEADER    Header;
  NDIS_PORT_NUMBER      PortNumber;
  NDIS_DEVICE_PNP_EVENT DevicePnPEvent;
  PVOID                 InformationBuffer;
  ULONG                 InformationBufferLength;
  UCHAR                 NdisReserved[2 * sizeof(PVOID)];
} NET_DEVICE_PNP_EVENT, *PNET_DEVICE_PNP_EVENT;
````

## Members

        
            `DevicePnPEvent`

            An event code that describes the PnP event as one of the following:
        
            `Header`

            The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NET_DEVICE_PNP_EVENT</b> structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to <b>NDIS_OBJECT_TYPE_DEFAULT</b>, the 
     <b>Revision</b> member to <b>NET_DEVICE_PNP_EVENT_REVISION_1</b>, and the 
     <b>Size</b> member to <b>NDIS_SIZEOF_NET_DEVICE_PNP_EVENT_REVISION_1</b>.
        
            `InformationBuffer`

            A pointer to a buffer. If NDIS sets the 
     <b>DevicePnPEvent</b> member to 
     <b>NdisDevicePnPEventPowerProfileChanged</b>, this buffer will contain a ULONG that NDIS sets to one of
     the following values:
        
            `InformationBufferLength`

            The length, in bytes, of the buffer in the 
     <b>InformationBuffer</b> member.
        
            `NdisReserved`

            Reserved for NDIS.
        
            `PortNumber`

            The source port of the PnP event notification. If the status indication is not specific to a port,
     
     <b>PortNumber</b> is zero.

    ## Remarks
        To provide a device PnP event notification, NDIS passes a pointer to a <b>NET_DEVICE_PNP_EVENT</b> structure
    to the 
    <a href="..\ndis\nc-ndis-miniport_device_pnp_event_notify.md">
    MiniportDevicePnPEventNotify</a> or 
    <a href="..\ndis\nc-ndis-filter_device_pnp_event_notify.md">
    FilterDevicePnPEventNotify</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ndis\nc-ndis-filter_device_pnp_event_notify.md">FilterDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_device_pnp_event_notify.md">
   MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_DEVICE_PNP_EVENT structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>