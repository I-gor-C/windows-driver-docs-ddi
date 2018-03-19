---
UID: NE:ntifs._MEMORY_INFORMATION_CLASS
title: "_MEMORY_INFORMATION_CLASS"
author: windows-driver-content
description: Defines classes of memory information that can be retrieved by using the ZwQueryVirtualMemory function.
old-location: kernel\memory_information_class.htm
old-project: kernel
ms.assetid: 7E3B531F-935C-41D6-94F7-DB18F82B9109
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: MEMORY_INFORMATION_CLASS, MEMORY_INFORMATION_CLASS enumeration [Kernel-Mode Driver Architecture], MemoryBasicInformation, _MEMORY_INFORMATION_CLASS, kernel.memory_information_class, ntifs/MEMORY_INFORMATION_CLASS, ntifs/MemoryBasicInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	MEMORY_INFORMATION_CLASS
product: Windows
targetos: Windows
req.typenames: MEMORY_INFORMATION_CLASS
---

# _MEMORY_INFORMATION_CLASS Enumeration
Defines classes of memory information that can be retrieved by using the  <a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a> function.

## Syntax
````
typedef enum _MEMORY_INFORMATION_CLASS { 
  MemoryBasicInformation
} MEMORY_INFORMATION_CLASS;
````

## Constants

<table>
            
                <tr>
                    <td>MemoryBasicInformation</td>
                    <td>Memory information described in the <a href="..\ntifs\ns-ntifs-_memory_basic_information.md">MEMORY_BASIC_INFORMATION</a> structure will be retrieved.</td>
                </tr>
</table>

## Remarks

Currently, only the <b>MemoryBasicInformation</b> value is supported for use with the <a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a> routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10. Available starting with Windows 10. |
| **Header** | ntifs.h |

## See Also

<a href="..\ntifs\nf-ntifs-zwqueryvirtualmemory.md">ZwQueryVirtualMemory</a>