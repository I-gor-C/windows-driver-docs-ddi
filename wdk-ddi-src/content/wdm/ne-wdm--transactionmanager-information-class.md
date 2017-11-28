---
UID: NE.wdm._TRANSACTIONMANAGER_INFORMATION_CLASS
title: TRANSACTIONMANAGER_INFORMATION_CLASS
author: windows-driver-content
description: The TRANSACTIONMANAGER_INFORMATION_CLASS enumeration specifies the type of information that the ZwQueryInformationTransactionManager routine can retrieve for a transaction manager object.
old-location: kernel\transactionmanager_information_class.htm
old-project: kernel
ms.assetid: 71d6db29-0a93-4793-92f4-3e85615e1b61
ms.author: windowsdriverdev
ms.date: 11/20/2017
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
req.alt-api: TRANSACTIONMANAGER_INFORMATION_CLASS
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# TRANSACTIONMANAGER_INFORMATION_CLASS enumeration



## -description
<p>The <b>TRANSACTIONMANAGER_INFORMATION_CLASS</b> enumeration specifies the type of information that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a> routine can retrieve for a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>.</p>


## -syntax

````
typedef enum _TRANSACTIONMANAGER_INFORMATION_CLASS { 
  TransactionManagerBasicInformation     = 0,
  TransactionManagerLogInformation       = 1,
  TransactionManagerLogPathInformation   = 2,
  TransactionManagerRecoveryInformation  = 4
} TRANSACTIONMANAGER_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field <a id="TransactionManagerBasicInformation"></a><a id="transactionmanagerbasicinformation"></a><a id="TRANSACTIONMANAGERBASICINFORMATION"></a><b>TransactionManagerBasicInformation</b>

<dd>
<p>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564753">TRANSACTIONMANAGER_BASIC_INFORMATION</a> structure. </p>
</dd>

### -field <a id="TransactionManagerLogInformation"></a><a id="transactionmanagerloginformation"></a><a id="TRANSACTIONMANAGERLOGINFORMATION"></a><b>TransactionManagerLogInformation</b>

<dd>
<p>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564767">TRANSACTIONMANAGER_LOG_INFORMATION</a> structure. </p>
</dd>

### -field <a id="TransactionManagerLogPathInformation"></a><a id="transactionmanagerlogpathinformation"></a><a id="TRANSACTIONMANAGERLOGPATHINFORMATION"></a><b>TransactionManagerLogPathInformation</b>

<dd>
<p>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564764">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a> structure. </p>
</dd>

### -field <a id="TransactionManagerRecoveryInformation"></a><a id="transactionmanagerrecoveryinformation"></a><a id="TRANSACTIONMANAGERRECOVERYINFORMATION"></a><b>TransactionManagerRecoveryInformation</b>

<dd>
<p>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564776">TRANSACTIONMANAGER_RECOVERY_INFORMATION</a> structure.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564753">TRANSACTIONMANAGER_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564767">TRANSACTIONMANAGER_LOG_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564764">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSACTIONMANAGER_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
