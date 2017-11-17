---
UID: NF.fwpsk.FwpsFlowAssociateContext0
title: FwpsFlowAssociateContext0
author: windows-driver-content
description: The FwpsFlowAssociateContext0 function associates a callout driver-defined context with a data flow.Note  FwpsFlowAssociateContext0 is a specific version of FwpsFlowAssociateContext.
old-location: netvista\fwpsflowassociatecontext0.htm
ms.assetid: 0a339457-77df-480b-adb8-9406507ec8d8
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
req.alt-api: FwpsFlowAssociateContext0
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
ms.keywords: FwpsFlowAssociateContext0
req.iface: 
---

# FwpsFlowAssociateContext0 function



## -description
<p>The 
  <b>FwpsFlowAssociateContext0</b> function associates a callout driver-defined context with a data
  flow.</p>


## -syntax

````
NTSTATUS NTAPI FwpsFlowAssociateContext0(
  _In_ UINT64 flowId,
  _In_ UINT16 layerId,
  _In_ UINT32 calloutId,
  _In_ UINT64 flowContext
);
````


## -parameters
<dl>

### -param <i>flowId</i> [in]

<dd>
<p>A run-time identifier that specifies the data flow with which to associate the context. The
     run-time identifier for a data flow is provided to a callout driver through the
     FWPS_METADATA_FIELD_FLOW_HANDLE metadata value that was passed to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The run-time identifier for the filtering layer with which the context is being associated. The context will be associated only with the specified filtering layer. For
     more information, see 
     <a href="netvista.run_time_filtering_layer_identifiers">Run-time Filtering Layer
     Identifiers</a>.</p>
</dd>

### -param <i>calloutId</i> [in]

<dd>
<p>The run-time identifier for the callout in the filter engine. This identifier was returned when
     the callout driver called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>, or  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a> function to
     register the callout with the filter engine.</p>
</dd>

### -param <i>flowContext</i> [in]

<dd>
<p>The callout driver-defined context to be associated with the data flow. This parameter must not be
     zero. This context is opaque to the filter engine.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsFlowAssociateContext0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The context was successfully associated with the data flow.</p><dl>
<dt><b>STATUS_INVALID PARAMETER</b></dt>
</dl><p>Either the <i>flowContext</i> parameter is <b>NULL</b> or the callout specified by the <i>calloutID</i> parameter does not have a <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> registered.</p><dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl><p>A context is already associated with the data flow. In this case, a callout driver should first
       call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551169">FwpsFlowRemoveContext0</a> function
       to remove the existing context and then call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a> function again to associate the new context with the data flow.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>When filtering a data flow, a callout driver can call the 
    <b>FwpsFlowAssociateContext0</b> function to associate a context with the data flow. It can then use this
    context to preserve any driver-specific data or state information between calls by the filter engine to a
    callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function for that data
    flow.</p>

<p>There must be a callout in the filter engine at the layer identified by the 
    <i>layerId</i> parameter that has registered a 
    <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function. Otherwise,
    the call to the 
    <b>FwpsFlowAssociateContext0</b> function will return STATUS_INVALID_PARAMETER. The filter engine calls that 
    <i>flowDeleteFn</i> callout function when the flow is terminated so that the callout driver can clean up
    the context associated with the flow.</p>

<p>You can call <b>FwpsFlowAssociateContext0</b> multiple times for the same flow. In each call, you must specify a different callout and a different context—one context per added callout.</p>

<p>The <b>FwpsFlowAssociateContext0</b> function associates a single context with a single added callout.</p>

<p>You can associate multiple contexts with a flow. However, each context must be associated with a different callout. The new callout can be at the same layer as the previous one or at a different layer.</p>

<p>For more information and sample code, see <a href="NULL">Associating Context with a Data Flow</a>
and the <a href="http://go.microsoft.com/fwlink/p/?LinkId=618934">Windows Filtering Platform Sample</a>.</p>

<p>When filtering a data flow, a callout driver can call the 
    <b>FwpsFlowAssociateContext0</b> function to associate a context with the data flow. It can then use this
    context to preserve any driver-specific data or state information between calls by the filter engine to a
    callout's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function for that data
    flow.</p>

<p>There must be a callout in the filter engine at the layer identified by the 
    <i>layerId</i> parameter that has registered a 
    <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function. Otherwise,
    the call to the 
    <b>FwpsFlowAssociateContext0</b> function will return STATUS_INVALID_PARAMETER. The filter engine calls that 
    <i>flowDeleteFn</i> callout function when the flow is terminated so that the callout driver can clean up
    the context associated with the flow.</p>

<p>You can call <b>FwpsFlowAssociateContext0</b> multiple times for the same flow. In each call, you must specify a different callout and a different context—one context per added callout.</p>

<p>The <b>FwpsFlowAssociateContext0</b> function associates a single context with a single added callout.</p>

<p>You can associate multiple contexts with a flow. However, each context must be associated with a different callout. The new callout can be at the same layer as the previous one or at a different layer.</p>

<p>For more information and sample code, see <a href="NULL">Associating Context with a Data Flow</a>
and the <a href="http://go.microsoft.com/fwlink/p/?LinkId=618934">Windows Filtering Platform Sample</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551169">FwpsFlowRemoveContext0</a>
</dt>
<dt>
<a href="NULL">Associating Context with a Data Flow</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?LinkId=618934">Windows Filtering Platform Sample</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsFlowAssociateContext0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
