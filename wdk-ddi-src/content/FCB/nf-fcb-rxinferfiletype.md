---
UID: NF.fcb.RxInferFileType
title: RxInferFileType
author: windows-driver-content
description: RxInferFileType tries to infer the file type (directory or non-directory) from a member in the RX_CONTEXT structure.
old-location: ifsk\rxinferfiletype.htm
ms.assetid: 340b304c-5484-4d98-9ef4-8814c68443a0
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fcb.h
req.include-header: Rxcontx.h, Nodetype.h, Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxInferFileType
req.alt-loc: fcb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: RxInferFileType
req.iface: 
---

# RxInferFileType function



## -description
<p><b>RxInferFileType</b> tries to infer the file type (directory or non-directory) from a member in the RX_CONTEXT structure.</p>


## -syntax

````
RX_FILE_TYPE RxInferFileType(
  _In_ PRX_CONTEXT RxContext
);
````


## -parameters
<dl>

### -param <i>RxContext</i> [in]

<dd>
<p>A pointer to the RX_CONTEXT structure.</p>
</dd>
</dl>

## -returns
<p><b>RxInferFileType </b>returns the storage type implied by the open. </p><dl>
<dt><b>FileTypeDirectory</b></dt>
</dl><p>The file type is a directory.</p><dl>
<dt><b>FileTypeFile</b></dt>
</dl><p>The file type is a file.</p><dl>
<dt><b>FileTypeNotYetKnown</b></dt>
</dl><p>The file type could not be determined. </p>

<p>If RxInferFileType cannot determine the file type, this routine returns this value.</p>

<p> </p>

## -remarks
<p><b>RxInferFileType</b> tries to infer the file type (directory or non-directory) from the <b>Create.NtCreateParameters.CreateOptions</b> member in the RX_CONTEXT structure.</p>

<p>The <b>RxInferFileType</b> routine is not called internally by RDBSS. The <b>RxInferFileType</b> routine might be used as a helper routine by a network mini-redirector driver in the <b>MRxCreate</b> routine provided by the network mini-redirector. <b>MRxCreate</b> would normally be called when an I/O request packet is received for IRP_MJ_CREATE. This IRP is normally received by RDBSS in response to a user-mode application requesting a file open or create operation. It is also possible for another kernel driver to issue such an IRP. </p>

<p><b>RxInferFileType</b> tries to infer the file type (directory or non-directory) from the <b>Create.NtCreateParameters.CreateOptions</b> member in the RX_CONTEXT structure.</p>

<p>The <b>RxInferFileType</b> routine is not called internally by RDBSS. The <b>RxInferFileType</b> routine might be used as a helper routine by a network mini-redirector driver in the <b>MRxCreate</b> routine provided by the network mini-redirector. <b>MRxCreate</b> would normally be called when an I/O request packet is received for IRP_MJ_CREATE. This IRP is normally received by RDBSS in response to a user-mode application requesting a file open or create operation. It is also possible for another kernel driver to issue such an IRP. </p>

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
<dt>Fcb.h (include Rxcontx.h, Nodetype.h, Mrxfcb.h, or Fcb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549862">MRxCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554751">RX_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxInferFileType function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
