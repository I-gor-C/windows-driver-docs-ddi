---
UID: NS.NTDDRILAPITYPES.RILMSGMWISUMMARYLIST
title: RILMSGMWISUMMARYLIST
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgmwisummarylist.htm
old-project: netvista
ms.assetid: b698f9df-5a67-4ddf-9956-21fbd4f6f385
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RILMSGMWISUMMARYLIST, *LPRILMSGMWISUMMARYLIST, RILMSGMWISUMMARYLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGMWISUMMARYLIST
req.alt-loc: ntddrilapitypes.h
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
---

# RILMSGMWISUMMARYLIST structure



## -description
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.


## -syntax

````
typedef struct _RILMSGMWISUMMARYLIST {
  DWORD                cbSize;
  DWORD                dwParams;
  DWORD                dwExecutor;
  DWORD                dwReferenceNumber;
  RILADDRESS           stAccountAddress;
  DWORD                dwTotalNumberOfDetailItems;
  DWORD                dwNumberOfSummaryItems;
  RILMSGMWISUMMARY [1] stMwiSummary;
} RILMSGMWISUMMARYLIST, RILMSGMWISUMMARYLIST;
````


## -struct-fields

### -field cbSize


### -field dwParams


### -field dwExecutor


### -field dwReferenceNumber


### -field stAccountAddress


### -field dwTotalNumberOfDetailItems


### -field dwNumberOfSummaryItems


### -field stMwiSummary


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>