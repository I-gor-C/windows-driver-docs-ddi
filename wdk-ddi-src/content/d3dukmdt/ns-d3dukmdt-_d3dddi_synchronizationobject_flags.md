---
UID: NS:d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
title: "_D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS"
author: windows-driver-content
description: Identifies attributes of a synchronization object.
old-location: display\d3dddi_synchronizationobject_flags.htm
old-project: display
ms.assetid: 57e5ea18-ccdd-40a7-9ff5-4d6b94908e7c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure [Display Devices], D3D_other_Structs_3d266c5b-53c9-47d1-abe9-f492d05660a4.xml, _D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, d3dukmdt/D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS, display.d3dddi_synchronizationobject_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dukmdt.h
api_name:
-	D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS
---

# _D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS structure
Identifies attributes of a synchronization object.

## Syntax
```
typedef struct _D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS {
  union {
    struct {
      UINT  : 1  Shared;
      UINT  : 1  NtSecuritySharing;
      UINT  : 1  CrossAdapter;
      UINT  : 1  TopOfPipeline;
      UINT  : 1  NoSignal;
      UINT  : 1  NoWait;
      UINT  : 1  NoSignalMaxValueOnTdr;
      UINT  : 1  NoGPUAccess;
#if ...
      UINT  : 23 Reserved;
#elif
      UINT  : 28 Reserved;
#else
      UINT  : 29 Reserved;
#endif
      UINT  : 1  D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS_RESERVED0;
    };
    UINT Value;
  };
} D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS;
```

## Members


## Remarks
Objects to be shared by using the <a href="https://msdn.microsoft.com/library/windows/hardware/hh780251">D3DKMTShareObjects</a> function must first be created with the <b>NtSecuritySharing</b> flag value set. This flag value is available in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547802">D3DKMT_CREATEALLOCATIONFLAGS</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh780254">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a>, and <b>D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</b> structures.

Drivers should follow these guidelines on <b>D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</b> flags:

<ul>
<li>If the synchronization object is not shared, set both  <b>Shared</b> and <b>NtSecuritySharing</b> to 0.</li>
<li>If the synchronization object is shared with a <b>D3DKMT_HANDLE</b> data type, set <b>Shared</b> = 1 and <b>NtSecuritySharing</b> = 0.</li>
<li>If the synchronization object is shared with an NT handle to the process (and without a global <b>D3DKMT_HANDLE</b> kernel-mode handle to the resource), set <b>Shared</b> = 1 and <b>NtSecuritySharing</b> = 1.</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system. D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS is supported beginning with the Windows 7 operating system. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544658">D3DDDI_SYNCHRONIZATIONOBJECTINFO2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff544662">D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780251">D3DKMTShareObjects</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547802">D3DKMT_CREATEALLOCATIONFLAGS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh780254">D3DKMT_CREATEKEYEDMUTEX2_FLAGS</a>