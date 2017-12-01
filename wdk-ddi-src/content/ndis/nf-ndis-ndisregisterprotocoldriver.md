---
UID: NF.ndis.NdisRegisterProtocolDriver
title: NdisRegisterProtocolDriver
author: windows-driver-content
description: A protocol driver calls the NdisRegisterProtocolDriver function to register its ProtocolXxx functions with NDIS.
old-location: netvista\ndisregisterprotocoldriver.htm
old-project: netvista
ms.assetid: b48571eb-13a2-4541-80ac-c8d31f378d37
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisRegisterProtocolDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRegisterProtocolDriver
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
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

# NdisRegisterProtocolDriver function



## -description
<p>A protocol driver calls the
  <b>NdisRegisterProtocolDriver</b> function to register its 
  <i>ProtocolXxx</i> functions with NDIS.</p>


## -syntax

````
NDIS_STATUS NdisRegisterProtocolDriver(
  _In_opt_ NDIS_HANDLE                           ProtocolDriverContext,
  _In_     PNDIS_PROTOCOL_DRIVER_CHARACTERISTICS ProtocolCharacteristics,
  _Out_    PNDIS_HANDLE                          NdisProtocolHandle
);
````


## -parameters
<dl>

### -param <i>ProtocolDriverContext</i> [in, optional]

<dd>
<p>A handle to a driver-allocated context area where the driver maintains state and configuration
     information.</p>
</dd>

### -param <i>ProtocolCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-protocol-driver-characteristics.md">
     NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</a> structure that the protocol driver created and initialized
     with its 
     <i>ProtocolXxx</i> function entry points.</p>
</dd>

### -param <i>NdisProtocolHandle</i> [out]

<dd>
<p>A pointer to a caller-supplied handle variable. NDIS writes a handle to this variable that
     uniquely identifies the driver that is registering. The driver must save this handle for use in
     subsequent 
     <b>Ndis<i>Xxx</i></b> function calls.</p>
</dd>
</dl>

## -returns
<p><b>NdisRegisterProtocolDriver</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">NdisRegisterProtocolDriver</a> returns NDIS_STATUS_SUCCESS if it registered the protocol
       driver.</p><dl>
<dt><b>NDIS_STATUS_BAD_VERSION</b></dt>
</dl><p>The version specified in the 
       <b>MajorNdisVersion</b> member of the structure at 
       <i>ProtocolCharacteristics</i> is invalid.</p><dl>
<dt><b>NDIS_STATUS_BAD_CHARACTERISTICS</b></dt>
</dl><p>Some members of the structure at the 
       <i>ProtocolCharacteristics</i> parameter are invalid.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">NdisRegisterProtocolDriver</a> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>
<a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">NdisRegisterProtocolDriver</a> returns NDIS_STATUS_FAILURE if none of the preceding values
       applies.</p>

<p> </p>

## -remarks
<p>A protocol driver calls the 
    <b>NdisRegisterProtocolDriver</b> function from its 
    <a href="..\wdm\nc-wdm-driver-initialize.md">DriverEntry</a> routine. For more information about 
    <b>DriverEntry</b>, see 
    <a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS
    Protocol Drivers</a>.</p>

<p>Drivers that call <b>
    NdisRegisterProtocolDriver</b> must be prepared for an immediate call to any of their <i>ProtocolXxx</i> functions.</p>

<p>Every protocol driver exports a set of 
    <i>ProtocolXxx</i> functions by setting up the 
    <a href="..\ndis\ns-ndis--ndis-protocol-driver-characteristics.md">
    NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</a> structure and calling 
    <b>NdisRegisterProtocolDriver</b>. NDIS copies this structure to the NDIS library's internal storage.</p>

<p>To allow protocol drivers to register optional services, NDIS calls the 
    <a href="..\ndis\nc-ndis-set-options.md">ProtocolSetOptions</a> function within
    the context of 
    <b>NdisRegisterProtocolDriver</b>.</p>

<p>Protocol drivers call the 
    <a href="..\ndis\nf-ndis-ndisderegisterprotocoldriver.md">
    NdisDeregisterProtocolDriver</a> function to release resources that were previously allocated with 
    <b>NdisRegisterProtocolDriver</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="devtest.ndis_irql_protocol_driver_function">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-driver-characteristics.md">
   NDIS_PROTOCOL_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisderegisterprotocoldriver.md">NdisDeregisterProtocolDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRegisterProtocolDriver function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
