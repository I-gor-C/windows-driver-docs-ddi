---
UID: NF.ndis.NdisSetOptionalHandlers
title: NdisSetOptionalHandlers
author: windows-driver-content
description: NDIS drivers can call the NdisSetOptionalHandlers function to set or change the entry points of driver functions.
old-location: netvista\ndissetoptionalhandlers.htm
old-project: netvista
ms.assetid: 97649f4f-942a-47fc-a541-6f160c8b4eb4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisSetOptionalHandlers
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSetOptionalHandlers
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisSetOptionalHandlers function



## -description
<p>NDIS drivers can call the 
  <b>NdisSetOptionalHandlers</b> function to set or change the entry points of driver functions.</p>


## -syntax

````
NDIS_STATUS NdisSetOptionalHandlers(
   NDIS_HANDLE                    NdisHandle,
   PNDIS_DRIVER_OPTIONAL_HANDLERS OptionalHandlers
);
````


## -parameters
<dl>

### -param <i>NdisHandle</i> 

<dd>
<p>An NDIS handle that identifies a driver or driver instance.
     </p>
<p>For a protocol driver, this is the 
     <i>NdisDriverHandle</i> value passed to the 
     <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function or the 
     <i>NdisBindingHandle</i> value obtained by calling the 
     <a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a> function.</p>
<p>For a miniport driver, this is the 
     <i>NdisDriverHandle</i> value passed to the 
     <a href="netvista.miniportsetoptions">MiniportSetOptions</a> function</p>
<p>For a filter driver, this is the 
     <i>NdisDriverHandle</i> value passed to the 
     <a href="netvista.filtersetoptions">FilterSetOptions</a> function or the 
     <i>NdisFilterHandle</i> value passed to the 
     <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function.</p>
</dd>

### -param <i>OptionalHandlers</i> 

<dd>
<p>A pointer to one of the following NDIS structures:
     </p>
<dl>
<dd>
<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-generic-characteristics.md">
        NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-tcp-characteristics.md">
        NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
        NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
        NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-filter-partial-characteristics.md">
        NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-miniport-co-characteristics.md">
        NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-miniport-pnp-characteristics.md">
        NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-miniport-ss-characteristics.md">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndisndk\ns-ndisndk--ndis-ndk-provider-characteristics.md">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
        NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndischimney\ns-ndischimney--ndis-provider-chimney-offload-generic-characteristics.md">
        NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndischimney\ns-ndischimney--ndis-provider-chimney-offload-tcp-characteristics.md">
        NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
        NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>NdisSetOptionalHandlers</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> returns <b>NDIS_STATUS_SUCCESS</b> if it set the driver entry points.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> failed because the miniport driver did not specify that it supports NDIS
       6.0 or later. A miniport driver specifies its NDIS version when it calls the 
       <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
       NdisMRegisterMiniportDriver</a> function.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> returns <b>NDIS_STATUS_FAILURE</b> if none of the preceding values
       applies.</p>

<p> </p>

## -remarks
<p>An NDIS driver can call 
    <b>NdisSetOptionalHandlers</b> to overwrite its default entry points. The structure types passed at 
    <i>OptionalHandlers</i> vary according to the type of driver.</p>

<p>Protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function. As an option, protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function or
    the 
    <a href="..\ndis\nc-ndis-protocol-open-adapter-complete-ex.md">
    ProtocolOpenAdapterCompleteEx</a> function after the protocol driver has a valid handle from the 
    <a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a> function.</p>

<p>In this case, the valid structures are:</p>

<p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-generic-characteristics.md">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-tcp-characteristics.md">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 2 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>Miniport drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="netvista.miniportsetoptions">MiniportSetOptions</a> function.</p>

<p>
<a href="..\ndis\ns-ndis--ndis-miniport-co-characteristics.md">
       NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-miniport-pnp-characteristics.md">
       NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-miniport-ss-characteristics.md">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndisndk\ns-ndisndk--ndis-ndk-provider-characteristics.md">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>

<p>Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="netvista.filtersetoptions">FilterSetOptions</a> function.</p>

<p>There are no optional filter driver services in the current Windows version.</p>

<p>Filter drivers can call 
    <b>NdisSetOptionalHandlers</b> for a filter module. Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="netvista.filtersetmoduleoptions">
    FilterSetModuleOptions</a> function.</p>

<p>
<a href="..\ndis\ns-ndis--ndis-filter-partial-characteristics.md">
       NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-generic-characteristics.md">NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-client-chimney-offload-tcp-characteristics.md">NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-provider-chimney-offload-generic-characteristics.md">NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--ndis-provider-chimney-offload-tcp-characteristics.md">NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 4 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>
</dt>
<dt>
<a href="netvista.filtersetoptions">FilterSetOptions</a>
</dt>
<dt>
<a href="netvista.miniportsetoptions">MiniportSetOptions</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
   NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
   NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-partial-characteristics.md">
   NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-co-characteristics.md">
   NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-pnp-characteristics.md">
   NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
   NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-shared-memory-provider-characteristics.md">
   NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-open-adapter-complete-ex.md">
   ProtocolOpenAdapterCompleteEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSetOptionalHandlers function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
