---
UID: NS.winsplp.PBranchOfficeJobDataError
title: PBranchOfficeJobDataError
author: windows-driver-content
description: This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler.
old-location: print\branchofficejobdataerror.htm
ms.assetid: 947C508E-2EB9-451D-AA8D-DCDDE27DEBE6
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
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
ms.keywords: PBranchOfficeJobDataError, BranchOfficeJobDataError, *PBranchOfficeJobDataError
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

### -field <b>LastError</b>

<dd>
<p>Specifies the LastError at the time the event was logged.</p>
</dd>

### -field <b>pDocumentName</b>

<dd>
<p>Specifies the name of the printed document.</p>
</dd>

### -field <b>pUserName</b>

<dd>
<p>Specifies the user who submitted the job.</p>
</dd>

### -field <b>pPrinterName</b>

<dd>
<p>Specifies the name of the print connection.</p>
</dd>

### -field <b>pDataType</b>

<dd>
<p>Specifies the data type of the job.</p>
</dd>

### -field <b>TotalSize</b>

<dd>
<p>Specifies the 64-bit size of the job.</p>
</dd>

### -field <b>PrintedSize</b>

<dd>
<p>Specifies the 64-bit size of the job.</p>
</dd>

### -field <b>TotalPages</b>

<dd>
<p>Specifies the total number of pages in the job.</p>
</dd>

### -field <b>PrintedPages</b>

<dd>
<p>Specifies the number of pages currently printed.</p>
</dd>

### -field <b>pMachineName</b>

<dd>
<p>Specifies the name of the client machine printing the job.</p>
</dd>

### -field <b>pJobError</b>

<dd>
<p>Specifies the failure code for a JOB_ERROR event.</p>
</dd>

### -field <b>pErrorDescription</b>

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