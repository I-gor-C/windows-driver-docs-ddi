---
UID: NF.fwpsk.FwpsAleEndpointGetById0
title: FwpsAleEndpointGetById0
author: windows-driver-content
description: The FwpsAleEndpointGetById0 function retrieves information about an application layer enforcement (ALE) endpoint.Note  FwpsAleEndpointGetById0 is a specific version of FwpsAleEndpointGetById.
old-location: netvista\fwpsaleendpointgetbyid0.htm
old-project: netvista
ms.assetid: fa9a5078-d254-4b4a-bbfb-256491beff5f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsAleEndpointGetById0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAleEndpointGetById0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FwpsAleEndpointGetById0 function



## -description
<p>The 
  <b>FwpsAleEndpointGetById0</b> function retrieves information about an application layer enforcement (ALE)
  endpoint.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAleEndpointGetById0(
  _In_  HANDLE                        engineHandle,
  _In_  UINT64                        endpointId,
  _Out_ FWPS_ALE_ENDPOINT_PROPERTIES0 **properties
);
````


## -parameters
<dl>

### -param <i>engineHandle</i> [in]

<dd>
<p>A handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a>.</p>
</dd>

### -param <i>endpointId</i> [in]

<dd>
<p>The unique endpoint identifier.</p>
</dd>

### -param <i>properties</i> [out]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_ale_endpoint_properties0">
     FWPS_ALE_ENDPOINT_PROPERTIES0</a> structure that contains the properties of the endpoint.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAleEndpointGetById0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks


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
<p>Available starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointenum0.md">FwpsAleEndpointEnum0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointgetsecurityinfo0.md">
   FwpsAleEndpointGetSecurityInfo0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointsetsecurityinfo0.md">
   FwpsAleEndpointSetSecurityInfo0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAleEndpointGetById0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
