---
UID: NF.wdfsync.WdfWaitLockAcquire
title: WdfWaitLockAcquire
author: windows-driver-content
description: The WdfWaitLockAcquire method acquires a specified wait lock.
old-location: wdf\wdfwaitlockacquire.htm
old-project: wdf
ms.assetid: 6fe7465d-938a-400f-b141-76e8a5ffbe90
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfWaitLockAcquire
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfsync.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfWaitLockAcquire
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, WdfWaitlock, WdfWaitlockRelease
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# WdfWaitLockAcquire function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfWaitLockAcquire</b> method acquires a specified wait lock.</p>


## -syntax

````
NTSTATUS WdfWaitLockAcquire(
  _In_     WDFWAITLOCK Lock,
  _In_opt_ PLONGLONG   Timeout
);
````


## -parameters
<dl>

### -param Lock [in]

<dd>
<p>A handle to a framework wait-lock object, obtained by a previous call to <a href="..\wdfsync\nf-wdfsync-wdfwaitlockcreate.md">WdfWaitLockCreate</a>.</p>
</dd>

### -param Timeout [in, optional]

<dd>
<p>An optional pointer to a time-out value. The time-out value is specified in system time units (100-nanosecond intervals).</p>
<p> If the pointer is non-<b>NULL</b>, the framework cancels the attempt to obtain the lock if it is not completed within the specified time-out period. Time-out values can be negative, positive, or zero, as follows:</p>
<ul>
<li>
<p>If the time-out value is negative, the expiration time is relative to the current system time.</p>
</li>
<li>
<p>If the time-out value is positive, the expiration time is specified as an absolute time (which is actually relative to January 1, 1601). </p>
</li>
<li>
<p>If the time-out value is zero, <b>WdfWaitLockAcquire</b> attempts to acquire the lock and then returns immediately, whether it has acquired the lock or not. </p>
</li>
</ul>
<p>Relative expiration times are not affected by any changes to the system time that might occur within the specified time-out period. Absolute expiration times do reflect system time changes.</p>
<p>The framework provides <a href="wdf.wdf_timer_object_reference">time conversion functions</a> that convert time values into system time units.</p>
<p>If the caller supplies a <b>NULL</b> pointer, the method waits indefinitely until it has acquired the lock.</p>
</dd>
</dl>

## -returns
<p><b>WdfWaitLockAcquire</b> can return the following <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The caller has acquired the wait lock.</p><dl>
<dt><b>STATUS_TIMEOUT</b></dt>
</dl><p>The specified <i>Timeout</i> interval expired before the lock was acquired.</p>

<p> </p>

<p>Note that <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(status) equals <b>TRUE</b> for all of these status values.

</p>

<p>The caller does not have to check the return value if the <i>Timeout</i> pointer is <b>NULL</b>, because in that case <b>WdfWaitLockAcquire</b> returns only after it acquires the lock.

</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfWaitLockAcquire</b> method does not return until it acquires the wait lock or until the time-out period expires. </p>

<p><b>WdfWaitLockAcquire</b> calls <a href="..\wdm\nf-wdm-keentercriticalregion.md">KeEnterCriticalRegion</a> before acquiring the wait lock.  As a result, when the method returns, <a href="https://msdn.microsoft.com/74ed953c-1b2a-40b9-9df3-16869b198b38">normal kernel APCs</a> are disabled. <b>WdfWaitLockAcquire</b> does not alter the caller's IRQL.</p>

<p>If the <i>Timeout</i> pointer is <b>NULL</b>, or if the time-out value is not zero, <b>WdfWaitLockAcquire</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>If the time-out value is zero, <b>WdfWaitLockAcquire</b> must be called at IRQL &lt; DISPATCH_LEVEL. Note that this is in disagreement with the header file (wdfsync.h), which indicates that this method can be called at DISPATCH_LEVEL.</p>

<p>For more information about wait locks, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.</p>

<p>The following code example acquires a wait lock, adds a device object to an object collection, and releases the wait lock.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfsync.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_wdfwaitlock">WdfWaitlock</a>, <a href="devtest.kmdf_wdfwaitlockrelease">WdfWaitlockRelease</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-keentercriticalregion.md">KeEnterCriticalRegion</a>
</dt>
<dt>
<a href="..\wdfsync\nf-wdfsync-wdfwaitlockcreate.md">WdfWaitLockCreate</a>
</dt>
<dt>
<a href="wdf.wdfwaitlockrelease">WdfWaitLockRelease</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWaitLockAcquire method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
