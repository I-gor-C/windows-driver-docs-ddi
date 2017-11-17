---
UID: NF.ndis.NdisMRegisterMiniportDriver
title: NdisMRegisterMiniportDriver
author: windows-driver-content
description: A miniport driver calls the NdisMRegisterMiniportDriver function to register MiniportXxx entry points with NDIS as the first step in initialization.
old-location: netvista\ndismregisterminiportdriver.htm
ms.assetid: bed68aa8-499d-41fd-997b-a46316913cc8
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
req.alt-api: NdisMRegisterMiniportDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMRegisterMiniportDriver
req.iface: 
---

# NdisMRegisterMiniportDriver function



## -description
<p>A miniport driver calls the 
  <b>NdisMRegisterMiniportDriver</b> function to register 
  <i>MiniportXxx</i> entry points with NDIS as the first step in initialization.</p>


## -syntax

````
NDIS_STATUS NdisMRegisterMiniportDriver(
  _In_     PDRIVER_OBJECT                        DriverObject,
  _In_     PUNICODE_STRING                       RegistryPath,
  _In_opt_ NDIS_HANDLE                           MiniportDriverContext,
  _In_     PNDIS_MINIPORT_DRIVER_CHARACTERISTICS MiniportDriverCharacteristics,
  _Out_    PNDIS_HANDLE                          NdisMiniportDriverHandle
);
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to an opaque driver object that the miniport driver received in its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine at the 
     <i>Argument1</i> parameter (see 
     <a href="https://msdn.microsoft.com/cb28d202-4ac5-494f-a208-2a86ff1d0a90">DriverEntry of NDIS
     Miniport Drivers</a>).</p>
</dd>

### -param <i>RegistryPath</i> [in]

<dd>
<p>A pointer to an opaque registry path that the miniport driver received in its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine at the 
     <i>Argument2</i> parameter.</p>
</dd>

### -param <i>MiniportDriverContext</i> [in, optional]

<dd>
<p>A handle to a driver-allocated context area where the driver maintains state and configuration
     information.</p>
</dd>

### -param <i>MiniportDriverCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/2e2c8522-127d-49d5-a5d6-97f9403bec89">
     NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a> structure that the caller initialized.</p>
</dd>

### -param <i>NdisMiniportDriverHandle</i> [out]

<dd>
<p>A pointer to a caller-supplied handle variable. NDIS writes a handle to this variable that
     uniquely identifies this driver. The driver must save this handle for use in subsequent 
     <b>Ndis<i>Xxx</i></b> function calls.</p>
</dd>
</dl>

## -returns
<p><b>NdisMRegisterMiniportDriver</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a> registered the miniport driver successfully.</p><dl>
<dt><b>NDIS_STATUS_BAD_CHARACTERISTICS</b></dt>
</dl><p>The 
       <i>CharacteristicsLength</i> parameter is incorrect for the NDIS version that is specified at the 
       <b>MajorNdisVersion</b> member in the structure at 
       <i>MiniportDriverCharacteristics</i> .</p><dl>
<dt><b>NDIS_STATUS_BAD_VERSION</b></dt>
</dl><p>The 
       <b>MajorNdisVersion</b> or 
       <b>MinorNdisVersion</b> specified in the characteristics structure is invalid.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>A shortage of resources, possibly memory, prevented NDIS from registering the caller.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>This is a default error status, returned when none of the preceding errors caused the
       registration to fail.</p>

<p> </p>

## -remarks
<p>An NDIS driver calls 
    <b>NdisMRegisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. For more information, see 
    <a href="https://msdn.microsoft.com/cb28d202-4ac5-494f-a208-2a86ff1d0a90">DriverEntry of NDIS
    Miniport Drivers</a>.</p>

<p>Every miniport driver exports a set of standard 
    <i>MiniportXxx</i> functions by setting up the characteristics structure and calling 
    <b>NdisMRegisterMiniportDriver</b>. NDIS copies the characteristics structure to NDIS internal storage.
    Therefore, after it has registered, a driver cannot change its 
    <i>MiniportXxx</i> entry points.</p>

<p>To register its virtual miniport interface, an NDIS intermediate drivers must call 
    <b>NdisMRegisterMiniportDriver</b> with the NDIS_INTERMEDIATE_DRIVER flag set in the structure at 
    <i>MiniportDriverCharacteristics</i> . NDIS drivers that have a WDM lower edge must call 
    <b>NdisMRegisterMiniportDriver</b> with the NDIS_WDM_DRIVER flag set in the structure at 
    <i>MiniportDriverCharacteristics</i> .</p>

<p>Drivers can register as a combined miniport driver and intermediate driver. To register its physical
    miniport driver, a miniport-intermediate driver calls 
    <b>NdisMRegisterMiniportDriver</b> with appropriate parameters just as for any miniport driver. To
    register its virtual miniport interface, the driver calls 
    <b>NdisMRegisterMiniportDriver</b> again, but with the NDIS_INTERMEDIATE_DRIVER flag set in the 
    <i>MiniportDriverCharacteristics</i> parameter.</p>

<p>To enable miniport drivers to register optional services, NDIS calls the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function within
    the context of 
    <b>NdisMRegisterMiniportDriver</b>.</p>

<p>After a driver calls 
    <b>NdisMRegisterMiniportDriver</b>, the driver should be prepared to be called back at the 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function that
    is specified in the 
    <i>MiniportDriverCharacteristics</i> parameter.</p>

<p>If an error occurs in 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> after 
    <b>NdisMRegisterMiniportDriver</b> returns successfully, the driver must call the 
    <a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
    NdisMDeregisterMiniportDriver</a> function before 
    <b>DriverEntry</b> returns. If 
    <b>DriverEntry</b> succeeds, the driver must call 
    <b>NdisMDeregisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">MiniportDriverUnload</a> function.</p>

<p>An NDIS driver calls 
    <b>NdisMRegisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. For more information, see 
    <a href="https://msdn.microsoft.com/cb28d202-4ac5-494f-a208-2a86ff1d0a90">DriverEntry of NDIS
    Miniport Drivers</a>.</p>

<p>Every miniport driver exports a set of standard 
    <i>MiniportXxx</i> functions by setting up the characteristics structure and calling 
    <b>NdisMRegisterMiniportDriver</b>. NDIS copies the characteristics structure to NDIS internal storage.
    Therefore, after it has registered, a driver cannot change its 
    <i>MiniportXxx</i> entry points.</p>

<p>To register its virtual miniport interface, an NDIS intermediate drivers must call 
    <b>NdisMRegisterMiniportDriver</b> with the NDIS_INTERMEDIATE_DRIVER flag set in the structure at 
    <i>MiniportDriverCharacteristics</i> . NDIS drivers that have a WDM lower edge must call 
    <b>NdisMRegisterMiniportDriver</b> with the NDIS_WDM_DRIVER flag set in the structure at 
    <i>MiniportDriverCharacteristics</i> .</p>

<p>Drivers can register as a combined miniport driver and intermediate driver. To register its physical
    miniport driver, a miniport-intermediate driver calls 
    <b>NdisMRegisterMiniportDriver</b> with appropriate parameters just as for any miniport driver. To
    register its virtual miniport interface, the driver calls 
    <b>NdisMRegisterMiniportDriver</b> again, but with the NDIS_INTERMEDIATE_DRIVER flag set in the 
    <i>MiniportDriverCharacteristics</i> parameter.</p>

<p>To enable miniport drivers to register optional services, NDIS calls the 
    <a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a> function within
    the context of 
    <b>NdisMRegisterMiniportDriver</b>.</p>

<p>After a driver calls 
    <b>NdisMRegisterMiniportDriver</b>, the driver should be prepared to be called back at the 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function that
    is specified in the 
    <i>MiniportDriverCharacteristics</i> parameter.</p>

<p>If an error occurs in 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> after 
    <b>NdisMRegisterMiniportDriver</b> returns successfully, the driver must call the 
    <a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
    NdisMDeregisterMiniportDriver</a> function before 
    <b>DriverEntry</b> returns. If 
    <b>DriverEntry</b> succeeds, the driver must call 
    <b>NdisMDeregisterMiniportDriver</b> from its 
    <a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">MiniportDriverUnload</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/25c803cf-f8a6-4e41-a731-c3ae7f1db211">MiniportDriverUnload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/feecae74-960c-43cf-aa70-8ab0da3d0dfe">MiniportSetOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2e2c8522-127d-49d5-a5d6-97f9403bec89">
   NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
   NdisMDeregisterMiniportDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterMiniportDriver function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
