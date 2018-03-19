---
UID: NE:printerextension.tagPrintJobStatus
title: tagPrintJobStatus
author: windows-driver-content
description: This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB_INFO_X structures.
old-location: print\printjobstatus.htm
old-project: print
ms.assetid: 856FDAE1-C1D9-458D-B386-0A2D8612EA33
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PrintJobStatus, PrintJobStatus enumeration [Print Devices], PrintJobStatus_BlockedDeviceQueue, PrintJobStatus_Complete, PrintJobStatus_Deleted, PrintJobStatus_Deleting, PrintJobStatus_Error, PrintJobStatus_Offline, PrintJobStatus_PaperOut, PrintJobStatus_Paused, PrintJobStatus_Printed, PrintJobStatus_Printing, PrintJobStatus_Restarted, PrintJobStatus_Retained, PrintJobStatus_Spooling, PrintJobStatus_UserIntervention, print.printjobstatus, printerextension/PrintJobStatus, printerextension/PrintJobStatus_BlockedDeviceQueue, printerextension/PrintJobStatus_Complete, printerextension/PrintJobStatus_Deleted, printerextension/PrintJobStatus_Deleting, printerextension/PrintJobStatus_Error, printerextension/PrintJobStatus_Offline, printerextension/PrintJobStatus_PaperOut, printerextension/PrintJobStatus_Paused, printerextension/PrintJobStatus_Printed, printerextension/PrintJobStatus_Printing, printerextension/PrintJobStatus_Restarted, printerextension/PrintJobStatus_Retained, printerextension/PrintJobStatus_Spooling, printerextension/PrintJobStatus_UserIntervention, tagPrintJobStatus
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
req.lib: 
req.dll: 
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Printerextension.h
api_name:
-	PrintJobStatus
product: Windows
targetos: Windows
req.typenames: PrintJobStatus
req.product: Windows 10 or later.
---

# tagPrintJobStatus Enumeration
This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB_INFO_X structures.

For example, <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a> has the same set of status flags as shown in the following list.

## Syntax
````
typedef enum _PrintJobStatus { 
  PrintJobStatus_Paused              = 0x1,
  PrintJobStatus_Error               = 0x2,
  PrintJobStatus_Deleting            = 0x4,
  PrintJobStatus_Spooling            = 0x8,
  PrintJobStatus_Printing            = 0x10,
  PrintJobStatus_Offline             = 0x20,
  PrintJobStatus_PaperOut            = 0x40,
  PrintJobStatus_Printed             = 0x80,
  PrintJobStatus_Deleted             = 0x100,
  PrintJobStatus_BlockedDeviceQueue  = 0x200,
  PrintJobStatus_UserIntervention    = 0x400,
  PrintJobStatus_Restarted           = 0x800,
  PrintJobStatus_Complete            = 0x1000,
  PrintJobStatus_Retained            = 0x2000
} PrintJobStatus;
````

## Constants

<table>
            
                <tr>
                    <td>PrintJobStatus_Paused</td>
                    <td>The job is paused.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Error</td>
                    <td>There is an error associated with the job.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Deleting</td>
                    <td>The job is being deleted.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Spooling</td>
                    <td>The job is spooling.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Printing</td>
                    <td>The job is printing.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Offline</td>
                    <td>The printer is offline.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_PaperOut</td>
                    <td>The printer is out of paper.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Printed</td>
                    <td>The job printing is completed.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Deleted</td>
                    <td>The job has been deleted.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_BlockedDeviceQueue</td>
                    <td>The driver cannot print the job.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_UserIntervention</td>
                    <td>The printer has an error that requires intervention from the user.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Restarted</td>
                    <td>The job has been restarted.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Complete</td>
                    <td>The job data transfer to the printer is complete. Note that  the printing of the job may not yet be complete.</td>
                </tr>
            
                <tr>
                    <td>PrintJobStatus_Retained</td>
                    <td>The job has been retained in the print queue and cannot be deleted.</td>
                </tr>
</table>

## Remarks

A <b>PrintJobStatus_Retained</b> flag can be raised for several reasons. For example, jobs could be kept in the queue if the administrator of the queue used the desktop print queue UI to set the “Keep Printed Jobs” feature to be on.

It is possible for a job to have multiple  flag values specified simultaneously.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/3C806C3B-78A1-44B6-A9AC-E7258D216637">IPrintJob::Status</a>



<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a>