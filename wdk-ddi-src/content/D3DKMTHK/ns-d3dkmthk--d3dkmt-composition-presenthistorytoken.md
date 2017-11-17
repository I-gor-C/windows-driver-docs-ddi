---
UID: NS.d3dkmthk._D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN
title: D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN
author: windows-driver-content
description: Identifies a composition swap chain present-history operation. This type of presentation is used for Extensible Application Markup Language (XAML)-based apps.
old-location: display\d3dkmt_composition_presenthistorytoken.htm
ms.assetid: F3F2DE77-9FC5-4AC1-B857-51B51557108E
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN, D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN
req.iface: 
---

# D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN structure



## -description
<p>Identifies a composition swap chain present-history operation. This type of presentation is used for Extensible Application Markup Language (XAML)-based apps.</p>


## -syntax

````
typedef struct _D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN {
  ULONG64 hPrivateData;
} D3DKMT_COMPOSITION_PRESENTHISTORYTOKEN;
````


## -struct-fields
<dl>

### -field <b>hPrivateData</b>

<dd>
<p>A driver-resident private data structure that identifies a composition swap chain present-history operation.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>