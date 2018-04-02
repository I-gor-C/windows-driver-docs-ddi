---
UID: NE:wudfwdm._POOL_TYPE
title: "_POOL_TYPE"
author: windows-driver-content
description: The POOL_TYPE enumeration type specifies the type of system memory to allocate.
old-location: kernel\pool_type.htm
old-project: kernel
ms.assetid: a3dd0c74-3835-4f03-8b62-08954baaffe7
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: DontUseThisType, DontUseThisTypeSession, MaxPoolType, NonPagedPool, NonPagedPoolBase, NonPagedPoolBaseCacheAligned, NonPagedPoolBaseCacheAlignedMustS, NonPagedPoolBaseMustSucceed, NonPagedPoolCacheAligned, NonPagedPoolCacheAlignedMustS, NonPagedPoolCacheAlignedMustSSession, NonPagedPoolCacheAlignedSession, NonPagedPoolExecute, NonPagedPoolMustSucceed, NonPagedPoolMustSucceedSession, NonPagedPoolNx, NonPagedPoolNxCacheAligned, NonPagedPoolSession, NonPagedPoolSessionNx, POOL_TYPE, POOL_TYPE enumeration [Kernel-Mode Driver Architecture], PagedPool, PagedPoolCacheAligned, PagedPoolCacheAlignedSession, PagedPoolSession, _POOL_TYPE, kernel.pool_type, sysenum_90446d42-0e73-4da3-a3df-27efe3daa67b.xml, wdm/DontUseThisType, wdm/DontUseThisTypeSession, wdm/MaxPoolType, wdm/NonPagedPool, wdm/NonPagedPoolBase, wdm/NonPagedPoolBaseCacheAligned, wdm/NonPagedPoolBaseCacheAlignedMustS, wdm/NonPagedPoolBaseMustSucceed, wdm/NonPagedPoolCacheAligned, wdm/NonPagedPoolCacheAlignedMustS, wdm/NonPagedPoolCacheAlignedMustSSession, wdm/NonPagedPoolCacheAlignedSession, wdm/NonPagedPoolExecute, wdm/NonPagedPoolMustSucceed, wdm/NonPagedPoolMustSucceedSession, wdm/NonPagedPoolNx, wdm/NonPagedPoolNxCacheAligned, wdm/NonPagedPoolSession, wdm/NonPagedPoolSessionNx, wdm/POOL_TYPE, wdm/PagedPool, wdm/PagedPoolCacheAligned, wdm/PagedPoolCacheAlignedSession, wdm/PagedPoolSession
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfwdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h
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
req.irql: Called at IRQL <= DISPATCH_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	POOL_TYPE
product: Windows
targetos: Windows
req.typenames: POOL_TYPE
req.product: Windows 10 or later.
---

# _POOL_TYPE Enumeration
The <b>POOL_TYPE</b> enumeration type specifies the type of system memory to allocate.

## Syntax
````
typedef enum _POOL_TYPE { 
  NonPagedPool,
  NonPagedPoolExecute                   = NonPagedPool,
  PagedPool,
  NonPagedPoolMustSucceed               = NonPagedPool + 2,
  DontUseThisType,
  NonPagedPoolCacheAligned              = NonPagedPool + 4,
  PagedPoolCacheAligned,
  NonPagedPoolCacheAlignedMustS         = NonPagedPool + 6,
  MaxPoolType,
  NonPagedPoolBase                      = 0,
  NonPagedPoolBaseMustSucceed           = NonPagedPoolBase + 2,
  NonPagedPoolBaseCacheAligned          = NonPagedPoolBase + 4,
  NonPagedPoolBaseCacheAlignedMustS     = NonPagedPoolBase + 6,
  NonPagedPoolSession                   = 32,
  PagedPoolSession                      = NonPagedPoolSession + 1,
  NonPagedPoolMustSucceedSession        = PagedPoolSession + 1,
  DontUseThisTypeSession                = NonPagedPoolMustSucceedSession + 1,
  NonPagedPoolCacheAlignedSession       = DontUseThisTypeSession + 1,
  PagedPoolCacheAlignedSession          = NonPagedPoolCacheAlignedSession + 1,
  NonPagedPoolCacheAlignedMustSSession  = PagedPoolCacheAlignedSession + 1,
  NonPagedPoolNx                        = 512,
  NonPagedPoolNxCacheAligned            = NonPagedPoolNx + 4,
  NonPagedPoolSessionNx                 = NonPagedPoolNx + 32
} POOL_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>NonPagedPool</td>
                    <td><i>Nonpaged pool</i>, which is nonpageable system memory. Nonpaged pool can be accessed from any IRQL, but it is a scarce resource and drivers should allocate it only when necessary.

System memory allocated with the <b>NonPagedPool</b> pool type is executable. For more information, see the description of the <b>NonPagedPoolExecute</b> pool type.

Starting with Windows 8, drivers should allocate most or all of their nonpaged memory from the no-execute (NX) nonpaged pool instead of the executable nonpaged pool. For more information, see the description of the <b>NonPagedPoolNx</b> pool type.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolExecute</td>
                    <td>Starting with Windows 8, <b>NonPagedPoolExecute</b> is an alternate name for the <b>NonPagedPool</b> value. This value indicates that the allocated memory is to be nonpaged and executable—that is, instruction execution is enabled in this memory. To port a driver from an earlier version of Windows, you should typically replace all or most instances of the <b>NonPagedPool</b> name in the driver source code with <b>NonPagedPoolNx</b>. Avoid replacing instances of the <b>NonPagedPool</b> name with <b>NonPagedPoolExecute</b> except in cases in which executable memory is explicitly required. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh920391">No-Execute (NX) Nonpaged Pool</a>.</td>
                </tr>
            
                <tr>
                    <td>PagedPool</td>
                    <td><i>Paged pool</i>, which is pageable system memory. Paged pool can only be allocated and accessed at IRQL &lt; DISPATCH_LEVEL.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolMustSucceed</td>
                    <td>This value is <u>for internal use only</u>, and is allowed only during system startup. Drivers must not specify this value at times other than system startup, because a "must succeed" request crashes the system if the requested memory size is unavailable.</td>
                </tr>
            
                <tr>
                    <td>DontUseThisType</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolCacheAligned</td>
                    <td>Nonpaged pool, aligned on processor cache boundaries. This value is <u>for internal use only</u>.</td>
                </tr>
            
                <tr>
                    <td>PagedPoolCacheAligned</td>
                    <td>Paged pool, aligned on processor cache boundaries. This value is <u>for internal use only</u>.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolCacheAlignedMustS</td>
                    <td>This value is <u>for internal use only</u>, and is allowed only during system startup. It is the cache-aligned equivalent of <b>NonPagedPoolMustSucceed</b>.</td>
                </tr>
            
                <tr>
                    <td>MaxPoolType</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolBase</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolBaseMustSucceed</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolBaseCacheAligned</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolBaseCacheAlignedMustS</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>PagedPoolSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolMustSucceedSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>DontUseThisTypeSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolCacheAlignedSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>PagedPoolCacheAlignedSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolCacheAlignedMustSSession</td>
                    <td>Deprecated. Do not use.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolNx</td>
                    <td><i>No-execute</i> (NX) nonpaged pool. This pool type is available starting with Windows 8. In contrast to the nonpaged pool designated by <b>NonPagedPool</b>, which allocates executable memory, the NX nonpaged pool  allocates memory in which instruction execution is disabled. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh920391">No-Execute (NX) Nonpaged Pool</a>.

Nonpaged pool can be accessed from any IRQL, but it is a scarce resource and drivers should allocate it only when necessary.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolNxCacheAligned</td>
                    <td>NX nonpaged pool, aligned on processor cache boundaries. This value is reserved for exclusive use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>NonPagedPoolSessionNx</td>
                    <td>Reserved for exclusive use by the operating system.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wudfwdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554322">LookasideListAllocateEx</a>



<a href="..\wdm\nf-wdm-exinitializepagedlookasidelist.md">ExInitializePagedLookasideList</a>



<a href="..\wdm\nf-wdm-exallocatepoolwithtagpriority.md">ExAllocatePoolWithTagPriority</a>



<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>



<a href="..\wdm\nf-wdm-seassignsecurityex.md">SeAssignSecurityEx</a>



<a href="..\wdm\nf-wdm-exinitializelookasidelistex.md">ExInitializeLookasideListEx</a>



<a href="..\wdm\nf-wdm-exallocatepoolwithquotatag.md">ExAllocatePoolWithQuotaTag</a>



<a href="..\wdm\nf-wdm-seassignsecurity.md">SeAssignSecurity</a>



<a href="..\wdm\nf-wdm-exinitializenpagedlookasidelist.md">ExInitializeNPagedLookasideList</a>