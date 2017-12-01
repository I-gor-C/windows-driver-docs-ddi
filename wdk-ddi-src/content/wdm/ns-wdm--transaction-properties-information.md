---
UID: NS.wdm._TRANSACTION_PROPERTIES_INFORMATION
title: TRANSACTION_PROPERTIES_INFORMATION
author: windows-driver-content
description: The TRANSACTION_PROPERTIES_INFORMATION structure contains a transaction object's properties.
old-location: kernel\transaction_properties_information.htm
old-project: kernel
ms.assetid: 76b0f102-0d09-4b16-b8e1-727a3a6e48c9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TRANSACTION_PROPERTIES_INFORMATION, TRANSACTION_PROPERTIES_INFORMATION, *PTRANSACTION_PROPERTIES_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRANSACTION_PROPERTIES_INFORMATION
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# TRANSACTION_PROPERTIES_INFORMATION structure



## -description
<p>The <b>TRANSACTION_PROPERTIES_INFORMATION</b> structure contains a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object's</a> properties.</p>


## -syntax

````
typedef struct _TRANSACTION_PROPERTIES_INFORMATION {
  ULONG         IsolationLevel;
  ULONG         IsolationFlags;
  LARGE_INTEGER Timeout;
  ULONG         Outcome;
  ULONG         DescriptionLength;
  WCHAR         Description[1];
} TRANSACTION_PROPERTIES_INFORMATION, *PTRANSACTION_PROPERTIES_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>IsolationLevel</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>IsolationFlags</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Timeout</b>

<dd>
<p>A time-out value. If the transaction has not been committed by the time specified by this parameter, KTM rolls back the transaction. The time-out value is expressed in system time units (100-nanosecond intervals), and can specify either an absolute time or a relative time. If the value of the <b>Timeout</b> member is negative, the expiration time is relative to the current system time. Otherwise, the expiration time is absolute. Set this member to zero if no time-out is required. If <b>Timeout</b> is zero, the transaction never times out.</p>
</dd>

### -field <b>Outcome</b>

<dd>
<p>A <a href="..\wdm\ne-wdm--transaction-outcome.md">TRANSACTION_OUTCOME</a>-typed value that identifies the transaction's outcome (result). You can obtain this value by calling <a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a>, but you cannot set the value with <a href="..\wdm\nf-wdm-zwsetinformationtransaction.md">ZwSetInformationTransaction</a>.</p>
</dd>

### -field <b>DescriptionLength</b>

<dd>
<p>The size, in bytes, of the buffer that contains the <b>Description</b> member's array.</p>
</dd>

### -field <b>Description</b>

<dd>
<p>A caller-allocated array of characters that contains or receives the transaction's description string. The <a href="https://msdn.microsoft.com/75d4758b-dfba-431b-9bfa-9dcb98c2a7cc">TPS client</a> can specify this string when it calls <a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>. The client can retrieve the string by calling by calling <b>ZwQueryInformationTransaction</b>, and it can modify the string by calling <b>ZwSetInformationTransaction</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>TRANSACTION_PROPERTIES_INFORMATION</b> structure is used with the <a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a> and <a href="..\wdm\nf-wdm-zwsetinformationtransaction.md">ZwSetInformationTransaction</a> routines.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<a href="..\wdm\ne-wdm--transaction-information-class.md">TRANSACTION_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--transaction-outcome.md">TRANSACTION_OUTCOME</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatetransaction.md">ZwCreateTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationtransaction.md">ZwQueryInformationTransaction</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationtransaction.md">ZwSetInformationTransaction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTION_PROPERTIES_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
