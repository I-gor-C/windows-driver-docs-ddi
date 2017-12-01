---
UID: NS.fwpsk.FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_
title: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_
author: windows-driver-content
description: The FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 structure specifies a callout driver-supplied virtual switch event dispatch table.Note  FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 is a specific version of FWPS_VSWITCH_EVENT_DISPATCH_TABLE.
old-location: netvista\fwps_vswitch_event_dispatch_table0.htm
old-project: netvista
ms.assetid: 7e949e6d-7448-4f76-b8a1-6d050261fb21
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
req.alt-loc: fwpsk.h
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

# FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_ structure



## -description
<p>The <b>FWPS_VSWITCH_EVENT_DISPATCH_TABLE0</b> structure specifies a callout driver-supplied virtual switch event dispatch table.<div class="alert"><b>Note</b>  <b>FWPS_VSWITCH_EVENT_DISPATCH_TABLE0</b> is a specific version of <b>FWPS_VSWITCH_EVENT_DISPATCH_TABLE</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
typedef struct FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_ {
  _Maybenull_ FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0              vSwitchLifetimeNotifyFn;
  _Maybenull_ FWPS_VSWITCH_PORT_EVENT_CALLBACK0                  vSwitchPortEventNotifyFn;
  _Maybenull_ FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0             vSwitchInterfaceEventNotifyFn;
     _Maybenull_
   FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 vSwitchFilterEngineReorderNotifyRn;
  _Maybenull_
   FWPS_VSWITCH_POLICY_EVENT_CALLBACK0             vSwitchPolicyEventNotifyFn;
  _Maybenull_
   FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0       vSwitchRuntimeStateSaveNotifyFn;
  _Maybenull_
   FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0    vSwitchRuntimeStateRestoreNotifyFn;
} FWPS_VSWITCH_EVENT_DISPATCH_TABLE0;
````


## -struct-fields
<dl>

### -field <b>vSwitchLifetimeNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-lifetime-event-callback0.md">FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchPortEventNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-port-event-callback0.md">FWPS_VSWITCH_PORT_EVENT_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchInterfaceEventNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-interface-event-callback0.md">FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchFilterEngineReorderNotifyRn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-filter-engine-reorder-callback0.md">FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchPolicyEventNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-policy-event-callback0.md">FWPS_VSWITCH_POLICY_EVENT_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchRuntimeStateSaveNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a> callback function or NULL.</p>
</dd>

### -field <b>vSwitchRuntimeStateRestoreNotifyFn</b>

<dd>
<p>The entry point for the <a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-restore-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a> callback function or NULL.</p>
</dd>
</dl>

## -remarks
<p>The callback driver passes a pointer to an initialized  FWPS_VSWITCH_EVENT_DISPATCH_TABLE0  structure to the <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a> function.</p>

<p>The following definition is in fwpvi.h: </p>

<p>
#define FWPS_VSWITCH_EVENT_DISPATCH_TABLE FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 </p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-filter-engine-reorder-callback0.md">FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-interface-event-callback0.md">FWPS_VSWITCH_INTERFACE_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-lifetime-event-callback0.md">FWPS_VSWITCH_LIFETIME_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-policy-event-callback0.md">FWPS_VSWITCH_POLICY_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-port-event-callback0.md">FWPS_VSWITCH_PORT_EVENT_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-restore-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_VSWITCH_EVENT_DISPATCH_TABLE0 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
