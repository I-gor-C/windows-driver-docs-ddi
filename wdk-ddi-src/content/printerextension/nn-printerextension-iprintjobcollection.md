---
UID : NN:printerextension.IPrintJobCollection
title : IPrintJobCollection
author : windows-driver-content
description : This interfaces provides an enumeration of the jobs in the print queue.
old-location : print\iprintjobcollection.htm
old-project : print
ms.assetid : 757328A6-DD2C-4057-820B-39EB83277194
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.iprintjobcollection, IPrintJobCollection interface [Print Devices], IPrintJobCollection interface [Print Devices], described, IPrintJobCollection, printerextension/IPrintJobCollection
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : printerextension.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : printerextension.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PrintSchemaSelectionType
req.product : Windows 10 or later.
---

# IPrintJobCollection interface

This interfaces provides an enumeration of the jobs in the print queue.

The enumerated list of jobs represents a snapshot of the current job status.

## Methods

<p>The <b>IPrintJobCollection</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [printerextension.IPrintJobCollection.GetAt](nf-printerextension-iprintjobcollection-getat.md) | Gets a pointer to an IPrintJob object. |

## Remarks

The order of print jobs in the enumerated list is the same as the order provided by <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625(v=vs.85).aspx">EnumJobs</a>, which is the actual print queue order.

<b>IPrintJobCollection</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625(v=vs.85).aspx">EnumJobs</a>

<a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintJobCollection interface%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>