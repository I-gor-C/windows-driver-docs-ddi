---
UID: NF.storport.StorPortGetActivityIdSrb
title: StorPortGetActivityIdSrb
author: windows-driver-content
description: Retrieves the Event Tracing for Windows (ETW) activity ID associated with a request block.
old-location: storage\storportgetactivityidsrb.htm
old-project: storage
ms.assetid: 63E956F5-C87C-45AA-BE16-2AD07F3BA050
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetActivityIdSrb
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetActivityIdSrb
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: Any
req.iface: 
req.product: Windows 10 or later.
---

# StorPortGetActivityIdSrb function



## -description
<p>Retrieves the Event Tracing for Windows (ETW) activity ID associated with a request block.</p>


## -syntax

````
ULONG StorPortGetActivityIdSrb(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _Out_ LPGUID              ActivityId
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param Srb [in]

<dd>
<p>The request block to retrieve the ETW activity ID for.</p>
</dd>

### -param ActivityId [out]

<dd>
<p>A pointer to a caller-supplied GUID to receive the ETW activity ID.</p>
</dd>
</dl>

## -returns
<p>A status value indicating the result of the notification. This can be one of these values:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The ETW activity ID was returned in <i>ActivityId</i>.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer in <i>ActivityId</i> or <i>Srb</i> is NULL.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An ETW activity ID is not associated with the request in <i>Srb</i>.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any</p>
</td>
</tr>
</table>