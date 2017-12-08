---
UID: NS.ndischimney._NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS
title: NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies a protocol driver's generic chimney offload entry points.
old-location: netvista\ndis_client_chimney_offload_generic_characteristics.htm
old-project: netvista
ms.assetid: 66eb9528-e026-44cd-a775-c8d963036adc
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS, NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS, *PNDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS
req.alt-loc: ndischimney.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure specifies a protocol driver's
  generic chimney offload entry points. Generic chimney offload entry points apply to all chimney offload
  types. Currently, TCP chimney offload is the only defined chimney offload type.</p>


## -syntax

````
typedef struct _NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS {
  NDIS_OBJECT_HEADER                  Header;
  ULONG                               Flags;
  INITIATE_OFFLOAD_COMPLETE_HANDLER   InitiateOffloadCompleteHandler;
  TERMINATE_OFFLOAD_COMPLETE_HANDLER  TerminateOffloadCompleteHandler;
  UPDATE_OFFLOAD_COMPLETE_HANDLER     UpdateOffloadCompleteHandler;
  INVALIDATE_OFFLOAD_COMPLETE_HANDLER InvalidateOffloadCompleteHandler;
  QUERY_OFFLOAD_COMPLETE_HANDLER      QueryOffloadCompleteHandler;
  INDICATE_OFFLOAD_EVENT_HANDLER      IndicateOffloadEventHandler;
} NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS, *PNDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The header of the NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure. The header is
     formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the
     NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure and the size of the
     NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure, including the header, in bytes. The 
     <b>Type</b> member of the header is not significant.</p>
</dd>

### -field Flags

<dd>
<p>Reserved for system use.</p>
</dd>

### -field InitiateOffloadCompleteHandler

<dd>
<p>Specifies the entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-initiate-offload-complete-handler.md">
     ProtocolInitiateOffloadComplete</a> function.</p>
</dd>

### -field TerminateOffloadCompleteHandler

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-terminate-offload-complete-handler.md">
     ProtocolTerminateOffloadComplete</a> function.</p>
</dd>

### -field UpdateOffloadCompleteHandler

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-update-offload-complete-handler.md">
     ProtocolUpdateOffloadComplete</a> function.</p>
</dd>

### -field InvalidateOffloadCompleteHandler

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-invalidate-offload-complete-handler.md">
     ProtocolInvalidateOffloadComplete</a> function.</p>
</dd>

### -field QueryOffloadCompleteHandler

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-query-offload-complete-handler.md">
     ProtocolQueryOffloadComplete</a> function.</p>
</dd>

### -field IndicateOffloadEventHandler

<dd>
<p>The entry point of the driver's 
     <a href="..\ndischimney\nc-ndischimney-indicate-offload-event-handler.md">
     ProtocolIndicateOffloadEvent</a> function.</p>
</dd>
</dl>

## -remarks
<p>To register its generic chimney offload entry points, a protocol or intermediate driver calls the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function
    in the context of the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function. To the 
    <b>NdisSetOptionalHandlers</b> function,
    the protocol or intermediate driver passes a pointer to the
    NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
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
<a href="..\ndischimney\nc-ndischimney-indicate-offload-event-handler.md">
   ProtocolIndicateOffloadEvent</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-initiate-offload-complete-handler.md">
   ProtocolInitiateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-invalidate-offload-complete-handler.md">
   ProtocolInvalidateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-query-offload-complete-handler.md">
   ProtocolQueryOffloadComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-terminate-offload-complete-handler.md">
   ProtocolTerminateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-update-offload-complete-handler.md">
   ProtocolUpdateOffloadComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
