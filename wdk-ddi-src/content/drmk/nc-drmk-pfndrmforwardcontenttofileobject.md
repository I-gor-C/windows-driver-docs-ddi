---
UID: NC.drmk.PFNDRMFORWARDCONTENTTOFILEOBJECT
title: PFNDRMFORWARDCONTENTTOFILEOBJECT
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmforwardcontenttofileobject.htm
old-project: audio
ms.assetid: 00ACCBFF-FEDE-4223-8503-4D75426E2BD6
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
req.alt-api: DRMForwardContentToFileObject
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

# PFNDRMFORWARDCONTENTTOFILEOBJECT callback



## -description
<p>This callback function is reserved for system use.</p>


## -prototype

````
PFNDRMFORWARDCONTENTTOFILEOBJECT DRMForwardContentToFileObject;

NTSTATUS DRMForwardContentToFileObject(
  _In_ ULONG        ContentId,
  _In_ PFILE_OBJECT FileObject
)
{ ... }

typedef PFNDRMFORWARDCONTENTTOFILEOBJECT DRMForwardContentToFileObject;
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>FileObject</i> [in]

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