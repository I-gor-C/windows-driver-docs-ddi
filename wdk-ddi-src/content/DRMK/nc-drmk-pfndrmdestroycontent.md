---
UID: NC.drmk.PFNDRMDESTROYCONTENT
title: PFNDRMDESTROYCONTENT
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmdestroycontent.htm
ms.assetid: 24B98C91-9EB3-4D00-8D58-F6C96610946A
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: audio
req.header: drmk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRMDestroyContent
req.alt-loc: Drmk.h
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
ms.keywords: WDI_TXRX_TARGET_CONFIGURATION, WDI_TXRX_TARGET_CONFIGURATION, *PWDI_TXRX_TARGET_CONFIGURATION
req.iface: 
---

# PFNDRMDESTROYCONTENT callback



## -description
<p>This callback function is reserved for system use.</p>


## -prototype

````
PFNDRMDESTROYCONTENT DRMDestroyContent;

NTSTATUS DRMDestroyContent(
  _In_ ULONG ContentId
)
{ ... }

typedef PFNDRMDESTROYCONTENT DRMDestroyContent;
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>
</dl>

## -returns
<p>This return value is reserved for system use.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.h</dt>
</dl>
</td>
</tr>
</table>