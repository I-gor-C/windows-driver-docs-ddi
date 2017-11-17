---
UID: NF.fwpsk.FwpsAleEndpointEnum0
title: FwpsAleEndpointEnum0
author: windows-driver-content
description: The FwpsAleEndpointEnum0 function enumerates application layer enforcement (ALE) endpoints.Note  FwpsAleEndpointEnum0 is a specific version of FwpsAleEndpointEnum.
old-location: netvista\fwpsaleendpointenum0.htm
ms.assetid: 8b3257ea-9eeb-426b-8c82-a4f0242861a8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAleEndpointEnum0
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
ms.keywords: FwpsAleEndpointEnum0
req.iface: 
---

# FwpsAleEndpointEnum0 function



## -description
<p>The 
  <b>FwpsAleEndpointEnum0</b> function enumerates application layer enforcement (ALE) endpoints.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAleEndpointEnum0(
  _In_  HANDLE                        engineHandle,
  _In_  HANDLE                        enumHandle,
  _In_  UINT32                        numEntriesRequested,
  _Out_ FWPS_ALE_ENDPOINT_PROPERTIES0 ***entries,
  _Out_ UINT32                        *numEntriesReturned
);
````


## -parameters
<dl>

### -param <i>engineHandle</i> [in]

<dd>
<p>The handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff550075">FwpmEngineOpen0</a>.</p>
</dd>

### -param <i>enumHandle</i> [in]

<dd>
<p>The enumeration handle created by a previous call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff550091">FwpsAleEndpointDestroyEnumHandle0</a>.</p>
</dd>

### -param <i>numEntriesRequested</i> [in]

<dd>
<p>The maximum number of endpoint property entries to return. The actual number of entries enumerated
     is returned in 
     <i>numEntriesReturned</i>. The actual number is less than the requested number only if fewer endpoints
     than the requested are present.</p>
</dd>

### -param <i>entries</i> [out]

<dd>
<p>A pointer to an array of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551218">FWPS_ALE_ENDPOINT_PROPERTIES0</a> structure pointers. Each structure contains the properties of a
     single endpoint. The array contains as many elements as the value returned in 
     <i>numEntriesReturned</i>.</p>
</dd>

### -param <i>numEntriesReturned</i> [out]

<dd>
<p>On return, the number of elements in the array of endpoint property structures pointed to by 
     <i>entries</i>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAleEndpointEnum0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>To enumerate ALE endpoints, the callout driver must first obtain an enumeration handle by calling 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550089">FwpsAleEndpointCreateEnumHandle0</a>. The handle returned is associated with any parameters specified
    in the optional 
    <i>enumTemplate</i> parameter of 
    <b>FwpsAleEndpointCreateEnumHandle0</b>.</p>

<p>After obtaining a handle, the callout driver can call 
    <b>FwpsAleEndpointEnum0</b> to get information about the endpoints that match the enumeration parameters
    of the handle.</p>

<p>When finished examining endpoint properties, the callout driver must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550091">FwpsAleEndpointDestroyEnumHandle0</a> to release the system resources associated with the enumeration
    handle.</p>

<p>To enumerate ALE endpoints, the callout driver must first obtain an enumeration handle by calling 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550089">FwpsAleEndpointCreateEnumHandle0</a>. The handle returned is associated with any parameters specified
    in the optional 
    <i>enumTemplate</i> parameter of 
    <b>FwpsAleEndpointCreateEnumHandle0</b>.</p>

<p>After obtaining a handle, the callout driver can call 
    <b>FwpsAleEndpointEnum0</b> to get information about the endpoints that match the enumeration parameters
    of the handle.</p>

<p>When finished examining endpoint properties, the callout driver must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff550091">FwpsAleEndpointDestroyEnumHandle0</a> to release the system resources associated with the enumeration
    handle.</p>

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
<a href="https://msdn.microsoft.com/5daa3dd4-e499-4a72-b784-8a0e1ef3e92b">
   FwpsAleEndpointCreateEnumHandle0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/45ec429e-d324-40c9-bedc-acd75ccb160e">
   FwpsAleEndpointDestroyEnumHandle0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551128">FwpsAleEndpointGetById0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0c825695-7fef-4eb1-8615-f41c526aa32d">
   FwpsAleEndpointGetSecurityInfo0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7b7fed83-dcf8-466d-8bd7-42a5ed15cced">
   FwpsAleEndpointSetSecurityInfo0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAleEndpointEnum0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
