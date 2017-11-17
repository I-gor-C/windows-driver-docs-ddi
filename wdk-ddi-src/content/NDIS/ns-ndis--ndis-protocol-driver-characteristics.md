---
UID: NS.ndis._NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
title: NDIS_PROTOCOL_DRIVER_CHARACTERISTICS
author: windows-driver-content
description: To specify its driver characteristics, a protocol driver initializes an NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure and passes it to NDIS.
old-location: netvista\ndis_protocol_driver_characteristics.htm
ms.assetid: db64c160-9db6-4b23-af14-e64acdb9ef57
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
ms.keywords: NDIS_PROTOCOL_DRIVER_CHARACTERISTICS, NDIS_PROTOCOL_DRIVER_CHARACTERISTICS, *PNDIS_PROTOCOL_DRIVER_CHARACTERISTICS
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

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_PROTOCOL_DRIVER_CHARACTERISTICS.
     </p>
<p>To indicate the version of the <b>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</b> structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_2"></a><a id="ndis_protocol_driver_characteristics_revision_2"></a>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_2

<dd>
<p>Added the 
        <b>DirectOidRequestCompleteHandler</b> member for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to
        NDIS_SIZEOF_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_2.</p>
</dd>

### -field <a id="NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1"></a><a id="ndis_protocol_driver_characteristics_revision_1"></a>NDIS_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1

<dd>
<p>Original version for NDIS 6.0.</p>
<p>Set the 
        <b>Size</b> member to
        NDIS_SIZEOF_PROTOCOL_DRIVER_CHARACTERISTICS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>MajorNdisVersion</b>

<dd>
<p>The major version of the NDIS library the protocol driver is using. The current value is
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
<p>Reserved for the major version number of the protocol driver. Protocol drivers can specify any
     value that they require.</p>
</dd>

### -field <b>MinorDriverVersion</b>

<dd>
<p>Reserved for the minor version number of the protocol driver. Protocol drivers can specify any
     value that they require.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS. Protocol drivers should set this member to zero.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>A Unicode string that is the service name of the protocol driver.</p>
</dd>

### -field <b>SetOptionsHandler</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a> function.</p>
</dd>

### -field <b>BindAdapterHandlerEx</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">
     ProtocolBindAdapterEx</a> function.</p>
</dd>

### -field <b>UnbindAdapterHandlerEx</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/19fa7be2-acb9-42f6-bd9f-5be3e3c8b5fa">
     ProtocolUnbindAdapterEx</a> function.</p>
</dd>

### -field <b>OpenAdapterCompleteHandlerEx</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/59d18822-8ce2-4506-90d7-9f1cdc7a9e10">
     ProtocolOpenAdapterCompleteEx</a> function.</p>
</dd>

### -field <b>CloseAdapterCompleteHandlerEx</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/62cc047a-bc91-4e1e-817e-7fd509d4d90e">
     ProtocolCloseAdapterCompleteEx</a> function.</p>
</dd>

### -field <b>NetPnPEventHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/3f50bcba-c7d2-4d81-bd8b-6080e08fbe74">ProtocolNetPnPEvent</a> function.</p>
</dd>

### -field <b>UninstallHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/959baf54-849c-4bb1-b4c5-4d5537e1d688">ProtocolUninstall</a> function, if any,
     or <b>NULL</b>.</p>
</dd>

### -field <b>OidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/2706577e-ba03-4347-9672-7303752ec0fe">
     ProtocolOidRequestComplete</a> function.</p>
</dd>

### -field <b>StatusHandlerEx</b>

<dd>
<p>The entry point of the caller's 
     <a href="https://msdn.microsoft.com/5bc5a24f-5f28-4502-8776-b1cf15fd8283">ProtocolStatusEx</a> function, if any, or
     <b>NULL</b>.</p>
</dd>

### -field <b>ReceiveNetBufferListsHandler</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/c964b4b8-ab07-4a07-9965-5cc06c028c20">
     ProtocolReceiveNetBufferLists</a> function.</p>
</dd>

### -field <b>SendNetBufferListsCompleteHandler</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/bc9197c5-ce0b-42b2-8225-fb9d83427ac8">
     ProtocolSendNetBufferListsComplete</a> function.</p>
</dd>

### -field <b>DirectOidRequestCompleteHandler</b>

<dd>
<p>The entry point of the caller's 
      <a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
      ProtocolDirectOidRequestComplete</a> function. This is an optional function. Set this entry point to
      <b>NULL</b> if the protocol driver does not support the direct OID request interface.</p>
</dd>
</dl>

## -remarks
<p>A protocol driver calls the 
    <a href="https://msdn.microsoft.com/b48571eb-13a2-4541-80ac-c8d31f378d37">
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564520">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/62cc047a-bc91-4e1e-817e-7fd509d4d90e">
   ProtocolCloseAdapterCompleteEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
   ProtocolDirectOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f50bcba-c7d2-4d81-bd8b-6080e08fbe74">ProtocolNetPnPEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2706577e-ba03-4347-9672-7303752ec0fe">ProtocolOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/59d18822-8ce2-4506-90d7-9f1cdc7a9e10">
   ProtocolOpenAdapterCompleteEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c964b4b8-ab07-4a07-9965-5cc06c028c20">
   ProtocolReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bc9197c5-ce0b-42b2-8225-fb9d83427ac8">
   ProtocolSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5bc5a24f-5f28-4502-8776-b1cf15fd8283">ProtocolStatusEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/19fa7be2-acb9-42f6-bd9f-5be3e3c8b5fa">ProtocolUnbindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/959baf54-849c-4bb1-b4c5-4d5537e1d688">ProtocolUninstall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
