---
UID: NF.fwpsk.FwpsFlowRemoveContext0
title: FwpsFlowRemoveContext0
author: windows-driver-content
description: The FwpsFlowRemoveContext0 function removes a previously associated context from a data flow.Note  FwpsFlowRemoveContext0 is a specific version of FwpsFlowRemoveContext.
old-location: netvista\fwpsflowremovecontext0.htm
ms.assetid: edc257bc-2805-47d8-827a-536e5d74793b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsFlowRemoveContext0
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsFlowRemoveContext0
req.iface: 
---

# FwpsFlowRemoveContext0 function



## -description
<p>The 
  <b>FwpsFlowRemoveContext0</b> function removes a previously associated context from a data flow.</p>


## -syntax

````
NTSTATUS NTAPI FwpsFlowRemoveContext0(
  _In_ UINT64 flowId,
  _In_ UINT16 layerId,
  _In_ UINT32 calloutId
);
````


## -parameters
<dl>

### -param <i>flowId</i> [in]

<dd>
<p>A run-time identifier that specifies the data flow from which to remove the context. The run-time
     identifier for a data flow is provided to a callout driver through the FWPS_METADATA_FIELD_FLOW_HANDLE
     metadata value that was passed to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The run-time identifier for the filtering layer from which the context is being removed. For more
     information, see 
     <a href="netvista.run_time_filtering_layer_identifiers">Run-time Filtering Layer
     Identifiers</a>. A callout driver should specify the same identifier that it specified when it called
     the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a> function to associate the context with the data flow.</p>
</dd>

### -param <i>calloutId</i> [in]

<dd>
<p>The run-time identifier for the callout in the filter engine. This identifier was returned when
     the callout driver called either the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> functions to
     register the callout with the filter engine.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsFlowRemoveContext0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The context was successfully removed from the data flow.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>There is no context currently associated with the data flow.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>If the 
    <b>FwpsFlowRemoveContext0</b> function returns STATUS_SUCCESS, 
    <b>FwpsFlowRemoveContext0</b> calls the 
    <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function
    synchronously. If 
    <b>FwpsFlowRemoveContext0</b> returns STATUS_PENDING, 
    <b>FwpsFlowRemoveContext0</b> calls 
    <i>flowDeleteFn</i> asynchronously because an active callout classification is in progress.</p>

<p>If the 
    <b>FwpsFlowRemoveContext0</b> function returns STATUS_SUCCESS, 
    <b>FwpsFlowRemoveContext0</b> calls the 
    <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function
    synchronously. If 
    <b>FwpsFlowRemoveContext0</b> returns STATUS_PENDING, 
    <b>FwpsFlowRemoveContext0</b> calls 
    <i>flowDeleteFn</i> asynchronously because an active callout classification is in progress.</p>

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
<p>Available starting with Windows Vista.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsFlowRemoveContext0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
