---
UID: NF.fwpsk.FwpsCalloutRegister0
title: FwpsCalloutRegister0
author: windows-driver-content
description: The FwpsCalloutRegister0 function registers a callout with the filter engine.Note  FwpsCalloutRegister0 is the specific version of FwpsCalloutRegister used in Windows Vista and later.
old-location: netvista\fwpscalloutregister0.htm
ms.assetid: 1f003775-4b93-44cd-8c58-18e0e3fb5656
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsCalloutRegister0
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
ms.keywords: FwpsCalloutRegister0
req.iface: 
---

# FwpsCalloutRegister0 function



## -description
<p>The 
  <b>FwpsCalloutRegister0</b> function registers a callout with the filter engine.</p>


## -syntax

````
NTSTATUS NTAPI FwpsCalloutRegister0(
  _Inout_         void          *deviceObject,
  _In_      const FWPS_CALLOUT0 *callout,
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
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a> structure that contains the
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
     <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function. This
     parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsCalloutRegister0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout was successfully registered with the filter engine.</p><dl>
<dt><b>STATUS_FWP_ALREADY_EXISTS</b></dt>
</dl><p>The callout could not be registered with the filter engine. A callout is already registered in
       the filter engine with an identifier identical to the GUID specified in the 
       <b>calloutKey</b> member of the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a> structure pointed to by the 
       <i>callout</i> parameter.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsCalloutRegister0</b> function to register a callout with the filter engine. A callout driver can
    register a callout with the filter engine at any time, even if the filter engine is not currently
    running.</p>

<p>A callout and filters that specify the callout for the filter's action can be added to the filter
    engine before a callout driver registers the callout with the filter engine. In this situation, filters
    with an action type of <b>FWP_ACTION_CALLOUT_TERMINATING</b> or <b>FWP_ACTION_CALLOUT_UNKNOWN</b> are treated as
    <b>FWP_ACTION_BLOCK</b>, and filters with an action type of <b>FWP_ACTION_CALLOUT_INSPECTION</b> are ignored until the
    callout is registered with the filter engine.</p>

<p>A callout driver unregisters a callout from the filter engine by calling either the 
    <a href="https://msdn.microsoft.com/81e7e704-c387-48a0-a222-cae751bba1d3">
    FwpsCalloutUnregisterById0</a> function or the 
    <a href="https://msdn.microsoft.com/24254e56-c7f5-4424-98b5-3b99bf210d5b">
    FwpsCalloutUnregisterByKey0</a> function. A callout driver cannot be unloaded until all of the callouts
    that were previously registered with the filter engine have been successfully unregistered.</p>

<p>A callout driver calls the 
    <b>FwpsCalloutRegister0</b> function to register a callout with the filter engine. A callout driver can
    register a callout with the filter engine at any time, even if the filter engine is not currently
    running.</p>

<p>A callout and filters that specify the callout for the filter's action can be added to the filter
    engine before a callout driver registers the callout with the filter engine. In this situation, filters
    with an action type of <b>FWP_ACTION_CALLOUT_TERMINATING</b> or <b>FWP_ACTION_CALLOUT_UNKNOWN</b> are treated as
    <b>FWP_ACTION_BLOCK</b>, and filters with an action type of <b>FWP_ACTION_CALLOUT_INSPECTION</b> are ignored until the
    callout is registered with the filter engine.</p>

<p>A callout driver unregisters a callout from the filter engine by calling either the 
    <a href="https://msdn.microsoft.com/81e7e704-c387-48a0-a222-cae751bba1d3">
    FwpsCalloutUnregisterById0</a> function or the 
    <a href="https://msdn.microsoft.com/24254e56-c7f5-4424-98b5-3b99bf210d5b">
    FwpsCalloutUnregisterByKey0</a> function. A callout driver cannot be unloaded until all of the callouts
    that were previously registered with the filter engine have been successfully unregistered.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439576">FwpsCalloutRegister2</a>
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
<a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsCalloutRegister0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
