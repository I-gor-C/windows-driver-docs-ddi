---
UID: NF.wdm.IoWMIAllocateInstanceIds
title: IoWMIAllocateInstanceIds
author: windows-driver-content
description: The IoWMIAllocateInstanceIds routine allocates one or more instance IDs that are unique to the GUID.
old-location: kernel\iowmiallocateinstanceids.htm
old-project: kernel
ms.assetid: c382689e-907c-473c-9ab1-da963d7f3ba3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoWMIAllocateInstanceIds
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
req.alt-api: IoWMIAllocateInstanceIds
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive5, PowerIrpDDis, HwStorPortProhibitedDDIs, SpNoWait, StorPortStartIo
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoWMIAllocateInstanceIds function



## -description
<p>The <b>IoWMIAllocateInstanceIds</b> routine allocates one or more instance IDs that are unique to the GUID.</p>


## -syntax

````
NTSTATUS IoWMIAllocateInstanceIds(
  _In_  GUID  *Guid,
  _In_  ULONG InstanceCount,
  _Out_ ULONG *FirstInstanceId
);
````


## -parameters
<dl>

### -param <i>Guid</i> [in]

<dd>
<p>Pointer to the GUID for which to generate instance identifiers. </p>
</dd>

### -param <i>InstanceCount</i> [in]

<dd>
<p>Specifies how many instance identifiers should be provided. </p>
</dd>

### -param <i>FirstInstanceId</i> [out]

<dd>
<p>Pointer to the first instance identifier that the driver should use. </p>
</dd>
</dl>

## -returns
<p><b>IoWMIAllocateInstanceIds</b> returns a status code from the following list:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Indicates that WMI successfully provided unique instance identifiers for the GUID specified.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>Indicates that the WMI services are not available. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that insufficient resources were available to provide the caller with instance IDs.</p>

<p> </p>

## -remarks
<p>If greater than one instance was requested in <i>InstanceCount</i> and the routine completed successfully, <i>FirstInstanceId</i> points to the first instance that the caller should use. For each instance requested beyond one, the caller should increment the value returned in *<i>FirstInstanceId</i>. For example, if the caller requested six instances and one was returned as the value of <i>FirstInstanceId</i>, the caller should use the values 1-6 as his unique instance identifiers.</p>

<p>If greater than one instance was requested in <i>InstanceCount</i> and the routine completed successfully, <i>FirstInstanceId</i> points to the first instance that the caller should use. For each instance requested beyond one, the caller should increment the value returned in *<i>FirstInstanceId</i>. For example, if the caller requested six instances and one was returned as the value of <i>FirstInstanceId</i>, the caller should use the values 1-6 as his unique instance identifiers.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547796">IrqlIoPassive5</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454274">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550505">IoWmiSuggestInstanceName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIAllocateInstanceIds routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
