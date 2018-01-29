---
UID : NS:d3dukmdt._D3DDDICB_LOCKFLAGS
title : _D3DDDICB_LOCKFLAGS
author : windows-driver-content
description : The D3DDDICB_LOCKFLAGS structure identifies how to lock an allocation.
old-location : display\d3dddicb_lockflags.htm
old-project : display
ms.assetid : 4b3a266f-4d60-4d39-81fb-ea2b4aa12a8d
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DDDICB_LOCKFLAGS, display.d3dddicb_lockflags, D3DDDICB_LOCKFLAGS structure [Display Devices], _D3DDDICB_LOCKFLAGS, D3D_other_Structs_6238800f-60d9-472d-aa18-10343abbcee7.xml, d3dukmdt/D3DDDICB_LOCKFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
req.include-header : D3dukmdt.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DDDICB_LOCKFLAGS
---

# _D3DDDICB_LOCKFLAGS structure
The D3DDDICB_LOCKFLAGS structure identifies how to lock an allocation.

## Syntax
````
typedef struct _D3DDDICB_LOCKFLAGS {
  union {
    struct {
      UINT ReadOnly  :1;
      UINT WriteOnly  :1;
      UINT DonotWait  :1;
      UINT IgnoreSync  :1;
      UINT LockEntire  :1;
      UINT DonotEvict  :1;
      UINT AcquireAperture  :1;
      UINT Discard  :1;
      UINT NoExistingReference  :1;
      UINT UseAlternateVA  :1;
      UINT IgnoreReadSync  :1;
      UINT Reserved  :21;
    };
    UINT   Value;
  };
} D3DDDICB_LOCKFLAGS;
````

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
An allocation can be locked only if it was created with the <b>CpuVisible</b>  member set in the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_allocationinfoflags.md">DXGK_ALLOCATIONINFOFLAGS</a> structure.

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
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h (include D3dukmdt.h) |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_lockcb.md">pfnLockCb</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_allocationinfoflags.md">DXGK_ALLOCATIONINFOFLAGS</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_acquireswizzlingrange.md">DxgkDdiAcquireSwizzlingRange</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddicb_lock.md">D3DDDICB_LOCK</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_LOCKFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>