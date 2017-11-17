---
UID: NF.ntifs.CcUnpinData
title: CcUnpinData
author: windows-driver-content
description: The CcUnpinData routine releases cached file data that was mapped or pinned by an earlier call to CcMapData, CcPinRead, or CcPreparePinWrite.
old-location: ifsk\ccunpindata.htm
ms.assetid: a06bbe25-9841-4aeb-9d51-257dd1472027
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CcUnpinData
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
req.irql: PASSIVE_LEVEL
ms.keywords: CcUnpinData
req.iface: 
---

# CcUnpinData function



## -description
<p>The <b>CcUnpinData</b> routine releases cached file data that was mapped or pinned by an earlier call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539155">CcMapData</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a>.</p>


## -syntax

````
VOID CcUnpinData(
  _In_ PVOID Bcb
);
````


## -parameters
<dl>

### -param <i>Bcb</i> [in]

<dd>
<p>Pointer to a buffer control block (BCB) for the data to be released.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcUnpinData</b> frees the BCB and performs any other necessary cleanup.</p>

<p>Every successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539155">CcMapData</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a> must be matched by a subsequent call to <b>CcUnpinData</b>. </p>

<p>BCBs that have been modified by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539207">CcSetBcbOwnerPointer</a> cannot be unpinned by calling <b>CcUnpinData</b>. <a href="https://msdn.microsoft.com/library/windows/hardware/ff539231">CcUnpinDataForThread</a> must be called instead.</p>

<p><b>CcUnpinData</b> frees the BCB and performs any other necessary cleanup.</p>

<p>Every successful call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff539155">CcMapData</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a> must be matched by a subsequent call to <b>CcUnpinData</b>. </p>

<p>BCBs that have been modified by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539207">CcSetBcbOwnerPointer</a> cannot be unpinned by calling <b>CcUnpinData</b>. <a href="https://msdn.microsoft.com/library/windows/hardware/ff539231">CcUnpinDataForThread</a> must be called instead.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539155">CcMapData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539180">CcPinRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539183">CcPreparePinWrite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539207">CcSetBcbOwnerPointer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539231">CcUnpinDataForThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcUnpinData routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
