---
UID: NF.wdm.TmInitializeTransactionManager
title: TmInitializeTransactionManager
author: windows-driver-content
description: The TmInitializeTransactionManager routine initializes a transaction manager object.
old-location: kernel\tminitializetransactionmanager_.htm
old-project: kernel
ms.assetid: A44B4B93-4EC7-4FC3-B64F-BF1FF19D067E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TmInitializeTransactionManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TmInitializeTransactionManager
req.alt-loc: Wdm.h,Ext-MS-Win-ntos-tm-l1-1-0.dll,tm.sys
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
req.product: Windows 10 or later.
---

# TmInitializeTransactionManager function



## -description
<p>The <b>TmInitializeTransactionManager</b> routine initializes a transaction manager object.</p>


## -syntax

````
NTSTATUS TmInitializeTransactionManager (
  _In_     PRKTM             TransactionManager,
  _In_opt_ PCUNICODE_STRING  LogFileName,
  _In_     PGUID             TmId,
  _In_opt_ ULONG             CreateOptions
);
````


## -parameters
<dl>

### -param TransactionManager [in]

<dd>
<p>A pointer to the transaction manager object to initialize.</p>
</dd>

### -param LogFileName [in, optional]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the path and file name of a <a href="https://msdn.microsoft.com/4da3cb49-dc20-4713-813b-ff458c99ab90">CLFS</a> log file stream associated with the transaction manager object. </p>
</dd>

### -param TmId [in]

<dd>
<p>Specifies a pointer to a GUID that identifies  the name of the transaction manager object to initialize.</p>
</dd>

### -param CreateOptions [in, optional]

<dd>
<p>Optional object creation flags. The following table contains the available flags.</p>
<table>
<tr>
<th>Option flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_VOLATILE</p>
</td>
<td>
<p>The transaction manager object will be volatile. Therefore, it will not use a log file.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_DEFAULT</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_COMMIT_LOWEST</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
<tr>
<td>
<p>TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS</p>
</td>
<td>
<p>For internal use only.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The <b>TmInitializeTransactionManager</b> routine  returns STATUS_SUCCESS if the operation succeeds.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>