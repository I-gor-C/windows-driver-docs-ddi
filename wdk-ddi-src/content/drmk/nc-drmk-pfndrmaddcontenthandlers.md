---
UID: NC.drmk.PFNDRMADDCONTENTHANDLERS
title: PFNDRMADDCONTENTHANDLERS
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmaddcontenthandlers.htm
old-project: audio
ms.assetid: 762604FC-34EA-41A1-9F2B-B3852AA4D167
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TXRX_TARGET_CONFIGURATION, WDI_TXRX_TARGET_CONFIGURATION, *PWDI_TXRX_TARGET_CONFIGURATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: drmk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRMAddContentHandlers
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
req.iface: 
---

# PFNDRMADDCONTENTHANDLERS callback



## -description
<p>This callback function is reserved for system use.</p>


## -prototype

````
PFNDRMADDCONTENTHANDLERS DRMAddContentHandlers;

NTSTATUS DRMAddContentHandlers(
  _In_ ULONG  ContentId,
  _In_ PVOID  *paHandlers,
  _In_ ULONG  NumHandlers
)
{ ... }

typedef PFNDRMADDCONTENTHANDLERS DRMAddContentHandlers;
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>paHandlers</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>NumHandlers</i> [in]

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