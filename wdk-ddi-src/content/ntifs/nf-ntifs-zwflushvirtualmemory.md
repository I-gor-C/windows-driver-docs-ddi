---
UID: NF.ntifs.ZwFlushVirtualMemory
title: ZwFlushVirtualMemory
author: windows-driver-content
description: The ZwFlushVirtualMemory routine flushes a range of virtual addresses within the virtual address space of a specified process which map to a data file back out to the data file if they have been modified.
old-location: kernel\zwflushvirtualmemory.htm
old-project: kernel
ms.assetid: 86e04896-2921-4f77-9bee-283ceb9a66bc
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwFlushVirtualMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwFlushVirtualMemory,NtFlushVirtualMemory
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ZwFlushVirtualMemory function



## -description
<p>The <b>ZwFlushVirtualMemory</b> routine flushes a range of virtual addresses within the virtual address space of a specified process which map to a data file back out to the data file if they have been modified.</p>


## -syntax

````
NTSTATUS ZwFlushVirtualMemory(
  _In_    HANDLE           ProcessHandle,
  _Inout_ PVOID            *BaseAddress,
  _Inout_ PSIZE_T          RegionSize,
  _Out_   PIO_STATUS_BLOCK IoStatus
);
````


## -parameters
<dl>

### -param ProcessHandle [in]

<dd>
<p>An open handle for the process in whose context the pages to be flushed reside. Use the <b>NtCurrentProcess</b> macro, defined in Ntddk.h, to specify the current process. </p>
</dd>

### -param BaseAddress [in, out]

<dd>
<p>A pointer to the base address of the virtual address range.</p>
<p>On entry, this parameter specifies a pointer to the initial value of the base address of the region of pages to flush.</p>
<p>On return, this parameter provides a pointer to a variable that will receive the base address of the flushed region.</p>
</dd>

### -param RegionSize [in, out]

<dd>
<p>The size, in bytes, of the virtual address range.</p>
<p>On entry, this parameter specifies a pointer to the initial value of the size in bytes of the region of pages to flush to disk. This argument is rounded up to the next host-page-size boundary by the <b>ZwFlushVirtualMemory</b>. If this value is specified as zero, the mapped range from the base address to the end of the range is flushed.</p>
<p>On return, this parameter specifies a pointer to a variable that will receive the actual size in bytes of the flushed region of pages.</p>
</dd>

### -param IoStatus [out]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure. This structure is where the value of the I/O status for the last attempted I/O operation is stored on output.</p>
</dd>
</dl>

## -returns
<p><b>ZwFlushVirtualMemory</b> returns either STATUS_SUCCESS or an error status code. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The specified <i>ProcessHandle</i> parameter was not a valid process handle. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Additional resources required by this function were not available. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The <i>BaseAddress</i> specified was an invalid address within the virtual address space or the <i>RegionSize</i> was invalid. </p><dl>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
</dl><p>The specified <i>ProcessHandle</i> parameter was not a valid process handle. </p><dl>
<dt><b>STATUS_NOT_MAPPED_VIEW</b></dt>
</dl><p>No virtual address space descriptor could be located for the supplied <i>BaseAddress</i>. </p><dl>
<dt><b>STATUS_PROCESS_IS_TERMINATING</b></dt>
</dl><p>The process and the associated virtual address space was deleted. </p><dl>
<dt><b>STATUS_FILE_LOCK_CONFLICT</b></dt>
</dl><p>The file system encountered a locking conflict. </p>

<p> </p>

## -remarks
<p>
     This routine accepts, as input parameters, a range of addresses in virtual memory that map a data file. If any memory in this range has been modified since the file was copied to memory, the routine flushes this memory back to the data file.</p>

<p>For more information about memory management support for kernel-mode drivers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554389">Memory Management for Windows Drivers</a>. </p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwallocatevirtualmemory.md">ZwAllocateVirtualMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwFlushVirtualMemory routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
