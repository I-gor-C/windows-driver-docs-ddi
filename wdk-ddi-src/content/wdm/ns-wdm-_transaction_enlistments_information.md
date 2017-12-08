---
UID: NS.WDM._TRANSACTION_ENLISTMENTS_INFORMATION
title: _TRANSACTION_ENLISTMENTS_INFORMATION
author: windows-driver-content
description: The TRANSACTION_ENLISTMENTS_INFORMATION structure contains information about the enlistments that are associated with a transaction object.
old-location: kernel\transaction_enlistments_information.htm
old-project: kernel
ms.assetid: 8b33a7ed-6892-4b2d-9d7a-cfc43c9fbf68
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _TRANSACTION_ENLISTMENTS_INFORMATION, TRANSACTION_ENLISTMENTS_INFORMATION, *PTRANSACTION_ENLISTMENTS_INFORMATION
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
req.alt-api: TRANSACTION_ENLISTMENTS_INFORMATION
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
req.product: Windows 10 or later.
---

# _TRANSACTION_ENLISTMENTS_INFORMATION structure



## -description
The <b>TRANSACTION_ENLISTMENTS_INFORMATION</b> structure contains information about the enlistments that are associated with a <a href="https://msdn.microsoft.com/124105bd-70be-49b1-8ea4-af6ba1f3cf16">transaction object</a>.


## -syntax

````
typedef struct _TRANSACTION_ENLISTMENTS_INFORMATION {
  ULONG                       NumberOfEnlistments;
  TRANSACTION_ENLISTMENT_PAIR EnlistmentPair[1];
} TRANSACTION_ENLISTMENTS_INFORMATION, *PTRANSACTION_ENLISTMENTS_INFORMATION;
````


## -struct-fields

### -field NumberOfEnlistments

The number of enlistments that are associated with a transaction object. This is also the number of elements in the array that the <b>EnlistmentPair</b> member specifies.

### -field EnlistmentPair

A caller-allocated array of <a href="kernel.transaction_enlistment_pair">TRANSACTION_ENLISTMENT_PAIR</a> structures. 

## -remarks
The <b>TRANSACTION_ENLISTMENTS_INFORMATION</b> structure is used with the <a href="kernel.zwqueryinformationtransaction">ZwQueryInformationTransaction</a> routine. This routine fills in the structure's members.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later operating system versions.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="kernel.transaction_enlistment_pair">TRANSACTION_ENLISTMENT_PAIR</a>
</dt>
<dt>
<a href="kernel.transaction_information_class">TRANSACTION_INFORMATION_CLASS</a>
</dt>
<dt>
<a href="kernel.zwqueryinformationtransaction">ZwQueryInformationTransaction</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTION_ENLISTMENTS_INFORMATION structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
