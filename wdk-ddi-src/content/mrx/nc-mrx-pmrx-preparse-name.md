---
UID: NC.mrx.PMRX_PREPARSE_NAME
title: PMRX_PREPARSE_NAME
author: windows-driver-content
description: The MRxPreparseName routine is called by RDBSS to give a network mini-redirector the opportunity to preparse a name.
old-location: ifsk\mrxpreparsename.htm
old-project: ifsk
ms.assetid: b74acc12-8fc2-497f-9f65-8b1a85a03286
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
req.alt-api: MRxPreparseName
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

# PMRX_PREPARSE_NAME callback



## -description
<p>The<i> MRxPreparseName</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to give a network mini-redirector the opportunity to preparse a name. </p>


## -prototype

````
PMRX_PREPARSE_NAME MRxPreparseName;

NTSTATUS MRxPreparseName(
  _Inout_ PRX_CONTEXT     RxContext,
  _In_    PUNICODE_STRING Name
)
{ ... }
````


## -parameters
<dl>

### -param <i>RxContext</i> [in, out]

<dd>
<p>A pointer to the RX_CONTEXT structure. This parameter contains the IRP that is requesting the operation. </p>
</dd>

### -param <i>Name</i> [in]

<dd>
<p>A pointer to a Unicode string that contains the name string.</p>
</dd>
</dl>

## -returns
<p><i>MRxPreparseName</i> returns STATUS_SUCCESS on success. </p>

## -remarks
<p><i>MRxPreparseName</i> is called by RDBSS after parsing a name to give a network mini-redirector a final opportunity to preparse the name. </p>

<p>RDBSS tries to convert the name to its canonical form, removing a dot (".") and two dots (".."), before calling <i>MRxPreparseName</i>. RDBSS will also parse the format used by NTFS streams. </p>

<p>RDBSS ignores the return value from <i>MRxPreparseName</i>. </p>

<p><i>MRxPreparseName</i> is called by RDBSS after parsing a name to give a network mini-redirector a final opportunity to preparse the name. </p>

<p>RDBSS tries to convert the name to its canonical form, removing a dot (".") and two dots (".."), before calling <i>MRxPreparseName</i>. RDBSS will also parse the format used by NTFS streams. </p>

<p>RDBSS ignores the return value from <i>MRxPreparseName</i>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549864">MRxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549869">MRxCreateVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550649">MRxExtractNetRootName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550653">MRxFinalizeNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550663">MRxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554426">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550824">MRxSrvCallWinnerNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxPreparseName routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
