---
UID: NF.wdm.MmMapMdl
title: MmMapMdl
author: windows-driver-content
description: This function maps physical pages described by a memory descriptor list (MDL) into the system virtual address space.
old-location: kernel\mmmapmdl.htm
ms.assetid: 4272f7a2-9379-40dd-a0a1-784dd25bc8bc
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmMapMdl
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: <=DISPATCH_LEVEL
ms.keywords: MmMapMdl
req.iface: 
req.product: Windows 10 or later.
---

# MmMapMdl function



## -description
<p>This function maps physical pages described by a memory descriptor
    list (MDL) into the system virtual address space.
</p>


## -syntax

````
 NTSTATUS  MmMapMdl(
  _In_ PMDL            MemoryDescriptorList,
  _In_ ULONG           Protection,
  _In_ PMM_MDL_ROUTINE DriverRoutine,
  _In_ PVOID           DriverContext
);
````


## -parameters
<dl>

### -param <i>MemoryDescriptorList</i> [in]

<dd>
<p>A pointer to a valid MDL.</p>
</dd>

### -param <i>Protection</i> [in]

<dd>
<p>A bitwise of flags that indicates the protection to set for the pages. Possible values are PAGE_Xxx constants defined in Wdm.h.</p>
</dd>

### -param <i>DriverRoutine</i> [in]

<dd>
<p> A pointer to a driver-supplied callback routine (<a href="https://msdn.microsoft.com/D8D946C9-8642-4D31-B983-DAF88B46B97B">MM_MDL_ROUTINE</a>) that is invoked after the MDL is mapped.</p>
</dd>

### -param <i>DriverContext</i> [in]

<dd>
<p>A pointer to a driver-defined context. The driver's callback function can store any status information  in the driver context and then examine the value, when the callback is invoked. </p>
</dd>
</dl>

## -returns
<p>    If the callback function pointed to by <i>DriverRoutine</i> was invoked, this function returns STATUS_SUCCESS. The function returns an appropriate NTSTATUS value if the MDL could not be mapped or the callback function could not be invoked.

</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
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
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/D8D946C9-8642-4D31-B983-DAF88B46B97B">MM_MDL_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmMapMdl function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
