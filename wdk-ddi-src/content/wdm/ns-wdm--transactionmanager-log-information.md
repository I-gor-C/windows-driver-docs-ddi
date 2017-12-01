---
UID: NS.wdm._TRANSACTIONMANAGER_LOG_INFORMATION
title: TRANSACTIONMANAGER_LOG_INFORMATION
author: windows-driver-content
description: The TRANSACTIONMANAGER_LOG_INFORMATION structure contains information about a transaction manager object.
old-location: kernel\transactionmanager_log_information.htm
old-project: kernel
ms.assetid: 7d0da54d-54a2-4440-910f-d99716660506
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TRANSACTIONMANAGER_LOG_INFORMATION, TRANSACTIONMANAGER_LOG_INFORMATION, *PTRANSACTIONMANAGER_LOG_INFORMATION
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
req.alt-api: TRANSACTIONMANAGER_LOG_INFORMATION
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

# TRANSACTIONMANAGER_LOG_INFORMATION structure



## -description
<p>The <b>TRANSACTIONMANAGER_LOG_INFORMATION</b> structure contains information about a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>.</p>


## -syntax

````
typedef struct _TRANSACTIONMANAGER_LOG_INFORMATION {
  GUID LogIdentity;
} TRANSACTIONMANAGER_LOG_INFORMATION, *PTRANSACTIONMANAGER_LOG_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>LogIdentity</b>

<dd>
<p>A GUID that KTM uses to identify restart records in a transaction manager object's log stream. For more information about restart records, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff566409">Writing Restart Records to a CLFS Stream</a>.</p>
</dd>
</dl>

## -remarks
<p>The <b>TRANSACTIONMANAGER_LOG_INFORMATION</b> structure is used with the <a href="..\wdm\nf-wdm-zwqueryinformationtransactionmanager.md">ZwQueryInformationTransactionManager</a> routine.</p>

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
<a href="..\wdm\ne-wdm--transactionmanager-information-class.md">TRANSACTIONMANAGER_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationtransactionmanager.md">ZwQueryInformationTransactionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTIONMANAGER_LOG_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
