---
UID: NS.ndis._NDIS_MINIPORT_DRIVER_CHARACTERISTICS
title: NDIS_MINIPORT_DRIVER_CHARACTERISTICS
author: windows-driver-content
description: An NDIS driver initializes an NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure to define its miniport driver characteristics, including the entry points for its MiniportXxx functions.
old-location: netvista\ndis_miniport_driver_characteristics.htm
ms.assetid: 2e2c8522-127d-49d5-a5d6-97f9403bec89
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_DRIVER_CHARACTERISTICS
req.alt-loc: ndis.h
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
ms.keywords: NDIS_MINIPORT_DRIVER_CHARACTERISTICS, NDIS_MINIPORT_DRIVER_CHARACTERISTICS, *PNDIS_MINIPORT_DRIVER_CHARACTERISTICS
req.iface: 
---

# NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure



## -description
<p>An NDIS driver initializes an <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure to define its miniport
  driver characteristics, including the entry points for its 
  <i>MiniportXxx</i> functions.</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS.
     </p>
<p>To indicate the version of the <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3"></a><a id="ndis_miniport_driver_characteristics_revision_3"></a>NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3

<dd>
<p>Added the <b>SynchronousOidRequestHandler</b> member for NDIS 6.80.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3.</p>
</dd>

### -field <a id="NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2"></a><a id="ndis_miniport_driver_characteristics_revision_2"></a>NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2

<dd>
<p>Added the <b>DirectOidRequestHandler</b>, and <b>CancelDirectOidRequestHandler</b> members for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2.</p>
</dd>

### -field <a id="NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1"></a><a id="ndis_miniport_driver_characteristics_revision_1"></a>NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>MajorNdisVersion</b>

<dd>
<p>The major version of the NDIS library the driver is using. The current value is 0x06.</p>
</dd>

### -field <b>MinorNdisVersion</b>

<dd>
<p>The minor NDIS version. The following are the available minor version value settings.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>NDIS 6</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 20

</dl>
</td>
<td width="60%">
<p>NDIS 6.20</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 30

</dl>
</td>
<td width="60%">
<p>NDIS 6.30</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 40

</dl>
</td>
<td width="60%">
<p>NDIS 6.40</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 50

</dl>
</td>
<td width="60%">
<p>NDIS 6.50</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 51

</dl>
</td>
<td width="60%">
<p>NDIS 6.51</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 60

</dl>
</td>
<td width="60%">
<p>NDIS 6.60</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 70

</dl>
</td>
<td width="60%">
<p>NDIS 6.70</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 80

</dl>
</td>
<td width="60%">
<p>NDIS 6.80</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MajorDriverVersion</b>

<dd>
<p>Reserved for the major version number of the driver. Miniport drivers can specify any value that
     they require.</p>
</dd>

### -field <b>MinorDriverVersion</b>

<dd>
<p>Reserved for the minor version number of the driver. Miniport drivers can specify any value that
     they require.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask that can be set to zero or any of the following flags, combined with bitwise OR: 
     </p>
<p></p>
<dl>

### -field <a id="NDIS_INTERMEDIATE_DRIVER"></a><a id="ndis_intermediate_driver"></a>NDIS_INTERMEDIATE_DRIVER

<dd>
<p>Set if the caller is an NDIS intermediate driver.</p>
</dd>

### -field <a id="NDIS_WDM_DRIVER"></a><a id="ndis_wdm_driver"></a>NDIS_WDM_DRIVER

<dd>
<p>Set if the caller is an NDIS-WDM miniport driver.</p>
</dd>
</dl>
</dd>

### -field <b>SetOptionsHandler</b>

<dd>
<p>The entry point for the caller's 
     <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function.</p>
<p>Required for Co-NDIS. Suggested for Ethernet miniport drivers that support RSS using MSI-C over PCI.</p>
</dd>

### -field <b>InitializeHandlerEx</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -field <b>HaltHandlerEx</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function.</p>
</dd>

### -field <b>UnloadHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">
     MiniportDriverUnload</a> function.</p>
</dd>

### -field <b>PauseHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/047241a5-6f52-4a82-a334-8508f0de5e1a">MiniportPause</a> function.</p>
</dd>

### -field <b>RestartHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a> function.</p>
</dd>

### -field <b>OidRequestHandler</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function. Required for all connection-less miniport drivers, including all Ethernet, WLAN, and IM drivers. Optional for some CoNDIS miniport drivers.</p>
</dd>

### -field <b>SendNetBufferListsHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">
     MiniportSendNetBufferLists</a> function.</p>
</dd>

### -field <b>ReturnNetBufferListsHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
     MiniportReturnNetBufferLists</a> function.</p>
</dd>

### -field <b>CancelSendHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/17111aa3-c02f-494a-af97-5ab34c152451">MiniportCancelSend</a> function.</p>
</dd>

### -field <b>CheckForHangHandlerEx</b>

<dd>
<p>Optional. The entry point for the 
     <a href="https://msdn.microsoft.com/ead0af85-0584-49de-82cc-8a059ebfdf4f">
     MiniportCheckForHangEx</a> function. 
     </p>
<p><i>MiniportCheckForHangEx</i> is not required for intermediate drivers or virtual miniports because they are not physical devices that can hang, so they must set this entry
     point to <b>NULL</b>. </p>
<p><i>MiniportCheckForHangEx</i> is forbidden on any AOAC device due to the impact on battery life, so miniport drivers for these devices must set this entry point to <b>NULL</b>.</p>
<p><i>MiniportCheckForHangEx</i> is discouraged for miniport drivers intended to be installed on non-AOAC, battery-powered devices due to the impact on battery life, so they should set this entry point to <b>NULL</b>.</p>
<p><i>MiniportCheckForHangEx</i> is permitted but not required for miniport drivers that are intended to be installed in line-powered (mains-powered) devices. For drivers targeting NDIS 6.30 and later, consider using <a href="https://msdn.microsoft.com/library/windows/hardware/jj647917">NdisMResetMiniport</a> instead.</p>
</dd>

### -field <b>ResetHandlerEx</b>

<dd>
<p>Optional (required if you provide <b>CheckForHangHandlerEx</b>). The entry point for the 
     <a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a> function. 
     <i>MiniportResetEx</i> is not required for intermediate drivers, so they should set this entry point to
     <b>NULL</b>.</p>
</dd>

### -field <b>DevicePnPEventNotifyHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/e41240c0-17be-42ef-a72c-c5311115cf64">
     MiniportDevicePnPEventNotify</a> function.</p>
</dd>

### -field <b>ShutdownHandlerEx</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/7c88ff02-e791-4642-ad40-78f2ef2cba7d">MiniportShutdownEx</a> function.</p>
</dd>

### -field <b>CancelOidRequestHandler</b>

<dd>
<p>Required. The entry point for the 
     <a href="https://msdn.microsoft.com/42faa43d-0993-40f7-bec3-fd7c3860d5ad">
     MiniportCancelOidRequest</a> function.</p>
</dd>

### -field <b>DirectOidRequestHandler</b>

<dd>
<p>The entry point for the 
      <a href="https://msdn.microsoft.com/60daba60-3e04-4e98-a458-4dc263f17761">
      MiniportDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle direct OID requests. </p>
<p>Optional for Ethernet; however, if one is provided, then both must be provided.</p>
<p>Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.</p>
</dd>

### -field <b>CancelDirectOidRequestHandler</b>

<dd>
<p>The entry point for the 
      <a href="https://msdn.microsoft.com/88639bb4-89f3-4e7f-9cce-ea541224572d">
      MiniportCancelDirectOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b>
      if the miniport driver does not handle direct OID requests.</p>
<p>Optional for Ethernet; however, if one is provided, then both must be provided.</p>
<p>Required for WLAN and Ethernet miniports that implement RDMA or IPSec offload.</p>
</dd>

### -field <b>SynchronousOidRequestHandler</b>

<dd>
<p>The entry point for the 
      <a href="https://msdn.microsoft.com/0DDF9CF8-91F6-4D7C-A8E8-FC425BF155CB">
      MiniportSynchronousOidRequest</a> function. This is an optional entry point. Set this member to <b>NULL</b> if
      the miniport driver does not handle Synchronous OID requests. </p>
<p>Required for WLAN and Ethernet miniports that implement RSSv2.</p>
</dd>
</dl>

## -remarks
<p>An NDIS driver passes a pointer to its <b>NDIS_MINIPORT_DRIVER_CHARACTERISTICS</b> structure in the 
    <i>MiniportDriverCharacteristics</i> parameter of the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function. A miniport driver calls 
    <b>NdisMRegisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine (see also 
    <a href="https://msdn.microsoft.com/cb28d202-4ac5-494f-a208-2a86ff1d0a90">DriverEntry of NDIS
    Miniport Drivers</a>).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/88639bb4-89f3-4e7f-9cce-ea541224572d">
   MiniportCancelDirectOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/42faa43d-0993-40f7-bec3-fd7c3860d5ad">MiniportCancelOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/17111aa3-c02f-494a-af97-5ab34c152451">MiniportCancelSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ead0af85-0584-49de-82cc-8a059ebfdf4f">MiniportCheckForHangEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/60daba60-3e04-4e98-a458-4dc263f17761">MiniportDirectOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">MiniportDriverUnload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/047241a5-6f52-4a82-a334-8508f0de5e1a">MiniportPause</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e41240c0-17be-42ef-a72c-c5311115cf64">
   MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/15f82163-a1b5-4cef-a53e-8a97adb2cd92">MiniportResetEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
   MiniportReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7c88ff02-e791-4642-ad40-78f2ef2cba7d">MiniportShutdownEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
