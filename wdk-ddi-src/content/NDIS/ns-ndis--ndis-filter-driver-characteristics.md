---
UID: NS.ndis._NDIS_FILTER_DRIVER_CHARACTERISTICS
title: NDIS_FILTER_DRIVER_CHARACTERISTICS
author: windows-driver-content
description: To specify its driver characteristics, a filter driver initializes an NDIS_FILTER_DRIVER_CHARACTERISTICS structure and passes it to NDIS.
old-location: netvista\ndis_filter_driver_characteristics.htm
ms.assetid: 1eb2bae0-70b9-4bc0-9d93-4fc9467f9532
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
ms.keywords: NDIS_FILTER_DRIVER_CHARACTERISTICS, NDIS_FILTER_DRIVER_CHARACTERISTICS, *PNDIS_FILTER_DRIVER_CHARACTERISTICS
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

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     filter driver characteristics structure (NDIS_FILTER_DRIVER_CHARACTERISTICS). Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_FILTER_DRIVER_CHARACTERISTICS.
     </p>
<p>To indicate the version of the NDIS_FILTER_DRIVER_CHARACTERISTICS structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_FILTER_CHARACTERISTICS_REVISION_3"></a><a id="ndis_filter_characteristics_revision_3"></a>NDIS_FILTER_CHARACTERISTICS_REVISION_3

<dd>
<p>Added the 
        <b>SynchronousOidRequestHandler</b> and <b>SynchronousOidRequestHandlerComplete</b> members for NDIS 6.80.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_3.</p>
</dd>

### -field <a id="NDIS_FILTER_CHARACTERISTICS_REVISION_2"></a><a id="ndis_filter_characteristics_revision_2"></a>NDIS_FILTER_CHARACTERISTICS_REVISION_2

<dd>
<p>Added the 
        <b>DirectOidRequestHandler</b>, 
        <b>DirectOidRequestCompleteHandler</b>, and 
        <b>CancelDirectOidRequestHandler</b> members for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2.</p>
</dd>

### -field <a id="NDIS_FILTER_CHARACTERISTICS_REVISION_1"></a><a id="ndis_filter_characteristics_revision_1"></a>NDIS_FILTER_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>MajorNdisVersion</b>

<dd>
<p>The major version of NDIS that the driver is using. The current value is
     0x06.</p>
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
<p>Reserved for the major version number of the filter driver. Filter drivers can specify any value
     that they require.</p>
</dd>

### -field <b>MinorDriverVersion</b>

<dd>
<p>Reserved for the minor version number of the filter driver. Filter drivers can specify any value
     that they require.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>FriendlyName</b>

<dd>
<p>A Unicode string that represents the user-readable description of the filter driver.</p>
</dd>

### -field <b>UniqueName</b>

<dd>
<p>A Unicode string that represents the unique name for the filter driver. This string must be a GUID, enclosed in curly braces, for example "{5cbf81bd-5055-47cd-9055-a76b2b4e3697}". This GUID must match the one in the <b>NetCfgInstanceId</b> INF file entry in the filter driver's INF file. For more information, see <a href="NULL">INF File Settings for Filter Drivers</a>.</p>
</dd>

### -field <b>ServiceName</b>

<dd>
<p>A Unicode string that represents the service name of the filter driver. This string must be the service name
     from the AddService directive in the filter driver's INF file. For more information, see <a href="NULL">INF File Settings for Filter Drivers</a>.</p>
</dd>

### -field <b>SetOptionsHandler</b>

<dd>
<p>Specifies the entry point of the caller's 
     <a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a> function.</p>
</dd>

### -field <b>SetFilterModuleOptionsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">
     FilterSetModuleOptions</a> function.</p>
</dd>

### -field <b>AttachHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -field <b>DetachHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540475">FilterDetach</a> function.</p>
</dd>

### -field <b>RestartHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a> function.</p>
</dd>

### -field <b>PauseHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/a239889e-ec39-48fc-9e82-c8bc3d7ca51a">FilterPause</a> function.</p>
</dd>

### -field <b>SendNetBufferListsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">
     FilterSendNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>SendNetBufferListsCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
     FilterSendNetBufferListsComplete</a> function. To bypass this function, set this member to
     <b>NULL</b>.</p>
</dd>

### -field <b>CancelSendNetBufferListsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/55979b0d-61a6-43da-8fa5-11159b1a48d1">
     FilterCancelSendNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>ReceiveNetBufferListsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/6359c2a7-1208-41ea-bbf9-015c91b6e8f6">
     FilterReceiveNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>ReturnNetBufferListsHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">
     FilterReturnNetBufferLists</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>OidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/238bfa21-a971-4fe4-a774-6ba834efc3c5">FilterOidRequest</a> function. To bypass
     this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>OidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/2dba21d8-512b-4a1a-9cf9-0240c94a69a0">
     FilterOidRequestComplete</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>CancelOidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/e7e3f67e-5353-4355-bf19-8a8041cafc84">
     FilterCancelOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>DevicePnPEventNotifyHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/dea4ab30-ba1d-4c9c-9f00-e48cc3cc0b46">
     FilterDevicePnPEventNotify</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>NetPnPEventHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/5c52b2d2-3fba-4d28-8172-7b6854386061">FilterNetPnPEvent</a> function. To
     bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>StatusHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/051ce37c-a7a5-4367-9495-023fc51349ba">FilterStatus</a> function. To bypass this
     function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>DirectOidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
      <a href="https://msdn.microsoft.com/a39f4b50-0183-4f92-82f2-3c8e2e2d0632">
      FilterDirectOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>DirectOidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
      <a href="https://msdn.microsoft.com/a97c86e9-4fd9-4e2f-9787-4fa19c38a69b">
      FilterDirectOidRequestComplete</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>CancelDirectOidRequestHandler</b>

<dd>
<p>The entry point of the caller's 
      <a href="https://msdn.microsoft.com/3587c5dc-3b4c-4aab-8c2d-cc9988373a56">
      FilterCancelDirectOidRequest</a> function. To bypass this function, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>SynchronousOidRequestHandler</b>

<dd>
<div class="alert"><b>Warning</b>  In Windows 10, version 1709, Synchronous OID requests are supported only for miniport and protocol drivers. Filter drivers cannot make Synchronous OID request calls in Windows 10, version 1709.</div>
<div> </div>
<p>This member is reserved.</p>
</dd>

### -field <b>SynchronousOidRequestHandlerComplete</b>

<dd>
<div class="alert"><b>Warning</b>  In Windows 10, version 1709, Synchronous OID requests are supported only for miniport and protocol drivers. Filter drivers cannot make Synchronous OID request calls in Windows 10, version 1709.</div>
<div> </div>
<p>This member is reserved.</p>
</dd>
</dl>

## -remarks
<p>A filter driver calls the 
    <a href="https://msdn.microsoft.com/14381de2-36d9-4ec8-9d4e-7af3e6d8ecf3">
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3587c5dc-3b4c-4aab-8c2d-cc9988373a56">
   FilterCancelDirectOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e7e3f67e-5353-4355-bf19-8a8041cafc84">FilterCancelOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/55979b0d-61a6-43da-8fa5-11159b1a48d1">
   FilterCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540475">FilterDetach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/dea4ab30-ba1d-4c9c-9f00-e48cc3cc0b46">FilterDevicePnPEventNotify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a39f4b50-0183-4f92-82f2-3c8e2e2d0632">FilterDirectOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a97c86e9-4fd9-4e2f-9787-4fa19c38a69b">
   FilterDirectOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5c52b2d2-3fba-4d28-8172-7b6854386061">FilterNetPnPEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6359c2a7-1208-41ea-bbf9-015c91b6e8f6">FilterReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/238bfa21-a971-4fe4-a774-6ba834efc3c5">FilterOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2dba21d8-512b-4a1a-9cf9-0240c94a69a0">FilterOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a239889e-ec39-48fc-9e82-c8bc3d7ca51a">FilterPause</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">FilterReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">FilterSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/051ce37c-a7a5-4367-9495-023fc51349ba">FilterStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
   NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="NULL">INF File Settings for Filter Drivers</a>
</dt>
<dt>
<a href="NULL">Initializing a Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_FILTER_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
