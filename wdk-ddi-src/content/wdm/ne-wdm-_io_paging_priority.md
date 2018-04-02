---
UID: NE:wdm._IO_PAGING_PRIORITY
title: "_IO_PAGING_PRIORITY"
author: windows-driver-content
description: The IO_PAGING_PRIORITY enumeration describes the priority value for a paging I/O IRP.
old-location: kernel\io_paging_priority.htm
old-project: kernel
ms.assetid: c96d1c81-429f-46de-b56c-6424734ccd7a
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IO_PAGING_PRIORITY, IO_PAGING_PRIORITY enumeration [Kernel-Mode Driver Architecture], IoPagingPriorityHigh, IoPagingPriorityInvalid, IoPagingPriorityNormal, IoPagingPriorityReserved1, IoPagingPriorityReserved2, _IO_PAGING_PRIORITY, kernel.io_paging_priority, sysenum_8e021ebd-f26a-4749-8e76-c540af5dfae1.xml, wdm/IO_PAGING_PRIORITY, wdm/IoPagingPriorityHigh, wdm/IoPagingPriorityInvalid, wdm/IoPagingPriorityNormal, wdm/IoPagingPriorityReserved1, wdm/IoPagingPriorityReserved2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
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
-	wdm.h
api_name:
-	IO_PAGING_PRIORITY
product:
- Windows
targetos: Windows
req.typenames: IO_PAGING_PRIORITY
req.product: Windows 10 or later.
---

# _IO_PAGING_PRIORITY Enumeration
The <b>IO_PAGING_PRIORITY</b> enumeration describes the priority value for a paging I/O IRP.

## Syntax
```
typedef enum _IO_PAGING_PRIORITY {
  IoPagingPriorityInvalid    ,
  IoPagingPriorityNormal     ,
  IoPagingPriorityHigh       ,
  IoPagingPriorityReserved1  ,
  IoPagingPriorityReserved2
} IO_PAGING_PRIORITY;
```

## Constants

<table>
            
                <tr>
                    <td>IoPagingPriorityInvalid</td>
                    <td>The IRP is not a paging I/O IRP.</td>
                </tr>
            
                <tr>
                    <td>IoPagingPriorityNormal</td>
                    <td>The associated IRP has a normal priority level for paging I/O.</td>
                </tr>
            
                <tr>
                    <td>IoPagingPriorityHigh</td>
                    <td>The associated IRP has a high priority level for paging I/O.</td>
                </tr>
            
                <tr>
                    <td>IoPagingPriorityReserved1</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>IoPagingPriorityReserved2</td>
                    <td>Reserved for system use.</td>
                </tr>
</table>

## Remarks

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff549269">IoGetPagingIoPriority</a> routine returns an <b>IO_PAGING_PRIORITY</b> value to indicate the priority value of a paging I/O IRP.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549269">IoGetPagingIoPriority</a>