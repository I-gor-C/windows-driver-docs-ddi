---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlLookupLastLargeMcbEntryAndIndex~r3
title: FsRtlLookupLastLargeMcbEntryAndIndex function
author: windows-driver-content
description: The FsRtlLookupLastLargeMcbEntryAndIndex routine retrieves the last mapping entry stored in a given map control block (MCB).
old-location: ifsk\fsrtllookuplastlargemcbentryandindex.htm
old-project: ifsk
ms.assetid: 53c3109d-16e4-4db4-9c62-27c6d8501707
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlLookupLastLargeMcbEntryAndIndex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlLookupLastLargeMcbEntryAndIndex
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

# FsRtlLookupLastLargeMcbEntryAndIndex function



## -description
The <b>FsRtlLookupLastLargeMcbEntryAndIndex</b> routine retrieves the last mapping entry stored in a given map control block (MCB). 



## -syntax

````
BOOLEAN FsRtlLookupLastLargeMcbEntryAndIndex(
  _In_  PLARGE_MCB OpaqueMcb,
  _Out_ PLONGLONG  LargeVbn,
  _Out_ PLONGLONG  LargeLbn,
  _Out_ PULONG     Index
);
````


## -parameters

### -param OpaqueMcb [in]

Pointer to an initialized MCB structure to be searched. 


### -param LargeVbn [out]

Pointer to a variable that receives the last virtual block number (VBN) that was mapped. 


### -param LargeLbn [out]

Pointer to a variable that receives the logical block number (LBN) that is mapped to the VBN pointed to by <i>LargeVbn</i>, or -1 if no such LBN exists. 


### -param Index [out]

Pointer to a variable that receives the index of the last run in the MCB. 


## -returns
<b>FsRtlLookupLastLargeMcbEntryAndIndex </b>returns <b>FALSE</b> if the MCB contains no mapping entries, <b>TRUE</b> otherwise. 


## -remarks
<b>FsRtlLookupLastLargeMcbEntryAndIndex </b>searches for the last mapping of the last run in the MCB: 

If the MCB contains no mappings, <b>FsRtlLookupLastLargeMcbEntryAndIndex </b>returns <b>FALSE</b>. 

If the last mapping is a hole, <b>FsRtlLookupLastLargeMcbEntryAndIndex </b>returns <b>TRUE</b>, but the lookup operation yields a value of -1 for the LBN. 

If the last mapping is not a hole, the lookup operation yields a positive value for the LBN, and <b>FsRtlLookupLastLargeMcbEntryAndIndex </b>returns <b>TRUE</b>. 


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
This routine is available on Microsoft Windows XP and later. 

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
<a href="ifsk.fsrtlnumberofrunsinlargemcb">FsRtlNumberOfRunsInLargeMcb</a>
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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlLookupLastLargeMcbEntryAndIndex routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

