---
UID: NF.printoem.OEMDevQueryPrintEx
title: OEMDevQueryPrintEx function
author: windows-driver-content
description: OEMDevQueryPrintEx function
old-location: print\oemdevqueryprintex.htm
old-project: print
ms.assetid: 3d555be3-2a1b-40b4-adf4-b797bb4b09b7
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: OEMDevQueryPrintEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMDevQueryPrintEx
req.alt-loc: printoem.h
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
req.product: Windows 10 or later.
---

# OEMDevQueryPrintEx function



## -description

## -syntax

````
BOOL APIENTRY OEMDevQueryPrintEx(
   POEMUIOBJ           poemuiobj,
   PDEVQUERYPRINT_INFO pDQPInfo,
   PDEVMODE            pPublicDM,
   PVOID               pOEMDM
);
````


## -parameters

### -param poemuiobj 


### -param pDQPInfo 


### -param pPublicDM 


### -param pOEMDM 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>