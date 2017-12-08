---
UID: NC.d3dumddi.PFND3DDDI_CHECKPRESENTDURATIONSUPPORT
title: PFND3DDDI_CHECKPRESENTDURATIONSUPPORT
author: windows-driver-content
description: Called by the Microsoft Direct3D runtime to request that the user-mode display driver get hardware device capabilities for seamlessly switching to a new monitor refresh rate.
old-location: display\checkpresentdurationsupport.htm
old-project: display
ms.assetid: 4D3FC503-A502-41D3-AB76-5A2BEBE4C551
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CheckPresentDurationSupport
req.alt-loc: D3dumddi.h
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
---

# PFND3DDDI_CHECKPRESENTDURATIONSUPPORT callback



## -description
Called by the Microsoft Direct3D runtime to request that the user-mode display driver  get  hardware device capabilities for seamlessly switching to a new monitor refresh rate. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.


## -prototype

````
PFND3DDDI_CHECKPRESENTDURATIONSUPPORT CheckPresentDurationSupport;

_Check_return_ HRESULT* CheckPresentDurationSupport(
  _In_ HANDLE                                hDevice,
  _In_ D3DDDIARG_CHECKPRESENTDURATIONSUPPORT *pPresentDurationSupport
)
{ ... }
````


## -parameters

### -param hDevice [in]

A handle to the display device (graphics context).

### -param pPresentDurationSupport [in]

A pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddiarg_checkpresentdurationsupport.md">D3DDDIARG_CHECKPRESENTDURATIONSUPPORT</a> structure that contains info on hardware device support for seamlessly switching to a new monitor refresh rate.

## -returns
If this routine succeeds, it returns <b>S_OK</b>. The driver should always return a success code.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
WDDM 1.3 and later
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-d3dddiarg_checkpresentdurationsupport.md">D3DDDIARG_CHECKPRESENTDURATIONSUPPORT</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CHECKPRESENTDURATIONSUPPORT callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
