---
UID: NS.ndis._NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
title: NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
author: windows-driver-content
description: To specify its driver characteristics, a protocol driver initializes an NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure and passes it to NDIS.
old-location: netvista\ndis_protocol_driver_characteristics.htm
old-project: netvista
ms.assetid: db64c160-9db6-4b23-af14-e64acdb9ef57
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_PROTOCOL_DRIVER_CHARACTERISTICS, NDIS_PROTOCOL_DRIVER_CHARACTERISTICS, *PNDIS_PROTOCOL_DRIVER_CHARACTERISTICS
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
req.alt-api: NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
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

# NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure



## -description
<p>To specify its driver characteristics, a protocol driver initializes an
  <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure and passes it to NDIS.</p>


## -syntax

````
typedef struct _NDIS_PROTOCOL_DRIVER_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                     Header;
  UCHAR                                  MajorNdisVersion;
  UCHAR                                  MinorNdisVersion;
  UCHAR                                  MajorDriverVersion;
  UCHAR                                  MinorDriverVersion;
  ULONG                                  Flags;
  NDIS_STRING                            Name;
  SET_OPTIONS_HANDLER                    SetOptionsHandler;
  BIND_HANDLER_EX                        BindAdapterHandlerEx;
  UNBIND_HANDLER_EX                      UnbindAdapterHandlerEx;
  OPEN_ADAPTER_COMPLETE_HANDLER_EX       OpenAdapterCompleteHandlerEx;
  CLOSE_ADAPTER_COMPLETE_HANDLER_EX      CloseAdapterCompleteHandlerEx;
  NET_PNP_EVENT_HANDLER                  NetPnPEventHandler;
  UNINSTALL_PROTOCOL_HANDLER             UninstallHandler;
  OID_REQUEST_COMPLETE_HANDLER           OidRequestCompleteHandler;
  STATUS_HANDLER_EX                      StatusHandlerEx;
  RECEIVE_NET_BUFFER_LISTS_HANDLER       ReceiveNetBufferListsHandler;
  SEND_NET_BUFFER_LISTS_COMPLETE_HANDLER SendNetBufferListsCompleteHandler;
#if (NDIS_SUPPORT_NDIS61)
  DIRECT_OID_REQUEST_COMPLETE_HANDLER    DirectOidRequestCompleteHandler;
#endif 
} NDIS_PROTOCOL_DRIVER_CHARACTERISTICS, *PNDIS_PROTOCOL_DRIVER_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_PROTOCOL_DRIVER_CHARACTERISTICS.
     </p>
<p>To indicate the version of the <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_2

<dd>
<p>Added the 
        <b>DirectOidRequestCompleteHandler</b> member for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to
        NDIS_SIZEOF_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_2.</p>
</dd>

### -field NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>Set the 
        <b>Size</b> member to
        NDIS_SIZEOF_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field MajorNdisVersion

<dd>
<p>The major version of the NDIS library the protocol driver is using. The current value is
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
<p>Reserved for the major version number of the protocol driver. Protocol drivers can specify any
     value that they require.</p>
</dd>

### -field MinorDriverVersion

<dd>
<p>Reserved for the minor version number of the protocol driver. Protocol drivers can specify any
     value that they require.</p>
</dd>

### -field Flags

<dd>
<p>Reserved for NDIS. Protocol drivers should set this member to zero.</p>
</dd>

### -field Name

<dd>
<p>A Unicode string that is the service name of the protocol driver.</p>
</dd>

### -field SetOptionsHandler

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function.</p>
</dd>

### -field BindAdapterHandlerEx

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">
     ProtocolBindAdapterEx</a> function.</p>
</dd>

### -field UnbindAdapterHandlerEx

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-unbind-adapter-ex.md">
     ProtocolUnbindAdapterEx</a> function.</p>
</dd>

### -field OpenAdapterCompleteHandlerEx

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-open-adapter-complete-ex.md">
     ProtocolOpenAdapterCompleteEx</a> function.</p>
</dd>

### -field CloseAdapterCompleteHandlerEx

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-close-adapter-complete-ex.md">
     ProtocolCloseAdapterCompleteEx</a> function.</p>
</dd>

### -field NetPnPEventHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a> function.</p>
</dd>

### -field UninstallHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-uninstall.md">ProtocolUninstall</a> function, if any,
     or <b>NULL</b>.</p>
</dd>

### -field OidRequestCompleteHandler

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-oid-request-complete.md">
     ProtocolOidRequestComplete</a> function.</p>
</dd>

### -field StatusHandlerEx

<dd>
<p>The entry point of the caller's 
     <a href="..\ndis\nc-ndis-protocol-status-ex.md">ProtocolStatusEx</a> function, if any, or
     <b>NULL</b>.</p>
</dd>

### -field ReceiveNetBufferListsHandler

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-receive-net-buffer-lists.md">
     ProtocolReceiveNetBufferLists</a> function.</p>
</dd>

### -field SendNetBufferListsCompleteHandler

<dd>
<p>The entry point for the 
     <a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
     ProtocolSendNetBufferListsComplete</a> function.</p>
</dd>

### -field DirectOidRequestCompleteHandler

<dd>
<p>The entry point of the caller's 
      <a href="..\ndis\nc-ndis-protocol-direct-oid-request-complete.md">
      ProtocolDirectOidRequestComplete</a> function. This is an optional function. Set this entry point to
      <b>NULL</b> if the protocol driver does not support the direct OID request interface.</p>
</dd>
</dl>

## -remarks
<p>A protocol driver calls the 
    <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
    NdisRegisterProtocolDriver</a> function to register its characteristics, including the default entry
    points for its protocol driver functions (<i>ProtocolXxx</i>). The protocol driver initializes an <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure
    and passes a pointer to this structure in the 
    <i>ProtocolCharacteristics</i> parameter of 
    <b>NdisRegisterProtocolDriver</b>.</p>

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
<a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-close-adapter-complete-ex.md">
   ProtocolCloseAdapterCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-direct-oid-request-complete.md">
   ProtocolDirectOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-net-pnp-event.md">ProtocolNetPnPEvent</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-oid-request-complete.md">ProtocolOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-open-adapter-complete-ex.md">
   ProtocolOpenAdapterCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-receive-net-buffer-lists.md">
   ProtocolReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-send-net-buffer-lists-complete.md">
   ProtocolSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-status-ex.md">ProtocolStatusEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-unbind-adapter-ex.md">ProtocolUnbindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-uninstall.md">ProtocolUninstall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
