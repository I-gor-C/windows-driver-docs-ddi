---
UID: NE.wdm._TRANSACTION_OUTCOME
title: TRANSACTION_OUTCOME
author: windows-driver-content
description: The TRANSACTION_OUTCOME enumeration defines the outcomes (results) that KTM can assign to a transaction.
old-location: kernel\transaction_outcome.htm
old-project: kernel
ms.assetid: 1612e8d8-996b-45d2-93cc-df5b388596d4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSACTION_OUTCOME
req.alt-loc: Wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# TRANSACTION_OUTCOME enumeration



## -description
<p>The <b>TRANSACTION_OUTCOME</b> enumeration defines the outcomes (results) that KTM can assign to a transaction.</p>


## -syntax

````
typedef enum _TRANSACTION_OUTCOME { 
  TransactionOutcomeUndetermined  = 1,
  TransactionOutcomeCommitted     = 2,
  TransactionOutcomeAborted       = 3
} TRANSACTION_OUTCOME;
````


## -enum-fields
<dl>

### -field TransactionOutcomeUndetermined

<dd>
<p>The transaction has not yet been committed or rolled back.</p>
</dd>

### -field TransactionOutcomeCommitted

<dd>
<p>The transaction has been committed.</p>
</dd>

### -field TransactionOutcomeAborted

<dd>
<p>The transaction has been rolled back.</p>
</dd>
</dl>

## -remarks
<p>The <b>TRANSACTION_OUTCOME</b> enumeration is used in the <a href="..\wdm\ns-wdm--transaction-basic-information.md">TRANSACTION_BASIC_INFORMATION</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later operating system versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--transaction-basic-information.md">TRANSACTION_BASIC_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTION_OUTCOME enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
