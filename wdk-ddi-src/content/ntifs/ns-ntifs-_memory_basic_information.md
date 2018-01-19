---
UID : NS:ntifs._MEMORY_BASIC_INFORMATION
title : _MEMORY_BASIC_INFORMATION
author : windows-driver-content
description : Contains information about a range of pages in the virtual address space of a process.
old-location : kernel\memory_basic_information.htm
old-project : kernel
ms.assetid : AFDDB789-E412-4EF7-8C77-2020EF81DF39
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _MEMORY_BASIC_INFORMATION, *PMEMORY_BASIC_INFORMATION, MEMORY_BASIC_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows 10.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MEMORY_BASIC_INFORMATION
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PMEMORY_BASIC_INFORMATION, MEMORY_BASIC_INFORMATION"
---

# _MEMORY_BASIC_INFORMATION structure
Contains information about a range of pages in the virtual address space of a process. The 
<a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a> routine uses this structure.

## Syntax
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

## Members

        
            `AllocationBase`

            A pointer to the base address of a range of allocated pages. The page pointed to by the <b>BaseAddress</b> member is contained within this allocation range.
        
            `AllocationProtect`

            The memory protection option when the region was initially allocated. This member can be one of the 
following constants defined in wdm.h, or 0 if the caller does not have access.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `BaseAddress`

            A pointer to the base address of the region of pages.
        
            `Protect`

            The access protection of the pages in the region. This member is one of the values listed for the <b>AllocationProtect</b> member.
        
            `RegionSize`

            The size of the region in bytes beginning at
                               the base address in which all pages have
                               identical attributes.
        
            `State`

            The state of the pages in the region. This member can be one of the following values. 



<table>
<tr>
<th>State</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Type`

            The type of pages in the region. The following types are defined. 



<table>
<tr>
<th>Type</th>
<th>Meaning</th>
</tr>
<tr>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h |

    ## See Also

        <dl>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MEMORY_BASIC_INFORMATION structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>