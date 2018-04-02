---
UID: NF:winsplp.PartialReplyPrinterChangeNotification
title: PartialReplyPrinterChangeNotification function
author: windows-driver-content
description: The print spooler's PartialReplyPrinterChangeNotification function allows a print provider to update the spooler's database of printer changes associated with a notification handle.
old-location: print\partialreplyprinterchangenotification.htm
old-project: print
ms.assetid: a884920c-1824-418f-90c8-0edf1381678b
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PartialReplyPrinterChangeNotification, PartialReplyPrinterChangeNotification function [Print Devices], print.partialreplyprinterchangenotification, spoolfnc_95f9f0ac-2340-463b-9c8d-6c27130020d9.xml, winsplp/PartialReplyPrinterChangeNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
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
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Spoolss.dll
api_name:
-	PartialReplyPrinterChangeNotification
product: Windows
targetos: Windows
req.typenames: NOTIFICATION_CONFIG_FLAGS
req.product: Windows 10 or later.
---


# PartialReplyPrinterChangeNotification function
The print spooler's <code>PartialReplyPrinterChangeNotification</code> function allows a print provider to update the spooler's database of printer changes associated with a notification handle.

## Syntax

```
BOOL PartialReplyPrinterChangeNotification(
  HANDLE                    hPrinter,
  PPRINTER_NOTIFY_INFO_DATA pDataSrc
);
```

## Parameters

`hPrinter`

TBD

`pDataSrc`

TBD


## Return Value

If the operation succeeds, the function returns <b>TRUE</b>. Otherwise the function returns <b>FALSE</b>. The caller can obtain an error code by calling <b>GetLastError</b>.

## Remarks

For the specified notification handle, the spooler's <code>PartialReplyPrinterChangeNotification</code> function adds the contents of the specified PRINTER_NOTIFY_INFO_DATA structure to the array within the spooler's stored PRINTER_NOTIFY_INFO structure. (These structures are described in the Windows SDK documentation.)

Calling <code>PartialReplyPrinterChangeNotification</code> does not cause the spooler to notify the application that changes have occurred. If the print provider's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548837">FindFirstPrinterChangeNotification</a> function did not set the PRINTER_NOTIFY_STATUS_POLL flag, the provider must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a> to cause the application to be notified.

If <i>pInfoDataSrc</i> is <b>NULL</b>, all stored information associated with the specified handle is deleted from the spooler. The function accomplishes this deletion by freeing all buffers associated with <i>pBuf</i> members of PRINTER_NOTIFY_INFO_DATA structures belonging to the specified handle. The function then sets the PRINTER_NOTIFY_INFO_DISCARDED flag in the stored PRINTER_NOTIFY_INFO structure.

For additional information, see <a href="https://msdn.microsoft.com/e75c6f89-9cef-4900-af89-edf1f7f786c7">Supporting Printer Change Notifications</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | winsplp.h (include Winsplp.h) |
| **Library** | Spoolss.lib |
| **DLL** | Spoolss.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548837">FindFirstPrinterChangeNotification</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561959">ReplyPrinterChangeNotification</a>