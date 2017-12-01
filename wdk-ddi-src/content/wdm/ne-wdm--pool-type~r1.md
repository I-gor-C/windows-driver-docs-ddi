---
UID: NE.wdm._POOL_TYPE~r1
title: POOL_TYPE
author: windows-driver-content
description: The POOL_TYPE enumeration type specifies the type of system memory to allocate.
old-location: kernel\pool_type.htm
old-project: kernel
ms.assetid: a3dd0c74-3835-4f03-8b62-08954baaffe7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.alt-api: POOL_TYPE
req.alt-loc: Wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# POOL_TYPE enumeration



## -description
<p>The <b>POOL_TYPE</b> enumeration type specifies the type of system memory to allocate.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="NonPagedPool"></a><a id="nonpagedpool"></a><a id="NONPAGEDPOOL"></a><b>NonPagedPool</b>

<dd>
<p><i>Nonpaged pool</i>, which is nonpageable system memory. Nonpaged pool can be accessed from any IRQL, but it is a scarce resource and drivers should allocate it only when necessary.</p>
<p>System memory allocated with the <b>NonPagedPool</b> pool type is executable. For more information, see the description of the <b>NonPagedPoolExecute</b> pool type.</p>
<p>Starting with Windows 8, drivers should allocate most or all of their nonpaged memory from the no-execute (NX) nonpaged pool instead of the executable nonpaged pool. For more information, see the description of the <b>NonPagedPoolNx</b> pool type.</p>
</dd>

### -field <a id="NonPagedPoolExecute"></a><a id="nonpagedpoolexecute"></a><a id="NONPAGEDPOOLEXECUTE"></a><b>NonPagedPoolExecute</b>

<dd>
<p>Starting with Windows 8, <b>NonPagedPoolExecute</b> is an alternate name for the <b>NonPagedPool</b> value. This value indicates that the allocated memory is to be nonpaged and executable—that is, instruction execution is enabled in this memory. To port a driver from an earlier version of Windows, you should typically replace all or most instances of the <b>NonPagedPool</b> name in the driver source code with <b>NonPagedPoolNx</b>. Avoid replacing instances of the <b>NonPagedPool</b> name with <b>NonPagedPoolExecute</b> except in cases in which executable memory is explicitly required. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh920391">No-Execute (NX) Nonpaged Pool</a>.</p>
</dd>

### -field <a id="PagedPool"></a><a id="pagedpool"></a><a id="PAGEDPOOL"></a><b>PagedPool</b>

<dd>
<p><i>Paged pool</i>, which is pageable system memory. Paged pool can only be allocated and accessed at IRQL &lt; DISPATCH_LEVEL.</p>
</dd>

### -field <a id="NonPagedPoolMustSucceed"></a><a id="nonpagedpoolmustsucceed"></a><a id="NONPAGEDPOOLMUSTSUCCEED"></a><b>NonPagedPoolMustSucceed</b>

<dd>
<p>This value is <u>for internal use only</u>, and is allowed only during system startup. Drivers must not specify this value at times other than system startup, because a "must succeed" request crashes the system if the requested memory size is unavailable.</p>
</dd>

### -field <a id="DontUseThisType"></a><a id="dontusethistype"></a><a id="DONTUSETHISTYPE"></a><b>DontUseThisType</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolCacheAligned"></a><a id="nonpagedpoolcachealigned"></a><a id="NONPAGEDPOOLCACHEALIGNED"></a><b>NonPagedPoolCacheAligned</b>

<dd>
<p>Nonpaged pool, aligned on processor cache boundaries. This value is <u>for internal use only</u>.</p>
</dd>

### -field <a id="PagedPoolCacheAligned"></a><a id="pagedpoolcachealigned"></a><a id="PAGEDPOOLCACHEALIGNED"></a><b>PagedPoolCacheAligned</b>

<dd>
<p>Paged pool, aligned on processor cache boundaries. This value is <u>for internal use only</u>.</p>
</dd>

### -field <a id="NonPagedPoolCacheAlignedMustS"></a><a id="nonpagedpoolcachealignedmusts"></a><a id="NONPAGEDPOOLCACHEALIGNEDMUSTS"></a><b>NonPagedPoolCacheAlignedMustS</b>

<dd>
<p>This value is <u>for internal use only</u>, and is allowed only during system startup. It is the cache-aligned equivalent of <b>NonPagedPoolMustSucceed</b>.</p>
</dd>

### -field <a id="MaxPoolType"></a><a id="maxpooltype"></a><a id="MAXPOOLTYPE"></a><b>MaxPoolType</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolBase"></a><a id="nonpagedpoolbase"></a><a id="NONPAGEDPOOLBASE"></a><b>NonPagedPoolBase</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolBaseMustSucceed"></a><a id="nonpagedpoolbasemustsucceed"></a><a id="NONPAGEDPOOLBASEMUSTSUCCEED"></a><b>NonPagedPoolBaseMustSucceed</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolBaseCacheAligned"></a><a id="nonpagedpoolbasecachealigned"></a><a id="NONPAGEDPOOLBASECACHEALIGNED"></a><b>NonPagedPoolBaseCacheAligned</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolBaseCacheAlignedMustS"></a><a id="nonpagedpoolbasecachealignedmusts"></a><a id="NONPAGEDPOOLBASECACHEALIGNEDMUSTS"></a><b>NonPagedPoolBaseCacheAlignedMustS</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="NonPagedPoolSession"></a><a id="nonpagedpoolsession"></a><a id="NONPAGEDPOOLSESSION"></a><b>NonPagedPoolSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="PagedPoolSession"></a><a id="pagedpoolsession"></a><a id="PAGEDPOOLSESSION"></a><b>PagedPoolSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="NonPagedPoolMustSucceedSession"></a><a id="nonpagedpoolmustsucceedsession"></a><a id="NONPAGEDPOOLMUSTSUCCEEDSESSION"></a><b>NonPagedPoolMustSucceedSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="DontUseThisTypeSession"></a><a id="dontusethistypesession"></a><a id="DONTUSETHISTYPESESSION"></a><b>DontUseThisTypeSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="NonPagedPoolCacheAlignedSession"></a><a id="nonpagedpoolcachealignedsession"></a><a id="NONPAGEDPOOLCACHEALIGNEDSESSION"></a><b>NonPagedPoolCacheAlignedSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="PagedPoolCacheAlignedSession"></a><a id="pagedpoolcachealignedsession"></a><a id="PAGEDPOOLCACHEALIGNEDSESSION"></a><b>PagedPoolCacheAlignedSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="NonPagedPoolCacheAlignedMustSSession"></a><a id="nonpagedpoolcachealignedmustssession"></a><a id="NONPAGEDPOOLCACHEALIGNEDMUSTSSESSION"></a><b>NonPagedPoolCacheAlignedMustSSession</b>

<dd>
<p>Deprecated. Do not use.</p>
</dd>

### -field <a id="NonPagedPoolNx"></a><a id="nonpagedpoolnx"></a><a id="NONPAGEDPOOLNX"></a><b>NonPagedPoolNx</b>

<dd>
<p><i>No-execute</i> (NX) nonpaged pool. This pool type is available starting with Windows 8. In contrast to the nonpaged pool designated by <b>NonPagedPool</b>, which allocates executable memory, the NX nonpaged pool  allocates memory in which instruction execution is disabled. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh920391">No-Execute (NX) Nonpaged Pool</a>.</p>
<p>Nonpaged pool can be accessed from any IRQL, but it is a scarce resource and drivers should allocate it only when necessary.</p>
</dd>

### -field <a id="NonPagedPoolNxCacheAligned"></a><a id="nonpagedpoolnxcachealigned"></a><a id="NONPAGEDPOOLNXCACHEALIGNED"></a><b>NonPagedPoolNxCacheAligned</b>

<dd>
<p>NX nonpaged pool, aligned on processor cache boundaries. This value is reserved for exclusive use by the operating system.</p>
</dd>

### -field <a id="NonPagedPoolSessionNx"></a><a id="nonpagedpoolsessionnx"></a><a id="NONPAGEDPOOLSESSIONNX"></a><b>NonPagedPoolSessionNx</b>

<dd>
<p>Reserved for exclusive use by the operating system.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithquotatag.md">ExAllocatePoolWithQuotaTag</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtagpriority.md">ExAllocatePoolWithTagPriority</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinitializelookasidelistex.md">ExInitializeLookasideListEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinitializenpagedlookasidelist.md">ExInitializeNPagedLookasideList</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-exinitializepagedlookasidelist.md">ExInitializePagedLookasideList</a>
</dt>
<dt>
<a href="kernel.lookasidelistallocateex">LookasideListAllocateEx</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-seassignsecurity.md">SeAssignSecurity</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-seassignsecurityex.md">SeAssignSecurityEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20POOL_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
