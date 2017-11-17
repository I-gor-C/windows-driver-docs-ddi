---
UID: NF.ndis.NdisSetOptionalHandlers
title: NdisSetOptionalHandlers
author: windows-driver-content
description: NDIS drivers can call the NdisSetOptionalHandlers function to set or change the entry points of driver functions.
old-location: netvista\ndissetoptionalhandlers.htm
ms.assetid: 97649f4f-942a-47fc-a541-6f160c8b4eb4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: NdisSetOptionalHandlers
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
     <a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a> function or the 
     <i>NdisBindingHandle</i> value obtained by calling the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>
<p>For a miniport driver, this is the 
     <i>NdisDriverHandle</i> value passed to the 
     <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function</p>
<p>For a filter driver, this is the 
     <i>NdisDriverHandle</i> value passed to the 
     <a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a> function or the 
     <i>NdisFilterHandle</i> value passed to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>OptionalHandlers</i> 

<dd>
<p>A pointer to one of the following NDIS structures:
     </p>
<dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
        NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
        NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
        NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
        NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
        NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
        NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
        NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451559">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451566">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
        NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/e80a9999-2e4e-4da0-8aae-54ee71d9249d">
        NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/3eabbad5-b84b-4034-a0b6-d4d515cbc117">
        NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> returns <b>NDIS_STATUS_SUCCESS</b> if it set the driver entry points.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> failed because the miniport driver did not specify that it supports NDIS
       6.0 or later. A miniport driver specifies its NDIS version when it calls the 
       <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
       NdisMRegisterMiniportDriver</a> function.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> returns <b>NDIS_STATUS_FAILURE</b> if none of the preceding values
       applies.</p>

<p> </p>

## -remarks
<p>An NDIS driver can call 
    <b>NdisSetOptionalHandlers</b> to overwrite its default entry points. The structure types passed at 
    <i>OptionalHandlers</i> vary according to the type of driver.</p>

<p>Protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a> function. As an option, protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a> function or
    the 
    <a href="https://msdn.microsoft.com/59d18822-8ce2-4506-90d7-9f1cdc7a9e10">
    ProtocolOpenAdapterCompleteEx</a> function after the protocol driver has a valid handle from the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 2 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>Miniport drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
       NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
       NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451559">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451566">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
       NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
       NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451559">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451566">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 2 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a> function.</p>

<p>There are no optional filter driver services in the current Windows version.</p>

<p>Filter drivers can call 
    <b>NdisSetOptionalHandlers</b> for a filter module. Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">
    FilterSetModuleOptions</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
       NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564840">NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564846">NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566846">NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566852">NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
       NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564840">NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564846">NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566846">NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566852">NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 4 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>An NDIS driver can call 
    <b>NdisSetOptionalHandlers</b> to overwrite its default entry points. The structure types passed at 
    <i>OptionalHandlers</i> vary according to the type of driver.</p>

<p>Protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a> function. As an option, protocol drivers can call 
    <b>NdisSetOptionalHandlers</b> from the 
    <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a> function or
    the 
    <a href="https://msdn.microsoft.com/59d18822-8ce2-4506-90d7-9f1cdc7a9e10">
    ProtocolOpenAdapterCompleteEx</a> function after the protocol driver has a valid handle from the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 2 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>Miniport drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
       NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
       NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451559">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451566">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
       NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
       NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451559">NDIS_MINIPORT_SS_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451566">NDIS_NDK_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
       NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/66eb9528-e026-44cd-a775-c8d963036adc">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/1925cfd4-f83f-48a5-b928-2c663ac0dc61">
       NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>For more information on the 2 chimney offload structures, see 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

<p>Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a> function.</p>

<p>There are no optional filter driver services in the current Windows version.</p>

<p>Filter drivers can call 
    <b>NdisSetOptionalHandlers</b> for a filter module. Filter drivers call 
    <b>NdisSetOptionalHandlers</b> in the context of the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">
    FilterSetModuleOptions</a> function.</p>

<p>In this case, the valid structures are:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
       NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564840">NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564846">NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566846">NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566852">NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
       NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564840">NDIS_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564846">NDIS_CLIENT_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566846">NDIS_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566852">NDIS_PROVIDER_CHIMNEY_OFFLOAD_TCP_CHARACTERISTICS</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/400f238d-f235-4926-ad7c-c6560ee84431">FilterSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/12d541e1-04dd-4512-827e-d27f16260fe3">
   NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1f2285bb-be70-4496-905d-89106bf3712a">
   NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a7f365c-a252-4d8e-bddf-684b3298db5c">
   NDIS_FILTER_PARTIAL_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9348c338-9fb4-4eee-a50f-f709748da56b">
   NDIS_MINIPORT_CO_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/97820a22-aa20-4d47-a4c2-0c0d50540823">
   NDIS_MINIPORT_PNP_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/855e3231-502c-4c6f-99f9-7ad85354ccd5">
   NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/45001da1-5fe3-4383-8da7-31e3ee115c1f">
   NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/59d18822-8ce2-4506-90d7-9f1cdc7a9e10">
   ProtocolOpenAdapterCompleteEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/342e23ad-d38b-4100-949a-220b8fbdcf6e">ProtocolSetOptions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSetOptionalHandlers function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
