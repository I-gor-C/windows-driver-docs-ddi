---
UID: NF.fwpsk.FwpsStreamContinue0
title: FwpsStreamContinue0
author: windows-driver-content
description: The FwpsStreamContinue0 function resumes the processing of an inbound data stream that was previously deferred.Note  FwpsStreamContinue0 is a specific version of FwpsStreamContinue.
old-location: netvista\fwpsstreamcontinue0.htm
old-project: netvista
ms.assetid: 26cf2630-9602-4c70-a326-11e72f188ef9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsStreamContinue0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsStreamContinue0
req.alt-loc: Fwpkclnt.lib,Fwpkclnt.dll
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
req.iface: 
---

# FwpsStreamContinue0 function



## -description
<p>The 
  <b>FwpsStreamContinue0</b> function resumes the processing of an inbound data stream that was previously
  deferred.</p>


## -syntax

````
NTSTATUS NTAPI FwpsStreamContinue0(
  _In_ UINT64 flowId,
  _In_ UINT32 calloutId,
  _In_ UINT16 layerId,
  _In_ UINT32 streamFlags
);
````


## -parameters
<dl>

### -param <i>flowId</i> [in]

<dd>
<p>A run-time identifier that specifies the data flow that is being resumed. The run-time identifier
     for a data flow is provided to a callout driver through the FWPS_METADATA_FIELD_FLOW_HANDLE metadata
     value that the filter engine provided to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function.</p>
</dd>

### -param <i>calloutId</i> [in]

<dd>
<p>The run-time identifier for the callout that deferred the inbound data stream. This identifier was
     returned when the callout driver called either the 
     <a href="..\fwpsk\nf-fwpsk-fwpscalloutregister0.md">FwpsCalloutRegister0</a> or 
     <a href="..\fwpsk\nf-fwpsk-fwpscalloutregister1.md">FwpsCalloutRegister1</a> functions to
     register the callout with the filter engine.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The run-time identifier for the filtering layer at which the data stream is being processed. This
     value must be either FWPS_LAYER_STREAM_V4 or FWPS_LAYER_STREAM_V6. The run-time identifier for the layer
     at which the data stream is being processed is provided to a callout in the 
     <b>layerId</b> member of the 
     <a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a> structure that
     the filter engine passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function.</p>
</dd>

### -param <i>streamFlags</i> [in]

<dd>
<p>Flags that specify characteristics of the inbound data stream that is being resumed. A callout
     driver should specify the same stream flags that were set in the 
     <b>streamFlags</b> member of the 
     <a href="netvista.fwps_stream_data0">FWPS_STREAM_DATA0</a> structure that the
     filter engine passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function when the
     callout deferred the data stream.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsStreamContinue0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Processing of the data stream was successfully resumed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsStreamContinue0</b> function to resume processing an inbound data stream that was previously
    deferred. A data stream is deferred when a callout's 
    <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function sets the 
    <b>streamAction</b> member of the 
    <a href="netvista.fwps_stream_callout_io_packet0">
    FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure to FWPS_STREAM_ACTION_DEFER. The <b>FwpsStreamContinue0</b> function cannot be called from within a callout's <i>classifyFn</i> context.</p>

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
<a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwps_stream_callout_io_packet0">
   FWPS_STREAM_CALLOUT_IO_PACKET0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpscalloutregister0.md">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpscalloutregister1.md">FwpsCalloutRegister1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsStreamContinue0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
