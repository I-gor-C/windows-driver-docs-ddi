---
UID : NF:wdm.MmAllocatePagesForMdlEx
title : MmAllocatePagesForMdlEx function
author : windows-driver-content
description : The MmAllocatePagesForMdlEx routine allocates nonpaged, physical memory pages to an MDL.
old-location : kernel\mmallocatepagesformdlex.htm
old-project : kernel
ms.assetid : f860c230-01ca-4c7f-8b67-5d92a80ff906
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : MmAllocatePagesForMdlEx
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : Available in Windows Server 2003 with Service Pack 1 (SP1) and later versions of Windows. You should use this routine instead of MmAllocatePagesForMdl on these operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MmAllocatePagesForMdlEx
req.alt-loc : NtosKrnl.exe
req.ddi-compliance : IrqlMmApcLte
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : See Remarks section.
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# MmAllocatePagesForMdlEx function
The <b>MmAllocatePagesForMdlEx</b> routine allocates nonpaged, physical memory pages to an MDL.

## Syntax

````
PMDL MmAllocatePagesForMdlEx(
  _In_ PHYSICAL_ADDRESS    LowAddress,
  _In_ PHYSICAL_ADDRESS    HighAddress,
  _In_ PHYSICAL_ADDRESS    SkipBytes,
  _In_ SIZE_T              TotalBytes,
  _In_ MEMORY_CACHING_TYPE CacheType,
  _In_ ULONG               Flags
);
````

## Parameters

`LowAddress`

Specifies the physical address of the start of the first address range from which the allocated pages can come. If <b>MmAllocatePagesForMdlEx</b> cannot allocate the requested number of bytes in the first address range, it iterates through additional address ranges to get more pages. At each iteration, <b>MmAllocatePagesForMdlEx</b> adds the value of <i>SkipBytes</i> to the previous start address to obtain the start of the next address range.

`HighAddress`

Specifies the physical address of the end of the first address range that the allocated pages can come from.

`SkipBytes`

Specifies the number of bytes to skip from the start of the previous address range that the allocated pages can come from. <i>SkipBytes</i> must be an integer multiple of the virtual memory page size, in bytes.

`TotalBytes`

Specifies the total number of bytes to allocate for the MDL.

`CacheType`

Specifies a <a href="..\wdm\ne-wdm-_memory_caching_type.md">MEMORY_CACHING_TYPE</a> value, which indicates the type of caching that is allowed for the requested memory.

`Flags`

Specifies flags for this operation. Set this parameter to zero or to the bitwise OR of one or more of the following <b>MM_ALLOCATE_<i>XXX</i></b> flag bits:

The last four items in the preceding list are supported only in Windows 7 and later versions of Windows.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

<b>MmAllocatePagesForMdlEx</b> returns one of the following:
<dl>
<dt><b>MDL pointer</b></dt>
</dl>A non-<b>NULL</b> return value is a pointer to an MDL that describes a set of physical pages in the specified address range. If the requested number of bytes is not available, the MDL describes as much physical memory as is available.
<dl>
<dt><b><b>NULL</b></b></dt>
</dl>Indicates that no physical memory pages are available in the specified address ranges, or that there is not enough memory pool for the MDL itself.

## Remarks

By default, the physical memory pages that <b>MmAllocatePagesForMdlEx</b> returns are not contiguous pages. Starting with Windows 7, callers can override the default behavior of this routine by setting the MM_ALLOCATE_PREFER_CONTIGUOUS or MM_ALLOCATE_REQUIRE_CONTIGUOUS_CHUNKS flag bit in the <i>Flags</i> parameter.

<b>MmAllocatePagesForMdlEx</b> is designed for kernel-mode drivers that do not need corresponding virtual addresses (that is, they need physical pages and do not need them to be physically contiguous), and for kernel-mode drivers that can achieve substantial performance gains if physical memory for a device is allocated in a specific physical address range (for example, an AGP graphics card).

Depending on how much physical memory is currently available in the requested ranges, <b>MmAllocatePagesForMdlEx</b> might return an MDL that describes less memory than was requested. The routine also might return <b>NULL</b> if no memory was allocated. The caller should check the amount of memory that is actually allocated to the MDL.

The caller must use <a href="..\wdm\nf-wdm-mmfreepagesfrommdl.md">MmFreePagesFromMdl</a> to release the memory pages that are described by an MDL that was created by <b>MmAllocatePagesForMdlEx</b>. After calling <b>MmFreePagesFromMdl</b>, the caller must also call <a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a> to release the memory that is allocated for the MDL structure.

By default, <b>MmAllocatePagesForMdlEx</b> fills the pages that it allocates with zeros. The caller can specify the MM_DONT_ZERO_ALLOCATION flag to override this default and to possibly improve performance.

The maximum amount of memory that <b>MmAllocatePagesForMdlEx</b> can allocate in a single call is (4 gigabytes - PAGE_SIZE). The routine can satisfy an allocation request for this amount only if enough pages are available.

<b>MmAllocatePagesForMdlEx</b> runs at IRQL &lt;= APC_LEVEL. In Windows Server 2008 and later versions of Windows, callers of <b>MmAllocatePagesForMdlEx </b>are allowed to be at DISPATCH_LEVEL. However, you can improve driver performance by calling at APC_LEVEL or below.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | See Remarks section. |
| **DDI compliance rules** | IrqlMmApcLte |

## See Also

<dl>
<dt>
<a href="..\ntddk\nf-ntddk-exfreepool.md">ExFreePool</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm-_memory_caching_type.md">MEMORY_CACHING_TYPE</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmallocatepagesformdl.md">MmAllocatePagesForMdl</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmfreepagesfrommdl.md">MmFreePagesFromMdl</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmmaplockedpages.md">MmMapLockedPages</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MmAllocatePagesForMdlEx routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>