---
UID: NE:wdm._TRANSACTIONMANAGER_INFORMATION_CLASS
title: "_TRANSACTIONMANAGER_INFORMATION_CLASS"
author: windows-driver-content
description: The TRANSACTIONMANAGER_INFORMATION_CLASS enumeration specifies the type of information that the ZwQueryInformationTransactionManager routine can retrieve for a transaction manager object.
old-location: kernel\transactionmanager_information_class.htm
old-project: kernel
ms.assetid: 71d6db29-0a93-4793-92f4-3e85615e1b61
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: TRANSACTIONMANAGER_INFORMATION_CLASS, TRANSACTIONMANAGER_INFORMATION_CLASS enumeration [Kernel-Mode Driver Architecture], TransactionManagerBasicInformation, TransactionManagerLogInformation, TransactionManagerLogPathInformation, TransactionManagerRecoveryInformation, _TRANSACTIONMANAGER_INFORMATION_CLASS, kernel.transactionmanager_information_class, ktm_ref_55fd8dd4-e88d-40df-9091-1aecc4de38a7.xml, wdm/TRANSACTIONMANAGER_INFORMATION_CLASS, wdm/TransactionManagerBasicInformation, wdm/TransactionManagerLogInformation, wdm/TransactionManagerLogPathInformation, wdm/TransactionManagerRecoveryInformation
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	TRANSACTIONMANAGER_INFORMATION_CLASS
product: Windows
targetos: Windows
req.typenames: TRANSACTIONMANAGER_INFORMATION_CLASS
req.product: Windows 10 or later.
---

# _TRANSACTIONMANAGER_INFORMATION_CLASS Enumeration
The <b>TRANSACTIONMANAGER_INFORMATION_CLASS</b> enumeration specifies the type of information that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a> routine can retrieve for a <a href="https://msdn.microsoft.com/af53cda4-e2ab-47df-9311-a4da2a2ee08d">transaction manager object</a>.

## Syntax
```
typedef enum _TRANSACTIONMANAGER_INFORMATION_CLASS {
  TransactionManagerBasicInformation     ,
  TransactionManagerLogInformation       ,
  TransactionManagerLogPathInformation   ,
  TransactionManagerRecoveryInformation
} TRANSACTIONMANAGER_INFORMATION_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>TransactionManagerBasicInformation</td>
                    <td>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564753">TRANSACTIONMANAGER_BASIC_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>TransactionManagerLogInformation</td>
                    <td>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564767">TRANSACTIONMANAGER_LOG_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>TransactionManagerLogPathInformation</td>
                    <td>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564764">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>TransactionManagerRecoveryInformation</td>
                    <td>Information about a transaction manager object is stored in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564776">TRANSACTIONMANAGER_RECOVERY_INFORMATION</a> structure.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later operating system versions. Available in Windows Vista and later operating system versions. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564753">TRANSACTIONMANAGER_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564764">TRANSACTIONMANAGER_LOGPATH_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564767">TRANSACTIONMANAGER_LOG_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567058">ZwQueryInformationTransactionManager</a>