---
UID: NS.KS.KSGRAPHMANAGER_FUNCTIONTABLE
title: KSGRAPHMANAGER_FUNCTIONTABLE
author: windows-driver-content
description: .
old-location: stream\ksgraphmanager_functiontable.htm
old-project: stream
ms.assetid: F077B970-F146-43BC-BB92-A836C8843890
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KSGRAPHMANAGER_FUNCTIONTABLE, KSGRAPHMANAGER_FUNCTIONTABLE, PKSGRAPHMANAGER_FUNCTIONTABLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSGRAPHMANAGER_FUNCTIONTABLE
req.alt-loc: Ks.h
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

# KSGRAPHMANAGER_FUNCTIONTABLE structure



## -description




## -syntax

````
typedef struct _KSGRAPHMANAGER_FUNCTIONTABLE {
  PFNKSGRAPHMANAGER_NOTIFY NotifyEvent;
} KSGRAPHMANAGER_FUNCTIONTABLE, PKSGRAPHMANAGER_FUNCTIONTABLE;
````


## -struct-fields

### -field NotifyEvent


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>