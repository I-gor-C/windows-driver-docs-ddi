---
UID: NC.fwpsk.FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0
title: FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0
author: windows-driver-content
description: The filter engine calls the vSwitchRuntimeStateSaveNotifyFn (FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0) callout function to notify a callout driver about virtual switch run-time state save events.Note  FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 is a specific version of FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwps_vswitch_runtime_state_save_callback0.htm
old-project: netvista
ms.assetid: 2CDD666F-3D88-4078-9A4C-D7A107806EA7
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: vSwitchRuntimeStateSaveNotifyFn
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

# FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 callback



## -description
<p>The filter engine calls the <i>vSwitchRuntimeStateSaveNotifyFn</i> (<i>FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</i>) callout function to notify a callout driver about virtual switch  run-time state save events.<div class="alert"><b>Note</b>  <i>FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</i> is a specific version of <i>FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK</i>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -prototype

````
FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 vSwitchRuntimeStateSaveNotifyFn;

NTSTATUS NTAPI vSwitchRuntimeStateSaveNotifyFn(
  _In_opt_       void                                             *notifyContext,
  _In_           void                                             *completionContext,
  _In_           FWPS_VSWITCH_EVENT_TYPE                          eventType,
  _In_     const NDIS_SWITCH_PARAMETERS                           *vSwitch,
  _In_           NDIS_SWITCH_PORT_ID                              portId,
                 _Outptr_result_buffer_(*runtimeStateLength) void **runtimeState,
  _Out_          SIZE_T                                           *runtimeStateLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>notifyContext</i> [in, optional]

<dd>
<p>A pointer to a context provided by the callout driver. The driver passed this pointer to the <i>notifyContext</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function. This parameter is optional and can be NULL.</p>
</dd>

### -param <i>completionContext</i> [in]

<dd>
<p>A pointer to a completion context provided by the callout driver. This parameter is optional and can be NULL.

</p>
</dd>

### -param <i>eventType</i> [in]

<dd>
<p>The type of virtual switch event  specified as one of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451265">FWPS_VSWITCH_EVENT_TYPE</a> enumeration values. For more information, see Remarks.</p>
</dd>

### -param <i>vSwitch</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh598220">NDIS_SWITCH_PARAMETERS</a> structure that contains information about a virtual switch.
</p>
<div class="alert"><b>Note</b>  The information in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598220">NDIS_SWITCH_PARAMETERS</a> structure reflects the initial state of the virtual switch, not necessarily its current state. In particular, the <b>NumSwitchPorts</b> and <b>IsActive</b> members might still have their initial value of zero, unless a virtual switch PnP event has been triggered. Current state information can be found in the other parameters to this callback function.</div>
<div> </div>
</dd>

### -param <i>portId</i> [in]

<dd>
<p>The source switch port identifier.</p>
</dd>

### -param <i>runtimeState</i> 

<dd>
<p>The location of the run-time state output result buffer.</p>
</dd>

### -param <i>runtimeStateLength</i> [out]

<dd>
<p>The length, in bytes, of the run-time state information in the run-time state buffer.</p>
</dd>
</dl>

## -returns
<p>A callout's 
  
  <i>FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout driver accepts the notification from the filter engine.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p> The operation is pending and will be completed later.  The callout  driver will  call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439695">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>A callout driver registers a 
  
  <i>vSwitchRuntimeStateSaveNotifyFn</i> function  by calling  
    
    the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function.</p>

<p>If the <i>vSwitchRuntimeStateSaveNotifyFn</i> callback is registered, the callout will be notified to retrieve a source VM’s run-time state and to restore a target VM’s run-time state during live migration or a local save and restore operation. In the save case, the <i>eventType</i> parameter of <i>vSwitchRuntimeStateSaveNotifyFn</i> is set to    FWPS_VSWITCH_EVENT_RUNTIME_STATE_SAVE.</p>

<p>The virtual switch extension protocol driver issues an object identifier (OID) method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598268">OID_SWITCH_NIC_SAVE</a> during an operation to save run-time data for a virtual switch port. The filter driver returns this data so that run-time data for a virtual switch port can be saved and restored at a later time. </p>

<p>	After the run-time data blob from all callouts are collected, WFP fills the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598216">NDIS_SWITCH_NIC_SAVE_STATE</a> structure with the harvested data and completes the save state request. </p>

<p>A callout can return STATUS_PENDING from <i>vSwitchRuntimeStateSaveNotifyFn</i>. In this case, WFP will return STATUS_PENDING in the <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> handler and will complete it at a later time. The callout  driver will  call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439695">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation. </p>

<p>See the <i>vSwitchRuntimeStateRestoreNotifyFn</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh451281">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>) function for information about restoring the run-time state.</p>

<p>A callout driver registers a 
  
  <i>vSwitchRuntimeStateSaveNotifyFn</i> function  by calling  
    
    the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function.</p>

<p>If the <i>vSwitchRuntimeStateSaveNotifyFn</i> callback is registered, the callout will be notified to retrieve a source VM’s run-time state and to restore a target VM’s run-time state during live migration or a local save and restore operation. In the save case, the <i>eventType</i> parameter of <i>vSwitchRuntimeStateSaveNotifyFn</i> is set to    FWPS_VSWITCH_EVENT_RUNTIME_STATE_SAVE.</p>

<p>The virtual switch extension protocol driver issues an object identifier (OID) method request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598268">OID_SWITCH_NIC_SAVE</a> during an operation to save run-time data for a virtual switch port. The filter driver returns this data so that run-time data for a virtual switch port can be saved and restored at a later time. </p>

<p>	After the run-time data blob from all callouts are collected, WFP fills the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598216">NDIS_SWITCH_NIC_SAVE_STATE</a> structure with the harvested data and completes the save state request. </p>

<p>A callout can return STATUS_PENDING from <i>vSwitchRuntimeStateSaveNotifyFn</i>. In this case, WFP will return STATUS_PENDING in the <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> handler and will complete it at a later time. The callout  driver will  call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439695">FwpsvSwitchNotifyComplete0</a> function to complete the pending operation. </p>

<p>See the <i>vSwitchRuntimeStateRestoreNotifyFn</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/hh451281">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>) function for information about restoring the run-time state.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451265">FWPS_VSWITCH_EVENT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451281">FWPS_VSWITCH_RUNTIME_STATE_RESTORE_CALLBACK0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439695">FwpsvSwitchNotifyComplete0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598216">NDIS_SWITCH_NIC_SAVE_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598220">NDIS_SWITCH_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598268">OID_SWITCH_NIC_SAVE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_VSWITCH_RUNTIME_STATE_SAVE_CALLBACK0 callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
