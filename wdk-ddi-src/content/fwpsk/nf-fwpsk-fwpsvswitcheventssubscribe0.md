---
UID: NF.fwpsk.FwpsvSwitchEventsSubscribe0
title: FwpsvSwitchEventsSubscribe0
author: windows-driver-content
description: The FwpsvSwitchEventsSubscribe0 function registers callback entry points for virtual switch layer events such as virtual port creation and deletion.Note  FwpsvSwitchEventsSubscribe0 is a specific version of FwpsvSwitchEventsSubscribe.
old-location: netvista\fwpsvswitcheventssubscribe0.htm
old-project: netvista
ms.assetid: 479ff048-f57f-42ca-8787-f87ed055fdbf
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsvSwitchEventsSubscribe0
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
req.alt-api: FwpsvSwitchEventsSubscribe0
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
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# FwpsvSwitchEventsSubscribe0 function



## -description
<p>The <b>FwpsvSwitchEventsSubscribe0</b> function registers callback entry points for virtual switch  layer events such as virtual port creation and deletion.<div class="alert"><b>Note</b>  <b>FwpsvSwitchEventsSubscribe0</b> is a specific version of <b>FwpsvSwitchEventsSubscribe</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS NTAPI FwpsvSwitchEventsSubscribe0(
   _In_opt_ const GUID                          *providerGuid,
   _In_opt_ void                                *notifyContext,
   _In_ _Reserved_ UINT32                       flags,
   _In_ _Reserved_ void                         *reserved,
   _In_ const FWPS_VSWITCH_EVENT_DISPATCH_TABLE *eventDispatchTable,
   _Out_ UINT32                                 *subscriptionId
);
````


## -parameters
<dl>

### -param <i>providerGuid</i> 

<dd>
<p>The provider GUID.

</p>
</dd>

### -param <i>notifyContext</i> 

<dd>
<p>An optional pointer to a callout driver–supplied context. Event notification functions  pass this parameter back to the driver.</p>
</dd>

### -param <i>flags</i> 

<dd>
<p>Reserved. Set to zero.</p>
</dd>

### -param <i>reserved</i> 

<dd>
<p>Reserved. Set to zero.</p>
</dd>

### -param <i>eventDispatchTable</i> 

<dd>
<p>A pointer to an <a href="netvista.fwps_vswitch_event_dispatch_table0">FWPS_VSWITCH_EVENT_DISPATCH_TABLE</a> structure that defines the callback entry points for virtual switch layer events.</p>
</dd>

### -param <i>subscriptionId</i> 

<dd>
<p>A pointer to a variable that contains a unique identifier that WFP assigns to the subscription. The caller must return the subscription identifier to WFP with the  <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventsunsubscribe0.md">FwpsvSwitchEventsUnsubscribe0</a> function.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsvSwitchEventsSubscribe0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A handle to the classify request was successfully returned. The variable that the 
       <i>classifyHandle</i> parameter points to contains the handle for the classify request.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the <b>FwpsvSwitchEventsSubscribe0</b> function to register callback entry points for virtual switch  layer events.</p>

<p>The entry points for the callback notification functions are specified in and <a href="netvista.fwps_vswitch_event_dispatch_table0">FWPS_VSWITCH_EVENT_DISPATCH_TABLE0</a> structure. </p>

<p>The callout driver must later call 
    <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventsunsubscribe0.md">FwpsvSwitchEventsUnsubscribe0</a>  to
    free the system resources.</p>

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
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwps_vswitch_event_dispatch_table0">FWPS_VSWITCH_EVENT_DISPATCH_TABLE0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventsunsubscribe0.md">FwpsvSwitchEventsUnsubscribe0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsvSwitchEventsSubscribe0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
