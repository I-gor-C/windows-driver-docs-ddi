---
UID: NF.fwpsk.FwpsAleEndpointCreateEnumHandle0
title: FwpsAleEndpointCreateEnumHandle0
author: windows-driver-content
description: The FwpsAleEndpointCreateEnumHandle0 function creates a handle that can be used with other application layer enforcement (ALE) endpoint functions to enumerate endpoint data.Note  FwpsAleEndpointCreateEnumHandle0 is a specific version of FwpsAleEndpointCreateEnumHandle. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwpsaleendpointcreateenumhandle0.htm
old-project: netvista
ms.assetid: 5daa3dd4-e499-4a72-b784-8a0e1ef3e92b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsAleEndpointCreateEnumHandle0
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
req.alt-api: FwpsAleEndpointCreateEnumHandle0
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

# FwpsAleEndpointCreateEnumHandle0 function



## -description
<p>The 
  <b>FwpsAleEndpointCreateEnumHandle0</b> function creates a handle that can be used with other application layer enforcement (ALE) endpoint
  functions to enumerate endpoint data.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAleEndpointCreateEnumHandle0(
  _In_           HANDLE                           engineHandle,
  _In_opt_ const FWPS_ALE_ENDPOINT_ENUM_TEMPLATE0 *enumTemplate,
  _Out_          HANDLE                           *enumHandle
);
````


## -parameters
<dl>

### -param <i>engineHandle</i> [in]

<dd>
<p>Handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a>.</p>
</dd>

### -param <i>enumTemplate</i> [in, optional]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_ale_endpoint_enum_template0">
     FWPS_ALE_ENDPOINT_ENUM_TEMPLATE0</a> structure that contains parameters to narrow the endpoint
     enumeration results.</p>
</dd>

### -param <i>enumHandle</i> [out]

<dd>
<p>The newly created enumeration handle.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAleEndpointCreateEnumHandle0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>After using the handle acquired by calling 
    <b>FwpsAleEndpointCreateEnumHandle0</b>, the callout driver must release the system resources associated
    with the handle by calling 
    <a href="..\fwpsk\nf-fwpsk-fwpsaleendpointdestroyenumhandle0.md">
    FwpsAleEndpointDestroyEnumHandle0</a>.</p>

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
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointdestroyenumhandle0.md">
   FwpsAleEndpointDestroyEnumHandle0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointenum0.md">FwpsAleEndpointEnum0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAleEndpointCreateEnumHandle0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
