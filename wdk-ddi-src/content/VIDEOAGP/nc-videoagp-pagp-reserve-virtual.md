---
UID: NC.videoagp.PAGP_RESERVE_VIRTUAL
title: PAGP_RESERVE_VIRTUAL
author: windows-driver-content
description: The AgpReserveVirtual function reserves a range of virtual addresses for AGP.
old-location: display\agpreservevirtual.htm
ms.assetid: 966dfc6c-6830-4872-b411-2801e3a4b753
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AgpReserveVirtual
req.alt-loc: videoagp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: VPOSVERSIONINFO, VPOSVERSIONINFO, *PVPOSVERSIONINFO
req.iface: 
req.product: Windows 10 or later.
---

# PAGP_RESERVE_VIRTUAL callback



## -description
<p>The <b>AgpReserveVirtual</b> function reserves a range of virtual addresses for AGP.</p>


## -prototype

````
PAGP_RESERVE_VIRTUAL AgpReserveVirtual;

PVOID APIENTRY AgpReserveVirtual(
  _In_  PVOID  HwDeviceExtension,
  _In_  HANDLE ProcessHandle,
  _In_  PVOID  PhysicalReserveContext,
  _Out_ PVOID  *VirtualReserveContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>ProcessHandle</i> [in]

<dd>
<p>Handle of the process in which to reserve the virtual address range. If <b>ProcessHandle</b> is 0, then the virtual address range is allocated in system space.</p>
</dd>

### -param <i>PhysicalReserveContext</i> [in]

<dd>
<p>Is the context handle that identifies the reserved physical address range with which to associate the virtual memory reservation. This context was obtained from <a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>.</p>
</dd>

### -param <i>VirtualReserveContext</i> [out]

<dd>
<p>Is the location in which the video port driver writes a context handle that identifies the reserved virtual memory.</p>
</dd>
</dl>

## -returns
<p><b>AgpReserveVirtual</b> returns the base address of the reserved virtual address range if successful; otherwise, returns <b>NULL</b>.</p>

## -remarks
<p>If <b>ProcessHandle</b> is not 0, then <b>AgpReserveVirtual</b> reserves, but does not commit, a range of virtual addresses in the address space of a user-mode process. In that case, you must call <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> to map the reserved (user-mode) virtual addresses to physical addresses.</p>

<p>If <b>ProcessHandle</b> is 0, then <b>AgpReserveVirtual</b> allocates a range of virtual addresses in system space and automatically maps (commits) the entire range of virtual addresses to physical addresses. Even though <b>AgpReserveVirtual</b> commits the entire virtual range, you still must call <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> before any code accesses the virtual range.</p>

<p>When you call <b>AgpReserveVirtual</b> to allocate a range of virtual addresses in system space (that is, if you set <b>ProcessHandle</b> to 0), the entire range of physical addresses identified by <b>PhysicalReserveContext</b> must be committed to locked pages of physical memory by a previous call to <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>.</p>

<p>The miniport driver can call <a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a> several times to reserve many smaller address ranges rather than one big range.</p>

<p>The miniport driver should call <a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a> to release the reserved virtual address range when it is no longer needed.</p>

<p>If <b>ProcessHandle</b> is not 0, then <b>AgpReserveVirtual</b> reserves, but does not commit, a range of virtual addresses in the address space of a user-mode process. In that case, you must call <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> to map the reserved (user-mode) virtual addresses to physical addresses.</p>

<p>If <b>ProcessHandle</b> is 0, then <b>AgpReserveVirtual</b> allocates a range of virtual addresses in system space and automatically maps (commits) the entire range of virtual addresses to physical addresses. Even though <b>AgpReserveVirtual</b> commits the entire virtual range, you still must call <a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a> before any code accesses the virtual range.</p>

<p>When you call <b>AgpReserveVirtual</b> to allocate a range of virtual addresses in system space (that is, if you set <b>ProcessHandle</b> to 0), the entire range of physical addresses identified by <b>PhysicalReserveContext</b> must be committed to locked pages of physical memory by a previous call to <a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>.</p>

<p>The miniport driver can call <a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a> several times to reserve many smaller address ranges rather than one big range.</p>

<p>The miniport driver should call <a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a> to release the reserved virtual address range when it is no longer needed.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Videoagp.h (include Video.h)</dt>
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
<a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PAGP_RESERVE_VIRTUAL callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
