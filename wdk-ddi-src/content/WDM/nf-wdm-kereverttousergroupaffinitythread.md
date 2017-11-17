---
UID: NF.wdm.KeRevertToUserGroupAffinityThread
title: KeRevertToUserGroupAffinityThread
author: windows-driver-content
description: The KeRevertToUserGroupAffinityThread routine restores the group affinity of the calling thread to its original value at the time that the thread was created.
old-location: kernel\kereverttousergroupaffinitythread.htm
ms.assetid: 13a1a106-0c5c-4c0e-964d-27e549e1c699
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Ntddk.h, Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeRevertToUserGroupAffinityThread
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section).
ms.keywords: KeRevertToUserGroupAffinityThread
req.iface: 
req.product: Windows 10 or later.
---

# KeRevertToUserGroupAffinityThread function



## -description
<p>The <b>KeRevertToUserGroupAffinityThread</b> routine restores the group affinity of the calling thread to its original value at the time that the thread was created. </p>


## -syntax

````
VOID KeRevertToUserGroupAffinityThread(
  _In_ PGROUP_AFFINITY PreviousAffinity
);
````


## -parameters
<dl>

### -param <i>PreviousAffinity</i> [in]

<dd>
<p>A pointer to the group affinity to restore. This parameter points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure that contains a group number and an affinity mask. The affinity mask specifies the set of logical processors that the user thread can run on. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine changes the group number and group-relative affinity mask of the calling thread. The group number and affinity mask identify a set of processors on which the thread can run. If successful, the routine schedules the thread to run on a processor in this set.</p>

<p>The <i>PreviousAffinity</i> parameter points to a <b>GROUP_AFFINITY</b> structure that specifies the new group number (<b>Group</b> member) and affinity mask (<b>Mask</b> member) for the thread. If <i>PreviousAffinity</i>-&gt;<b>Mask</b> is nonzero, <b>KeRevertToUserGroupAffinityThread</b> sets the group number and affinity mask of the calling thread to the values in the structure. If <i>PreviousAffinity</i>-&gt;<b>Mask</b> is zero, the routine restores the group number and affinity mask to their original values at the time that the thread was initialized.</p>

<p>A process can have affinity for more than one group at a time. However, a thread can be assigned to only one group at any time, and that group is always in the affinity of the thread's process.</p>

<p>A thread can change the group to which it is assigned by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553275">KeSetSystemGroupAffinityThread</a> routine. Following one or more calls to <b>KeSetSystemGroupAffinityThread</b>, the thread can restore the original group affinity that it had when the thread was created by calling <b>KeRevertToUserGroupAffinityThread</b>.</p>

<p>After the thread is created, a call to <b>KeRevertToUserGroupAffinityThread</b> has no effect (that is, the group number and affinity mask of the thread remain unchanged) unless the thread first calls <b>KeSetSystemGroupAffinityThread</b>. Following a call to <b>KeRevertToUserGroupAffinityThread</b>, a second call to <b>KeRevertToUserGroupAffinityThread</b> has no effect unless the thread first calls <b>KeSetSystemGroupAffinityThread</b>.</p>

<p>The routine changes the group number and affinity mask to the values that are specified in *<i>PreviousAffinity</i> only if the following are true:</p>

<p>The group number is valid.</p>

<p>The affinity mask is valid (that is, only mask bits that correspond to logical processors in the group are set).</p>

<p>At least one of the processors that is specified in the affinity mask is active.</p>

<p>If any of these conditions is not met, the call to <b>KeRevertToUserGroupAffinityThread</b> has no effect.</p>

<p>A related routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553190">KeRevertToUserAffinityThreadEx</a>, changes the affinity mask of the calling thread, but this routine, unlike <b>KeRevertToUserGroupAffinityThread</b>, does not accept a group number as an input parameter. In Windows 7 and later versions of the Windows operating system, <b>KeRevertToUserAffinityThreadEx</b> assumes that the affinity mask refers to processors in group 0, which is compatible with the behavior of this routine in earlier versions of Windows that do not support groups. This behavior ensures that existing drivers that call <b>KeRevertToUserAffinityThreadEx</b> and that use no group-oriented features will run correctly in multiprocessor systems that have two or more groups. However, drivers that use any group-oriented features in Windows 7 and later versions of the Windows operating system should call <b>KeRevertToUserGroupAffinityThread</b> instead of <b>KeRevertToUserAffinityThreadEx</b>.</p>

<p>If <b>KeRevertToUserGroupAffinityThread</b> is called at IRQL &lt;= APC_LEVEL and the call is successful, the new (reverted) group affinity takes effect immediately. When the call returns, the calling thread is already running on a processor that is specified in the new group affinity. If <b>KeRevertToUserGroupAffinityThread</b> is called at IRQL = DISPATCH_LEVEL and the call is successful, the pending processor change is deferred until the caller lowers the IRQL below DISPATCH_LEVEL.</p>

<p>This routine changes the group number and group-relative affinity mask of the calling thread. The group number and affinity mask identify a set of processors on which the thread can run. If successful, the routine schedules the thread to run on a processor in this set.</p>

<p>The <i>PreviousAffinity</i> parameter points to a <b>GROUP_AFFINITY</b> structure that specifies the new group number (<b>Group</b> member) and affinity mask (<b>Mask</b> member) for the thread. If <i>PreviousAffinity</i>-&gt;<b>Mask</b> is nonzero, <b>KeRevertToUserGroupAffinityThread</b> sets the group number and affinity mask of the calling thread to the values in the structure. If <i>PreviousAffinity</i>-&gt;<b>Mask</b> is zero, the routine restores the group number and affinity mask to their original values at the time that the thread was initialized.</p>

<p>A process can have affinity for more than one group at a time. However, a thread can be assigned to only one group at any time, and that group is always in the affinity of the thread's process.</p>

<p>A thread can change the group to which it is assigned by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553275">KeSetSystemGroupAffinityThread</a> routine. Following one or more calls to <b>KeSetSystemGroupAffinityThread</b>, the thread can restore the original group affinity that it had when the thread was created by calling <b>KeRevertToUserGroupAffinityThread</b>.</p>

<p>After the thread is created, a call to <b>KeRevertToUserGroupAffinityThread</b> has no effect (that is, the group number and affinity mask of the thread remain unchanged) unless the thread first calls <b>KeSetSystemGroupAffinityThread</b>. Following a call to <b>KeRevertToUserGroupAffinityThread</b>, a second call to <b>KeRevertToUserGroupAffinityThread</b> has no effect unless the thread first calls <b>KeSetSystemGroupAffinityThread</b>.</p>

<p>The routine changes the group number and affinity mask to the values that are specified in *<i>PreviousAffinity</i> only if the following are true:</p>

<p>The group number is valid.</p>

<p>The affinity mask is valid (that is, only mask bits that correspond to logical processors in the group are set).</p>

<p>At least one of the processors that is specified in the affinity mask is active.</p>

<p>If any of these conditions is not met, the call to <b>KeRevertToUserGroupAffinityThread</b> has no effect.</p>

<p>A related routine, <a href="https://msdn.microsoft.com/library/windows/hardware/ff553190">KeRevertToUserAffinityThreadEx</a>, changes the affinity mask of the calling thread, but this routine, unlike <b>KeRevertToUserGroupAffinityThread</b>, does not accept a group number as an input parameter. In Windows 7 and later versions of the Windows operating system, <b>KeRevertToUserAffinityThreadEx</b> assumes that the affinity mask refers to processors in group 0, which is compatible with the behavior of this routine in earlier versions of Windows that do not support groups. This behavior ensures that existing drivers that call <b>KeRevertToUserAffinityThreadEx</b> and that use no group-oriented features will run correctly in multiprocessor systems that have two or more groups. However, drivers that use any group-oriented features in Windows 7 and later versions of the Windows operating system should call <b>KeRevertToUserGroupAffinityThread</b> instead of <b>KeRevertToUserAffinityThreadEx</b>.</p>

<p>If <b>KeRevertToUserGroupAffinityThread</b> is called at IRQL &lt;= APC_LEVEL and the call is successful, the new (reverted) group affinity takes effect immediately. When the call returns, the calling thread is already running on a processor that is specified in the new group affinity. If <b>KeRevertToUserGroupAffinityThread</b> is called at IRQL = DISPATCH_LEVEL and the call is successful, the pending processor change is deferred until the caller lowers the IRQL below DISPATCH_LEVEL.</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h, Wdm.h, or Ntddk.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL (see Remarks section).</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553190">KeRevertToUserAffinityThreadEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553275">KeSetSystemGroupAffinityThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRevertToUserGroupAffinityThread routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
