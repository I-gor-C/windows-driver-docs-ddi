---
UID: NF.wdm.PoCallDriver
title: PoCallDriver
author: windows-driver-content
description: The PoCallDriver routine passes a power IRP to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.).
old-location: kernel\pocalldriver.htm
old-project: kernel
ms.assetid: e5ce7786-717a-4e0f-bc57-342655a59ca1
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PoCallDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoCallDriver
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequestStatusCheck, CompletionRoutineRegistered, DeleteDevice, ForwardedAtBadIrql, ForwardedAtBadIrqlAllocate, ForwardedAtBadIrqlFsdAsync, ForwardedAtBadIrqlFsdSync, IoAllocateForward, IoAllocateIrpSignalEventInCompletionTimeout, IoBuildDeviceControlWait, IoBuildDeviceControlWaitTimeout, IoBuildFsdForward, IoBuildSynchronousFsdRequestWait, IoBuildSynchronousFsdRequestWaitTimeout, IoSetCompletionRoutineExCheck, IrpProcessingComplete, LowerDriverReturn, MarkDevicePower, MarkingQueuedIrps, MarkIrpPending, MarkIrpPending2, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PendedCompletedRequest, PendedCompletedRequest2, PendedCompletedRequest3, PendedCompletedRequestEx, PnpIrpCompletion, PowerDownFail, PowerUpFail, RemoveLockForward, RemoveLockForward2, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControl2, RemoveLockForwardDeviceControlInternal, RemoveLockForwardDeviceControlInternal2, RemoveLockForwardRead, RemoveLockForwardRead2, RemoveLockForwardWrite, RemoveLockForwardWrite2, RemoveLockMnRemove2, RemoveLockMnSurpriseRemove, RemoveLockQueryMnRemove, TargetRelationNeedsRef, WmiForward, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# PoCallDriver function



## -description
<p>The <b>PoCallDriver</b> routine passes a power <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> to the next-lower driver in the device stack. (Windows Server 2003, Windows XP, and Windows 2000 only.)</p>


## -syntax

````
NTSTATUS PoCallDriver(
  _In_    PDEVICE_OBJECT DeviceObject,
  _Inout_ PIRP           Irp
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>A pointer to the driver-created <a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a> to which the IRP is to be routed.</p>
</dd>

### -param <i>Irp</i> [in, out]

<dd>
<p>A pointer to an IRP. </p>
</dd>
</dl>

## -returns
<p><b>PoCallDriver</b> returns STATUS_SUCCESS to indicate success. It returns STATUS_PENDING if it has queued the IRP.</p>

## -remarks
<p>Beginning with Windows Vista, drivers should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>, not <b>PoCallDriver</b> to pass a power IRP to the next-lower driver. However, on Windows Server 2003, Windows XP, and Windows 2000, drivers must call <b>PoCallDriver</b>, not <b>IoCallDriver</b>  to pass a power IRP to the next-lower driver. On Windows Server 2003, Windows XP, an Windows 2000, drivers must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559776">PoStartNextPowerIrp</a> before calling <b>PoCallDriver</b>.</p>

<p>A driver that requires a new IRP should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>. A driver must not allocate its own power IRP.</p>

<p>When passing a power IRP down to the next-lower driver, the caller should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a> to set the IRP stack location, then call <b>PoCallDriver</b>. Use <b>IoCopyCurrentIrpStackLocationToNext</b> if processing the IRP requires setting an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine, or <b>IoSkipCurrentStackLocation</b> if no <i>IoCompletion</i> routine is required.</p>

<p>When a device is powering up, its drivers must set <i>IoCompletion</i> routines to perform start-up tasks (initializing the device, restoring context, and so on) after the bus driver has set the device in the working state. Set <i>IoCompletion</i> routines before calling <b>PoCallDriver</b>.</p>

<p>When a device is powering down, its drivers must perform necessary power-down tasks before passing the IRP to the next lower driver. After the IRP has reached the bus driver, the device will be powered off and its drivers will no longer have access to it. On Windows Server 2003, Windows XP, and Windows 2000, an <i>IoCompletion</i> routine that is associated with a power-down IRP is only required to call <b>PoStartNextPowerIrp</b>.</p>

<p>Only one inrush IRP can be active in the system at a time. When passing a power-up IRP for a device that requires inrush current (in other words, the DO_POWER_INRUSH flag is set in the device object), <b>PoCallDriver</b> checks whether another inrush IRP is already active. If so, <b>PoCallDriver</b> queues the current IRP for handling after the previous IRP completes, and then returns STATUS_PENDING. For more information about inrush IRPs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563746">Setting Device Object Flags for Power Management</a>. </p>

<p>If an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a> request is already active for <i>DeviceObject</i>, <b>PoCallDriver</b> queues this IRP and returns STATUS_PENDING.</p>

<p>On Windows 2000 and later systems, pageable drivers (the DO_POWER_PAGABLE flag is set in the device object) must call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL. Drivers that cannot be paged (DO_POWER_PAGABLE is not set in the device object) or that require inrush current (DO_POWER_INRUSH is set in the device object) can call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL or DISPATCH_LEVEL.</p>

<p>On Windows 98/Me, all drivers call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL.</p>

<p>Beginning with Windows Vista, drivers should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>, not <b>PoCallDriver</b> to pass a power IRP to the next-lower driver. However, on Windows Server 2003, Windows XP, and Windows 2000, drivers must call <b>PoCallDriver</b>, not <b>IoCallDriver</b>  to pass a power IRP to the next-lower driver. On Windows Server 2003, Windows XP, an Windows 2000, drivers must also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559776">PoStartNextPowerIrp</a> before calling <b>PoCallDriver</b>.</p>

<p>A driver that requires a new IRP should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>. A driver must not allocate its own power IRP.</p>

<p>When passing a power IRP down to the next-lower driver, the caller should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a> to set the IRP stack location, then call <b>PoCallDriver</b>. Use <b>IoCopyCurrentIrpStackLocationToNext</b> if processing the IRP requires setting an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine, or <b>IoSkipCurrentStackLocation</b> if no <i>IoCompletion</i> routine is required.</p>

<p>When a device is powering up, its drivers must set <i>IoCompletion</i> routines to perform start-up tasks (initializing the device, restoring context, and so on) after the bus driver has set the device in the working state. Set <i>IoCompletion</i> routines before calling <b>PoCallDriver</b>.</p>

<p>When a device is powering down, its drivers must perform necessary power-down tasks before passing the IRP to the next lower driver. After the IRP has reached the bus driver, the device will be powered off and its drivers will no longer have access to it. On Windows Server 2003, Windows XP, and Windows 2000, an <i>IoCompletion</i> routine that is associated with a power-down IRP is only required to call <b>PoStartNextPowerIrp</b>.</p>

<p>Only one inrush IRP can be active in the system at a time. When passing a power-up IRP for a device that requires inrush current (in other words, the DO_POWER_INRUSH flag is set in the device object), <b>PoCallDriver</b> checks whether another inrush IRP is already active. If so, <b>PoCallDriver</b> queues the current IRP for handling after the previous IRP completes, and then returns STATUS_PENDING. For more information about inrush IRPs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563746">Setting Device Object Flags for Power Management</a>. </p>

<p>If an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a> request is already active for <i>DeviceObject</i>, <b>PoCallDriver</b> queues this IRP and returns STATUS_PENDING.</p>

<p>On Windows 2000 and later systems, pageable drivers (the DO_POWER_PAGABLE flag is set in the device object) must call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL. Drivers that cannot be paged (DO_POWER_PAGABLE is not set in the device object) or that require inrush current (DO_POWER_INRUSH is set in the device object) can call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL or DISPATCH_LEVEL.</p>

<p>On Windows 98/Me, all drivers call <b>PoCallDriver</b> at IRQL = PASSIVE_LEVEL.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543504">CompletionRoutineRegistered</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975146">DeleteDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546166">ForwardedAtBadIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975147">ForwardedAtBadIrqlAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975148">ForwardedAtBadIrqlFsdAsync</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975149">ForwardedAtBadIrqlFsdSync</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975153">IoAllocateForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975158">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975161">IoBuildDeviceControlWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975162">IoBuildDeviceControlWaitTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975165">IoBuildFsdForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975173">IoBuildSynchronousFsdRequestWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975174">IoBuildSynchronousFsdRequestWaitTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975179">IoSetCompletionRoutineExCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547325">IrpProcessingComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548273">LowerDriverReturn</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975187">MarkDevicePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549016">MarkingQueuedIrps</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549018">MarkIrpPending</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549021">MarkIrpPending2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550374">PendedCompletedRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975198">PendedCompletedRequest2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975199">PendedCompletedRequest3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975200">PendedCompletedRequestEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550407">PnpIrpCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975203">PowerDownFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975205">PowerUpFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975208">RemoveLockForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975209">RemoveLockForward2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975210">RemoveLockForwardDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975211">RemoveLockForwardDeviceControl2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975212">RemoveLockForwardDeviceControlInternal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975213">RemoveLockForwardDeviceControlInternal2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975214">RemoveLockForwardRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975215">RemoveLockForwardRead2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975216">RemoveLockForwardWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975217">RemoveLockForwardWrite2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975233">RemoveLockMnRemove2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975234">RemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975235">RemoveLockQueryMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552918">TargetRelationNeedsRef</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556175">WmiForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548387">IoCopyCurrentIrpStackLocationToNext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551699">IRP_MN_QUERY_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551744">IRP_MN_SET_POWER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559734">PoRequestPowerIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559776">PoStartNextPowerIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoCallDriver routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
