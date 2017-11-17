---
UID: NS.ntddk._TXN_PARAMETER_BLOCK
title: TXN_PARAMETER_BLOCK
author: windows-driver-content
description: The TXN_PARAMETER_BLOCK structure contains information about a transacted file operation.
old-location: ifsk\txn_parameter_block.htm
ms.assetid: 973f440a-ba17-466a-a9f4-f21c07e854d8
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: The TXN_PARAMETER_BLOCK structure is available on Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TXN_PARAMETER_BLOCK
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: TXN_PARAMETER_BLOCK, TXN_PARAMETER_BLOCK, *PTXN_PARAMETER_BLOCK
req.iface: 
---

# TXN_PARAMETER_BLOCK structure



## -description
<p>The TXN_PARAMETER_BLOCK structure contains information about a transacted file operation. </p>


## -syntax

````
typedef struct _TXN_PARAMETER_BLOCK {
  USHORT Length;
  USHORT TxFsContext;
  PVOID  TransactionObject;
} TXN_PARAMETER_BLOCK, *PTXN_PARAMETER_BLOCK;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The size, in bytes, of the TXN_PARAMETER_BLOCK structure. </p>
</dd>

### -field <b>TxFsContext</b>

<dd>
<p>The miniversion ID for the file. </p>
</dd>

### -field <b>TransactionObject</b>

<dd>
<p>An opaque pointer to the transaction object for the transaction. </p>
</dd>
</dl>

## -remarks
<p>A <i>miniversion</i> is a version of a file that a transacted writer creates during a transaction. (A <i>transacted writer</i> is a transacted file handle opened with any permission that is not part of generic read access, but is part of generic write access.) </p>

<p>If a specific miniversion number for the file is not provided, the <b>TxFsContext</b> member must be set to TXF_MINIVERSION_DEFAULT_VIEW.</p>

<p>The <b>TxFsContext</b> member of the <b>TXN_PARAMETER_BLOCK</b> uses TXF_MINIVERSION_DEFAULT_VIEW to get the default view of the requested file that is based on the value of the <b>TransactionObject</b> member.  So if <b>TransactionObject</b> is the same transaction that has the requested file locked for transacted modification, the caller can see those modifications (the "dirty" view of the file) if the caller can specify the value of the <b>TransactionObject</b> member.  If <b>TransactionObject</b> is not the same transaction that has the requested file locked for transacted modification, the caller gets a transactionally isolated view of the file if it specifies this value.  </p>

<p>A miniversion exists only as a point-in-time view of a file and has not yet been written as an actual on-disk variant of a given file.  A transacted writer creates a miniversion by using the <a href="http://go.microsoft.com/fwlink/p/?linkid=139790">FSCTL_TXFS_CREATE_MINIVERSION</a> control code to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff566462">ZwFsControlFile</a>.  In response, the system creates a miniversion and returns its miniversion ID.  The transacted writer can continue to make changes to the file thereafter.  If the file is opened later by using the returned miniversion ID as the <b>TxFsContext</b> member of the <b>TXN_PARAMETER_BLOCK</b> structure, the resulting file handle shows the file as it was at the time that miniversion was created.</p>

<p>All miniversions created in a transaction go away when the transaction ends.  Afterwards, the file can no longer be opened by using the miniversion IDs.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff548412">IoGetTransactionParameterBlock</a> routine returns a pointer to this structure. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>The TXN_PARAMETER_BLOCK structure is available on Windows Vista and later Windows operating systems. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h, Ntifs.h, or FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548412">IoGetTransactionParameterBlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566462">ZwFsControlFile</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=139790">FSCTL_TXFS_CREATE_MINIVERSION</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20TXN_PARAMETER_BLOCK structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
