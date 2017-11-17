---
UID: NC.fwpsk.FWPS_CALLOUT_CLASSIFY_FN2
title: FWPS_CALLOUT_CLASSIFY_FN2
author: windows-driver-content
description: The filter engine calls a callout's classifyFn2 callout function whenever there is data to be processed by the callout.Note  classifyFn2 is the specific version of classifyFn used in Windows 8 and later.
old-location: netvista\classifyfn2.htm
ms.assetid: de8220de-cf71-4718-876e-ef02c15fc948
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: FwpmEngineOpen0
req.iface: 
---

# FWPS_CALLOUT_CLASSIFY_FN2 callback



## -description
<p>The filter engine calls a callout's 
  <i>classifyFn2</i> callout function whenever there is data to be processed by the callout.<div class="alert"><b>Note</b>  <i>classifyFn2</i> is the specific version of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> used in Windows 8 and later. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information. For Windows 7, <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a> is available. For Windows Vista, <a href="https://msdn.microsoft.com/e8423c27-d3eb-4bef-a835-37fae0e2b68c">classifyFn0</a> is available.</div>
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

### -param <i>inFixedValues</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a> structure. This
     structure contains the values for each of the data fields in the layer being filtered.</p>
</dd>

### -param <i>inMetaValues</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
     FWPS_INCOMING_METADATA_VALUES0</a> structure. This structure contains the values for each of the
     metadata fields in the layer being filtered.</p>
</dd>

### -param <i>layerData</i> [in, out, optional]

<dd>
<p>A pointer to a structure that describes the raw data in the layer being filtered. This parameter
     might be NULL, depending on the layer being filtered and the conditions under which the 
     <i>classifyFn2</i> callout function is called. For the stream layer, this parameter points to an 
     <a href="https://msdn.microsoft.com/2c0539f0-116e-4344-9584-db7416d258e0">
     FWPS_STREAM_CALLOUT_IO_PACKET0</a> structure. For all of the other layers, this parameter points to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure if it is not
     NULL.</p>
</dd>

### -param <i>classifyContext</i> [in, optional]

<dd>
<p>A pointer to context data associated with the callout driver by the filter engine.</p>
</dd>

### -param <i>filter</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a> structure. This structure
     describes the filter that specifies the callout for the filter's action.</p>
</dd>

### -param <i>flowContext</i> [in]

<dd>
<p>A UINT64-typed variable that contains the context associated with the data flow. If no context is
     associated with the data flow, then this parameter is zero. If the callout is added to the filter engine
     at a filtering layer that does not support data flows, the 
     <i>classifyFn2</i> callout function should ignore this parameter.</p>
</dd>

### -param <i>classifyOut</i> [in, out]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure that
     receives any data that the 
     <i>classifyFn2</i> callout function returns to the caller.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a> function.</p>

<p>The filter engine calls a callout's 
    <i>classifyFn2</i> callout function with data to be processed whenever all of the test conditions are true
    for a filter in the filter engine that specifies the callout for the filter's action.</p>

<p>A callout's 
    <i>classifyFn2</i> callout function should clear the FWPS_RIGHT_ACTION_WRITE flag in the 
    <b>rights</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure in any of
    the following situations:</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_BLOCK.</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_PERMIT and the FWPS_FILTER_FLAG_CLEAR_ACTION_RIGHT flag is set in the 
      <b>Flags</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a> structure.</p>

<p>When a callout has indicated that it intends to modify the clone net buffer list by setting the 
      <i>intendToModify</i> parameter to TRUE in a call to the 
      <a href="https://msdn.microsoft.com/ff387b49-fecb-41d0-aac5-0a83eb8835d6">
      FwpsReferenceNetBufferList0</a> function.</p>

<p>This function is essentially identical to the previous version, 
    <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a>. However, the updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a> structure is pointed to by the 
       <i>filter</i> parameter and the <i>layerData</i> parameter is optional.</p>

<p>A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a> function.</p>

<p>The filter engine calls a callout's 
    <i>classifyFn2</i> callout function with data to be processed whenever all of the test conditions are true
    for a filter in the filter engine that specifies the callout for the filter's action.</p>

<p>A callout's 
    <i>classifyFn2</i> callout function should clear the FWPS_RIGHT_ACTION_WRITE flag in the 
    <b>rights</b> member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure in any of
    the following situations:</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_BLOCK.</p>

<p>When the 
      <i>classifyFn2</i> callout function sets the 
      <b>actionType</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a> structure to
      FWP_ACTION_PERMIT and the FWPS_FILTER_FLAG_CLEAR_ACTION_RIGHT flag is set in the 
      <b>Flags</b> member of the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a> structure.</p>

<p>When a callout has indicated that it intends to modify the clone net buffer list by setting the 
      <i>intendToModify</i> parameter to TRUE in a call to the 
      <a href="https://msdn.microsoft.com/ff387b49-fecb-41d0-aac5-0a83eb8835d6">
      FwpsReferenceNetBufferList0</a> function.</p>

<p>This function is essentially identical to the previous version, 
    <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a>. However, the updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a> structure is pointed to by the 
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e8423c27-d3eb-4bef-a835-37fae0e2b68c">classifyFn0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551206">FwpsReferenceNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551229">FWPS_CLASSIFY_OUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439768">FWPS_FILTER2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552401">FWPS_INCOMING_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="NULL">Associating Context with a Data Flow</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
<dt>
<a href="NULL">Data Logging</a>
</dt>
<dt>
<a href="NULL">Packet Modification Examples</a>
</dt>
<dt>
<a href="NULL">Registering Callouts with the Filter Engine</a>
</dt>
<dt>
<a href="NULL">Using a Callout for Deep Inspection</a>
</dt>
<dt>
<a href="netvista.using_a_callout_for_deep_inspection_of_stream_data">Using a Callout
    for Deep Inspection of Stream Data</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT_CLASSIFY_FN2 callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
