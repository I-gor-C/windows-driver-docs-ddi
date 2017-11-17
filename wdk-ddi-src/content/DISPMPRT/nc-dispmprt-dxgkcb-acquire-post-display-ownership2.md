---
UID: NC.dispmprt.DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2
title: DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2
author: windows-driver-content
description: Called by a display miniport driver to obtain the display information from the current power-on self-test (POST) display device or the previously running Windows Display Driver Model (WDDM) driver.
old-location: display\dxgkcb_acquire_post_display_ownership2.htm
ms.assetid: 923A2107-8F5E-4EF7-8C3C-4EFDE26A50F5
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
req.alt-api: DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2
req.alt-loc: tbd
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Tbd
req.dll: Tbd
req.irql: 
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2 callback



## -description
<p>Called by a display miniport driver to obtain the display information from the current  power-on self-test (POST) display device or the previously running Windows Display Driver Model (WDDM) driver.</p>


## -prototype

````
NTSTATUS APIENTRY* DXGKCB_ACQUIRE_POST_DISPLAY_OWNERSHIP2(
  _In_  HANDLE                         DeviceHandle,
  _Out_ PDXGK_DISPLAY_INFORMATION      DisplayInfo,
  _Out_ PDXGK_DISPLAY_OWNERSHIP_FLAGS  Flags
);
````


## -parameters
<dl>

### -param <i>DeviceHandle</i> [in]

<dd>
<p>A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a>.</p>
</dd>

### -param <i>DisplayInfo</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh464017">DXGK_DISPLAY_INFORMATION</a> structure that is allocated by the display miniport driver. If <a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a> returns STATUS_SUCCESS, this structure contains display information for the current display device that is used for POST operations.</p>
</dd>

### -param <i>Flags</i> [out]

<dd>
<p>A pointer to a DXGK_DISPLAY_OWNERSHIP_FLAGS structure that is allocated by the display miniport driver. If DxgkCbAcquirePostDisplayOwnership2 returns STATUS_SUCCESS, this structure contains flags in bit fields describing the ownership of the display.  The only bit fields defined in WDDM 2.2 contain a DXGK_FRAMEBUFFER_STATE enum indicating how the frame buffer was initialized.</p>
</dd>
</dl>

## -returns
<p>
<a href="display.DxgkCbAcquirePostDisplayOwnership">DxgkCbAcquirePostDisplayOwnership</a> returns STATUS_SUCCESS if it succeeds. </p>

## -remarks


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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Tbd</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Tbd</dt>
</dl>
</td>
</tr>
</table>