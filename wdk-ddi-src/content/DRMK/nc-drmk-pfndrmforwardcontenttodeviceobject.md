---
UID: NC.drmk.PFNDRMFORWARDCONTENTTODEVICEOBJECT
title: PFNDRMFORWARDCONTENTTODEVICEOBJECT
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmforwardcontenttodeviceobject.htm
ms.assetid: A6256D6D-A952-4E10-B8E7-A28E3D8D9585
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
req.alt-api: DRMForwardContentToDeviceObject
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

# PFNDRMFORWARDCONTENTTODEVICEOBJECT callback



## -description
<p>This callback function is reserved for system use.</p>


## -prototype

````
PFNDRMFORWARDCONTENTTODEVICEOBJECT DRMForwardContentToDeviceObject;

NTSTATUS DRMForwardContentToDeviceObject(
  _In_ ULONG        ContentId,
  _In_ PVOID        Reserved,
  _In_ PCDRMFORWARD DrmForward
)
{ ... }

typedef PFNDRMFORWARDCONTENTTODEVICEOBJECT DRMForwardContentToDeviceObject;
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>Reserved</i> [in]

<dd>
<p>This parameter is reserved for system use.</p>
</dd>

### -param <i>DrmForward</i> [in]

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