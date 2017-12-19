---
UID: NF.ntifs.CcSetBcbOwnerPointer
title: CcSetBcbOwnerPointer function
author: windows-driver-content
description: The CcSetBcbOwnerPointer routine sets the owner thread pointer for a pinned buffer control block (BCB).
old-location: ifsk\ccsetbcbownerpointer.htm
old-project: ifsk
ms.assetid: fa99ebc4-72d3-42ef-9dda-dcfdd438f66f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CcSetBcbOwnerPointer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcSetBcbOwnerPointer
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: 
---

# CcSetBcbOwnerPointer function



## -description
The <b>CcSetBcbOwnerPointer</b> routine sets the owner thread pointer for a pinned buffer control block (BCB).



## -syntax

````
VOID CcSetBcbOwnerPointer(
  _In_ PVOID Bcb,
  _In_ PVOID OwnerPointer
);
````


## -parameters

### -param Bcb [in]

Pointer to a pinned BCB structure that is owned by the current thread.


### -param OwnerPointer [in]

A valid resource owner pointer, which means a pointer to an allocated system address, with the low-order two bits set. This address may not be deallocated until after the BCB is unpinned by a subsequent call to <a href="ifsk.ccunpindataforthread">CcUnpinDataForThread</a>.


## -returns
None


## -remarks
File systems call <b>CcSetBcbOwnerPointer</b> to set the resource owner for a pinned buffer control block (BCB), in cases where another thread will unpin the BCB and thus the current thread can exit.

Each call to <b>CcSetBcbOwnerPointer</b> must be matched by a subsequent call to <a href="ifsk.ccunpindataforthread">CcUnpinDataForThread</a>, which must be called with the same owner pointer.

BCBs that have been modified by <b>CcSetBcbOwnerPointer</b> cannot be unpinned by calling <a href="ifsk.ccunpindata">CcUnpinData</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.ccunpindata">CcUnpinData</a>
</dt>
<dt>
<a href="ifsk.ccunpindataforthread">CcUnpinDataForThread</a>
</dt>
<dt>
<a href="kernel.exsetresourceownerpointer">ExSetResourceOwnerPointer</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcSetBcbOwnerPointer routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

