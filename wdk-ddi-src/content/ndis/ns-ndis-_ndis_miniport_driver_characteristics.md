---
UID: NS:ndis._NDIS_MINIPORT_DRIVER_CHARACTERISTICS
title: "_NDIS_MINIPORT_DRIVER_CHARACTERISTICS"
author: windows-driver-content
description: An NDIS driver initializes an NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure to define its miniport driver characteristics, including the entry points for its MiniportXxx functions.
old-location: netvista\ndis_miniport_driver_characteristics.htm
old-project: netvista
ms.assetid: 2e2c8522-127d-49d5-a5d6-97f9403bec89
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, NDIS_MINIPORT_DRIVER_CHARACTERISTICS, NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure [Network Drivers Starting with Windows Vista], PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, PNDIS_MINIPORT_DRIVER_CHARACTERISTICS structure pointer [Network Drivers Starting with Windows Vista], _NDIS_MINIPORT_DRIVER_CHARACTERISTICS, miniport_structures_ref_9a538743-5c3f-40c7-a83d-07d5efde350c.xml, ndis/NDIS_MINIPORT_DRIVER_CHARACTERISTICS, ndis/PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, netvista.ndis_miniport_driver_characteristics"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndis.h
api_name:
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
```
typedef struct _NDIS_MINIPORT_DRIVER_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                         Header;
  UCHAR                                      MajorNdisVersion;
  UCHAR                                      MinorNdisVersion;
  UCHAR                                      MajorDriverVersion;
  UCHAR                                      MinorDriverVersion;
  ULONG                                      Flags;
  SET_OPTIONS_HANDLER                        SetOptionsHandler;
  MINIPORT_INITIALIZE_HANDLER                InitializeHandlerEx;
  MINIPORT_HALT_HANDLER                      HaltHandlerEx;
  MINIPORT_DRIVER_UNLOAD                     UnloadHandler;
  MINIPORT_PAUSE_HANDLER                     PauseHandler;
  MINIPORT_RESTART_HANDLER                   RestartHandler;
  MINIPORT_OID_REQUEST_HANDLER               OidRequestHandler;
  MINIPORT_SEND_NET_BUFFER_LISTS_HANDLER     SendNetBufferListsHandler;
  MINIPORT_RETURN_NET_BUFFER_LISTS_HANDLER   ReturnNetBufferListsHandler;
  MINIPORT_CANCEL_SEND_HANDLER               CancelSendHandler;
  MINIPORT_CHECK_FOR_HANG_HANDLER            CheckForHangHandlerEx;
  MINIPORT_RESET_HANDLER                     ResetHandlerEx;
  MINIPORT_DEVICE_PNP_EVENT_NOTIFY_HANDLER   DevicePnPEventNotifyHandler;
  MINIPORT_SHUTDOWN_HANDLER                  ShutdownHandlerEx;
  MINIPORT_CANCEL_OID_REQUEST_HANDLER        CancelOidRequestHandler;
  MINIPORT_DIRECT_OID_REQUEST_HANDLER        DirectOidRequestHandler;
  MINIPORT_CANCEL_DIRECT_OID_REQUEST_HANDLER CancelDirectOidRequestHandler;
  MINIPORT_SYNCHRONOUS_OID_REQUEST_HANDLER   SynchronousOidRequestHandler;
} *PNDIS_MINIPORT_DRIVER_CHARACTERISTICS, NDIS_MINIPORT_DRIVER_CHARACTERISTICS;
```

## Members


`Header`

The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS.
     

To indicate the version of the <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure, set the 
     <b>Revision</b> member to one of the following values:





#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3

Added the <b>SynchronousOidRequestHandler</b> member for NDIS 6.80.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3.



#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2

Added the <b>DirectOidRequestHandler</b>, and <b>CancelDirectOidRequestHandler</b> members for NDIS 6.1.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2.



#### NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1

Original version for NDIS 6.0.

Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1.

`MajorNdisVersion`

The major version of the NDIS library the driver is using. The current value is 0x06.

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

`MajorDriverVersion`

Reserved for the major version number of the driver. Miniport drivers can specify any value that
     they require.

`MinorDriverVersion`

Reserved for the minor version number of the driver. Miniport drivers can specify any value that
     they require.

`Flags`

A bitmask that can be set to zero or any of the following flags, combined with bitwise OR: 
     





#### NDIS_INTERMEDIATE_DRIVER

Set if the caller is an NDIS intermediate driver.



#### NDIS_WDM_DRIVER

Set if the caller is an NDIS-WDM miniport driver.

`SetOptionsHandler`

The entry point for the caller's 
     <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff570269">MiniportSetOptions</a> function.

Required for Co-NDIS. Suggested for Ethernet miniport drivers that support RSS using MSI-C over PCI.

`InitializeHandlerEx`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.

`HaltHandlerEx`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function.

`UnloadHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">
     MiniportDriverUnload</a> function.

`PauseHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/047241a5-6f52-4a82-a334-8508f0de5e1a">MiniportPause</a> function.

`RestartHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a> function.

`OidRequestHandler`

The entry point for the 
     <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function. Required for all connection-less miniport drivers, including all Ethernet, WLAN, and IM drivers. Optional for some CoNDIS miniport drivers.

`SendNetBufferListsHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">
     MiniportSendNetBufferLists</a> function.

`ReturnNetBufferListsHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
     MiniportReturnNetBufferLists</a> function.

`CancelSendHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/17111aa3-c02f-494a-af97-5ab34c152451">MiniportCancelSend</a> function.

`CheckForHangHandlerEx`

Optional. The entry point for the 
     <a href="https://msdn.microsoft.com/ead0af85-0584-49de-82cc-8a059ebfdf4f">
     MiniportCheckForHangEx</a> function. 
     

<i>MiniportCheckForHangEx</i> is not required for intermediate drivers or virtual miniports because they are not physical devices that can hang, so they must set this entry
     point to <b>NULL</b>. 

<i>MiniportCheckForHangEx</i> is forbidden on any AOAC device due to the impact on battery life, so miniport drivers for these devices must set this entry point to <b>NULL</b>.

<i>MiniportCheckForHangEx</i> is discouraged for miniport drivers intended to be installed on non-AOAC, battery-powered devices due to the impact on battery life, so they should set this entry point to <b>NULL</b>.

<i>MiniportCheckForHangEx</i> is permitted but not required for miniport drivers that are intended to be installed in line-powered (mains-powered) devices. For drivers targeting NDIS 6.30 and later, consider using <a href="https://msdn.microsoft.com/library/windows/hardware/jj647917">NdisMResetMiniport</a> instead.

`ResetHandlerEx`

Optional (required if you provide <b>CheckForHangHandlerEx</b>). The entry point for the 
     <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function. 
     <i>MiniportResetEx</i> is not required for intermediate drivers, so they should set this entry point to
     <b>NULL</b>.

`DevicePnPEventNotifyHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/e41240c0-17be-42ef-a72c-c5311115cf64">
     MiniportDevicePnPEventNotify</a> function.

`ShutdownHandlerEx`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/7c88ff02-e791-4642-ad40-78f2ef2cba7d">MiniportShutdownEx</a> function.

`CancelOidRequestHandler`

Required. The entry point for the 
     <a href="https://msdn.microsoft.com/42faa43d-0993-40f7-bec3-fd7c3860d5ad">
     MiniportCancelOidRequest</a> function.

`DirectOidRequestHandler`

The entry point for the 
      <a href="https://msdn.microsoft.com/60daba60-3e04-4e98-a458-4dc263f17761">
      MiniportDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle direct OID requests. 

Optional for Ethernet; however, if one is provided, then both must be provided.

Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.

`CancelDirectOidRequestHandler`

The entry point for the 
      <a href="https://msdn.microsoft.com/88639bb4-89f3-4e7f-9cce-ea541224572d">
      MiniportCancelDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b>
      if the miniport driver does not handle direct OID requests.

Optional for Ethernet; however, if one is provided, then both must be provided.

Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.

`SynchronousOidRequestHandler`

The entry point for the 
      <a href="https://msdn.microsoft.com/0DDF9CF8-91F6-4D7C-A8E8-FC425BF155CB">
      MiniportSynchronousOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle Synchronous OID requests. 

Required for WLAN and Ethernet miniports that implement RSSv2.

## Remarks
An NDIS driver passes a pointer to its <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure in the 
    <i>MiniportDriverCharacteristics</i> parameter of the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function. A miniport driver calls 
    <b>NdisMRegisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine (see also 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff548818">DriverEntry of NDIS
    Miniport Drivers</a>).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>



<a href="https://msdn.microsoft.com/88639bb4-89f3-4e7f-9cce-ea541224572d">
   MiniportCancelDirectOidRequest</a>



<a href="https://msdn.microsoft.com/42faa43d-0993-40f7-bec3-fd7c3860d5ad">MiniportCancelOidRequest</a>



<a href="https://msdn.microsoft.com/17111aa3-c02f-494a-af97-5ab34c152451">MiniportCancelSend</a>



<a href="https://msdn.microsoft.com/ead0af85-0584-49de-82cc-8a059ebfdf4f">MiniportCheckForHangEx</a>



<a href="https://msdn.microsoft.com/e41240c0-17be-42ef-a72c-c5311115cf64">
   MiniportDevicePnPEventNotify</a>



<a href="https://msdn.microsoft.com/60daba60-3e04-4e98-a458-4dc263f17761">MiniportDirectOidRequest</a>



<a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">MiniportDriverUnload</a>



<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>



<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>



<a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>



<a href="https://msdn.microsoft.com/047241a5-6f52-4a82-a334-8508f0de5e1a">MiniportPause</a>



<a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a>



<a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a>



<a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
   MiniportReturnNetBufferLists</a>



<a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">MiniportSendNetBufferLists</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff570269">MiniportSetOptions</a>



<a href="https://msdn.microsoft.com/7c88ff02-e791-4642-ad40-78f2ef2cba7d">MiniportShutdownEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>