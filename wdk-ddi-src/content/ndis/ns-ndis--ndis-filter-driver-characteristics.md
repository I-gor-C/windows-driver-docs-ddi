---
UID: NS.ndis._NDIS_FILTER_DRIVER_CHARACTERISTICS
title: NDIS_FILTER_DRIVER_CHARACTERISTICS
author: windows-driver-content
description: To specify its driver characteristics, a filter driver initializes an NDIS_FILTER_DRIVER_CHARACTERISTICS structure and passes it to NDIS.
old-location: netvista\ndis_filter_driver_characteristics.htm
old-project: netvista
ms.assetid: 1eb2bae0-70b9-4bc0-9d93-4fc9467f9532
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_FILTER_DRIVER_CHARACTERISTICS, NDIS_FILTER_DRIVER_CHARACTERISTICS, *PNDIS_FILTER_DRIVER_CHARACTERISTICS
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
req.alt-api: NDIS_FILTER_DRIVER_CHARACTERISTICS
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
req.iface: 
---

# NDIS_FILTER_DRIVER_CHARACTERISTICS structure



## -description
<p>To specify its driver characteristics, a filter driver initializes an
  NDIS_FILTER_DRIVER_CHARACTERISTICS structure and passes it to NDIS.</p>


## -syntax

````
typedef struct _NDIS_FILTER_DRIVER_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                              Header;
  UCHAR                                           MajorNdisVersion;
  UCHAR                                           MinorNdisVersion;
  UCHAR                                           MajorDriverVersion;
  UCHAR                                           MinorDriverVersion;
  ULONG                                           Flags;
  NDIS_STRING                                     FriendlyName;
  NDIS_STRING                                     UniqueName;
  NDIS_STRING                                     ServiceName;
  SET_OPTIONS_HANDLER                             SetOptionsHandler;
  FILTER_SET_FILTER_MODULE_OPTIONS_HANDLER        SetFilterModuleOptionsHandler;
  FILTER_ATTACH_HANDLER                           AttachHandler;
  FILTER_DETACH_HANDLER                           DetachHandler;
  FILTER_RESTART_HANDLER                          RestartHandler;
  FILTER_PAUSE_HANDLER                            PauseHandler;
  FILTER_SEND_NET_BUFFER_LISTS_HANDLER            SendNetBufferListsHandler;
  FILTER_SEND_NET_BUFFER_LISTS_COMPLETE_HANDLER   SendNetBufferListsCompleteHandler;
  FILTER_CANCEL_SEND_HANDLER                      CancelSendNetBufferListsHandler;
  FILTER_RECEIVE_NET_BUFFER_LISTS_HANDLER         ReceiveNetBufferListsHandler;
  FILTER_RETURN_NET_BUFFER_LISTS_HANDLER          ReturnNetBufferListsHandler;
  FILTER_OID_REQUEST_HANDLER                      OidRequestHandler;
  FILTER_OID_REQUEST_COMPLETE_HANDLER             OidRequestCompleteHandler;
  FILTER_CANCEL_OID_REQUEST_HANDLER               CancelOidRequestHandler;
  FILTER_DEVICE_PNP_EVENT_NOTIFY_HANDLER          DevicePnPEventNotifyHandler;
  FILTER_NET_PNP_EVENT_HANDLER                    NetPnPEventHandler;
  FILTER_STATUS_HANDLER                           StatusHandler;
#if (NDIS_SUPPORT_NDIS61)
  FILTER_DIRECT_OID_REQUEST_HANDLER               DirectOidRequestHandler;
  FILTER_DIRECT_OID_REQUEST_COMPLETE_HANDLER      DirectOidRequestCompleteHandler;
  FILTER_CANCEL_DIRECT_OID_REQUEST_HANDLER        CancelDirectOidRequestHandler;
#endif 
#if (NDIS_SUPPORT_NDIS680)
  FILTER_SYNCHRONOUS_OID_REQUEST_HANDLER          SynchronousOidRequestHandler;
  FILTER_SYNCHRONOUS_OID_REQUEST_COMPLETE_HANDLER SynchronousOidRequestHandlerComplete;
#endif 
} NDIS_FILTER_DRIVER_CHARACTERISTICS, *PNDIS_FILTER_DRIVER_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     filter driver characteristics structure (NDIS_FILTER_DRIVER_CHARACTERISTICS). Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_FILTER_DRIVER_CHARACTERISTICS.
     </p>
<p>To indicate the version of the NDIS_FILTER_DRIVER_CHARACTERISTICS structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field NDIS_FILTER_CHARACTERISTICS_REVISION_3

<dd>
<p>Added the 
        <b>SynchronousOidRequestHandler</b> and <b>SynchronousOidRequestHandlerComplete</b> members for NDIS 6.80.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_3.</p>
</dd>

### -field NDIS_FILTER_CHARACTERISTICS_REVISION_2

<dd>
<p>Added the 
        <b>DirectOidRequestHandler</b>, 
        <b>DirectOidRequestCompleteHandler</b>, and 
        <b>CancelDirectOidRequestHandler</b> members for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2.</p>
</dd>

### -field NDIS_FILTER_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field MajorNdisVersion

<dd>
<p>The major version of NDIS that the driver is using. The current value is
     0x06.</p>
</dd>

### -field MinorNdisVersion

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

### -field MajorDriverVersion

<dd>
<p>Reserved for the major version number of the filter driver. Filter drivers can specify any value
     that they require.</p>
</dd>

### -field MinorDriverVersion

<dd>
<p>Reserved for the minor version number of the filter driver. Filter drivers can specify any value
     that they require.</p>
</dd>

### -field Flags

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field FriendlyName

<dd>
<p>A Unicode string that represents the user-readable description of the filter driver.</p>
</dd>

### -field UniqueName

<dd>
<p>A Unicode string that represents the unique name for the filter driver. This string must be a GUID, enclosed in curly braces, for example "{5cbf81bd-5055-47cd-9055-a76b2b4e3697}". This GUID must match the one in the <b>NetCfgInstanceId</b> INF file entry in the filter driver's INF file. For more information, see <a href="netvista.inf_file_settings_for_filter_drivers">INF File Settings for Filter Drivers</a>.</p>
</dd>

### -field ServiceName

<dd>
<p>A Unicode string that represents the service name of the filter driver. This string must be the service name
     from the AddService directive in the filter driver's INF file. For more information, see <a href="netvista.inf_file_settings_for_filter_drivers">INF File Settings for Filter Drivers</a>.</p>
</dd>

### -field SetOptionsHandler

<dd>
<p>Specifies the entry point of the caller's 
     <a href="netvista.filtersetoptions">FilterSetOptions</a> function.</p>
</dd>

### -field SetFilterModuleOptionsHandler

<dd>
<p>The entry point of the caller's 
     <a href="netvista.filtersetmoduleoptions">
     FilterSetModuleOptions</a> function.</p>
</dd>

### -field AttachHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function.</p>
</dd>

### -field DetachHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-detach.md">FilterDetach</a> function.</p>
</dd>

### -field RestartHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a> function.</p>
</dd>

### -field PauseHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-pause.md">FilterPause</a> function.</p>
</dd>

### -field SendNetBufferListsHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-send-net-buffer-lists.md">
     FilterSendNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field SendNetBufferListsCompleteHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-send-net-buffer-lists-complete.md">
     FilterSendNetBufferListsComplete</a> function. To bypass this function, set this member to
     <b>NULL</b>.</p>
</dd>

### -field CancelSendNetBufferListsHandler

<dd>
<p>The entry point of the caller's 
     <a href="netvista.filtercancelsendnetbufferlists">
     FilterCancelSendNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field ReceiveNetBufferListsHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">
     FilterReceiveNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field ReturnNetBufferListsHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">
     FilterReturnNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field OidRequestHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> function. To bypass
     this function, set this member to <b>NULL</b>.</p>
</dd>

### -field OidRequestCompleteHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-oid-request-complete.md">
     FilterOidRequestComplete</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field CancelOidRequestHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-cancel-oid-request.md">
     FilterCancelOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field DevicePnPEventNotifyHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-device-pnp-event-notify.md">
     FilterDevicePnPEventNotify</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field NetPnPEventHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a> function. To
     bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field StatusHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-filter-status.md">FilterStatus</a> function. To bypass this
     function, set this member to <b>NULL</b>.</p>
</dd>

### -field DirectOidRequestHandler

<dd>
<p>The entry point of the caller's 
      <a href="..\ndis\nc-ndis-filter-direct-oid-request.md">
      FilterDirectOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field DirectOidRequestCompleteHandler

<dd>
<p>The entry point of the caller's 
      <a href="..\ndis\nc-ndis-filter-direct-oid-request-complete.md">
      FilterDirectOidRequestComplete</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field CancelDirectOidRequestHandler

<dd>
<p>The entry point of the caller's 
      <a href="..\ndis\nc-ndis-filter-cancel-direct-oid-request.md">
      FilterCancelDirectOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field SynchronousOidRequestHandler

<dd>
<div class="alert"><b>Warning</b>  In Windows 10, version 1709, Synchronous OID requests are supported only for miniport and protocol drivers. Filter drivers cannot make Synchronous OID request calls in Windows 10, version 1709.</div>
<div> </div>
<p>This member is reserved.</p>
</dd>

### -field SynchronousOidRequestHandlerComplete

<dd>
<div class="alert"><b>Warning</b>  In Windows 10, version 1709, Synchronous OID requests are supported only for miniport and protocol drivers. Filter drivers cannot make Synchronous OID request calls in Windows 10, version 1709.</div>
<div> </div>
<p>This member is reserved.</p>
</dd>
</dl>

## -remarks
<p>A filter driver calls the 
    <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> function to register its characteristics, including the default entry
    points for its filter driver functions (<i>FilterXxx</i>). The filter driver initializes an NDIS_FILTER_DRIVER_CHARACTERISTICS structure and
    passes a pointer to this structure in the 
    <i>FilterCharacteristics</i> parameter of 
    <b>NdisFRegisterFilterDriver</b>.</p>

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
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-cancel-direct-oid-request.md">
   FilterCancelDirectOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-cancel-oid-request.md">FilterCancelOidRequest</a>
</dt>
<dt>
<a href="netvista.filtercancelsendnetbufferlists">
   FilterCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-detach.md">FilterDetach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-device-pnp-event-notify.md">FilterDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-direct-oid-request.md">FilterDirectOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-direct-oid-request-complete.md">
   FilterDirectOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-net-pnp-event.md">FilterNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-receive-net-buffer-lists.md">FilterReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-oid-request-complete.md">FilterOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-pause.md">FilterPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-return-net-buffer-lists.md">FilterReturnNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-send-net-buffer-lists.md">FilterSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-send-net-buffer-lists-complete.md">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="netvista.filtersetmoduleoptions">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="netvista.filtersetoptions">FilterSetOptions</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-status.md">FilterStatus</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-partial-characteristics.md">
   NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="netvista.inf_file_settings_for_filter_drivers">INF File Settings for Filter Drivers</a>
</dt>
<dt>
<a href="netvista.initializing_a_filter_driver">Initializing a Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_FILTER_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
