---
UID: NS.winsplp.PBranchOfficeJobDataError
title: PBranchOfficeJobDataError
author: windows-driver-content
description: This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler.
old-location: print\branchofficejobdataerror.htm
old-project: print
ms.assetid: 947C508E-2EB9-451D-AA8D-DCDDE27DEBE6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PBranchOfficeJobDataError, BranchOfficeJobDataError, *PBranchOfficeJobDataError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BranchOfficeJobDataError
req.alt-loc: Winsplp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PBranchOfficeJobDataError structure



## -description
<p>This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler.</p>


## -syntax

````
typedef struct {
  DWORD    LastError;
  LPWSTR   pDocumentName;
  LPWSTR   pUserName;
  LPWSTR   pPrinterName;
  LPWSTR   pDataType;
  LONGLONG TotalSize;
  LONGLONG PrintedSize;
  DWORD    TotalPages;
  DWORD    PrintedPages;
  LPWSTR   pMachineName;
  LPWSTR   pJobError;
  LPWSTR   pErrorDescription;
} BranchOfficeJobDataError, *PBranchOfficeJobDataError;
````


## -struct-fields
<dl>

### -field LastError

<dd>
<p>Specifies the LastError at the time the event was logged.</p>
</dd>

### -field pDocumentName

<dd>
<p>Specifies the name of the printed document.</p>
</dd>

### -field pUserName

<dd>
<p>Specifies the user who submitted the job.</p>
</dd>

### -field pPrinterName

<dd>
<p>Specifies the name of the print connection.</p>
</dd>

### -field pDataType

<dd>
<p>Specifies the data type of the job.</p>
</dd>

### -field TotalSize

<dd>
<p>Specifies the 64-bit size of the job.</p>
</dd>

### -field PrintedSize

<dd>
<p>Specifies the 64-bit size of the job.</p>
</dd>

### -field TotalPages

<dd>
<p>Specifies the total number of pages in the job.</p>
</dd>

### -field PrintedPages

<dd>
<p>Specifies the number of pages currently printed.</p>
</dd>

### -field pMachineName

<dd>
<p>Specifies the name of the client machine printing the job.</p>
</dd>

### -field pJobError

<dd>
<p>Specifies the failure code for a JOB_ERROR event.</p>
</dd>

### -field pErrorDescription

<dd>
<p>Specifies the text description of the error, if available.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h</dt>
</dl>
</td>
</tr>
</table>