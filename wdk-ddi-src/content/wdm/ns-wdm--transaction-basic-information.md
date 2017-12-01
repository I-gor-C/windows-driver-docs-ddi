---
UID: NS.wdm._TRANSACTION_BASIC_INFORMATION
title: TRANSACTION_BASIC_INFORMATION
author: windows-driver-content
description: The TRANSACTION_BASIC_INFORMATION structure contains information about a transaction object.
old-location: kernel\transaction_basic_information.htm
old-project: kernel
ms.assetid: 79dd9ff3-2a5f-457a-8a8a-4963a799055c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TRANSACTION_BASIC_INFORMATION, TRANSACTION_BASIC_INFORMATION, *PTRANSACTION_BASIC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later operating system versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSACTION_BASIC_INFORMATION
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# TRANSACTION_BASIC_INFORMATION structure



## -description
<p>The <b>TRANSACTION_BASIC_INFORMATION</b> structure contains information about a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a>.</p>


## -syntax

````
typedef struct _TRANSACTION_BASIC_INFORMATION {
  GUID  TransactionId;
  ULONG State;
  ULONG Outcome;
} TRANSACTION_BASIC_INFORMATION, *PTRANSACTION_BASIC_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>TransactionId</b>

<dd>
<p>A GUID that KTM has assigned to the transaction object. This value is also known as the transaction's <a href="https://msdn.microsoft.com/927a417b-35f5-49b8-85f3-7e6b1f5c0225">unit of work (UOW) identifier</a>.</p>
</dd>

### -field <b>State</b>

<dd>
<p>A <a href="..\wdm\ne-wdm--transaction-state.md">TRANSACTION_STATE</a>-typed value that specifies the transaction's current state.</p>
</dd>

### -field <b>Outcome</b>

<dd>
<p>A <a href="..\wdm\ne-wdm--transaction-outcome.md">TRANSACTION_OUTCOME</a>-typed value that specifies the transaction's outcome (result).</p>
</dd>
</dl>

## -remarks
<p>The <b>TRANSACTION_BASIC_INFORMATION</b> structure is used with the <a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a> routine. This routine fills in the structure's members.</p>

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
<a href="..\wdm\nf-wdm-tmgettransactionid.md">TmGetTransactionId</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--transaction-information-class.md">TRANSACTION_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--transaction-outcome.md">TRANSACTION_OUTCOME</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--transaction-state.md">TRANSACTION_STATE</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTION_BASIC_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
