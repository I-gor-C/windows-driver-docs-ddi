---
UID: NC.mrx.PMRX_EXTRACT_NETROOT_NAME
title: PMRX_EXTRACT_NETROOT_NAME
author: windows-driver-content
description: The MRxExtractNetRootName routine is called by RDBSS to request that a network mini-redirector extract the name of the NET_ROOT structure from a given pathname.
old-location: ifsk\mrxextractnetrootname.htm
old-project: ifsk
ms.assetid: e990b7fc-a341-419d-b358-eac4fa2dca78
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
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
req.alt-api: MRxExtractNetRootName
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
req.iface: 
---

# PMRX_EXTRACT_NETROOT_NAME callback



## -description
<p>The<i> MRxExtractNetRootName</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request that a network mini-redirector extract the name of the NET_ROOT structure from a given pathname. </p>


## -prototype

````
PMRX_EXTRACT_NETROOT_NAME MRxExtractNetRootName;

VOID MRxExtractNetRootName(
  _In_      PUNICODE_STRING FilePathName,
  _In_      PMRX_SRV_CALL   SrvCall,
  _Out_     PUNICODE_STRING NetRootName,
  _Out_opt_ PUNICODE_STRING RestOfName
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilePathName</i> [in]

<dd>
<p>A pointer to a Unicode string that contains a pathname. </p>
</dd>

### -param <i>SrvCall</i> [in]

<dd>
<p>A pointer to the SRV_CALL structure. </p>
</dd>

### -param <i>NetRootName</i> [out]

<dd>
<p>On input, a pointer for storing a Unicode string. On success, this parameter will contain a pointer to a Unicode string that contains a NET_ROOT structure name. </p>
</dd>

### -param <i>RestOfName</i> [out, optional]

<dd>
<p>A pointer to a Unicode string that contains the rest of the name on success. This parameter is optional and can be a <b>NULL</b> pointer on input.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>MRxExtractNetRootName</i> parses the input name into the SRV_CALL structure, the NET_ROOT structure, and the rest of the pathname.</p>

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
<p>Header</p>
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
<a href="ifsk.mrxcreatesrvcall">MRxCreateSrvCall</a>
</dt>
<dt>
<a href="ifsk.mrxcreatevnetroot">MRxCreateVNetRoot</a>
</dt>
<dt>
<a href="ifsk.mrxfinalizenetroot">MRxFinalizeNetRoot</a>
</dt>
<dt>
<a href="ifsk.mrxfinalizesrvcall">MRxFinalizeSrvCall</a>
</dt>
<dt>
<a href="ifsk.mrxfinalizevnetroot">MRxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="ifsk.mrxpreparsename">MRxPreparseName</a>
</dt>
<dt>
<a href="ifsk.mrxsrvcallwinnernotify">MRxSrvCallWinnerNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxExtractNetRootName routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
