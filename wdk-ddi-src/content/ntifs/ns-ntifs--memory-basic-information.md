---
UID: NS.ntifs._MEMORY_BASIC_INFORMATION
title: MEMORY_BASIC_INFORMATION
author: windows-driver-content
description: Contains information about a range of pages in the virtual address space of a process.
old-location: kernel\memory_basic_information.htm
old-project: kernel
ms.assetid: AFDDB789-E412-4EF7-8C77-2020EF81DF39
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: MEMORY_BASIC_INFORMATION, MEMORY_BASIC_INFORMATION, *PMEMORY_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MEMORY_BASIC_INFORMATION
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# MEMORY_BASIC_INFORMATION structure



## -description
<p>Contains information about a range of pages in the virtual address space of a process. The 
<a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a> routine uses this structure.</p>


## -syntax

````
typedef struct _MEMORY_BASIC_INFORMATION {
  PVOID  BaseAddress;
  PVOID  AllocationBase;
  DWORD  AllocationProtect;
  SIZE_T RegionSize;
  DWORD  State;
  DWORD  Protect;
  DWORD  Type;
} MEMORY_BASIC_INFORMATION, *PMEMORY_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>BaseAddress</b>

<dd>
<p>A pointer to the base address of the region of pages.</p>
</dd>

### -field <b>AllocationBase</b>

<dd>
<p>A pointer to the base address of a range of allocated pages. The page pointed to by the <b>BaseAddress</b> member is contained within this allocation range.</p>
</dd>

### -field <b>AllocationProtect</b>

<dd>
<p>The memory protection option when the region was initially allocated. This member can be one of the 
following constants defined in wdm.h, or 0 if the caller does not have access.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PAGE_NOACCESS"></a><a id="page_noaccess"></a><dl>

### -field <b>PAGE_NOACCESS</b>


### -field 0x01

</dl>
</td>
<td width="60%">
<p>No access to the region of pages is allowed.
                                An attempt to read, write, or execute within
                                the region results in an access violation.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_EXECUTE"></a><a id="page_execute"></a><dl>

### -field <b>PAGE_EXECUTE</b>


### -field 0x10

</dl>
</td>
<td width="60%">
<p>Execute access to the region of pages
                               is allowed. An attempt to read or write within
                               the region results in an access violation.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_READONLY"></a><a id="page_readonly"></a><dl>

### -field <b>PAGE_READONLY</b>


### -field 0x02

</dl>
</td>
<td width="60%">
<p>Read-only and execute access to the region
                                of pages is allowed. An attempt to write within
                                the region results in an access violation.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_READWRITE"></a><a id="page_readwrite"></a><dl>

### -field <b>PAGE_READWRITE</b>


### -field 0x04

</dl>
</td>
<td width="60%">
<p>Read, write, and execute access to the region
                                 of pages is allowed. If write access to the
                                 underlying section is allowed, then a single
                                 copy of the pages are shared. Otherwise,
                                 the pages are shared read-only/copy-on-write.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_GUARD"></a><a id="page_guard"></a><dl>

### -field <b>PAGE_GUARD</b>


### -field 0x100

</dl>
</td>
<td width="60%">
<p>Read, write, and execute access to the
                             region of pages is allowed; however, access to
                             the region causes a "guard region entered"
                             condition to be raised in the subject process.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_NOCACHE"></a><a id="page_nocache"></a><dl>

### -field <b>PAGE_NOCACHE</b>


### -field 0x200

</dl>
</td>
<td width="60%">
<p>Disable the placement of committed
                               pages into the data cache.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PAGE_WRITECOMBINE"></a><a id="page_writecombine"></a><dl>

### -field <b>PAGE_WRITECOMBINE</b>


### -field 0x400

</dl>
</td>
<td width="60%">
<p>Disable the placement of committed
                                    pages into the data cache, combine the
                                    writes as well.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RegionSize</b>

<dd>
<p>The size of the region in bytes beginning at
                               the base address in which all pages have
                               identical attributes.</p>
</dd>

### -field <b>State</b>

<dd>
<p>The state of the pages in the region. This member can be one of the following values. 

</p>
<table>
<tr>
<th>State</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="MEM_COMMIT"></a><a id="mem_commit"></a><dl>

### -field <b>MEM_COMMIT</b>


### -field 0x1000

</dl>
</td>
<td width="60%">
<p>Indicates committed pages for which physical storage has been allocated, either in memory or in the paging file on disk.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEM_FREE"></a><a id="mem_free"></a><dl>

### -field <b>MEM_FREE</b>


### -field 0x10000

</dl>
</td>
<td width="60%">
<p>Indicates free pages not accessible to the calling process and available to be allocated. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEM_RESERVE"></a><a id="mem_reserve"></a><dl>

### -field <b>MEM_RESERVE</b>


### -field 0x2000

</dl>
</td>
<td width="60%">
<p>Indicates reserved pages where a range of the process's virtual address space is reserved without any physical storage being allocated.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Protect</b>

<dd>
<p>The access protection of the pages in the region. This member is one of the values listed for the <b>AllocationProtect</b> member.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The type of pages in the region. The following types are defined. 

</p>
<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="MEM_IMAGE"></a><a id="mem_image"></a><dl>

### -field <b>MEM_IMAGE</b>


### -field 0x1000000

</dl>
</td>
<td width="60%">
<p>Indicates that the memory pages within the region are mapped into the view of an image section.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEM_MAPPED"></a><a id="mem_mapped"></a><dl>

### -field <b>MEM_MAPPED</b>


### -field 0x40000

</dl>
</td>
<td width="60%">
<p>Indicates that the memory pages within the region are mapped into the view of a section.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEM_PRIVATE"></a><a id="mem_private"></a><dl>

### -field <b>MEM_PRIVATE</b>


### -field 0x20000

</dl>
</td>
<td width="60%">
<p>Indicates that the memory pages within the region are private (that is, not shared by other processes).</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MEMORY_BASIC_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
