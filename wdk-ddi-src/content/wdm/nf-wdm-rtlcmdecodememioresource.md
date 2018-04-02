---
UID: NF:wdm.RtlCmDecodeMemIoResource
title: RtlCmDecodeMemIoResource function
author: windows-driver-content
description: The RtlCmDecodeMemIoResource routine provides the starting address and length of a CM_PARTIAL_RESOURCE_DESCRIPTOR structure that describes a range of memory or I/O port addresses.
old-location: kernel\rtlcmdecodememioresource.htm
old-project: kernel
ms.assetid: cc2394ce-128e-46a2-8688-a71851af06cf
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: RtlCmDecodeMemIoResource, RtlCmDecodeMemIoResource routine [Kernel-Mode Driver Architecture], k109_da737a74-2fce-4731-b24d-9014272991f1.xml, kernel.rtlcmdecodememioresource, wdm/RtlCmDecodeMemIoResource
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlCmDecodeMemIoResource
product:
- Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# RtlCmDecodeMemIoResource function
The <b>RtlCmDecodeMemIoResource</b> routine provides the starting address and length of a <a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes a range of memory or I/O port addresses.

## Syntax

```
NTSYSAPI ULONGLONG RtlCmDecodeMemIoResource(
  PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor,
  PULONGLONG                      Start
);
```

## Parameters

`Descriptor`

A pointer to the <a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure to provide the starting address and length for.

`Start`

A pointer to a variable that receives the starting address of the range of memory or I/O port addresses.


## Return Value

<b>RtlCmDecodeMemIoResource</b> returns the length of the address range, in bytes.

## Remarks

The <b>Type</b> member of the <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure must be <b>CmResourceTypeMemory</b>, <b>CmResourceTypeMemoryLarge</b>, or <b>CmResourceTypePort</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561774">RtlCmEncodeMemIoResource</a>