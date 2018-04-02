---
UID: NS:ntddk._KEY_VIRTUALIZATION_INFORMATION
title: "_KEY_VIRTUALIZATION_INFORMATION"
author: windows-driver-content
description: The KEY_VIRTUALIZATION_INFORMATION structure defines the basic information that is available for a registry key or subkey.
old-location: kernel\key_virtualization_information.htm
old-project: kernel
ms.assetid: 128dd4ed-12c6-472a-b63c-d2d217b5c716
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PKEY_VIRTUALIZATION_INFORMATION, KEY_VIRTUALIZATION_INFORMATION, KEY_VIRTUALIZATION_INFORMATION structure [Kernel-Mode Driver Architecture], PKEY_VIRTUALIZATION_INFORMATION, PKEY_VIRTUALIZATION_INFORMATION structure pointer [Kernel-Mode Driver Architecture], _KEY_VIRTUALIZATION_INFORMATION, kernel.key_virtualization_information, kstruct_c_00c77a09-ed8d-4a66-9b18-b971c9eab5ce.xml, ntddk/KEY_VIRTUALIZATION_INFORMATION, ntddk/PKEY_VIRTUALIZATION_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available on Windows Vista and later versions of the Windows operating system.
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
-	ntddk.h
api_name:
-	KEY_VIRTUALIZATION_INFORMATION
product: Windows
targetos: Windows
req.typenames: KEY_VIRTUALIZATION_INFORMATION, *PKEY_VIRTUALIZATION_INFORMATION
---

# _KEY_VIRTUALIZATION_INFORMATION structure
The <b>KEY_VIRTUALIZATION_INFORMATION</b> structure defines the basic information that is available for a registry key or subkey.

## Syntax
```
typedef struct _KEY_VIRTUALIZATION_INFORMATION {
  ULONG  : 1  VirtualizationCandidate;
  ULONG  : 1  VirtualizationEnabled;
  ULONG  : 1  VirtualTarget;
  ULONG  : 1  VirtualStore;
  ULONG  : 1  VirtualSource;
  ULONG  : 27 Reserved;
} KEY_VIRTUALIZATION_INFORMATION, *PKEY_VIRTUALIZATION_INFORMATION;
```

## Members


`VirtualizationCandidate`

Specifies whether the key is part of the virtualization namespace scope.

`VirtualizationEnabled`

Specifies whether virtualization is enabled on this key. This value can be set to 1 only if <b>VirtualizationCandidate</b> is 1.

`VirtualTarget`

Specifies whether the key is a virtual key. This value can be set to 1 only if <b>VirtualizationCandidate</b> and <b>VirtualizationEnabled</b> are both 0. This value is valid only on the virtual store key handles.

`VirtualStore`

Specified whether the key is a part of the virtual store path.

`VirtualSource`

Specifies whether the key has ever been virtualized. This value can be set to 1 only if <b>VirtualizationCandidate</b> is 1.

`Reserved`

This value is reserved for system use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available on Windows Vista and later versions of the Windows operating system. Available on Windows Vista and later versions of the Windows operating system. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553355">KEY_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553358">KEY_CACHED_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553367">KEY_FULL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553373">KEY_INFORMATION_CLASS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553381">KEY_NAME_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553392">KEY_NODE_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566447">ZwEnumerateKey</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567060">ZwQueryKey</a>