---
UID: NF.ntifs.CcSetAdditionalCacheAttributes
title: CcSetAdditionalCacheAttributes
author: windows-driver-content
description: Call the CcSetAdditionalCacheAttributes routine to enable or disable read-ahead (also called &#0034;lazy read&#0034;) or write-behind (also called &#0034;lazy write&#0034;) on a cached file.
old-location: ifsk\ccsetadditionalcacheattributes.htm
ms.assetid: 2f891543-0222-45c8-97cd-719ec5dd2fa8
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
req.alt-api: CcSetAdditionalCacheAttributes
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
req.irql: <= APC_LEVEL
ms.keywords: CcSetAdditionalCacheAttributes
req.iface: 
---

# CcSetAdditionalCacheAttributes function



## -description
<p>Call the <b>CcSetAdditionalCacheAttributes</b> routine to enable or disable read-ahead (also called "lazy read") or write-behind (also called "lazy write") on a cached file.</p>


## -syntax

````
VOID CcSetAdditionalCacheAttributes(
  _In_ PFILE_OBJECT FileObject,
  _In_ BOOLEAN      DisableReadAhead,
  _In_ BOOLEAN      DisableWriteBehind
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to a file object for the cached file.</p>
</dd>

### -param <i>DisableReadAhead</i> [in]

<dd>
<p>Set to <b>TRUE</b> to disable read-ahead, <b>FALSE</b> to enable it. The caller must specify a value for <i>DisableReadAhead</i> in each call to <b>CcSetAdditionalCacheAttributes</b>, even if a value was already specified in a previous call.</p>
</dd>

### -param <i>DisableWriteBehind</i> [in]

<dd>
<p>Set to <b>TRUE</b> to disable write-behind, <b>FALSE</b> to enable it. The caller must specify a value for <i>DisableWriteBehind</i> in each call to <b>CcSetAdditionalCacheAttributes</b>, even if a value was already specified in a previous call.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>CcSetAdditionalCacheAttributes</b> can be called any time after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>. Initially, both read-ahead and write-behind are enabled.</p>

<p><b>CcSetAdditionalCacheAttributes</b> can be called any time after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>. Initially, both read-ahead and write-behind are enabled.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539135">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539191">CcReadAhead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539224">CcSetReadAheadGranularity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcSetAdditionalCacheAttributes routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
