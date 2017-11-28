---
UID: NF.wdm.NtSetInformationTransactionManager
title: NtSetInformationTransactionManager
author: windows-driver-content
description: Do not call this routine from kernel-mode code.
old-location: kernel\ntsetinformationtransactionmanager.htm
old-project: kernel
ms.assetid: a1e2f40f-5aea-4c8b-8692-95721ad4bc9d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NtSetInformationTransactionManager
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NtSetInformationTransactionManager
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# NtSetInformationTransactionManager function



## -description
<p>Do not call this routine from kernel-mode code.</p>


## -syntax

````
NTSTATUS NtSetInformationTransactionManager(
  _In_opt_ HANDLE                                                   TmHandle,
  _In_     TRANSACTIONMANAGER_INFORMATION_CLASS                     TransactionManagerInformationClass,
  _In_     _reads_bytes_(TransactionManagerInformationLength) PVOID TransactionManagerInformation,
  _In_     ULONG                                                    TransactionManagerInformationLength
);
````


## -parameters
<dl>

### -param <i>TmHandle</i> [in, optional]

<dd></dd>

### -param <i>TransactionManagerInformationClass</i> [in]

<dd></dd>

### -param <i>TransactionManagerInformation</i> [in]

<dd></dd>

### -param <i>TransactionManagerInformationLength</i> [in]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
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
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>