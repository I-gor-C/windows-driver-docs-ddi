---
UID: NS.winsplp.PBranchOfficeJobDataPrinted
title: PBranchOfficeJobDataPrinted
author: windows-driver-content
description: Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler.
old-location: print\branchofficejobdataprinted.htm
ms.assetid: 77737A33-9592-43A3-B12A-5BFDCA0209BE
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
req.alt-api: BranchOfficeJobDataPrinted
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
ms.keywords: PBranchOfficeJobDataPrinted, BranchOfficeJobDataPrinted, *PBranchOfficeJobDataPrinted
req.iface: 
req.product: Windows 10 or later.
---

# PBranchOfficeJobDataPrinted structure



## -description
<p>Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler.</p>


## -syntax

````
typedef struct {
  DWORD    Status;
  LPWSTR   pDocumentName;
  LPWSTR   pUserName;
  LPWSTR   pMachineName;
  LPWSTR   pPrinterName;
  LPWSTR   pPortName;
  LONGLONG Size;
  DWORD    TotalPages;
} BranchOfficeJobDataPrinted, *PBranchOfficeJobDataPrinted;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd>
<p>Specifies the current status, or the failure code for a JOB_ERROR event.</p>
</dd>

### -field <b>pDocumentName</b>

<dd>
<p>Specifies the name of the printed document.</p>
</dd>

### -field <b>pUserName</b>

<dd>
<p>Specifies the user who submitted the job.</p>
</dd>

### -field <b>pMachineName</b>

<dd>
<p>Specifies the name of the client machine printing the job</p>
</dd>

### -field <b>pPrinterName</b>

<dd>
<p>Specifies the name of the print connection.</p>
</dd>

### -field <b>pPortName</b>

<dd>
<p>Specifies the name of the port the job printed on.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the 64-bit size of the job.</p>
</dd>

### -field <b>TotalPages</b>

<dd>
<p>Specifies the total number of pages in the job.</p>
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