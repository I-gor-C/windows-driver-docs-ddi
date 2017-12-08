---
UID: NC.fwpsk.FWPS_CALLOUT_CLASSIFY_FN1
title: FWPS_CALLOUT_CLASSIFY_FN1
author: windows-driver-content
description: The filter engine calls a callout's classifyFn1 callout function whenever there is data to be processed by the callout.Note  classifyFn1 is the specific version of classifyFn used in Windows 7 and later.
old-location: netvista\classifyfn1.htm
old-project: netvista
ms.assetid: 128fd929-6e83-46a0-9475-e459ede58f30
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: classifyFn1
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
---

# FWPS_CALLOUT_CLASSIFY_FN1 callback



## -description
The filter engine calls a callout's 
  <i>classifyFn1</i> callout function whenever there is data to be processed by the callout.


## -prototype

````
FWPS_CALLOUT_CLASSIFY_FN1 classifyFn1;

void NTAPI classifyFn1(
  _In_     const FWPS_INCOMING_VALUES0          *inFixedValues,
  _In_     const FWPS_INCOMING_METADATA_VALUES0 *inMetaValues,
  _Inout_        void                           *layerData,
  _In_opt_ const void                           *classifyContext,
  _In_     const FWPS_FILTER1                   *filter,
  _In_           UINT64                         flowContext,
  _Inout_        FWPS_CLASSIFY_OUT0             *classifyOut
)
{ ... }
````


## -parameters

### -param inFixedValues [in]

A pointer to an 
     <a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a> structure. This
     structure contains the values for each of the data fields in the layer being filtered.

### -param inMetaValues [in]

A pointer to an 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure. This structure contains the values for each of the
     metadata fields in the layer being filtered.

### -param layerData [in, out]

A pointer to a structure that describes the raw data in the layer being filtered. This parameter
     might be <b>NULL</b>, depending on the layer being filtered and the conditions under which the 
     <i>classifyFn1</i> callout function is called. For the stream layer, this parameter points to an 
     <a href="netvista.fwps_stream_callout_io_packet0">
     FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure. For all of the other layers, this parameter points to a 
     <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure if it is not
     <b>NULL</b>.

### -param classifyContext [in, optional]

A pointer to context data associated with the callout driver by the filter engine.

### -param filter [in]

A pointer to an 
     <a href="netvista.fwps_filter1">FWPS_FILTER1</a> structure. This structure
     describes the filter that specifies the callout for the filter's action.

### -param flowContext [in]

A UINT64-typed variable that contains the context associated with the data flow. If no context is
     associated with the data flow, then this parameter is zero. If the callout is added to the filter engine
     at a filtering layer that does not support data flows, the 
     <i>classifyFn1</i> callout function should ignore this parameter.

### -param classifyOut [in, out]

A pointer to an 
     <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure that
     receives any data that the 
     <i>classifyFn1</i> callout function returns to the caller.

## -returns
None.

## -remarks
A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="netvista.fwpscalloutregister1">FwpsCalloutRegister1</a> function.

The filter engine calls a callout's 
    <i>classifyFn1</i> callout function with data to be processed whenever all of the test conditions are true
    for a filter in the filter engine that specifies the callout for the filter's action.

A callout's 
    <i>classifyFn1</i> callout function should clear the FWPS_RIGHT_ACTION_WRITE flag in the 
    <b>rights</b> member of the 
    <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure in any of
    the following situations:

When the 
      <i>classifyFn1</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_BLOCK.

When the 
      <i>classifyFn1</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_PERMIT and the FWPS_FILTER_FLAG_CLEAR_ACTION_RIGHT flag is set in the 
      <b>Flags</b> member of the 
      <a href="netvista.fwps_filter1">FWPS_FILTER1</a> structure.

When a callout has indicated that it intends to modify the clone net buffer list by setting the 
      <i>intendToModify</i> parameter to <b>TRUE</b> in a call to the 
      <a href="netvista.fwpsreferencenetbufferlist0">
      FwpsReferenceNetBufferList0</a> function.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 7.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.classifyfn">classifyFn</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn2.md">classifyFn2</a>
</dt>
<dt>
<a href="netvista.fwpscalloutregister1">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="netvista.fwpsreferencenetbufferlist0">FwpsReferenceNetBufferList0</a>
</dt>
<dt>
<a href="netvista.fwps_callout0">FWPS_CALLOUT0</a>
</dt>
<dt>
<a href="netvista.fwps_classify_out0">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="netvista.fwps_filter1">FWPS_FILTER1</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_values0">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
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
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT_CLASSIFY_FN1 callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
