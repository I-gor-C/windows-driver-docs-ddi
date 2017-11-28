---
UID: NF.fwpsk.FwpsCalloutRegister2
title: FwpsCalloutRegister2
author: windows-driver-content
description: The FwpsCalloutRegister2 function registers a callout with the filter engine.Note  FwpsCalloutRegister2 is the specific version of FwpsCalloutRegister used in Windows 8 and later.
old-location: netvista\fwpscalloutregister2.htm
old-project: netvista
ms.assetid: 7e60d536-607f-469f-8de4-5f6b77443b3e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsCalloutRegister2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsCalloutRegister2
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FwpsCalloutRegister2 function



## -description
<p>The 
  <b>FwpsCalloutRegister2</b> function registers a callout with the filter engine.<div class="alert"><b>Note</b>  <b>FwpsCalloutRegister2</b> is the specific version of <b>FwpsCalloutRegister</b> used in Windows 8 and later. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information. For Windows 7, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> is available. For Windows Vista, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> is available. </div>
<div> </div>
</p>


## -syntax

````
NTSTATUS NTAPI FwpsCalloutRegister2(
  _Inout_         void          *deviceObject,
  _In_      const FWPS_CALLOUT2 *callout,
  _Out_opt_       UINT32        *calloutId
);
````


## -parameters
<dl>

### -param <i>deviceObject</i> [in, out]

<dd>
<p>A pointer to a device object that was previously created by the callout driver. For more
     information about how a callout driver creates a device object, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff542862">Creating a Device Object</a>.</p>
</dd>

### -param <i>callout</i> [in]

<dd>
<p>A pointer to a constant 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a> structure that contains the
     data that is required to register the callout with the filter engine.</p>
</dd>

### -param <i>calloutId</i> [out, optional]

<dd>
<p>A pointer to a UINT32-typed variable that receives a run-time identifier that identifies the
     callout in the filter engine. The callout driver passes this identifier to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551144">FwpsCalloutUnregisterById0</a> function when unregistering the callout from the filter engine. If a
     callout driver is filtering a data flow, it also passes this identifier to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551169">FwpsFlowRemoveContext0</a> functions.
     If a callout driver injects data into data streams, it also passes this identifier to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a> function. 
     The filter engine also passes this
     identifier to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-flow-delete-notify-fn0.md">flowDeleteFn</a> callout function. This
     parameter is optional and can be NULL.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsCalloutRegister2</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout was successfully registered with the filter engine.</p><dl>
<dt><b>STATUS_FWP_ALREADY_EXISTS</b></dt>
</dl><p>The callout could not be registered with the filter engine. A callout is already registered in
       the filter engine with an identifier identical to the GUID specified in the 
       <b>calloutKey</b> member of the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a> structure pointed to by the 
       <i>callout</i> parameter.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsCalloutRegister2</b> function to register a callout with the filter engine. A callout driver can
    register a callout with the filter engine at any time, even if the filter engine is not currently
    running.</p>

<p>A callout and filters that specify the callout for the filter's action can be added to the filter
    engine before a callout driver registers the callout with the filter engine. In this situation, filters
    with an action type of <b>FWP_ACTION_CALLOUT_TERMINATING</b> or <b>FWP_ACTION_CALLOUT_UNKNOWN</b> are treated as
    <b>FWP_ACTION_BLOCK</b>, and filters with an action type of <b>FWP_ACTION_CALLOUT_INSPECTION</b> are ignored until the
    callout is registered with the filter engine.</p>

<p>A callout driver unregisters a callout from the filter engine by calling either the 
    <a href="..\fwpsk\nf-fwpsk-fwpscalloutunregisterbyid0.md">
    FwpsCalloutUnregisterById0</a> function or the 
    <a href="..\fwpsk\nf-fwpsk-fwpscalloutunregisterbykey0.md">
    FwpsCalloutUnregisterByKey0</a> function. A callout driver cannot be unloaded until all of the callouts
    that were previously registered with the filter engine have been successfully unregistered.</p>

<p>This function is essentially identical to the previous version, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>. The only difference is the 
       updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a> structure pointed to by the 
       <i>callout</i> parameter.</p>

<p>A callout driver calls the 
    <b>FwpsCalloutRegister2</b> function to register a callout with the filter engine. A callout driver can
    register a callout with the filter engine at any time, even if the filter engine is not currently
    running.</p>

<p>A callout and filters that specify the callout for the filter's action can be added to the filter
    engine before a callout driver registers the callout with the filter engine. In this situation, filters
    with an action type of <b>FWP_ACTION_CALLOUT_TERMINATING</b> or <b>FWP_ACTION_CALLOUT_UNKNOWN</b> are treated as
    <b>FWP_ACTION_BLOCK</b>, and filters with an action type of <b>FWP_ACTION_CALLOUT_INSPECTION</b> are ignored until the
    callout is registered with the filter engine.</p>

<p>A callout driver unregisters a callout from the filter engine by calling either the 
    <a href="..\fwpsk\nf-fwpsk-fwpscalloutunregisterbyid0.md">
    FwpsCalloutUnregisterById0</a> function or the 
    <a href="..\fwpsk\nf-fwpsk-fwpscalloutunregisterbykey0.md">
    FwpsCalloutUnregisterByKey0</a> function. A callout driver cannot be unloaded until all of the callouts
    that were previously registered with the filter engine have been successfully unregistered.</p>

<p>This function is essentially identical to the previous version, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>. The only difference is the 
       updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a> structure pointed to by the 
       <i>callout</i> parameter.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551144">FwpsCalloutUnregisterById0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551145">FwpsCalloutUnregisterByKey0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551169">FwpsFlowRemoveContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551213">FwpsStreamInjectAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-callout-flow-delete-notify-fn0.md">flowDeleteFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542862">Creating a Device Object</a>
</dt>
<dt>
<a href="NULL">Types of Callouts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsCalloutRegister2 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
