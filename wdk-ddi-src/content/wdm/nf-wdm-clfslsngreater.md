---
UID: NF.wdm.ClfsLsnGreater
title: ClfsLsnGreater
author: windows-driver-content
description: The ClfsLsnGreater routine determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream.
old-location: kernel\clfslsngreater.htm
old-project: kernel
ms.assetid: 77ad073e-5dac-4d89-869e-547e1aec25da
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ClfsLsnGreater
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsLsnGreater
req.alt-loc: Clfs.sys,Ext-MS-Win-fs-clfs-l1-1-0.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Clfs.lib
req.dll: Clfs.sys
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# ClfsLsnGreater function



## -description
<p>The <b>ClfsLsnGreater</b> routine determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream.</p>


## -syntax

````
BOOLEAN ClfsLsnGreater(
  _In_ const CLFS_LSN *plsn1,
  _In_ const CLFS_LSN *plsn2
);
````


## -parameters
<dl>

### -param <i>plsn1</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that supplies one of the LSNs to be compared.</p>
</dd>

### -param <i>plsn2</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824">CLFS_LSN</a> structure that supplies the other LSN to be compared.</p>
</dd>
</dl>

## -returns
<p><b>ClfsLsnGreater</b> returns <b>TRUE</b> if <i>plsn1</i> is strictly greater than <i>plsn2</i>; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>CLFS_LSN_NULL (the smallest LSN) and CLFS_LSN_INVALID (larger than any valid LSN) are valid arguments to <b>ClfsLsnGreater</b>.</p>

<p>LSNs from different streams are not comparable. Do not use <a href="https://msdn.microsoft.com/library/windows/hardware/ff541590">ClfsLsnEqual</a>, <b>ClfsLsnGreater</b>, and the like to compare LSNs from different streams.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

<p>CLFS_LSN_NULL (the smallest LSN) and CLFS_LSN_INVALID (larger than any valid LSN) are valid arguments to <b>ClfsLsnGreater</b>.</p>

<p>LSNs from different streams are not comparable. Do not use <a href="https://msdn.microsoft.com/library/windows/hardware/ff541590">ClfsLsnEqual</a>, <b>ClfsLsnGreater</b>, and the like to compare LSNs from different streams.</p>

<p>For an explanation of CLFS concepts and terminology, see <a href="https://msdn.microsoft.com/a9685648-b08c-48ca-b020-e683068f2ea2">Common Log File System</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Clfs.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541590">ClfsLsnEqual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541608">ClfsLsnLess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541609">ClfsLsnNull</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsLsnGreater routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
