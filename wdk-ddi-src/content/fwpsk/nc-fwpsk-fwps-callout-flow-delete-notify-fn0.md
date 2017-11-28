---
UID: NC.fwpsk.FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0
title: FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0
author: windows-driver-content
description: The filter engine calls a callout's flowDeleteFn callout function to notify the callout that a data flow that is being processed by the callout is being terminated.
old-location: netvista\flowdeletefn.htm
old-project: netvista
ms.assetid: 65449a23-da5d-4884-b98e-030461eb019a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: flowDeleteFn
req.alt-loc: Fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 callback



## -description
<p>The filter engine calls a callout's 
  <i>flowDeleteFn</i> callout function to notify the callout that a data flow that is being processed by the
  callout is being terminated.</p>


## -prototype

````
FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 flowDeleteFn;

void NTAPI flowDeleteFn(
  _In_ UINT16 layerId,
  _In_ UINT32 calloutId,
  _In_ UINT64 flowContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>layerId</i> [in]

<dd>
<p>The run-time identifier for the filtering layer at which the data flow is being terminated. For
     more information, see 
     <a href="netvista.run_time_filtering_layer_identifiers">Run-time Filtering Layer
     Identifiers</a>.</p>
</dd>

### -param <i>calloutId</i> [in]

<dd>
<p>The run-time identifier for the callout in the filter engine. This is the same identifier that was
     returned when the callout driver called either the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> functions to
     register the callout with the filter engine.</p>
</dd>

### -param <i>flowContext</i> [in]

<dd>
<p>The most recent context that has been associated with the data flow by a call to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a> function.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A callout driver registers a callout's callout functions with the filter engine by calling either the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> functions.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function when it terminates a data flow so that the callout can clean up the
    context associated with the data flow. For example, this callout function will be called after an abrupt
    halt from RST, without 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> being called first. The filter
    engine calls this callout function only if the callout driver associated a context with the data flow.
    The context will be automatically removed from the data flow by the filter engine when the data flow
    terminates.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function only if the callout has been previously added to the filter engine at
    a filtering layer that supports data flows and the callout driver associates a context with the data
    flows that it processes. If a callout driver does not associate a context with the data flows that the
    callout processes, it should not implement a 
    <i>flowDeleteFn</i> callout function for the callout. In this situation, the callout driver should set the
    
    <i>flowDeleteFn</i> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a> structure to <b>NULL</b> when it
    registers the callout with the filter engine.</p>

<p>The FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 type is defined as a pointer to the 
    <i>flowDeleteFn</i> function as follows.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>A callout driver registers a callout's callout functions with the filter engine by calling either the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> functions.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function when it terminates a data flow so that the callout can clean up the
    context associated with the data flow. For example, this callout function will be called after an abrupt
    halt from RST, without 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> being called first. The filter
    engine calls this callout function only if the callout driver associated a context with the data flow.
    The context will be automatically removed from the data flow by the filter engine when the data flow
    terminates.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function only if the callout has been previously added to the filter engine at
    a filtering layer that supports data flows and the callout driver associates a context with the data
    flows that it processes. If a callout driver does not associate a context with the data flows that the
    callout processes, it should not implement a 
    <i>flowDeleteFn</i> callout function for the callout. In this situation, the callout driver should set the
    
    <i>flowDeleteFn</i> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a> structure to <b>NULL</b> when it
    registers the callout with the filter engine.</p>

<p>The FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 type is defined as a pointer to the 
    <i>flowDeleteFn</i> function as follows.</p>

<p>The filter engine calls a callout's 
    <i>flowDeleteFn</i> callout function at IRQL &lt;= DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
