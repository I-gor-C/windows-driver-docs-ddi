---
UID: NF.portcls.IResourceList.NumberOfEntries
title: IResourceList::NumberOfEntries method
author: windows-driver-content
description: The NumberOfEntries method returns the number of resource items in the resource list.
old-location: audio\iresourcelist_numberofentries.htm
old-project: audio
ms.assetid: cb882170-5c8e-455d-89a6-b09ca77e63fb
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IResourceList, IResourceList::NumberOfEntries, NumberOfEntries
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IResourceList.NumberOfEntries
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# IResourceList::NumberOfEntries method



## -description
The <code>NumberOfEntries</code> method returns the number of resource items in the resource list.



## -syntax

````
ULONG NumberOfEntries(
    None
);
````


## -parameters

### -param None 


## -returns
<code>NumberOfEntries</code> returns the number of items in the resource list.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>