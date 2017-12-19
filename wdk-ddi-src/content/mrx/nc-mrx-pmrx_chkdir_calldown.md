---
UID: NC.mrx.PMRX_CHKDIR_CALLDOWN
title: PMRX_CHKDIR_CALLDOWN
author: windows-driver-content
description: TheMRxIsValidDirectory routine is called by RDBSS to request that a network mini-redirector check for the existence of a remote directory.
old-location: ifsk\mrxisvaliddirectory.htm
old-project: ifsk
ms.assetid: c52441d8-b273-4e1f-b251-2b35afeda55d
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
req.alt-api: MRxIsValidDirectory
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

# PMRX_CHKDIR_CALLDOWN callback



## -description
The<i>MRxIsValidDirectory</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request that a network mini-redirector check for the existence of a remote directory. 



## -prototype

````
PMRX_CHKDIR_CALLDOWN MRxIsValidDirectory;

NTSTATUS MRxIsValidDirectory(
  _Inout_ PRX_CONTEXT     RxContext,
  _In_    PUNICODE_STRING DirectoryName
)
{ ... }
````


## -parameters

### -param RxContext [in, out]

A pointer to the RX_CONTEXT structure. This parameter contains the IRP that is requesting the operation. 


### -param DirectoryName [in]

A pointer to a Unicode string that contains the name of the remote directory.


## -returns
<i>MRxIsValidDirectory</i> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as the following: 
<dl>
<dt><b>STATUS_BAD_NETWORK_PATH</b></dt>
</dl>This remote directory does not exist. 

 


## -remarks
<i>MRxIsValidDirectory</i> is called as part of create or open request processing for the remaining name string beyond the V_NET_ROOT structure, if the <b>IrpSp-&gt;Parameters.Create.Options</b> member has the FILE_CREATE_TREE_CONNECTION bit set on. 


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
<a href="ifsk.mrxquerydirectory">MRxQueryDirectory</a>
</dt>
<dt>
<a href="ifsk.mrxqueryeainfo">MRxQueryEaInfo</a>
</dt>
<dt>
<a href="ifsk.mrxqueryfileinfo">MRxQueryFileInfo</a>
</dt>
<dt>
<a href="ifsk.mrxqueryquotainfo">MRxQueryQuotaInfo</a>
</dt>
<dt>
<a href="ifsk.mrxquerysdinfo">MRxQuerySdInfo</a>
</dt>
<dt>
<a href="ifsk.mrxqueryvolumeinfo">MRxQueryVolumeInfo</a>
</dt>
<dt>
<a href="ifsk.mrxseteainfo">MRxSetEaInfo</a>
</dt>
<dt>
<a href="ifsk.mrxsetfileinfo">MRxSetFileInfo</a>
</dt>
<dt>
<a href="ifsk.mrxsetfileinfoatcleanup">MRxSetFileInfoAtCleanup</a>
</dt>
<dt>
<a href="ifsk.mrxsetquotainfo">MRxSetQuotaInfo</a>
</dt>
<dt>
<a href="ifsk.mrxsetsdinfo">MRxSetSdInfo</a>
</dt>
<dt>
<a href="ifsk.mrxsetvolumeinfo">MRxSetVolumeInfo</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxIsValidDirectory routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

