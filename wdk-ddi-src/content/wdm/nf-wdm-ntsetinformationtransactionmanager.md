---
UID: NF:wdm.NtSetInformationTransactionManager
title: NtSetInformationTransactionManager function
author: windows-driver-content
description: Do not call this routine from kernel-mode code.
old-location: kernel\ntsetinformationtransactionmanager.htm
old-project: kernel
ms.assetid: a1e2f40f-5aea-4c8b-8692-95721ad4bc9d
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: NtSetInformationTransactionManager, NtSetInformationTransactionManager routine [Kernel-Mode Driver Architecture], kernel.ntsetinformationtransactionmanager, ntx_b4f057ac-bca8-44e6-874e-4f33bd487a20.xml, wdm/NtSetInformationTransactionManager
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: "<=APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	NtSetInformationTransactionManager
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# NtSetInformationTransactionManager function
Do not call this routine from kernel-mode code.

## Syntax

````
NTSTATUS NtSetInformationTransactionManager(
  _In_opt_ HANDLE                                                   TmHandle,
  _In_     TRANSACTIONMANAGER_INFORMATION_CLASS                     TransactionManagerInformationClass,
  _In_     _reads_bytes_(TransactionManagerInformationLength) PVOID TransactionManagerInformation,
  _In_     ULONG                                                    TransactionManagerInformationLength
);
````

## Parameters

`TmHandle`



`TransactionManagerInformationClass`



`TransactionManagerInformation`



`TransactionManagerInformationLength`




## Return Value

See the <b>Zw<i>Xxx</i></b> equivalent.

Do not call this routine from kernel-mode code; instead, call the <b>Zw<i>Xxx</i></b> equivalent. User-mode code can call this routine or the <b>Zw<i>Xxx</i></b> equivalent. For further comments, if any, see the ZwXxx equivalent

The driver must check the return value of the function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wdm.h |
| **Library** | NtosKrnl.exe |
| **IRQL** | "<=APC_LEVEL" |

## See Also

See the <b>Zw<i>Xxx</i></b> equivalent.