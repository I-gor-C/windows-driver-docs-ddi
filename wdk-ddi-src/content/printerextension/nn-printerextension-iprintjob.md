---
UID: NN:printerextension.IPrintJob
title: IPrintJob
author: windows-driver-content
description: Contains properties that represent a print job.
old-location: print\iprintjob.htm
old-project: print
ms.assetid: 068E53EC-26B8-48E7-A605-081709C94043
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintJob, IPrintJob interface [Print Devices], IPrintJob interface [Print Devices], described, print.iprintjob, printerextension/IPrintJob
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: printerextension.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Printerextension.h
api_name:
-	IPrintJob
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintJob interface

Contains properties that represent a print job.

This interface also provides a method that allows a print job to be cancelled.

## Methods

<p>The <b>IPrintJob</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintJob::get_Id](nf-printerextension-iprintjob-get_id.md) | Gets the print job identifier (ID). |
| [IPrintJob::get_Name](nf-printerextension-iprintjob-get_name.md) | Gets the name of the printer for this print queue. |
| [IPrintJob::get_PrintedPages](nf-printerextension-iprintjob-get_printedpages.md) | Gets the number of pages that have been printed. |
| [IPrintJob::get_Status](nf-printerextension-iprintjob-get_status.md) | Gets the current status of the print job. |
| [IPrintJob::get_SubmissionTime](nf-printerextension-iprintjob-get_submissiontime.md) | Gets the submission time, in the “DATE” format, provided in the user’s local time (not in the UTC format that is provided by the spooler). |
| [IPrintJob::get_TotalPages](nf-printerextension-iprintjob-get_totalpages.md) | Gets the total number of pages that the document contains. |
| [IPrintJob::RequestCancel](nf-printerextension-iprintjob-requestcancel.md) | Requests the cancellation of a print job. |

## Remarks

The <b>IPrintJob</b> interface provides a wrapper around select properties of the spooler’s <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a> structure.

<b>IPrintJob</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/D1236DD2-D4AD-4615-9036-7EC75D6CADCE">Job Management</a>



<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintJob interface%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>