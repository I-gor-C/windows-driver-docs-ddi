---
UID: NF.winsplp.LogJobInfoForBranchOffice
title: LogJobInfoForBranchOffice
author: windows-driver-content
description: Allows Branch Office clients to send job events to the host print server.
old-location: print\logjobinfoforbranchoffice.htm
ms.assetid: 6D1AB299-2E26-42AF-9613-CA321173080D
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LogJobInfoForBranchOffice
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
ms.keywords: LogJobInfoForBranchOffice
req.iface: 
req.product: Windows 10 or later.
---

# LogJobInfoForBranchOffice function



## -description
<p>Allows Branch Office clients to send job events to the host print server.</p>


## -syntax

````
HRESULT WINAPI LogJobInfoForBranchOffice(
  _In_ HANDLE                        hPrinter,
  _In_ PBranchOfficeJobDataContainer pJobDataContainer
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>Specifies a handle to the CSR printer.</p>
</dd>

### -param <i>pJobDataContainer</i> [in]

<dd>
<p>Specifies a pointer to an array of <a href="RID">BranchOfficeJobData</a> structures, containing the events to be logged.</p>
</dd>
</dl>

## -returns
<p>Indicates success or failure.</p>

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