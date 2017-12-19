---
UID: NF.fwpsk.FwpsCalloutRegister0
title: FwpsCalloutRegister0 function
author: windows-driver-content
description: The FwpsCalloutRegister0 function registers a callout with the filter engine.Note  FwpsCalloutRegister0 is the specific version of FwpsCalloutRegister used in Windows Vista and later.
old-location: netvista\fwpscalloutregister0.htm
old-project: NetVista
ms.assetid: 1f003775-4b93-44cd-8c58-18e0e3fb5656
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FwpsCalloutRegister0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
---

# FwpsCalloutRegister0 function



## -description
The 
  <b>FwpsCalloutRegister0</b> function registers a callout with the filter engine.



## -syntax

````
NTSTATUS NTAPI FwpsCalloutRegister0(
  _Inout_         void          *deviceObject,
  _In_      const FWPS_CALLOUT0 *callout,
  _Out_opt_       UINT32        *calloutId
);
````


## -parameters

### -param deviceObject [in, out]

A pointer to a device object that was previously created by the callout driver. For more
     information about how a callout driver creates a device object, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff542862">Creating a Device Object</a>.


### -param callout [in]

A pointer to a constant 
     <a href="netvista.fwps_callout0">FWPS_CALLOUT0</a> structure that contains the
     data that is required to register the callout with the filter engine.


### -param calloutId [out, optional]

A pointer to a UINT32-typed variable that receives a run-time identifier that identifies the
     callout in the filter engine. The callout driver passes this identifier to the 
     <a href="netvista.fwpscalloutunregisterbyid0">FwpsCalloutUnregisterById0</a> function when unregistering the callout from the filter engine. If a
     callout driver is filtering a data flow, it also passes this identifier to the 
     <a href="netvista.fwpsflowassociatecontext0">FwpsFlowAssociateContext0</a> and 
     <a href="netvista.fwpsflowremovecontext0">FwpsFlowRemoveContext0</a> functions.
     If a callout driver injects data into data streams, it also passes this identifier to the 
     <a href="netvista.fwpsstreaminjectasync0">FwpsStreamInjectAsync0</a> function. 
     The filter engine also passes this
     identifier to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps_callout_flow_delete_notify_fn0.md">flowDeleteFn</a> callout function. This
     parameter is optional and can be <b>NULL</b>.


## -returns
The 
     <b>FwpsCalloutRegister0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The callout was successfully registered with the filter engine.
<dl>
<dt><b>STATUS_FWP_ALREADY_EXISTS</b></dt>
</dl>The callout could not be registered with the filter engine. A callout is already registered in
       the filter engine with an identifier identical to the GUID specified in the 
       <b>calloutKey</b> member of the 
       <a href="netvista.fwps_callout0">FWPS_CALLOUT0</a> structure pointed to by the 
       <i>callout</i> parameter.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 


## -remarks
A callout driver calls the 
    <b>FwpsCalloutRegister0</b> function to register a callout with the filter engine. A callout driver can
    register a callout with the filter engine at any time, even if the filter engine is not currently
    running.

A callout and filters that specify the callout for the filter's action can be added to the filter
    engine before a callout driver registers the callout with the filter engine. In this situation, filters
    with an action type of <b>FWP_ACTION_CALLOUT_TERMINATING</b> or <b>FWP_ACTION_CALLOUT_UNKNOWN</b> are treated as
    <b>FWP_ACTION_BLOCK</b>, and filters with an action type of <b>FWP_ACTION_CALLOUT_INSPECTION</b> are ignored until the
    callout is registered with the filter engine.

A callout driver unregisters a callout from the filter engine by calling either the 
    <a href="netvista.fwpscalloutunregisterbyid0">
    FwpsCalloutUnregisterById0</a> function or the 
    <a href="netvista.fwpscalloutunregisterbykey0">
    FwpsCalloutUnregisterByKey0</a> function. A callout driver cannot be unloaded until all of the callouts
    that were previously registered with the filter engine have been successfully unregistered.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows Vista.

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
Library

</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwps_callout0">FWPS_CALLOUT0</a>
</dt>
<dt>
<a href="netvista.fwpscalloutregister1">FwpsCalloutRegister1</a>
</dt>
<dt>
<a href="netvista.fwpscalloutregister2">FwpsCalloutRegister2</a>
</dt>
<dt>
<a href="netvista.fwpscalloutunregisterbyid0">FwpsCalloutUnregisterById0</a>
</dt>
<dt>
<a href="netvista.fwpscalloutunregisterbykey0">FwpsCalloutUnregisterByKey0</a>
</dt>
<dt>
<a href="netvista.fwpsflowassociatecontext0">FwpsFlowAssociateContext0</a>
</dt>
<dt>
<a href="netvista.fwpsflowremovecontext0">FwpsFlowRemoveContext0</a>
</dt>
<dt>
<a href="netvista.fwpsstreaminjectasync0">FwpsStreamInjectAsync0</a>
</dt>
<dt>
<a href="kernel.iocreatedevice">IoCreateDevice</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_flow_delete_notify_fn0.md">flowDeleteFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542862">Creating a Device Object</a>
</dt>
<dt>
<a href="netvista.types_of_callouts">Types of Callouts</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FwpsCalloutRegister0 function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

