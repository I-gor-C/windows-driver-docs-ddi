---
UID: NC.fwpsk.FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0
title: FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0
author: windows-driver-content
description: The filter engine calls the vSwitchRuntimeStateRestoreNotifyFn (FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0) callout function to notify a callout driver about virtual switch run-time state restore events.Note  FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 is a specific version of FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwps_vswitch_runtime_state_restore_callback0.htm
old-project: netvista
ms.assetid: E684429C-1BDC-4821-89DF-08FF20D25315
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
req.alt-api: vSwitchRuntimeStateRestoreNotifyFn
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

# FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 callback



## -description
<p>The filter engine calls the <i>vSwitchRuntimeStateRestoreNotifyFn</i>  (<i>FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</i>) callout function to notify a callout driver about virtual switch run-time state restore events.<div class="alert"><b>Note</b>  <i>FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</i> is a specific version of <i>FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK</i>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -prototype

````
FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 vSwitchRuntimeStateRestoreNotifyFn;

NTSTATUS NTAPI vSwitchRuntimeStateRestoreNotifyFn(
  _In_opt_       void                                      *notifyContext,
  _In_           void                                      *completionContext,
  _In_           FWPS_VSWITCH_EVENT_TYPE                   eventType,
  _In_     const NDIS_SWITCH_PARAMETERS                    *vSwitch,
  _In_           NDIS_SWITCH_PORT_ID                       portId,
                 _In_reads_bytes_(runtimeStateLength) void *runtimeState,
  _In_           SIZE_T                                    runtimeStateLength
)
{ ... }
````


## -parameters
<dl>

### -param notifyContext [in, optional]

<dd>
<p>A pointer to a context provided by the callout driver. The driver passed this pointer to the <i>notifyContext</i> parameter of the <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>
 function. This parameter is optional and can be NULL.</p>
</dd>

### -param completionContext [in]

<dd>
<p>A pointer to a completion context provided by the callout driver. This parameter is optional and can be NULL.

</p>
</dd>

### -param eventType [in]

<dd>
<p>The type of virtual switch event  specified as one of the <a href="netvista.fwps_vswitch_event_type">FWPS_VSWITCH_EVENT_TYPE</a> enumeration values. For more information, see Remarks.</p>
</dd>

### -param vSwitch [in]

<dd>
<p>A pointer to an <a href="..\fwpsk\ns-fwpsk--ndis-switch-parameters.md">NDIS_SWITCH_PARAMETERS</a> structure that contains information about a virtual switch.
</p>
<div class="alert"><b>Note</b>  The information in the <a href="..\fwpsk\ns-fwpsk--ndis-switch-parameters.md">NDIS_SWITCH_PARAMETERS</a> structure reflects the initial state of the virtual switch, not necessarily its current state. In particular, the <b>NumSwitchPorts</b> and <b>IsActive</b> members might still have their initial value of zero, unless a virtual switch PnP event has been triggered. Current state information can be found in the other parameters to this callback function.</div>
<div> </div>
</dd>

### -param portId [in]

<dd>
<p>The source switch port identifier.</p>
</dd>

### -param runtimeState 

<dd>
<p>The location of the run-time state output result buffer.</p>
</dd>

### -param runtimeStateLength [in]

<dd>
<p>The length, in bytes, of the run-time state information in the run-time state buffer.</p>
</dd>
</dl>

## -returns
<p>A callout's 
  
  <i>FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout driver accepts the notification from the filter engine.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later.  The callout  driver will  call the <a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>A callout driver registers a 
  
  <i>vSwitchRuntimeStateRestoreNotifyFn</i> function  by calling  
    
    the <a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>
 function.</p>

<p>See the <i>vSwitchRuntimeStateSaveNotifyFn</i> (<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a>) function for information about saving the run-time state.</p>

<p>Each saved data segment will be restored with an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598267">OID_SWITCH_NIC_RESTORE</a> OID sent through the virtual switch extension stacks on the target system or on the local system during a restore operation. WFP will dispatch the data to the correct callout through <i>vSwitchRuntimeStateRestoreNotifyFn</i> after matching with a registered provider GUID. In this case, the <i>eventType</i> parameter of <i>vSwitchRuntimeStateRestoreNotifyFn</i> is set to    FWPS_VSWITCH_EVENT_RUNTIME_STATE_RESTORE.</p>

<p>A callout can return STATUS_PENDING from <i>vSwitchRuntimeStateRestoreNotifyFn</i>. In this case, WFP will return STATUS_PENDING in the <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> handler and will complete it at a later time. The callout  driver will  call the <a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation.</p>

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
<a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a>
</dt>
<dt>
<a href="netvista.fwps_vswitch_event_type">FWPS_VSWITCH_EVENT_TYPE</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-vswitch-runtime-state-save-callback0.md">FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsvswitcheventssubscribe0.md">FwpsvSwitchEventsSubscribe0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsvswitchnotifycomplete0.md">FwpsvSwitchNotifyComplete0</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--ndis-switch-parameters.md">NDIS_SWITCH_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598267">OID_SWITCH_NIC_RESTORE</a>
</dt>
<dt>
<a href="netvista.callout_driver_callout_functions">Callout Driver Callout Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0 callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
