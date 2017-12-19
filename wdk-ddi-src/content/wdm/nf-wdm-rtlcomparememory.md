---
UID: NF.wdm.RtlCompareMemory
title: RtlCompareMemory function
author: windows-driver-content
description: The RtlCompareMemory routine compares two blocks of memory and returns the number of bytes that match.
old-location: kernel\rtlcomparememory.htm
old-project: kernel
ms.assetid: 1801fc27-53bf-4ac5-be41-072dfd8b0696
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlCompareMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
req.lib: NtosKrnl.lib; OneCoreUAP.lib on Windows 10
req.dll: NtDll.dll (user mode); Kernel32.dll (user mode); NtosKrnl.exe (kernel mode)
req.irql: Any level (See Remarks section)
req.product: Windows 10 or later.
---

# RtlCompareMemory function



## -description
The <b>RtlCompareMemory</b> routine compares two blocks of memory and returns the number of bytes that match.



## -syntax

````
SIZE_T RtlCompareMemory(
  _In_ const VOID   *Source1,
  _In_ const VOID   *Source2,
  _In_       SIZE_T Length
);
````


## -parameters

### -param Source1 [in]

A pointer to the first block of memory.


### -param Source2 [in]

A pointer to the second block of memory.


### -param Length [in]

The number of bytes to compare.


## -returns
<b>RtlCompareMemory</b> returns the number of bytes in the two blocks that match. If all bytes match up to the specified <i>Length</i> value, the <i>Length</i> value is returned.


## -remarks
The routine starts by comparing the first byte in the first block to the first byte in the second block, and continues to compare successive bytes in the two blocks while the bytes match. The routine stops comparing bytes when it encounters the first pair of bytes that are not equal, or when the number of matching bytes equals the <i>Length</i> parameter value, whichever occurs first.

Callers of <b>RtlCompareMemory</b> can be running at any IRQL if both blocks of memory are resident.


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
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

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
DLL

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
IRQL

</th>
<td width="70%">
Any level (See Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>
</td>
</tr>
</table>