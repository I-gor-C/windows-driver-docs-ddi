---
UID: NC.dispmprt.DXGKDDI_EXCHANGEPRESTARTINFO
title: DXGKDDI_EXCHANGEPRESTARTINFO
author: windows-driver-content
description: Allows very simple data to be exchanged between the OS and driver which may be required prior to DxgkDdiStartDevice device being called and therefore cannot be queried through normal caps or adapter info DDIs.
old-location: display\dxgkddi_exchangeprestartinfo.htm
ms.assetid: B23EDC08-18E4-4826-AC51-163C706D4F43
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKDDI_EXCHANGEPRESTARTINFO
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKDDI_EXCHANGEPRESTARTINFO callback



## -description
<p>Allows very simple data to be exchanged between the OS and driver which may be required prior to DxgkDdiStartDevice device being called and therefore cannot be queried through normal caps or adapter info DDIs.</p>


## -prototype

````
NTSTATUS APIENTRY DXGKDDI_EXCHANGEPRESTARTINFO(
  _In_    const Handle               hAdapter,
  _Inout_       PDXGK_PRE_START_INFO pPreStartInfo
);
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>[in] Identifies the adapter.</p>
</dd>

### -param <i>pPreStartInfo</i> [in, out]

<dd>
<p>[in] Pointer to a DXGK_PRE_START_INFO structure which contains both fields for the OS to pass info and fields for the driver to return info.  Only SupportPreserveBootDisplay is defined initially.</p>
<p>[out] SupportPreserveBootDisplay</p>
<p>The driver and hardware support the requirements to allow the boot frame buffer to be used and displayed throughout the hardware initialization performed during DxgkDdiStartDevice.</p>
</dd>
</dl>

## -returns
<p>If this routine succeeds and returns the requested change, it returns STATUS_SUCCESS.</p>

## -remarks
<p>This DDI will be called after DxgkDdiAddDevice and before DxgkDdiStartDevice so the driver does not have access to its own hardware resources yet however it can use the PhysicalDeviceObject passed to the driver in DxgkDdiAddDevice to call IoGetDeviceProperty, for example to find the hardware id to decide what to return in the output fields of the DXGK_PRE_START_INFO structure.</p>

<p> 

This function is always called at PASSIVE level so the supporting code should be made pageable where possible.
</p>

<p>This DDI will be called after DxgkDdiAddDevice and before DxgkDdiStartDevice so the driver does not have access to its own hardware resources yet however it can use the PhysicalDeviceObject passed to the driver in DxgkDdiAddDevice to call IoGetDeviceProperty, for example to find the hardware id to decide what to return in the output fields of the DXGK_PRE_START_INFO structure.</p>

<p> 

This function is always called at PASSIVE level so the supporting code should be made pageable where possible.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>