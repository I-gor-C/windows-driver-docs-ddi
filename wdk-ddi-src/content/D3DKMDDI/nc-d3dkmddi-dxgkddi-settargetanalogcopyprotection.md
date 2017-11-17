---
UID: NC.d3dkmddi.DXGKDDI_SETTARGETANALOGCOPYPROTECTION
title: DXGKDDI_SETTARGETANALOGCOPYPROTECTION
author: windows-driver-content
description: Sets the analog copy protection on the specified target id. This is functionally equivalent to the DxgkDdiUpdateActiveVidPnPresentPath in previous WDDM versions if only the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION is changed.
old-location: display\dxgkddi_settargetanalogcopyprotection.htm
ms.assetid: D41A1867-C654-4747-B804-CAE047025458
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKDDI_SETTARGETANALOGCOPYPROTECTION
req.alt-loc: d3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGKDDI_SETTARGETANALOGCOPYPROTECTION callback



## -description
<p>Sets the analog copy protection on the specified target id.  This is functionally equivalent to the DxgkDdiUpdateActiveVidPnPresentPath in previous WDDM versions if only the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION is changed.</p>


## -prototype

````
NTSTATUS APIENTRY DXGKDDI_SETTARGETANALOGCOPYPROTECTION(
  _In_ const HANDLE                                 hAdapter,
  _In_ const PDXGKARG_SETTARGETANALOGCOPYPROTECTION pSetTargetAnalogCopyProtectionArg
);
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>Identifies the adapter.</p>
</dd>

### -param <i>pSetTargetAnalogCopyProtectionArg</i> [in]

<dd>
<p>A pointer to a DXGKARG_SETTARGETANALOGCOPYPROTECTION structure that provides the target id and the analog content protection parameters being requested.</p>
</dd>
</dl>

## -returns
<p>If this routine succeeds, it returns STATUS_SUCCESS. </p>

## -remarks
<p>This is an optional DDI so the function pointer in the DRIVER_INITIALIZATION_DATA should be set to null if the DDI is not implemented for every adapter supported by the driver.  Since analog content protection is only supported on analog targets and may not be supported through dongles it is increasingly likely over time that drivers will have no need to support this DDI.
</p>

<p>The OEMCopyProtection byte array which is part of the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION structure used in the old DDI has been dropped as it was reserved and never defined so always contained zeroes.  

</p>

<p>This function is always called at PASSIVE level so the supporting code should be made pageable.</p>

<p>This is an optional DDI so the function pointer in the DRIVER_INITIALIZATION_DATA should be set to null if the DDI is not implemented for every adapter supported by the driver.  Since analog content protection is only supported on analog targets and may not be supported through dongles it is increasingly likely over time that drivers will have no need to support this DDI.
</p>

<p>The OEMCopyProtection byte array which is part of the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION structure used in the old DDI has been dropped as it was reserved and never defined so always contained zeroes.  

</p>

<p>This function is always called at PASSIVE level so the supporting code should be made pageable.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>