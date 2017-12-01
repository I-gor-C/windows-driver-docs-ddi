---
UID: NC.drmk.PFNDRMFORWARDCONTENTTOINTERFACE
title: PFNDRMFORWARDCONTENTTOINTERFACE
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmforwardcontenttointerface.htm
old-project: audio
ms.assetid: DFD077B7-307B-439B-828D-DC225FC5AAA0
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
req.alt-api: DRMForwardContentToInterface
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

# PFNDRMFORWARDCONTENTTOINTERFACE callback



## -description
<p>This callback function is reserved for system use.</p>


## -prototype

````
PFNDRMFORWARDCONTENTTOINTERFACE DRMForwardContentToInterface;

NTSTATUS DRMForwardContentToInterface(
  _In_ ULONG     ContentId,
  _In_ PUNKNOWN  pUnknown,
  _In_ ULONG     NumMethods
)
{ ... }

typedef PFNDRMFORWARDCONTENTTOINTERFACE DRMForwardContentToInterface;
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>pUnknown</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>NumMethods</i> [in]

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