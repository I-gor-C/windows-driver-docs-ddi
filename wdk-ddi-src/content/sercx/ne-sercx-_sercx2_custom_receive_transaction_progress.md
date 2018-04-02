---
UID: NE:sercx._SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS
title: "_SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS"
author: windows-driver-content
description: The SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS enumeration defines constants that indicate whether process is being made toward completing a custom-receive transaction.
old-location: serports\sercx2_custom_receive_transaction_progress.htm
old-project: serports
ms.assetid: B832554C-FB37-416F-9586-EFAB5A3633E5
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PSERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, 2/SERCX2_CUSTOM_RECEIVE_BYTES_TRANSFERRED, 2/SERCX2_CUSTOM_RECEIVE_NO_PROGRESS, 2/SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, SERCX2_CUSTOM_RECEIVE_BYTES_TRANSFERRED, SERCX2_CUSTOM_RECEIVE_NO_PROGRESS, SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS enumeration [Serial Ports], _SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, serports.sercx2_custom_receive_transaction_progress"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sercx.h
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
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	2.0\Sercx.h
api_name:
-	SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS
product: Windows
targetos: Windows
req.typenames: SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, *PSERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS
req.product: Windows 10 or later.
---

# _SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS Enumeration
The <b>SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS</b> enumeration defines constants that indicate whether process is being made toward completing a custom-receive transaction.

## Syntax
```
typedef enum _SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS {
  SerCx2CustomReceiveTransactionNoProgress        ,
  SerCx2CustomReceiveTransactionBytesTransferred
} SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS, *PSERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS;
```

## Constants

<table>
            
                <tr>
                    <td>SerCx2CustomReceiveTransactionNoProgress</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>SerCx2CustomReceiveTransactionBytesTransferred</td>
                    <td></td>
                </tr>
</table>

## Remarks

The constants in this enumeration are used by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265254">SerCx2CustomReceiveTransactionReportProgress</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | sercx.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn265254">SerCx2CustomReceiveTransactionReportProgress</a>