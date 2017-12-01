---
UID: NF.wdm.TmRenameTransactionManager
title: TmRenameTransactionManager
author: windows-driver-content
description: The TmRenameTransactionManager routine changes the identity of the transaction manager object that is stored in the CLFS log file stream contained in the log file name.
old-location: kernel\tmrenametransactionmanager_.htm
old-project: kernel
ms.assetid: B4124FF4-50CC-474A-B42F-17BCF698AB59
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TmRenameTransactionManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TmRenameTransactionManager
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# TmRenameTransactionManager function



## -description
<p>The <b>TmRenameTransactionManager</b> routine changes the identity of the transaction manager object that is stored in the <a href="https://msdn.microsoft.com/4da3cb49-dc20-4713-813b-ff458c99ab90">CLFS</a> log file stream contained in the log file name.</p>


## -syntax

````
NTSTATUS TmRenameTransactionManager (
  _In_ PUNICODE_STRING  LogFileName,
  _In_ LPGUID           ExistingTransactionManagerGuid
);
````


## -parameters
<dl>

### -param <i>LogFileName</i> [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the path and file name of a <a href="https://msdn.microsoft.com/4da3cb49-dc20-4713-813b-ff458c99ab90">CLFS</a> log file stream to be associated with the transaction manager object.</p>
</dd>

### -param <i>ExistingTransactionManagerGuid</i> [in]

<dd>
<p>A pointer to a GUID structure that represents the current name of the transaction manager object.</p>
</dd>
</dl>

## -returns
<p>The <b>TmRenameTransactionManager</b> routine returns an NTSTATUS value. If the routine fails, it returns one of the following error codes:</p><dl>
<dd>ERROR_ACCESS_DENIED</dd>
<dd>ERROR_INVALID_HANDLE</dd>
<dd>ERROR_INSUFFICIENT_RESOURCES</dd>
<dd>ERROR_OBJECT_NAME_NOT_FOUND</dd>
<dd>ERROR_OBJECT_TYPE_MISMATCH</dd>
</dl>

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
<p>Available starting with Windows Vista.</p>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>