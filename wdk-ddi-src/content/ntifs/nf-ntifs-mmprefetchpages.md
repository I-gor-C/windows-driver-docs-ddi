---
UID: NF.ntifs.MmPrefetchPages
title: MmPrefetchPages
author: windows-driver-content
description: The MmPrefetchPages routine reads groups of pages from secondary storage in the optimal fashion.
old-location: ifsk\mmprefetchpages.htm
old-project: ifsk
ms.assetid: fd76dfed-2c47-4289-a672-1db8129f5a9e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MmPrefetchPages
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MmPrefetchPages
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
req.iface: 
---

# MmPrefetchPages function



## -description
<p>The <b>MmPrefetchPages</b> routine reads groups of pages from secondary storage in the optimal fashion. </p>


## -syntax

````
NTSTATUS MmPrefetchPages(
  _In_ ULONG      NumberOfLists,
  _In_ PREAD_LIST *ReadLists
);
````


## -parameters
<dl>

### -param NumberOfLists [in]

<dd>
<p>The number of read-lists in the array passed in the <i>ReadLists</i> parameter.</p>
</dd>

### -param ReadLists [in]

<dd>
<p>A pointer to an array of read-lists to be prefetched.</p>
</dd>
</dl>

## -returns
<p><b>MmPrefetchPages</b> returns STATUS_SUCCESS or an appropriate error status representing the final completion status of the operation. Possible error status codes include the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A temporary buffer required by this function could not be allocated. </p>

<p> </p>

<p><b>MmPrefetchPages</b> returns STATUS_SUCCESS on success and also if all of the requested pages were already in memory indicating no reads from secondary storage were required. </p>

## -remarks
<p><b>MmPrefetchPages</b> reads pages from secondary storage described in the read-lists in the optimal fashion. The caller builds a list of various file objects and logical block offsets, passing them to the <b>MmPrefetchPages</b> function which examines the internal pages, reading in those that are not already valid or in transition. The pages are read with a single read, using a dummy page to bridge small gaps. If the gap is "large", then separate reads are issued. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Microsoft Windows XP and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Ntifs.h)</dt>
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