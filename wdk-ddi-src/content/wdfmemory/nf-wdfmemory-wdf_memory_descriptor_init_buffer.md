---
UID: NF:wdfmemory.WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
title: WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function
author: windows-driver-content
description: The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer.
old-location: wdf\wdf_memory_descriptor_init_buffer.htm
old-project: wdf
ms.assetid: 16e1b0cb-8543-4700-8f8c-d7301c6de622
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFMemoryObjectRef_706a9ee6-c0f1-4cb4-a887-cbb535d94d17.xml, WDF_MEMORY_DESCRIPTOR_INIT_BUFFER, WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function, kmdf.wdf_memory_descriptor_init_buffer, wdf.wdf_memory_descriptor_init_buffer, wdfmemory/WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfmemory.h
api_name:
-	WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
product: Windows
targetos: Windows
req.typenames: WDF_MEMORY_DESCRIPTOR_TYPE
req.product: Windows 10 or later.
---


# WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure so that it describes a specified buffer.

## Syntax

```
void WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(
  PWDF_MEMORY_DESCRIPTOR Descriptor,
  PVOID                  Buffer,
  ULONG                  BufferLength
);
```

## Parameters

`Descriptor`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure.

`Buffer`

A pointer to a memory buffer.

`BufferLength`

The size, in bytes, of the memory buffer that <i>Buffer</i> points to.


## Return Value

None

## Remarks

The <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure and sets the structure's <b>Type</b> member to <b>WdfMemoryDescriptorTypeBuffer</b>. Then it sets the structure's <b>u.BufferType.Buffer</b> and <b>u.BufferType.Length</b> members to the values that the <i>Buffer</i> and <i>BufferLength</i> parameters specify, respectively.


#### Examples

For a code example that uses <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>.

<div class="code"></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfmemory.h (include Wdf.h) |
| **DDI compliance rules** | BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552395">WDF_MEMORY_DESCRIPTOR_INIT_HANDLE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552396">WDF_MEMORY_DESCRIPTOR_INIT_MDL</a>