---
UID: NF.wdm.ClfsMgmtTailAdvanceFailure
title: ClfsMgmtTailAdvanceFailure
author: windows-driver-content
description: The ClfsMgmtTailAdvanceFailure routine notifies CLFS management that the client could not advance the log's tail.
old-location: kernel\clfsmgmttailadvancefailure.htm
ms.assetid: 21a2f593-716a-434a-922c-23544ddb0122
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 R2, Windows Vista, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClfsMgmtTailAdvanceFailure
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
req.irql: <= APC_LEVEL
ms.keywords: ClfsMgmtTailAdvanceFailure
req.iface: 
req.product: Windows 10 or later.
---

# ClfsMgmtTailAdvanceFailure function



## -description
<p>The <b>ClfsMgmtTailAdvanceFailure</b> routine notifies CLFS management that the client could not advance the log's tail.</p>


## -syntax

````
NTSTATUS ClfsMgmtTailAdvanceFailure(
  _In_ CLFS_MGMT_CLIENT Client,
  _In_ NTSTATUS         Reason
);
````


## -parameters
<dl>

### -param <i>Client</i> [in]

<dd>
<p>A pointer to the client. This is the value that was obtained through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541642">ClfsMgmtRegisterManagedClient</a> routine.</p>
</dd>

### -param <i>Reason</i> [in]

<dd>
<p>A value that indicates why the log's tail could not be advanced. </p>
</dd>
</dl>

## -returns
<p>The <b>ClfsMgmtTailAdvanceFailure</b> routine returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>CLFS management has processed the notification that the log's tail could not be advanced.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A <b>NULL</b> value was supplied for the <i>Client</i> parameter.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The value that  was supplied for the <i>Client</i> parameter does not represent a valid client.</p>

<p> </p>

## -remarks
<p>If a client cannot advance its log's tail to or beyond the requested LSN, then the client must call the <b>ClfsMgmtTailAdvanceFailure</b> routine to indicate that it is not able to advance its tail. Until the client either moves its tail as requested or calls the <b>ClfsMgmtTailAdvanceFailure</b> routine, the client will not receive any further requests to move its tail.</p>

<p>The value of the <i>Reason</i> parameter is passed back to the client as the value of the <i>OperationStatus</i> parameter when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541562">ClfsLogGrowthCompleteCallback</a> function is invoked.</p>

<p>If a client cannot advance its log's tail to or beyond the requested LSN, then the client must call the <b>ClfsMgmtTailAdvanceFailure</b> routine to indicate that it is not able to advance its tail. Until the client either moves its tail as requested or calls the <b>ClfsMgmtTailAdvanceFailure</b> routine, the client will not receive any further requests to move its tail.</p>

<p>The value of the <i>Reason</i> parameter is passed back to the client as the value of the <i>OperationStatus</i> parameter when the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541562">ClfsLogGrowthCompleteCallback</a> function is invoked.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541642">ClfsMgmtRegisterManagedClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ClfsMgmtTailAdvanceFailure routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
