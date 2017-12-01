---
UID: NF.ntifs.KeGetProcessorIndexFromNumber
title: KeGetProcessorIndexFromNumber
author: windows-driver-content
description: The KeGetProcessorIndexFromNumber routine converts a group number and a group-relative processor number to a systemwide processor index.
old-location: kernel\kegetprocessorindexfromnumber.htm
old-project: kernel
ms.assetid: c7d8ca52-a1e1-4f5f-9ffe-d64cec47eac7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeGetProcessorIndexFromNumber
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeGetProcessorIndexFromNumber
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
req.irql: Any level
req.iface: 
---

# KeGetProcessorIndexFromNumber function



## -description
<p>The <b>KeGetProcessorIndexFromNumber</b> routine converts a group number and a group-relative processor number to a systemwide processor index.</p>


## -syntax

````
ULONG KeGetProcessorIndexFromNumber(
  _In_ PPROCESSOR_NUMBER ProcNumber
);
````


## -parameters
<dl>

### -param <i>ProcNumber</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="..\miniport\ns-miniport--processor-number.md">PROCESSOR_NUMBER</a> structure that contains a group number and a group-relative processor number.</p>
</dd>
</dl>

## -returns
<p><b>KeGetProcessorIndexFromNumber</b> returns a systemwide processor index if the call is successful. If <i>ProcNumber</i> points to an invalid <b>PROCESSOR_NUMBER</b> value, the routine returns INVALID_PROCESSOR_INDEX, which is defined in the Wdm.h header file. </p>

## -remarks
<p>This routine accepts as input a <b>PROCESSOR_NUMBER</b> structure that identifies a processor by its group number and its processor number within the group. The return value is a processor index that identifies the processor across the entire multiprocessor system.</p>

<p>For example, if a multiprocessor system contains two groups, and each group contains 64 logical processors, the processor numbers in each group range from 0 to 63, but the systemwide processor indexes range from 0 to 127.</p>

<p>To obtain the total number of active logical processors in the system, call the <a href="..\ntddk\nf-ntddk-kequeryactiveprocessorcountex.md">KeQueryActiveProcessorCountEx</a> routine and set this routine's <i>GroupNumber</i> parameter to ALL_PROCESSOR_GROUPS.</p>

<p>The <a href="..\wdm\nf-wdm-kegetprocessornumberfromindex.md">KeGetProcessorNumberFromIndex</a> routine converts a systemwide processor index to a group number and a group-relative processor number.</p>

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
<p>Available in Windows 7 and later versions of Windows.</p>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-kegetprocessornumberfromindex.md">KeGetProcessorNumberFromIndex</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-kequeryactiveprocessorcountex.md">KeQueryActiveProcessorCountEx</a>
</dt>
<dt>
<a href="..\miniport\ns-miniport--processor-number.md">PROCESSOR_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeGetProcessorIndexFromNumber routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
