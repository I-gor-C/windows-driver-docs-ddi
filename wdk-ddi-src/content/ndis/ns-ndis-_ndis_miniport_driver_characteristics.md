---
UID: NS:ndis._NDIS_MINIPORT_DRIVER_CHARACTERISTICS
title: "_NDIS_MINIPORT_DRIVER_CHARACTERISTICS"
author: windows-driver-content
description: An NDIS driver initializes an NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure to define its miniport driver characteristics, including the entry points for its MiniportXxx functions.
old-location: netvista\ndis_miniport_driver_characteristics.htm
old-project: netvista
ms.assetid: 2e2c8522-127d-49d5-a5d6-97f9403bec89
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure [Network Drivers Starting with Windows Vista], miniport_structures_ref_9a538743-5c3f-40c7-a83d-07d5efde350c.xml, _NDIS_MINIPORT_DRIVER_CHARACTERISTICS, ndis/PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, PNDIS_MINIPORT_DRIVER_CHARACTERISTICS structure pointer [Network Drivers Starting with Windows Vista], NDIS_MINIPORT_DRIVER_CHARACTERISTICS, ndis/NDIS_MINIPORT_DRIVER_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, netvista.ndis_miniport_driver_characteristics
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
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
req.irql: See Remarks section
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ndis.h
apiname:
-	NDIS_MINIPORT_DRIVER_CHARACTERISTICS
product: Windows
targetos: Windows
req.typenames: NDIS_MINIPORT_DRIVER_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_CHARACTERISTICS
---

# _NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure
An NDIS driver initializes an <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure to define its miniport
  driver characteristics, including the entry points for its 
  <i>MiniportXxx</i> functions.

## Syntax
````
typedef struct _NDIS_MINIPORT_DRIVER_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                         Header;
  UCHAR                                      MajorNdisVersion;
  UCHAR                                      MinorNdisVersion;
  UCHAR                                      MajorDriverVersion;
  UCHAR                                      MinorDriverVersion;
  ULONG                                      Flags;
  SET_OPTIONS_HANDLER                        SetOptionsHandler;
  MINIPORT_INITIALIZE_HANDLER                InitializeHandlerEx;
  MINIPORT_HALT_HANDLER                      HaltHandlerEx;
  MINIPORT_DRIVER_UNLOAD                     UnloadHandler;
  MINIPORT_PAUSE_HANDLER                     PauseHandler;
  MINIPORT_RESTART_HANDLER                   RestartHandler;
  MINIPORT_OID_REQUEST_HANDLER               OidRequestHandler;
  MINIPORT_SEND_NET_BUFFER_LISTS_HANDLER     SendNetBufferListsHandler;
  MINIPORT_RETURN_NET_BUFFER_LISTS_HANDLER   ReturnNetBufferListsHandler;
  MINIPORT_CANCEL_SEND_HANDLER               CancelSendHandler;
  MINIPORT_CHECK_FOR_HANG_HANDLER            CheckForHangHandlerEx;
  MINIPORT_RESET_HANDLER                     ResetHandlerEx;
  MINIPORT_DEVICE_PNP_EVENT_NOTIFY_HANDLER   DevicePnPEventNotifyHandler;
  MINIPORT_SHUTDOWN_HANDLER                  ShutdownHandlerEx;
  MINIPORT_CANCEL_OID_REQUEST_HANDLER        CancelOidRequestHandler;
#if (NDIS_SUPPORT_NDIS61)
  MINIPORT_DIRECT_OID_REQUEST_HANDLER        DirectOidRequestHandler;
  MINIPORT_CANCEL_DIRECT_OID_REQUEST_HANDLER CancelDirectOidRequestHandler;
#endif 
#if (NDIS_SUPPORT_NDIS680)
  MINIPORT_SYNCHRONOUS_OID_REQUEST_HANDLER   SynchronousOidRequestHandler;
#endif 
} NDIS_MINIPORT_DRIVER_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_CHARACTERISTICS;
````

## Members


`CancelDirectOidRequestHandler`

The entry point for the 
      <a href="..\ndis\nc-ndis-miniport_cancel_direct_oid_request.md">
      MiniportCancelDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b>
      if the miniport driver does not handle direct OID requests.

Optional for Ethernet; however, if one is provided, then both must be provided.

Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.

`CancelOidRequestHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_cancel_oid_request.md">
     MiniportCancelOidRequest</a> function.

`CancelSendHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_cancel_send.md">MiniportCancelSend</a> function.

`CheckForHangHandlerEx`

Optional. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_check_for_hang.md">
     MiniportCheckForHangEx</a> function. 
     

<i>MiniportCheckForHangEx</i> is not required for intermediate drivers or virtual miniports because they are not physical devices that can hang, so they must set this entry
     point to <b>NULL</b>. 

<i>MiniportCheckForHangEx</i> is forbidden on any AOAC device due to the impact on battery life, so miniport drivers for these devices must set this entry point to <b>NULL</b>.

<i>MiniportCheckForHangEx</i> is discouraged for miniport drivers intended to be installed on non-AOAC, battery-powered devices due to the impact on battery life, so they should set this entry point to <b>NULL</b>.

<i>MiniportCheckForHangEx</i> is permitted but not required for miniport drivers that are intended to be installed in line-powered (mains-powered) devices. For drivers targeting NDIS 6.30 and later, consider using <a href="..\ndis\nf-ndis-ndismresetminiport.md">NdisMResetMiniport</a> instead.

`DevicePnPEventNotifyHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_device_pnp_event_notify.md">
     MiniportDevicePnPEventNotify</a> function.

`DirectOidRequestHandler`

The entry point for the 
      <a href="..\ndis\nc-ndis-miniport_direct_oid_request.md">
      MiniportDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle direct OID requests. 

Optional for Ethernet; however, if one is provided, then both must be provided.

Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.

`Flags`

A bitmask that can be set to zero or any of the following flags, combined with bitwise OR: 
     




#### NDIS_INTERMEDIATE_DRIVER

Set if the caller is an NDIS intermediate driver.


#### NDIS_WDM_DRIVER

Set if the caller is an NDIS-WDM miniport driver.

`HaltHandlerEx`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a> function.

`Header`

The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS.
     

To indicate the version of the <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure, set the 
     <b>Revision</b> member to one of the following values:




#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1

Original version for NDIS 6.0.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1.


#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2

Added the <b>DirectOidRequestHandler</b>, and <b>CancelDirectOidRequestHandler</b> members for NDIS 6.1.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2.


#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3

Added the <b>SynchronousOidRequestHandler</b> member for NDIS 6.80.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3.

`InitializeHandlerEx`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">
     MiniportInitializeEx</a> function.

`MajorDriverVersion`

Reserved for the major version number of the driver. Miniport drivers can specify any value that
     they require.

`MajorNdisVersion`

The major version of the NDIS library the driver is using. The current value is 0x06.

`MinorDriverVersion`

Reserved for the minor version number of the driver. Miniport drivers can specify any value that
     they require.

`MinorNdisVersion`

The minor NDIS version. The following are the available minor version value settings.
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt>0</dt>
</dl>
</td>
<td width="60%">
NDIS 6

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>20</dt>
</dl>
</td>
<td width="60%">
NDIS 6.20

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>30</dt>
</dl>
</td>
<td width="60%">
NDIS 6.30

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>40</dt>
</dl>
</td>
<td width="60%">
NDIS 6.40

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>50</dt>
</dl>
</td>
<td width="60%">
NDIS 6.50

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>51</dt>
</dl>
</td>
<td width="60%">
NDIS 6.51

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>60</dt>
</dl>
</td>
<td width="60%">
NDIS 6.60

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>70</dt>
</dl>
</td>
<td width="60%">
NDIS 6.70

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt>80</dt>
</dl>
</td>
<td width="60%">
NDIS 6.80

</td>
</tr>
</table>

`OidRequestHandler`

The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a> function. Required for all connection-less miniport drivers, including all Ethernet, WLAN, and IM drivers. Optional for some CoNDIS miniport drivers.

`PauseHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a> function.

`ResetHandlerEx`

Optional (required if you provide <b>CheckForHangHandlerEx</b>). The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_reset.md">MiniportResetEx</a> function. 
     <i>MiniportResetEx</i> is not required for intermediate drivers, so they should set this entry point to
     <b>NULL</b>.

`RestartHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_restart.md">MiniportRestart</a> function.

`ReturnNetBufferListsHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_return_net_buffer_lists.md">
     MiniportReturnNetBufferLists</a> function.

`SendNetBufferListsHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_send_net_buffer_lists.md">
     MiniportSendNetBufferLists</a> function.

`SetOptionsHandler`

The entry point for the caller's 
     <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff570269">MiniportSetOptions</a> function.

Required for Co-NDIS. Suggested for Ethernet miniport drivers that support RSS using MSI-C over PCI.

`ShutdownHandlerEx`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_shutdown.md">MiniportShutdownEx</a> function.

`SynchronousOidRequestHandler`

The entry point for the 
      <a href="..\ndis\nf-ndis-miniport_synchronous_oid_request.md">
      MiniportSynchronousOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle Synchronous OID requests. 

Required for WLAN and Ethernet miniports that implement RSSv2.

`UnloadHandler`

Required. The entry point for the 
     <a href="..\ndis\nc-ndis-miniport_unload.md">
     MiniportDriverUnload</a> function.

## Remarks
An NDIS driver passes a pointer to its <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure in the 
    <i>MiniportDriverCharacteristics</i> parameter of the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function. A miniport driver calls 
    <b>NdisMRegisterMiniportDriver</b> from its 
    <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine (see also 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff548818">DriverEntry of NDIS
    Miniport Drivers</a>).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="..\ndis\nc-ndis-miniport_cancel_direct_oid_request.md">
   MiniportCancelDirectOidRequest</a>

<a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a>

<a href="..\ndis\nc-ndis-miniport_send_net_buffer_lists.md">MiniportSendNetBufferLists</a>

<a href="..\ndis\nc-ndis-miniport_pause.md">MiniportPause</a>

<a href="..\ndis\nc-ndis-miniport_cancel_send.md">MiniportCancelSend</a>

<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff570269">MiniportSetOptions</a>

<a href="..\ndis\nc-ndis-miniport_device_pnp_event_notify.md">
   MiniportDevicePnPEventNotify</a>

<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>

<a href="..\ndis\nc-ndis-miniport_restart.md">MiniportRestart</a>

<a href="..\ndis\nc-ndis-miniport_reset.md">MiniportResetEx</a>

<a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a>

<a href="..\ndis\nc-ndis-miniport_shutdown.md">MiniportShutdownEx</a>

<a href="..\ndis\nc-ndis-miniport_cancel_oid_request.md">MiniportCancelOidRequest</a>

<a href="..\ndis\nc-ndis-miniport_direct_oid_request.md">MiniportDirectOidRequest</a>

<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>

<a href="..\ndis\nc-ndis-miniport_return_net_buffer_lists.md">
   MiniportReturnNetBufferLists</a>

<a href="..\ndis\nc-ndis-miniport_unload.md">MiniportDriverUnload</a>

<a href="..\ndis\nc-ndis-miniport_check_for_hang.md">MiniportCheckForHangEx</a>

<a href="..\ndis\nc-ndis-miniport_halt.md">MiniportHaltEx</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>