---
UID: NS.ndis._NDIS_PROTOCOL_CO_CHARACTERISTICS
title: NDIS_PROTOCOL_CO_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_PROTOCOL_CO_CHARACTERISTICS structure specifies CoNDIS entry points for CoNDIS protocol drivers.
old-location: netvista\ndis_protocol_co_characteristics.htm
old-project: netvista
ms.assetid: 855e3231-502c-4c6f-99f9-7ad85354ccd5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PROTOCOL_CO_CHARACTERISTICS, NDIS_PROTOCOL_CO_CHARACTERISTICS, *PNDIS_PROTOCOL_CO_CHARACTERISTICS
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
req.alt-api: NDIS_PROTOCOL_CO_CHARACTERISTICS
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

# NDIS_PROTOCOL_CO_CHARACTERISTICS structure



## -description
<p>The NDIS_PROTOCOL_CO_CHARACTERISTICS structure specifies CoNDIS entry points for CoNDIS protocol
  drivers.</p>


## -syntax

````
typedef struct _NDIS_PROTOCOL_CO_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                        Header;
  ULONG                                     Flags;
  CO_STATUS_HANDLER_EX                      CoStatusHandlerEx;
  CO_AF_REGISTER_NOTIFY_HANDLER             CoAfRegisterNotifyHandler;
  CO_RECEIVE_NET_BUFFER_LISTS_HANDLER       CoReceiveNetBufferListsHandler;
  CO_SEND_NET_BUFFER_LISTS_COMPLETE_HANDLER CoSendNetBufferListsCompleteHandler;
} NDIS_PROTOCOL_CO_CHARACTERISTICS, *PNDIS_PROTOCOL_CO_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     protocol driver CoNDIS characteristics structure (NDIS_PROTOCOL_CO_CHARACTERISTICS). The driver sets the
     
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_CO_PROTOCOL_CHARACTERISTICS, the 
     <b>Revision</b> member to NDIS_PROTOCOL_CO_CHARACTERISTICS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PROTOCOL_CO_CHARACTERISTICS_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field <b>CoStatusHandlerEx</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndis\nc-ndis-protocol-co-status-ex.md">ProtocolCoStatusEx</a> function.</p>
</dd>

### -field <b>CoAfRegisterNotifyHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndis\nc-ndis-protocol-co-af-register-notify.md">
     ProtocolCoAfRegisterNotify</a> function.</p>
</dd>

### -field <b>CoReceiveNetBufferListsHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
     ProtocolCoReceiveNetBufferLists</a> function.</p>
</dd>

### -field <b>CoSendNetBufferListsCompleteHandler</b>

<dd>
<p>The entry point of the driver's 
     <a href="..\ndis\nc-ndis-protocol-co-send-net-buffer-lists-complete.md">
     ProtocolCoSendNetBufferListsComplete</a> function.</p>
</dd>
</dl>

## -remarks
<p>To specify entry points for CoNDIS, a protocol driver initializes an NDIS_PROTOCOL_CO_CHARACTERISTICS
    structure and passes it to the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">
    NdisSetOptionalHandlers</a> function.</p>

<p>The protocol driver calls 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function.</p>

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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-af-register-notify.md">ProtocolCoAfRegisterNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
   ProtocolCoReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-send-net-buffer-lists-complete.md">
   ProtocolCoSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-status-ex.md">ProtocolCoStatusEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROTOCOL_CO_CHARACTERISTICS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
