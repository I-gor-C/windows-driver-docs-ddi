---
UID: NF.ntifs.CcUnpinDataForThread
title: CcUnpinDataForThread
author: windows-driver-content
description: The CcUnpinDataForThread routine releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to CcSetBcbOwnerPointer.
old-location: ifsk\ccunpindataforthread.htm
old-project: ifsk
ms.assetid: 9c29689c-ce5e-4b29-a17b-32d96f8f87e7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: CcUnpinDataForThread
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
req.alt-api: CcUnpinDataForThread
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

# CcUnpinDataForThread function



## -description
<p>The <b>CcUnpinDataForThread</b> routine releases pages of a cached file whose buffer control block (BCB) was modified by an earlier call to <a href="..\ntifs\nf-ntifs-ccsetbcbownerpointer.md">CcSetBcbOwnerPointer</a>.</p>


## -syntax

````
VOID CcUnpinDataForThread(
  _In_ PVOID            Bcb,
  _In_ ERESOURCE_THREAD ResourceThreadId
);
````


## -parameters
<dl>

### -param <i>Bcb</i> [in]

<dd>
<p>Pointer to the BCB for the pages to be released.</p>
</dd>

### -param <i>ResourceThreadId</i> [in]

<dd>
<p>Identifies the thread that originally acquired the BCB. Must match the owner pointer used in the call to <a href="..\ntifs\nf-ntifs-ccsetbcbownerpointer.md">CcSetBcbOwnerPointer</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcUnpinDataForThread</b> releases the BCB for the indicated thread and performs any other necessary cleanup.</p>

<p>Each call to <a href="..\ntifs\nf-ntifs-ccsetbcbownerpointer.md">CcSetBcbOwnerPointer</a> must be matched by a subsequent call to <b>CcUnpinDataForThread</b>.</p>

<p><b>CcUnpinDataForThread</b> is functionally equivalent to <a href="..\ntifs\nf-ntifs-ccunpindata.md">CcUnpinData</a>, except that it also releases the BCB resource for the indicated thread.</p>

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
<a href="..\ntifs\nf-ntifs-ccsetbcbownerpointer.md">CcSetBcbOwnerPointer</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccunpindata.md">CcUnpinData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcUnpinDataForThread routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
