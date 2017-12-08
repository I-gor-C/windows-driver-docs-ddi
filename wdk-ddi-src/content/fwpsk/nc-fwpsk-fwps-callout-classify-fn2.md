---
UID: NC.fwpsk.FWPS_CALLOUT_CLASSIFY_FN2
title: FWPS_CALLOUT_CLASSIFY_FN2
author: windows-driver-content
description: The filter engine calls a callout's classifyFn2 callout function whenever there is data to be processed by the callout.Note  classifyFn2 is the specific version of classifyFn used in Windows 8 and later.
old-location: netvista\classifyfn2.htm
old-project: netvista
ms.assetid: de8220de-cf71-4718-876e-ef02c15fc948
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: classifyFn2
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

# FWPS_CALLOUT_CLASSIFY_FN2 callback



## -description
<p>The filter engine calls a callout's 
  <i>classifyFn2</i> callout function whenever there is data to be processed by the callout.<div class="alert"><b>Note</b>  <i>classifyFn2</i> is the specific version of <a href="netvista.classifyfn">classifyFn</a> used in Windows 8 and later. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information. For Windows 7, <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn1.md">classifyFn1</a> is available. For Windows Vista, <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn0</a> is available.</div>
<div> </div>
</p>


## -prototype

````
FWPS_CALLOUT_CLASSIFY_FN2 classifyFn2;

void NTAPI classifyFn2(
  _In_        const FWPS_INCOMING_VALUES0          *inFixedValues,
  _In_        const FWPS_INCOMING_METADATA_VALUES0 *inMetaValues,
  _Inout_opt_       void                           *layerData,
  _In_opt_    const void                           *classifyContext,
  _In_        const FWPS_FILTER2                   *filter,
  _In_              UINT64                         flowContext,
  _Inout_           FWPS_CLASSIFY_OUT0             *classifyOut
)
{ ... }
````


## -parameters
<dl>

### -param inFixedValues [in]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a> structure. This
     structure contains the values for each of the data fields in the layer being filtered.</p>
</dd>

### -param inMetaValues [in]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure. This structure contains the values for each of the
     metadata fields in the layer being filtered.</p>
</dd>

### -param layerData [in, out, optional]

<dd>
<p>A pointer to a structure that describes the raw data in the layer being filtered. This parameter
     might be NULL, depending on the layer being filtered and the conditions under which the 
     <i>classifyFn2</i> callout function is called. For the stream layer, this parameter points to an 
     <a href="netvista.fwps_stream_callout_io_packet0">
     FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure. For all of the other layers, this parameter points to a 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure if it is not
     NULL.</p>
</dd>

### -param classifyContext [in, optional]

<dd>
<p>A pointer to context data associated with the callout driver by the filter engine.</p>
</dd>

### -param filter [in]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_filter2">FWPS_FILTER2</a> structure. This structure
     describes the filter that specifies the callout for the filter's action.</p>
</dd>

### -param flowContext [in]

<dd>
<p>A UINT64-typed variable that contains the context associated with the data flow. If no context is
     associated with the data flow, then this parameter is zero. If the callout is added to the filter engine
     at a filtering layer that does not support data flows, the 
     <i>classifyFn2</i> callout function should ignore this parameter.</p>
</dd>

### -param classifyOut [in, out]

<dd>
<p>A pointer to an 
     <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure that
     receives any data that the 
     <i>classifyFn2</i> callout function returns to the caller.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="..\fwpsk\nf-fwpsk-fwpscalloutregister2.md">FwpsCalloutRegister2</a> function.</p>

<p>The filter engine calls a callout's 
    <i>classifyFn2</i> callout function with data to be processed whenever all of the test conditions are true
    for a filter in the filter engine that specifies the callout for the filter's action.</p>

<p>A callout's 
    <i>classifyFn2</i> callout function should clear the FWPS_RIGHT_ACTION_WRITE flag in the 
    <b>rights</b> member of the 
    <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure in any of
    the following situations:</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_BLOCK.</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_PERMIT and the FWPS_FILTER_FLAG_CLEAR_ACTION_RIGHT flag is set in the 
      <b>Flags</b> member of the 
      <a href="netvista.fwps_filter2">FWPS_FILTER2</a> structure.</p>

<p>When a callout has indicated that it intends to modify the clone net buffer list by setting the 
      <i>intendToModify</i> parameter to TRUE in a call to the 
      <a href="..\fwpsk\nf-fwpsk-fwpsreferencenetbufferlist0.md">
      FwpsReferenceNetBufferList0</a> function.</p>

<p>This function is essentially identical to the previous version, 
    <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn1.md">classifyFn1</a>. However, the updated <a href="netvista.fwps_filter2">FWPS_FILTER2</a> structure is pointed to by the 
       <i>filter</i> parameter and the <i>layerData</i> parameter is optional.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
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
<a href="netvista.classifyfn">classifyFn</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn1.md">classifyFn1</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpscalloutregister2.md">FwpsCalloutRegister2</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsreferencenetbufferlist0.md">FwpsReferenceNetBufferList0</a>
</dt>
<dt>
<a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="netvista.fwps_filter2">FWPS_FILTER2</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.associating_context_with_a_data_flow">Associating Context with a Data Flow</a>
</dt>
<dt>
<a href="netvista.callout_driver_callout_functions">Callout Driver Callout Functions</a>
</dt>
<dt>
<a href="netvista.data_logging">Data Logging</a>
</dt>
<dt>
<a href="netvista.packet_modification_examples">Packet Modification Examples</a>
</dt>
<dt>
<a href="netvista.registering_callouts_with_the_filter_engine">Registering Callouts with the Filter Engine</a>
</dt>
<dt>
<a href="netvista.using_a_callout_for_deep_inspection">Using a Callout for Deep Inspection</a>
</dt>
<dt>
<a href="netvista.using_a_callout_for_deep_inspection_of_stream_data">Using a Callout
    for Deep Inspection of Stream Data</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT_CLASSIFY_FN2 callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
