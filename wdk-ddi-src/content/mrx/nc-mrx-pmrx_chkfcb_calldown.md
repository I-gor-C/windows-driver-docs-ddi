---
UID: NC.mrx.PMRX_CHKFCB_CALLDOWN
title: PMRX_CHKFCB_CALLDOWN
author: windows-driver-content
description: The MRxAreFilesAliased routine is called by RDBSS to request the network mini-redirector to determine if two FCB structures represent the same file.
old-location: ifsk\mrxarefilesaliased.htm
old-project: ifsk
ms.assetid: 273266b3-98f4-4c93-a06b-8e149440ad24
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _SetDSMCounters_IN, *PSetDSMCounters_IN, SetDSMCounters_IN, PSetDSMCounters_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MRxAreFilesAliased
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# PMRX_CHKFCB_CALLDOWN callback



## -description
The<b> MRxAreFilesAliased</b> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request the network mini-redirector to determine if two FCB structures represent the same file. 



## -prototype

````
PMRX_CHKFCB_CALLDOWN MRxAreFilesAliased;

NTSTATUS MRxAreFilesAliased(
  _In_ PFCB Fcb1,
  _In_ PFCB Fcb2
)
{ ... }
````


## -parameters

### -param Fcb1 [in]

A pointer to the first FCB structure. 


### -param Fcb2 [in]

A pointer to the second FCB structure.


## -returns
<b>MRxAreFilesAliased</b> returns STATUS_SUCCESS indicating that the files are not aliased, or an appropriate NTSTATUS value, such as the following: 
<dl>
<dt><b>STATUS_MORE_PROCESSING_REQUIRED</b></dt>
</dl>The <b>IndexNumber.QuadPart</b> members of the two FCB structures are identical. This value indicates that the two files that are being compared are aliases.

 


## -remarks
RDBSS calls this routine when processing two files that appear to be the same but have different names (for example, an MS-DOS short name and a long name).

<b>MRxAreFilesAliased</b> is called by the <a href="ifsk.rxpurgerelatedfobxs">RxPurgeRelatedFobxs</a> routine when purging all the structures of an FOBX structure associated with a NET_ROOT structure. As part of this process, an attempt is made to purge all the FOBX structures that had a close pending before the purge request was received. RDBSS needs to scavenge any temporary FOBX structures in the following cases: 

The <i>PurgingFcb</i> parameter that is passed to the <a href="ifsk.rxpurgerelatedfobxs">RxPurgeRelatedFobxs</a> routine is the FCB structure for which the scavenging should occur. When this parameter is a directory, RDBSS needs to ensure that files that can potentially be in that directory are closed.

The FCB structure that is associated with the FOBX structure on the <b>FobxsToBeFinalized</b> member of the RDBSS_SCAVENGER structure doesn't point to the same FCB structure as the <i>PurgingFCB</i> parameter passed to <a href="ifsk.rxpurgerelatedfobxs">RxPurgeRelatedFobxs</a>. This is complicated by the fact that they might not be the same FCB structures, but are actually the same file because of aliasing. In this case, the <b>MRxAreFilesAliased</b> routine is called to determine if the FCB structure is aliased.

<b>MRxAreFilesAliased</b> is also called by the <a href="ifsk.rxscavengefobxsfornetroot">RxScavengeFobxsForNetRoot</a> routine when purging all the file objects associated with a NET_ROOT structure. This is complicated by the fact that the <i>PurgingFCB</i> parameter passed to <b>RxScavengeFobxsForNetRoot</b> and the FCB structure that is associated with the NET_ROOT structure might actually be the same file because of aliasing. In this case, the <b>MRxAreFilesAliased</b> routine is called to determine if the FCB structure is aliased.  


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mrx.h (include Mrx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.mrxcleanupfobx">MRxCleanupFobx</a>
</dt>
<dt>
<a href="ifsk.mrxclosesrvopen">MRxCloseSrvOpen</a>
</dt>
<dt>
<a href="ifsk.mrxcollapseopen">MRxCollapseOpen</a>
</dt>
<dt>
<a href="ifsk.mrxcreate">MRxCreate</a>
</dt>
<dt>
<a href="ifsk.mrxdeallocateforfcb">MRxDeallocateForFcb</a>
</dt>
<dt>
<a href="ifsk.mrxdeallocateforfobx">MRxDeallocateForFobx</a>
</dt>
<dt>
<a href="ifsk.mrxextendforcache">MRxExtendForCache</a>
</dt>
<dt>
<a href="ifsk.mrxextendfornoncache">MRxExtendForNonCache</a>
</dt>
<dt>
<a href="ifsk.mrxflush">MRxFlush</a>
</dt>
<dt>
<a href="ifsk.mrxforceclosed">MRxForceClosed</a>
</dt>
<dt>
<a href="ifsk.mrxislockrealizable">MRxIsLockRealizable</a>
</dt>
<dt>
<a href="ifsk.mrxshouldtrytocollapsethisopen">MRxShouldTryToCollapseThisOpen</a>
</dt>
<dt>
<a href="ifsk.mrxtruncate">MRxTruncate</a>
</dt>
<dt>
<a href="ifsk.mrxzeroextend">MRxZeroExtend</a>
</dt>
<dt>
<a href="ifsk.rxpurgerelatedfobxs">RxPurgeRelatedFobxs</a>
</dt>
<dt>
<a href="ifsk.rxscavengefobxsfornetroot">RxScavengeFobxsForNetRoot</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxAreFilesAliased routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

