---
UID : NS:ndis._NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
title : _NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
author : windows-driver-content
description : An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure to define registration attributes that are associated with a miniport adapter.
old-location : netvista\ndis_miniport_adapter_registration_attributes.htm
old-project : netvista
ms.assetid : 8f0d539a-50c5-4ecd-b62d-6b32fe7cfaba
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
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
req.alt-api : NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
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
req.typenames : NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES
---

# _NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure
An NDIS miniport driver sets up an <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure to define
  registration attributes that are associated with a miniport adapter.

## Syntax
````
typedef struct _NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES {
  NDIS_OBJECT_HEADER  Header;
  NDIS_HANDLE         MiniportAdapterContext;
  ULONG               AttributeFlags;
  UINT                CheckForHangTimeInSeconds;
  NDIS_INTERFACE_TYPE InterfaceType;
} NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES, *PNDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES;
````

## Members

        
            `AttributeFlags`

            A bitmask of flags that are combined with a bitwise OR. NDIS miniport drivers should set one or more of
     the following flags:
        
            `CheckForHangTimeInSeconds`

            The time-out interval, in seconds, at which NDIS should call the 
     <a href="..\ndis\nc-ndis-miniport_check_for_hang.md">
     MiniportCheckForHangEx</a> function. If a miniport driver has not responded to an OID request or a send request
     within two successive calls to 
     <i>MiniportCheckForHangEx</i>, NDIS can call the miniport driver's 
     <a href="..\ndis\nc-ndis-miniport_reset.md">MiniportResetEx</a> function.
     

The  interval that NDIS uses when calling 
     <i>MiniportCheckForHangEx</i> is always a multiple of 2 seconds. For example, if you specify 5
     seconds, the interval will be approximately 4 seconds.

If this member is 0, the default time-out interval is 2 seconds.

<div class="alert"><b>Note</b>  The time-out interval must be greater than your miniport driver's initialization time. For more information, see <a href="https://msdn.microsoft.com/53ffc5a9-bcba-4189-8845-73adfcf6816d">Miniport Adapter Check-for-Hang and Reset Operations</a>.</div>
<div> </div>
        
            `Header`

            The type, revision, and size of the <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.

The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES. To specify the version of the <b>NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to one of the following values:
        
            `InterfaceType`

            The I/O bus interface type of the miniport adapter. This is usually the type of I/O bus on which
     the miniport adapter is connected. The following values are supported in NDIS 6.0:
        
            `MiniportAdapterContext`

            A handle to a context area that the miniport driver allocated in its 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.

    ## Remarks
        A miniport driver passes a pointer to an NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure in
    the 
    <i>MiniportAttributes</i> parameter of the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function. A miniport driver calls 
    <b>NdisMSetMiniportAttributes</b> from its 
    <a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a> function
    during initialization.

Miniport drivers should set the attributes in NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES as soon as
    possible within 
    <i>MiniportInitializeEx</i>. Setting these attributes is mandatory.

NDIS issues an OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> to the miniport driver before the underlying miniport adapter is transitioned to a low power state of D1, D2, or D3. When the driver handles this OID, it must prepare the miniport adapter for the transition to the lower power state and must not wait for the completion of pending receive packet indications.

In some cases, before NDIS issues the OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> to the miniport driver, NDIS calls the miniport driver's <a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a> function as described below:

If the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag is not set, NDIS   calls the miniport driver's <a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a> function before the OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> is issued to the driver. Within the context of the <i>MiniportPause</i> call, the driver must wait for the completion of pending receive packet indications.

If the <b>NDIS_MINIPORT_ATTRIBUTES_NO_PAUSE_ON_SUSPEND</b> flag is  set, NDIS does not call the miniport driver's <a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a> function before the OID  request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a> is issued to the driver.  When the miniport driver  handles the OID request, it must not assume that it had been previously paused when preparing the miniport adapter for the transition to a low-power state.

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
<a href="..\ndis\nc-ndis-miniport_check_for_hang.md">MiniportCheckForHangEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_device_pnp_event_notify.md">
   MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismnetpnpevent.md">NdisMNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569780">OID_PNP_SET_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/53ffc5a9-bcba-4189-8845-73adfcf6816d">Miniport Adapter Check-for-Hang and Reset Operations</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>