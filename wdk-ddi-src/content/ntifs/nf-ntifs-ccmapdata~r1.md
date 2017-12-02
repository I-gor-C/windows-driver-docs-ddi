---
UID: NF.ntifs.CcMapData~r1
title: CcMapData
author: windows-driver-content
description: The CcMapData routine maps a specified byte range of a cached file to a buffer in memory.
old-location: ifsk\ccmapdata.htm
old-project: ifsk
ms.assetid: dccc79ba-68d9-41cf-b86d-37adb83558a0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: CcMapData
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
req.alt-api: CcMapData
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
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# CcMapData function



## -description
<p>The <b>CcMapData</b> routine maps a specified byte range of a cached file to a buffer in memory.</p>


## -syntax

````
BOOLEAN CcMapData(
  _In_  PFILE_OBJECT   FileObject,
  _In_  PLARGE_INTEGER FileOffset,
  _In_  ULONG          Length,
  _In_  ULONG          Flags,
  _Out_ PVOID          *Bcb,
  _Out_ PVOID          *Buffer
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>Pointer to a file object for the file whose data is to be mapped for read access.</p>
</dd>

### -param FileOffset [in]

<dd>
<p>Pointer to a variable that specifies the starting byte offset within the cached file where the desired data resides.</p>
</dd>

### -param Length [in]

<dd>
<p>Length of desired data in bytes.</p>
</dd>

### -param Flags [in]

<dd>
<p>Bitmask of flags specifying how the mapping operation is to be performed. This is a bitwise OR combination of one or more of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>MAP_WAIT</p>
</td>
<td>
<p>The caller can be put into a wait state until the data has been mapped. </p>
</td>
</tr>
<tr>
<td>
<p>MAP_NO_READ</p>
</td>
<td>
<p>Only pages that are already resident in memory are to be mapped. </p>
</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>    In Windows 2000and earlier, this parameter was a BOOLEAN value named <i>Wait</i>: </div>
<div> </div>
<p></p>
<dl>

### -param Wait

<dd>
<p>Set to <b>TRUE</b> if the caller can be put into a wait state until the data has been mapped, <b>FALSE</b> otherwise.</p>
</dd>
</dl>
</dd>

### -param Bcb [out]

<dd>
<p>On the first call this returns a pointer to a buffer control block (BCB) structure. This pointer must be supplied as input on all subsequent calls, for this buffer.</p>
</dd>

### -param Buffer [out]

<dd>
<p>Pointer to a buffer containing the mapped data.</p>
</dd>
</dl>

## -returns
<p><b>CcMapData</b> returns <b>TRUE</b> if the data for the cached file was mapped successfully, <b>FALSE</b> otherwise.</p>

## -remarks
<p><b>CcMapData</b> maps data in a cached file for read access. Note that after <b>CcMapData</b> is called, the data is mapped; but it is not pinned. This distinction is important. Data that is mapped but not pinned cannot safely be modified. To pin the data, use <a href="..\ntifs\nf-ntifs-ccpinmappeddata.md">CcPinMappedData</a>, <a href="..\ntifs\nf-ntifs-ccpinread.md">CcPinRead</a>, or <a href="..\ntifs\nf-ntifs-ccpreparepinwrite.md">CcPreparePinWrite</a>.</p>

<p>Every successful call to <b>CcMapData</b> must be matched by a subsequent call to <a href="..\ntifs\nf-ntifs-ccunpindata.md">CcUnpinData</a>. </p>

<p><b>CcMapData</b> cannot map data across view boundaries in the cache manager. The cache manager manages files in the system in 256 KB-aligned views. (The cache manager's view size is specified by the system-defined constant <b>VACB_MAPPING_GRANULARITY</b>, which is set to 256 KB in <i>ntifs.h</i>.) Mapped regions cannot span more than one 256 KB view. Therefore, the largest region that can be mapped is 256 KB, beginning at a 256 KB-aligned offset in the file. </p>

<p>Mapping a byte range in a cached file does not ensure that the pages remain resident in memory. As long as the pages are mapped, the byte range is guaranteed to stay mapped into the system cache virtual address space, but the memory manager can page out the physical pages as the system's memory demand requires. </p>

<p>If the <b>MAP_WAIT</b> flag is set (or <i>Wait</i> is <b>TRUE</b>), <b>CcMapData</b> is guaranteed to complete the mapping request and return <b>TRUE</b>. If the required pages of the cached file are already resident in memory, the data is mapped immediately and no blocking will occur. If any needed pages are not resident, the caller is put in a wait state until all required pages have been made resident and the data can be mapped. If the <b>MAP_WAIT</b> flag is not set (or <i>Wait</i> is <b>FALSE</b>) and the data cannot be mapped immediately, <b>CcMapData</b> returns <b>FALSE</b>.</p>

<p>The pointer returned in <i>Buffer</i> is valid until <a href="..\ntifs\nf-ntifs-ccunpindata.md">CcUnpinData</a> is called. If <a href="..\ntifs\nf-ntifs-ccpinmappeddata.md">CcPinMappedData</a> is called while this pointer is still valid, the pointer remains valid after the call to <b>CcPinMappedData</b> (but only until <b>CcUnpinData</b> is called).</p>

<p>If any failure occurs, <b>CcMapData</b> raises a status exception for that particular failure. For example, if a pool allocation failure occurs, <b>CcMapData</b> raises a <b>STATUS_INSUFFICIENT_RESOURCES</b> exception; if an I/O error occurs, <b>CcMapData</b> raises the status exception of the I/O error. Therefore, to gain control if a failure occurs, the driver should wrap the call to <b>CcMapData</b> in a <b>try-except</b> or <b>try-finally</b> statement.</p>

<p>To cache a file, use <a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>.</p>

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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccpinmappeddata.md">CcPinMappedData</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccpinread.md">CcPinRead</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccpreparepinwrite.md">CcPreparePinWrite</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccunpindata.md">CcUnpinData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcMapData routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
