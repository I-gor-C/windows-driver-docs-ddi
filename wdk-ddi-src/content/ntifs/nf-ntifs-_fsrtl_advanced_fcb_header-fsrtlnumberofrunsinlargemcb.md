---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlNumberOfRunsInLargeMcb
title: FsRtlNumberOfRunsInLargeMcb function
author: windows-driver-content
description: The FsRtlNumberOfRunsInLargeMcb routine returns the number of runs in a map control block (MCB).
old-location: ifsk\fsrtlnumberofrunsinlargemcb.htm
old-project: ifsk
ms.assetid: a0722e8c-224c-4710-8cd1-68f9bd3051db
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlNumberOfRunsInLargeMcb
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
req.alt-api: FsRtlNumberOfRunsInLargeMcb
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
---

# FsRtlNumberOfRunsInLargeMcb function



## -description
The <b>FsRtlNumberOfRunsInLargeMcb</b> routine returns the number of runs in a map control block (MCB).


## -syntax

````
ULONG FsRtlNumberOfRunsInLargeMcb(
  _In_ PLARGE_MCB OpaqueMcb
);
````


## -parameters

### -param OpaqueMcb [in]

Supplies the MCB being examined.

## -returns
Returns the number of distinct runs mapped by the input MCB.

## -remarks
<b>FsRtlNumberOfRunsInLargeMcb</b> returns the number of distinct runs mapped by an MCB. 

Runs can be mappings or holes. A <i>mapping</i> is a continuous range of VBNs that is mapped to a corresponding range of logical block numbers (LBN). Mappings cannot overlap. A <i>hole</i> is a continuous range of unmapped VBNs that falls between two mappings. Within the entire range of mapped VBNs, every VBN belongs to exactly one mapping or hole.

<b>FsRtlNumberOfRunsInLargeMcb</b> counts both types of runs. For example, an MCB containing a mapping for only VBNs zero and three will have three runs: one for VBN 0, one for the hole covering VBN 1 and VBN 2, and one for VBN 3.

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
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= APC_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtladdlargemcbentry">FsRtlAddLargeMcbEntry</a>
</dt>
<dt>
<a href="ifsk.fsrtlgetnextlargemcbentry">FsRtlGetNextLargeMcbEntry</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializelargemcb">FsRtlInitializeLargeMcb</a>
</dt>
<dt>
<a href="ifsk.fsrtllookuplargemcbentry">FsRtlLookupLargeMcbEntry</a>
</dt>
<dt>
<a href="ifsk.fsrtllookuplastlargemcbentry">FsRtlLookupLastLargeMcbEntry</a>
</dt>
<dt>
<a href="ifsk.fsrtllookuplastlargemcbentryandindex">FsRtlLookupLastLargeMcbEntryAndIndex</a>
</dt>
<dt>
<a href="ifsk.fsrtlremovelargemcbentry">FsRtlRemoveLargeMcbEntry</a>
</dt>
<dt>
<a href="ifsk.fsrtlsplitlargemcb">FsRtlSplitLargeMcb</a>
</dt>
<dt>
<a href="ifsk.fsrtltruncatelargemcb">FsRtlTruncateLargeMcb</a>
</dt>
<dt>
<a href="ifsk.fsrtluninitializelargemcb">FsRtlUninitializeLargeMcb</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlNumberOfRunsInLargeMcb routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
