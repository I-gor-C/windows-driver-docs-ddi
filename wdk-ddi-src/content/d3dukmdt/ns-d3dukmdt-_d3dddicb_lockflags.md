---
UID: NS:d3dukmdt._D3DDDICB_LOCKFLAGS
title: "_D3DDDICB_LOCKFLAGS"
author: windows-driver-content
description: The D3DDDICB_LOCKFLAGS structure identifies how to lock an allocation.
old-location: display\d3dddicb_lockflags.htm
old-project: display
ms.assetid: 4b3a266f-4d60-4d39-81fb-ea2b4aa12a8d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDICB_LOCKFLAGS, D3DDDICB_LOCKFLAGS structure [Display Devices], D3D_other_Structs_6238800f-60d9-472d-aa18-10343abbcee7.xml, _D3DDDICB_LOCKFLAGS, d3dukmdt/D3DDDICB_LOCKFLAGS, display.d3dddicb_lockflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	D3DDDICB_LOCKFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDICB_LOCKFLAGS
---

# _D3DDDICB_LOCKFLAGS structure
The D3DDDICB_LOCKFLAGS structure identifies how to lock an allocation.

## Syntax
```
typedef struct _D3DDDICB_LOCKFLAGS {
  union {
    struct {
      UINT  : 1  ReadOnly;
      UINT  : 1  WriteOnly;
      UINT  : 1  DonotWait;
      UINT  : 1  IgnoreSync;
      UINT  : 1  LockEntire;
      UINT  : 1  DonotEvict;
      UINT  : 1  AcquireAperture;
      UINT  : 1  Discard;
      UINT  : 1  NoExistingReference;
      UINT  : 1  UseAlternateVA;
      UINT  : 1  IgnoreReadSync;
      UINT  : 21 Reserved;
    };
    UINT Value;
  };
} D3DDDICB_LOCKFLAGS;
```

## Members


## Remarks
When you use a D3DDDICB_LOCKFLAGS structure to specify how to lock an allocation, you must adhere to the following rules:

<ul>
<li>
Simultaneously specifying the <b>ReadOnly</b> and <b>WriteOnly</b> members is invalid.

</li>
<li>
The <b>IgnoreSync</b> member has no effect if specified with the <b>Discard</b> member.

</li>
<li>
The <b>DonotWait</b> member has no effect if specified with the <b>Discard</b> member.

</li>
<li>
Simultaneously specifying the <b>IgnoreSync</b> and <b>AcquireAperture</b> members is invalid.

</li>
<li>
Because specifying the <b>UseAlternateVA</b> member indicates that an aperture is acquired, the <b>AcquireAperture</b> member must also be set.

</li>
<li>
Retired or offered allocations cannot be locked. See also <a href="https://msdn.microsoft.com/f22e19ba-9ff3-4aa1-a3f0-103f67ea7c60">Requesting to Rename an Allocation</a>.

</li>
<li>
An allocation can be locked only if it was created with the <b>CpuVisible</b>  member set in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560966">DXGK_ALLOCATIONINFOFLAGS</a> structure.

</li>
<li>
Only the owner (creator) of a shared allocation can lock it, unless it's a GDI non-managed primary allocation.

</li>
<li>
An allocation that is locked with a swizzled range must be unlocked before it can be locked again.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dukmdt.h (include D3dukmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544205">D3DDDICB_LOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560966">DXGK_ALLOCATIONINFOFLAGS</a>



<a href="https://msdn.microsoft.com/f861e055-70db-4e0a-9c62-87e2d41f92ae">DxgkDdiAcquireSwizzlingRange</a>



<a href="https://msdn.microsoft.com/69022797-432a-410b-8cbf-e1ef7111e7ea">pfnLockCb</a>