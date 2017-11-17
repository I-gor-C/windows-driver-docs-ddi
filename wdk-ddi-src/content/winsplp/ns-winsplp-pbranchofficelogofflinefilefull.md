---
UID: NS.winsplp.PBranchOfficeLogOfflineFileFull
title: PBranchOfficeLogOfflineFileFull
author: windows-driver-content
description: Contains the necessary data for logging that the offline log archive on the current client overflowed at some point.
old-location: print\branchofficelogofflinefilefull.htm
ms.assetid: 41190CE8-8779-477C-BFB0-6410DF096EFD
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
req.alt-api: BranchOfficeLogOfflineFileFull
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
ms.keywords: PBranchOfficeLogOfflineFileFull, BranchOfficeLogOfflineFileFull, *PBranchOfficeLogOfflineFileFull
req.iface: 
req.product: Windows 10 or later.
---

# PBranchOfficeLogOfflineFileFull structure



## -description
<p>Contains the necessary data for logging that the offline log archive on the current client overflowed at some point.</p>


## -syntax

````
typedef struct {
  LPWSTR pMachineName;
} BranchOfficeLogOfflineFileFull, *PBranchOfficeLogOfflineFileFull;
````


## -struct-fields
<dl>

### -field <b>pMachineName</b>

<dd>
<p>Specifies the name of the print client.</p>
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