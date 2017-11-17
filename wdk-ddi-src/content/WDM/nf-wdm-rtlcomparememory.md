---
UID: NF.wdm.RtlCompareMemory
title: RtlCompareMemory
author: windows-driver-content
description: The RtlCompareMemory routine compares two blocks of memory and returns the number of bytes that match.
old-location: kernel\rtlcomparememory.htm
ms.assetid: 1801fc27-53bf-4ac5-be41-072dfd8b0696
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCompareMemory
req.alt-loc: NtDll.dll,Kernel32.dll,NtosKrnl.exe,API-MS-Win-Core-rtlsupport-l1-1-0.dll,API-MS-Win-Core-rtlsupport-l1-2-0.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib; 
OneCoreUAP.lib on Windows 10
req.dll: NtDll.dll (user mode); 
Kernel32.dll (user mode); 
NtosKrnl.exe (kernel mode)
req.irql: Any level (See Remarks section)
ms.keywords: RtlCompareMemory
req.iface: 
req.product: Windows 10 or later.
---

# RtlCompareMemory function



## -description
<p>The <b>RtlCompareMemory</b> routine compares two blocks of memory and returns the number of bytes that match.</p>


## -syntax

````
SIZE_T RtlCompareMemory(
  _In_ const VOID   *Source1,
  _In_ const VOID   *Source2,
  _In_       SIZE_T Length
);
````


## -parameters
<dl>

### -param <i>Source1</i> [in]

<dd>
<p>A pointer to the first block of memory.</p>
</dd>

### -param <i>Source2</i> [in]

<dd>
<p>A pointer to the second block of memory.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to compare.</p>
</dd>
</dl>

## -returns
<p><b>RtlCompareMemory</b> returns the number of bytes in the two blocks that match. If all bytes match up to the specified <i>Length</i> value, the <i>Length</i> value is returned.</p>

## -remarks
<p>The routine starts by comparing the first byte in the first block to the first byte in the second block, and continues to compare successive bytes in the two blocks while the bytes match. The routine stops comparing bytes when it encounters the first pair of bytes that are not equal, or when the number of matching bytes equals the <i>Length</i> parameter value, whichever occurs first.</p>

<p>Callers of <b>RtlCompareMemory</b> can be running at any IRQL if both blocks of memory are resident.</p>

<p>The routine starts by comparing the first byte in the first block to the first byte in the second block, and continues to compare successive bytes in the two blocks while the bytes match. The routine stops comparing bytes when it encounters the first pair of bytes that are not equal, or when the number of matching bytes equals the <i>Length</i> parameter value, whichever occurs first.</p>

<p>Callers of <b>RtlCompareMemory</b> can be running at any IRQL if both blocks of memory are resident.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib; </dt>
<dt>OneCoreUAP.lib on Windows 10</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtDll.dll (user mode); </dt>
<dt>Kernel32.dll (user mode); </dt>
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (See Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975066">BufAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542318">BufAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542328">BufAfterReqCompletedReadA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542340">BufAfterReqCompletedWriteA</a>
</td>
</tr>
</table>